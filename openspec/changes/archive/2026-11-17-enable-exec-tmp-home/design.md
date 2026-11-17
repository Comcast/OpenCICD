# Design

## Context

`job_runner` assembles runtime Docker arguments and calls `build_tmp_home_mount_option(docker_user)` for the tmpfs value. That helper starts with `/tmp/home:rw` and appends numeric uid/gid options. The CLI enables tmp-home explicitly or by default with `--cicd`; see proposal.md for the motivation and the spec delta for the resulting behavior.

## Goals / Non-Goals

**Goals:**
- Keep one mount-option construction path for printed and executed runtime commands, including numeric Docker users.
- Make the execution permission explicit in the generated tmpfs option without changing tmp-home selection or ownership semantics.

**Non-Goals:**
- Add a separate execution-permission flag or change other mounts, image builds, or the container's default home when tmp-home is disabled.

## Decisions

- Add `exec` to the helper's base option, yielding `/tmp/home:rw,exec` before optional `uid` and `gid` suffixes. This preserves current ordering and shared behavior across print and exec modes. Changing command assembly at individual call sites would duplicate option construction and risk divergence.
- Keep execution enabled whenever tmp-home is enabled. A new opt-in or opt-out switch would introduce extra policy states not requested by the changed contract.
- Check the exact generated mount options in the existing CLI print tests, including `--cicd` and numeric user variants; update the runtime examples and explain the execution permission.

## Risks / Trade-offs

- [Executables in a writable home can run, broadening what a job can execute there] -> Limit this change to the explicitly configured `/tmp/home` runtime mount; document the behavior so callers can use `--no-tmp-home` if they do not need it in `--cicd` mode.
- [A command-print assertion does not prove a specific Docker host accepts the mount option] -> Keep the option in Docker's existing `--tmpfs` format; run a Docker smoke check where an engine is available during implementation.
