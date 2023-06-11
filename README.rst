Explore CMake-Presets
===============================================================================

:Date: 2023-06-11

Explore how `cmake-presets` can be used.

.. code:: bash

    # -- STEP: Which cmake-presets are available ?!
    $ cmake --list-presets
    Available configure presets:

      "debug"         - debug
      "release"       - release
      "multi"         - multi
      "multi.release" - multi.release

    # -- STEP: Init/configure CMAKE_BUILD_DIR by using a preset=<PRESET_NAME>
    $ cmake --preset=multi

    # -- STEP: Run a  workflow by using a preset=<PRESET_NAME>
    # WORKFLOW STEPS: init, build, test, ...
    $ cmake --workflow --preset=multi

SEE ALSO:

* cmake-presets: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html
* SCHEMA: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#id13
  https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json

.. _cmake: https://cmake.org
.. _cmake-presets: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html
.. _cmake-presets.schema.json: https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json

EXAMPLES FOR: CMakePresets.json

* https://gitlab.kitware.com/cmake/cmake/-/blob/master/Help/manual/presets/example.json ,
  https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/example.json

* https://gitlab.kitware.com/cmake/cmake/-/blob/master/Tests/RunCMake/CMakePresetsTest/Good.json.in ,
  https://gitlab.kitware.com/cmake/cmake/-/raw/master/Tests/RunCMake/CMakePresetsTest/Good.json.in

* https://github.com/cpp-best-practices/cmake_template/blob/main/CMakePresets.json ,
  https://raw.githubusercontent.com/cpp-best-practices/cmake_template/main/CMakePresets.json

RELATED TO: spelling

* https://github.com/codespell-project/codespell  (language: Python3, license: GPL-2.0)
* EXAMPLE: https://gitlab.kitware.com/cmake/cmake/-/blob/master/.codespellrc
* https://www.thegeekdiary.com/codespell-spellchecker-for-source-code/


ASPECT: Invalid Preset
-------------------------------------------------------------------------------

You often run in problems while developing a "CMakePresets.json" file,
where `cmake`_ just states ``invalid preset`` without any explanation.

REASONS:

* Invalid JSON, like: `trailing-comma` for last entry in a list/dict
* Violates JSON schema: Does not conform to the JSON schema for `cmake-presets`_
* check-schema is OK, but `cmake`_ still complains:

  - Preset data is internally inconsistent for `cmake`_.

    EXAMPLE: ``generator = ...`` is missing in inherited ``ConfigurePreset``

  - macro-expansion fails,
    because ``placeholder`` is not supported for this preset-type.

    EXAMPLE: Using ``"outputLogfile" = "${binaryDir}/some.log" in ``TestPreset``

  - macro-expansion fails, like: ...


BEST PRACTICE:

Use a JSON schema checker/linter to find the most common errors.
This solves the following problem points:

* Invalid JSON
* Violates JSON schema for `cmake-presets`_

.. code:: bash

# REQUIRES: pip install check-jsonschema
# cmake-presets.schema.json: https://gitlab.kitware.com/cmake/cmake/-/blob/master/Help/manual/presets/schema.json
$ check-jsonschema --schemafile cmake-preset.schema.json --verbose CMakePresets.json

SEE ALSO:

* cmake-presets: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html
* cmake-presets.schema.json:
  https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json
