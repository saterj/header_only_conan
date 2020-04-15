# CMakeLists files in this project can
cmake_minimum_required (VERSION 3.4)

file(GLOB include_files "${CMAKE_CURRENT_SOURCE_DIR}/src/*")
set( AGCO_GATEWAY_PARTS_STORE_SHARED_TYPES_INCLUDES ${include_files} )

add_library( Shared_Types INTERFACE)
target_include_directories(Shared_Types INTERFACE src/ )
