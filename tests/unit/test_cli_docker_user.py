import asyncio
from pathlib import Path

import pytest

from opencicd.__main__ import async_main


pytestmark = pytest.mark.unit

TEST_PROJECT_DIR = Path(__file__).resolve().parents[2] / "test"


def run_print_command(capsys: pytest.CaptureFixture[str], *extra_args: str) -> list[str]:
    asyncio.run(
        async_main(
            [
                "opencicd",
                "--project-folder",
                str(TEST_PROJECT_DIR),
                "--host-project-folder",
                ".",
                "--method=print",
                "--no-posix",
                "--quiet",
                *extra_args,
                "publish",
                "test2",
            ]
        )
    )
    return [line for line in capsys.readouterr().out.splitlines() if line.startswith('"docker" "run"')]


def test_print_commands_include_docker_user_when_requested(capsys: pytest.CaptureFixture[str]):
    run_lines = run_print_command(capsys, "--docker-user", "1000:1000")

    assert run_lines
    assert all('"--user" "1000:1000"' in line for line in run_lines)
    assert '"--user" "1000:1000"' in run_lines[0]
    assert run_lines[0].index('"--user" "1000:1000"') < run_lines[0].index('"alpine:3.21"')


def test_print_commands_omit_docker_user_by_default(capsys: pytest.CaptureFixture[str]):
    run_lines = run_print_command(capsys)

    assert run_lines
    assert all('"--user"' not in line for line in run_lines)