cmake_minimum_required(VERSION 3.10)
project(meepcity_roblox_trainer)

set(CMAKE_CXX_STANDARD 17)

add_executable(meepcity_trainer
    src/main.cpp
    src/memory_utils.cpp
    src/roblox_offsets.cpp
)

target_link_libraries(meepcity_trainer PRIVATE kernel32 user32)