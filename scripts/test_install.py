import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('bundle_install', Path(__file__).with_name('install.py'))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class InstallTests(unittest.TestCase):
    def test_fresh_repeat_and_modified_copy(self):
        expected = {p.parent.name for p in (installer.ROOT/'skills').glob('*/SKILL.md')}
        self.assertTrue({'frontend-design', 'vercel-react-best-practices',
                         'web-design-guidelines', 'webapp-testing', 'slides',
                         'explore-data', 'validate-data', 'data-visualization',
                         'llm-evaluation', 'systematic-debugging'} <= expected)
        with tempfile.TemporaryDirectory(prefix='bundle test ') as tmp:
            root = Path(tmp)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(installer.install(root), len(expected))
            skills = root / '.agents/skills'
            self.assertEqual({p.parent.name for p in skills.glob('*/SKILL.md')}, expected)
            self.assertTrue((skills/'understand/runtime/packages/core/package.json').is_file())
            self.assertTrue((skills/'graphify/references').is_dir())
            self.assertTrue((skills/'visual-explainer/kit/render.mjs').is_file())
            for relative in ['slides/scripts/render_slides.py', 'slides/BUNDLE.md',
                             'webapp-testing/scripts/with_server.py', 'webapp-testing/BUNDLE.md',
                             'web-design-guidelines/references/web-interface-guidelines.md',
                             'vercel-react-best-practices/AGENTS.md',
                             'vercel-react-best-practices/upstream-metadata.json',
                             'probe-hackathon-coach/references/field-guide.md',
                             'probe-hackathon-coach/references/score-playbook.md',
                             'probe-hackathon-coach/references/evidence-skills.md',
                             'explore-data/CONNECTORS.md', 'validate-data/CONNECTORS.md',
                             'llm-evaluation/references/details.md',
                             'llm-evaluation/references/hackathon-eval.md',
                             'systematic-debugging/root-cause-tracing.md',
                             'systematic-debugging/condition-based-waiting-example.ts']:
                self.assertTrue((skills/relative).is_file(), relative)
            for name in ['frontend-design', 'webapp-testing', 'slides',
                         'vercel-react-best-practices', 'web-design-guidelines',
                         'explore-data', 'validate-data', 'data-visualization',
                         'llm-evaluation', 'systematic-debugging']:
                self.assertTrue((skills/name/'LICENSE.txt').is_file(), name)
            with contextlib.redirect_stdout(io.StringIO()) as output:
                installer.install(root)
            self.assertEqual(output.getvalue().count('UNCHANGED '), len(expected))
            handoff = skills/'handoff/SKILL.md'
            handoff.write_text('my local customization', encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()):
                installer.install(root)
            backups = list((root/'.agents/skill-backups').glob('*/handoff/SKILL.md'))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding='utf-8'), 'my local customization')
            self.assertEqual(handoff.read_bytes(), (installer.ROOT/'skills/handoff/SKILL.md').read_bytes())

    def test_incomplete_destination_reports_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError):
                installer.install(Path(tmp)/'missing-project')

if __name__ == '__main__':
    unittest.main()
