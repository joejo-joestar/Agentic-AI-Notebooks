"""Utility functions to set, list, and unset environment variables in a conda environment."""

from pathlib import Path
import subprocess

# !Note: `shell=True` is set due to every os being a bitch
# reference: https://stackoverflow.com/questions/73193119/python-filenotfounderror-winerror-2-the-system-cannot-find-the-file-specifie


def set_env_variables(env_file: Path):
    """Set an environment variable in the conda env from the .env file."""
    with open(
        file=env_file,
    ) as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            key = key.strip()
            value = value.strip()
            return_code = subprocess.run(
                ["conda", "env", "config", "vars", "set", f"{key}={value}"], shell=True
            )
            if return_code.returncode != 0:
                raise RuntimeError(f"Failed to set environment variable {key}")
            print(f"Set environment variable {key} successfully.")


def list_env_variables():
    """List all environment variables set in the conda env."""
    return_code = subprocess.run(
        ["conda", "env", "config", "vars", "list"],
        capture_output=True,
        text=True,
        shell=True,
    )
    if return_code.returncode != 0:
        raise RuntimeError("Failed to list environment variables")
    print(return_code.stdout)


def unset_env_variable(key: str):
    """Unset an environment variable in the conda env."""
    return_code = subprocess.run(
        [
            "conda",
            "env",
            "config",
            "vars",
            "unset",
            key,
        ],
        shell=True,
    )
    if return_code.returncode != 0:
        raise RuntimeError(f"Failed to unset environment variable {key}")
    print(f"Unset environment variable {key} successfully.")
