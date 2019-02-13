#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, CMake, tools


class LibImagequantConan(ConanFile):
    name = "libimagequant"
    version = "2.12.2"
    description = "Palette quantization library that powers pngquant and other PNG optimizers"
    topics = ("conan", "libimagequant", "quantization", "palette", "pngquant")
    url = "https://github.com/conan-community/conan-libimagequant"
    homepage = "https://github.com/ImageOptim/libimagequant"
    author = "Conan Community"
    license = "GPL-3.0+"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False], "sse": [True, False]}
    default_options = {"shared": False, "fPIC": True, "sse": True}
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        sha256 = "23ccecb4898ec17474914cfd2fbc4684425f7fd249117f2f1e3f3ba0bf8159e6"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["USE_SSE"] = self.options.sse
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYRIGHT", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            self.cpp_info.libs.append('m')
