#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pylint: disable=C0103
# pylint: disable=missing-docstring
"""
Check cmake-presets file(s) by using the JSON schema.
"""
# REQUIRES: pip install check-jsonschema requests

from __future__ import absolute_import, print_function
import argparse
from pathlib import Path
from subprocess import run
import textwrap
import sys

# -- DEPENDENCIES:
# NOT_NEEDED_HERE: from check_jsonschema import main as check_jsonschema_main
import requests


# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------
SCRIPT = Path(__file__).stem
HERE = Path(__file__).parent.absolute()
CMAKE_PRESETS_FILE = Path("CMakePresets.json")
CMAKE_USER_PRESETS_FILE = Path("CMakeUserPresets.json")
CMAKE_PRESETS_SCHEMA_FILE = Path("cmake-presets.schema.json")
CMAKE_PRESETS_SCHEMA_URL = \
    "https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json"


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------
def download_cmake_presets_schema(filepath=None, destdir=None):
    """
    Download "cmake-presets.schema.json" file from "cmake" repository.

    :param filepath:  Destination path for JSON schema file (optional).
    :return: Path to "cmake-presets.schema.json".
    """
    if filepath is None:
        filepath = CMAKE_PRESETS_SCHEMA_FILE
    if destdir:
        filepath = Path(destdir)/Path(filepath).stem

    print("DOWNLOAD: cmake-presets.schema.json ... (from: cmake.repo)")
    download_request = requests.get(CMAKE_PRESETS_SCHEMA_URL, timeout=30)
    if not download_request.ok:
        print(f"DOWNLOAD: FAILED -- {download_request!r}")
        return None

    # -- NORMAL CASE:
    content_size = len(download_request.content)
    print(f"DOWNLOAD: OK (size={content_size})")
    this_directory = Path(filepath).parent
    if not this_directory.is_dir():
        print(f"CREATE-DIR: {this_directory}")
        this_directory.mkdir(parents=True, exist_ok=True)

    print(f"DOWNLOAD: Store {filepath}")
    with open(filepath, "wb") as f:
        f.write(download_request.content)
    return Path(filepath)


def ensure_cmake_presets_schema_exists():
    if not CMAKE_PRESETS_SCHEMA_FILE.exists():
        download_cmake_presets_schema()
    return CMAKE_PRESETS_SCHEMA_FILE


def check_cmake_presets_file(filename): # MAYBE: , schema_file=None):
    # from shutil import which
    # if schema_file is None:
    #     schema_file = CMAKE_PRESETS_SCHEMA_FILE
    print(f"{filename} ... ", end="")
    command = "check-jsonschema"
    result = run(
        f"{command} --schemafile=cmake-presets.schema.json --verbose {filename}",
        shell=True, capture_output=True, check=False)

    # -- SHOW VALIDATION-OUTCOME:
    validation_succeeded = result.returncode == 0
    if validation_succeeded:
        print("OK")
    else:
        # -- CASE VALIDATION-FAILED:
        captured = result.stdout.decode("UTF-8").strip()
        best_match_pos = captured.find("Best Match:")
        if best_match_pos:
            # -- COMPRESS INFO: Cut the leading JSON crap and shown the reasons.
            text = captured[best_match_pos:]
            print(f"NOT_OK\n{text}")
        else:
            print(f"NOT_OK: {captured}")

    return validation_succeeded
    # return check_jsonschema_main(instancefiles=[str(filename)],
    #                              schemafile=CMAKE_PRESETS_SCHEMA_FILE,
    #                               verbose=True)


def check_cmake_presets_files(filenames):
    failed_counts = 0
    for json_filename in filenames:
        if not check_cmake_presets_file(json_filename):
            failed_counts += 1
    return failed_counts


# -----------------------------------------------------------------------------
# MAIN FUNCTION
# -----------------------------------------------------------------------------
def main(args=None):
    """Check cmake-presets file(s) by using the JSON schema."""
    if args is None:
        args = sys.argv[1:]

    epilog = """
        If no CMAKE_PRESETS_FILE is provided, checks:
    
        * CMakePresets.json
        * CMakeUserPresets.json (if exists)
    
        NOTE: Downloads the "cmake-presets.schema.json" if necessary.
        SEE:  https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html
        """
    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog=SCRIPT,
                description=textwrap.dedent(__doc__),
                epilog=textwrap.dedent(epilog),
                formatter_class=formatter_class)
    parser.add_argument("--update", action="store_true",
                        dest="update_needed", help="Update the JSON schema.")
    parser.add_argument("files", metavar="CMAKE_PRESETS_FILE", nargs="*",
                        help="cmake-presets file(s) (as JSON files)")
    args = parser.parse_args(args)
    if not args.files:
        args.files = [CMAKE_PRESETS_FILE]
        if CMAKE_USER_PRESETS_FILE.exists():
            args.files.append(CMAKE_USER_PRESETS_FILE)

    if args.update_needed or not CMAKE_PRESETS_SCHEMA_FILE.exists():
        download_cmake_presets_schema()
    # MAYBE: ensure_cmake_presets_schema_exists()
    failed_counts = check_cmake_presets_files(args.files)
    if failed_counts > 0:
        return 1
    # -- OTHERWISE: SUCCESS
    return 0


# -----------------------------------------------------------------------------
# AUTO-MAIN
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
