# Created by TheMaskedCrusader on 2021/12/13.
cmake_minimum_required(VERSION 3.16)
project(advent_of_code_2021)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(input_dir "${CMAKE_CURRENT_SOURCE_DIR}/input")


function (advent name)
    set(options "")
    add_executable(${name}
        advent/${name}.cpp
    )
    target_compile_features(${name} PRIVATE
        cxx_std_17
    )
endfunction(advent)

advent(01a)
advent(01b)
