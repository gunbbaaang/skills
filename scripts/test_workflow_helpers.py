"""Smoke-test copied Superpowers helpers without changing user repositories."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
GIT_BASH = Path('C:/Program Files/Git/bin/bash.exe')
BASH = str(GIT_BASH) if GIT_BASH.is_file() else shutil.which('bash')


@unittest.skipUnless(BASH and shutil.which('git'), 'Bash and Git are required for optional helpers')
class WorkflowHelperTests(unittest.TestCase):
    def test_failure_never_records_completion(self):
        with tempfile.TemporaryDirectory(prefix='workflow helper ') as tmp:
            project = Path(tmp).resolve()
            def run(args, check=True):
                return subprocess.run(args, cwd=project, capture_output=True, text=True,
                                      encoding='utf-8', check=check)

            run(['git', 'init', '-q'])
            plan = project/'plan.md'
            plan.write_text('# Fixture plan\n\n## Task 1: First action\nExpected first task.\n\n## Task 2: Later action\nDo not include this.\n', encoding='utf-8')
            run(['git', 'add', 'plan.md'])
            run(['git', '-c', 'user.name=Bundle Test', '-c', 'user.email=bundle-test@example.invalid',
                 '-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=', 'commit', '-qm', 'Fixture'])
            base = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
            start = ROOT/'skills/executing-plans/scripts/task-start'
            done = ROOT/'skills/executing-plans/scripts/task-done'
            result = run([BASH, start.as_posix(), 'plan.md', '1'])
            self.assertIn(base, result.stdout)
            workspace = project/'.superpowers/sdd/plan'
            brief = (workspace/'task-1-brief.md').read_text(encoding='utf-8')
            self.assertIn('Expected first task.', brief)
            self.assertNotIn('Do not include this.', brief)

            failure = run([BASH, done.as_posix(), 'plan.md', '1', base, '--', BASH, '-c', 'exit 7'], check=False)
            self.assertEqual(failure.returncode, 7, failure.stderr)
            self.assertFalse((workspace/'progress.md').exists())
            self.assertIn('NOT recorded', failure.stderr+failure.stdout)

            success = run([BASH, done.as_posix(), 'plan.md', '1', base, '--', BASH, '-c', "printf 'fixture passed\\n'"])
            ledger = (workspace/'progress.md').read_text(encoding='utf-8')
            self.assertEqual(ledger.count('Task 1: complete'), 1)
            self.assertIn('fixture passed', ledger)
            self.assertIn('ledger:', success.stdout)


if __name__ == '__main__':
    unittest.main()
