# Tasks

## 1. Executable temporary home

- [x] 1.1 Add `exec` to the base tmpfs option in `src/opencicd/action_runner.py`; update `tests/unit/test_cli_docker_user.py` assertions for explicit tmp-home, the `--cicd` default, and uid/uid:gid users; verify with `pytest tests/unit/test_cli_docker_user.py`.
- [x] 1.2 Update the tmp-home explanation and both generated-command examples in `docs/running.md` to show `rw,exec` and ownership suffixes; verify examples match CLI print output and `--no-tmp-home` remains unchanged.

## 2. Integration verification

- [x] 2.1 Run `openspec validate enable-exec-tmp-home --strict` and, when a Docker engine is available, run a container with the generated tmpfs option and execute a file created under `/tmp/home`; verify the mount accepts execution.
