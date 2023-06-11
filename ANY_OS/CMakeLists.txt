# ===========================================================================
# CMAKE: explore.cmake-presets
# ===========================================================================
# DESCRIPTION:
#   Simple "CMakeLists.txt" to explore "cmake-presets".
#
# EXAMPLE:
#   # -- STEP: Use CMake to build compile-database: $BUILD_DIR/compile_commands.json
#   cmake --preset=variadic
#   cmake --workflow --preset=variadic
#
# SEE ALSO:
#  * https://cmake.org/
# ===========================================================================

cmake_minimum_required(VERSION 3.24..3.26)

if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
    # -- SCOPE: MASTER_PROJECT
    message(STATUS "cmake.version: ${CMAKE_VERSION}")
endif()


# --------------------------------------------------------------------------
# EXPLORE: ANY_OS presets
# ---------------------------------------------------------------------------
if(NOT DEFINED "MY_TOOLCHAIN1")
    if(DEFINED "$ENV{MY_TOOLCHAIN2}")
        set(MY_TOOLCHAIN1 "$env{MY_TOOLCHAIN2}::from_env")
    else()
        set(MY_TOOLCHAIN1 "__UNDEFINED__")
    endif()
endif()
message(STATUS "MY_TOOLCHAIN1  = ${MY_TOOLCHAIN1}")
message(STATUS "MY_TOOLCHAIN2 = ${MY_TOOLCHAIN2}")


# --------------------------------------------------------------------------
# PROJECT:
# ---------------------------------------------------------------------------
project(explore-cmake-presets VERSION 0.1 LANGUAGES CXX)

if(NOT DEFINED CMAKE_EXPORT_COMPILE_COMMANDS)
    set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
endif()
if(NOT DEFINED CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 17)
endif()
if(NOT DEFINED CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()
message(STATUS "USING: CMAKE_CXX_STANDARD=${CMAKE_CXX_STANDARD}")
message(STATUS "USING: CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message(STATUS "USING: CMAKE_CONFIG_TYPE=$ENV{CMAKE_CONFIG_TYPE}")
