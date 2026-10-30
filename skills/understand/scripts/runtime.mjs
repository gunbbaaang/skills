import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import { spawnSync } from 'node:child_process';

const root = fileURLToPath(new URL('../runtime/', import.meta.url));
const mode = process.argv[2] ?? '--check';
if (!['--check', '--setup'].includes(mode)) {
  console.error('Usage: node runtime.mjs [--check|--setup]');
  process.exit(2);
}
console.log(`PLUGIN_ROOT=${root}`);
if (Number(process.versions.node.split('.')[0]) < 22) {
  console.error('Node.js 22+ is required.');
  process.exit(1);
}
for (const name of ['package.json', 'pnpm-lock.yaml', 'pnpm-workspace.yaml', 'packages/core/package.json']) {
  if (!existsSync(resolve(root, name))) {
    console.error(`Incomplete bundle: ${name}`);
    process.exit(1);
  }
}
function run(args) {
  const windows = process.platform === 'win32';
  // cmd.exe only launches npm's command shim; no filesystem operations are composed through it.
  const result = windows
    ? spawnSync(process.env.ComSpec || 'cmd.exe', ['/d', '/s', '/c', `npx.cmd --yes pnpm@10.6.2 ${args.join(' ')}`], { cwd: root, stdio: 'inherit' })
    : spawnSync('npx', ['--yes', 'pnpm@10.6.2', ...args], { cwd: root, stdio: 'inherit' });
  if (result.error || result.status !== 0) {
    console.error(result.error?.message ?? 'Runtime setup failed. See the dependency/build error above.');
    process.exit(result.status || 1);
  }
}
if (mode === '--setup') {
  run(['install', '--frozen-lockfile']);
  run(['--filter', '@understand-anything/core', 'build']);
}
const core = resolve(root, 'packages/core/dist/index.js');
if (!existsSync(core) || !existsSync(resolve(root, 'node_modules'))) {
  console.error('Runtime source is present; dependencies/core are not ready. Run this command with --setup.');
  process.exit(1);
}
// Verify an actual import, not only the presence of generated files.
const { pathToFileURL } = await import('node:url');
await import(pathToFileURL(core).href);
console.log('Understand Anything runtime ready. Project analysis has not been run.');
