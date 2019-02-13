cmake_minimum_required(VERSION 2.8.12)
project(imagequant C)

include(conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_VERBOSE_MAKEFILE ON)

option(USE_SSE "Avticate SSE feature for x86" OFF)

set(SOURCE_FILES    source_subfolder/pam.c
                    source_subfolder/mediancut.c
                    source_subfolder/blur.c
                    source_subfolder/mempool.c
                    source_subfolder/kmeans.c
                    source_subfolder/nearest.c
                    source_subfolder/libimagequant.c
                    source_subfolder/pam.c
                    source_subfolder/mediancut.c
                    source_subfolder/blur.c
                    source_subfolder/mempool.c
                    source_subfolder/kmeans.c
                    source_subfolder/nearest.c
                    source_subfolder/libimagequant.c)

set(HEADER_FILES    source_subfolder/blur.h
                    source_subfolder/kmeans.h
                    source_subfolder/libimagequant.h
                    source_subfolder/mediancut.h
                    source_subfolder/mempool.h
                    source_subfolder/nearest.h
                    source_subfolder/pam.h)

add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES C_STANDARD 99)

if (USE_SSE)
    target_compile_definitions(${CMAKE_PROJECT_NAME} PUBLIC USE_SSE=1)
    if ((CMAKE_C_COMPILER_ID MATCHES "(Clang)|(GNU)") AND
        (CMAKE_SYSTEM_PROCESSOR MATCHES "(x86)|(X86)|(amd64)|(AMD64)"))
        target_compile_options(${CMAKE_PROJECT_NAME} PUBLIC -msse -mfpmath=sse)
    endif()
endif()

export(TARGETS ${CMAKE_PROJECT_NAME}
       NAMESPACE ${CMAKE_PROJECT_NAME}::
       FILE "${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}-config.cmake")

install(TARGETS ${CMAKE_PROJECT_NAME}
        EXPORT ${CMAKE_PROJECT_NAME}-config
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(FILES ${HEADER_FILES} DESTINATION include)

install(EXPORT ${CMAKE_PROJECT_NAME}-config
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME}/cmake"
        NAMESPACE ${CMAKE_PROJECT_NAME}::)
