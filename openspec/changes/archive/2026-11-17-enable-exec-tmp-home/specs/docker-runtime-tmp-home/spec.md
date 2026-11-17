# Spec Delta

## MODIFIED Requirements

### Requirement: Runtime docker commands configure a temporary home mount
OpenCICD SHALL add an executable tmpfs mount at `/tmp/home` and SHALL set `HOME=/tmp/home` for each generated runtime `docker run` command when tmp-home mode is enabled.

#### Scenario: Printed commands include tmpfs and home override
- **WHEN** a caller runs `opencicd --method print --tmp-home`
- **THEN** each printed runtime `docker run` command SHALL include `--tmpfs` followed by `/tmp/home:rw,exec`
- **THEN** each printed runtime `docker run` command SHALL include `-e` followed by `HOME=/tmp/home`

#### Scenario: Numeric docker user retains executable tmpfs
- **WHEN** a caller runs `opencicd --method print --tmp-home --docker-user 1000:1001`
- **THEN** each printed runtime `docker run` command SHALL include `--tmpfs` followed by `/tmp/home:rw,exec,uid=1000,gid=1001`

#### Scenario: Tmp-home overrides other generated home values
- **WHEN** tmp-home mode is enabled for a runtime `docker run` command
- **THEN** the generated command SHALL set `HOME=/tmp/home` even if other generated environment mappings would otherwise set `HOME` to a different value

### Requirement: Documentation explains temporary runtime home behavior
The user-facing documentation SHALL describe `--tmp-home`, the executable `/tmp/home` runtime tmpfs, the `--cicd` default, and the fact that the option affects generated runtime `docker run` commands only.

#### Scenario: Runtime documentation shows tmp-home behavior
- **WHEN** a user reads the documented CLI runtime options
- **THEN** the documentation SHALL include an example that uses `--tmp-home` and shows `--tmpfs /tmp/home:rw,exec`
- **THEN** the documentation SHALL explain that `--cicd` enables tmp-home by default
- **THEN** the documentation SHALL explain that the option does not affect non-runtime docker commands
