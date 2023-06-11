#!/bin/bash
# =============================================================================
# check_cmake-presets.sh
# =============================================================================
# REQUIRES: pip install check-jsonschema
# USAGE:
#   check_cmake-presets.sh                      # CHECK: CMakePresets.json (implicitl)
#   check_cmake-presets.sh CMakePresets.json    # CHECK: CMakePresets.json (explicit)
#   check_cmake-presets.sh CMakePresets1.json ...  # CHECK: Many cmake-preset files
#
# SEE ALSO:
#  * https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#schema
#  * https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#id13
#
# SCHEMA-FILE:
#  * https://gitlab.kitware.com/cmake/cmake/-/raw/master/Help/manual/presets/schema.json
# =============================================================================

set -e
HERE=$(dirname $0)

# MAYBE: : CMAKE_PRESETS_FILES="${*:-'CMakePresets.json'}"
CMAKE_PRESETS_FILES="${*}"
if [ -z "${CMAKE_PRESETS_FILES}" ]; then
    CMAKE_PRESETS_FILES="CMakePresets.json"
fi

for CMAKE_PRESETS_FILE in ${CMAKE_PRESETS_FILES}; do
    printf "${CMAKE_PRESETS_FILE}  ... "
    check-jsonschema --schemafile ${HERE}/cmake-presets.schema.json --verbose ${CMAKE_PRESETS_FILE}
done


