CMakePresets: Use ANY_OS inheritance mechanism
===============================================================================

:Date: 2023-06-10 .. 11
:Status: IDEA, not working

Inherit from multiple ``_setup.${OS}`` base-presets (needs: condition=true).

SEE ALSO:

* https://gitlab.kitware.com/cmake/cmake/-/issues/24976
* https://gitlab.kitware.com/cmake/cmake/-/issues/21310  -- General problem


EXPLORING
-------------------------------------------------------------------------------

* Environment variables from first ``_setup.*`` preset is used

.. code:: json

    # -- SOLUTION 1: Use condition=true in combining preset.
    {
        "inherits": ["_setup.linux", "_setup.macOS", "_setup.windows"],
        "name": "variadic",
        "condition": {
            "type": "const",
            "value": true
        },
        ...
    }

.. code:: json

    # -- SOLUTION 2: Use condition=anyOf in combining preset.
    {
        "inherits": ["_setup.linux", "_setup.macOS", "_setup.windows"],
        "name": "variadic",
        "condition": {
            "type": "anyOf",
            "conditions": [
                {
                    "type": "equals",
                    "lhs": "${hostSystemName}",
                    "rhs": "Linux"
              },
              {
                "type": "equals",
                "lhs": "${hostSystemName}",
                "rhs": "Darwin"
              },
              {
                "type": "equals",
                "lhs": "${hostSystemName}",
                "rhs": "Windows"
              }
            ]
        },
        ...
    }

.. code:: json

    # -- SOLUTION 3: Use condition=null in combining preset.
    {
        "inherits": ["_setup.linux", "_setup.macOS", "_setup.windows"],
        "name": "variadic",
        "condition": null,
        ...
    }
