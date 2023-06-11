#!/bin/bash
# SEE:    https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#schema
# REQUIRES: pip install check-jsonschema

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
