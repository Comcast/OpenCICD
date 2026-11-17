# Proposal

## Why

Docker's default tmpfs mount is not executable, so programs that place and run files under the temporary runtime home can fail. The generated `/tmp/home` mount needs to permit execution while retaining its current writable and disposable behavior.

## What Changes

- Add `exec` to the `/tmp/home` tmpfs options whenever tmp-home mode is enabled, producing `--tmpfs /tmp/home:rw,exec`.
- Retain numeric uid/gid ownership options when `--docker-user` is provided, alongside the new `exec` option.
- Update runtime documentation and command-generation tests to reflect the executable mount.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `docker-runtime-tmp-home`: Require the temporary runtime home tmpfs mount to allow execution.

## Impact

- Runtime `docker run` command generation in `src/opencicd/action_runner.py`.
- Tmp-home assertions in `tests/unit/test_cli_docker_user.py` and examples in `docs/running.md`.
- No CLI flag changes, new dependencies, or changes to non-runtime Docker commands.
