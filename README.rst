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

* https://cmake.org
* `cmake-presets <https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html>`_ docs
* `cmake-presets.schema.json <https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json>`_
  (or: `cmake-presets schema pointer <https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#id13>`_)

.. _cmake: https://cmake.org
.. _cmake-presets: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html
.. _cmake-presets.schema.json: https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json

EXAMPLES FOR: CMakePresets.json

* `repo: cmake/Help/manual/presets/example.json <https://gitlab.kitware.com/cmake/cmake/-/blob/master/Help/manual/presets/example.json>`_ (
  file: `example.json <https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/example.json>`_)

* `repo: cmake/Tests/RunCMake/CMakePresetsTest/Good.json.in <https://gitlab.kitware.com/cmake/cmake/-/blob/master/Tests/RunCMake/CMakePresetsTest/Good.json.in>`_ (
  file: `CMakePresetsTest/Good.json.in <https://gitlab.kitware.com/cmake/cmake/-/raw/master/Tests/RunCMake/CMakePresetsTest/Good.json.in>`_)

* `repo: cpp-best-practices/cmake_template/CMakePresets.json <https://github.com/cpp-best-practices/cmake_template/blob/main/CMakePresets.json>`_ (
  file: `CMakePresets.json <https://raw.githubusercontent.com/cpp-best-practices/cmake_template/main/CMakePresets.json>`_)


RELATED TO: cmake-presets issues

* ON_ERROR: `cmake #21310: Presets-related error messages don't provide enough information <https://gitlab.kitware.com/cmake/cmake/-/issues/21310>`_
* ANY_OS: `cmake #23283: presets: Inheritance of conditional presets <https://gitlab.kitware.com/cmake/cmake/-/issues/23283>`_
* ANY_OS: `cmake #24976: Portable way to set filepaths in presets <https://gitlab.kitware.com/cmake/cmake/-/issues/24976>`_


cmake: Invalid Preset
-------------------------------------------------------------------------------

You often run into problems while developing a ``CMakePresets.json`` file,
where `cmake`_ just states ``invalid preset`` without any explanation.

REASONS:

* Invalid JSON, like: ``trailing-comma`` for last entry in a ``list``/``dict``.
* Violates JSON schema: Does not conform to the JSON schema for `cmake-presets`_
* ``JSON schema`` check is ``OK``, but `cmake`_ still complains:

  - **preset** data is **internally inconsistent** for `cmake`_.

    EXAMPLE: ``generator = ...`` is missing in inherited ``ConfigurePreset``

  - **macro-expansion fails**,
    because ``placeholder`` is not supported for this preset-type.

    EXAMPLE: Using ``"outputLogfile" = "${binaryDir}/some.log"`` in ``TestPreset``

  - **macro-expansion fails**, like: ...


BEST PRACTICE:
~~~~~~~~~~~~~~~

Use a JSON schema checker/linter to find the most common errors.
This solves the following problem points:

* Invalid JSON
* Violates JSON schema for `cmake-presets`_

.. code:: bash

    # -- REQUIRES: pip install check-jsonschema
    # cmake-presets.schema.json: https://gitlab.kitware.com/cmake/cmake/-/blob/master/Help/manual/presets/schema.json
    $ check-jsonschema --schemafile cmake-preset.schema.json --verbose CMakePresets.json

.. code:: bash

    # -- ALTERNATIVE: USE SCRIPT: bin/check_cmake-presets.sh
    $ bin/check_cmake-presets.sh                    # CHECKS: CMakePresets.json (implicit)
    $ bin/check_cmake-presets.sh CMakePresets.json  # CHECKS: CMakePresets.json (explicit)
    $ bin/check_cmake-presets.sh CMakePresets1.json CMakePresets2.json ...  # CHECKS: Many files


SEE ALSO:

* `cmake-presets docs <https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html>`_
* `cmake-presets.schema.json <https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json>`_


SIDE NOTE: codespell
-------------------------------------------------------------------------------

:Category: spelling-checker

* https://github.com/codespell-project/codespell  (language: Python3, license: GPL-2.0)
* EXAMPLE: https://gitlab.kitware.com/cmake/cmake/-/blob/master/.codespellrc
* https://www.thegeekdiary.com/codespell-spellchecker-for-source-code/
