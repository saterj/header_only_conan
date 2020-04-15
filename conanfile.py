from conans import ConanFile, CMake

class SharedtypesConan(ConanFile):
    name = "Shared_Types"
    version = "trunk"
    license = "nunya.1.0"
    author = "whos.who@corp.com"
    url = "http://server.com/svn/Parts_Store/trunk/ECU/Shared_Types"
    description = "internal appareo library"
    exports_sources = "src/*", "CMakeLists.txt"
    enerators = "cmake"
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
   
    def package(self):
        self.copy("*.h")
        self.copy("CMakeLists.txt")
    
    def package_info(self):
        self.output.warn( self.env_info )
        self.cpp_info.includedirs= ['src']
