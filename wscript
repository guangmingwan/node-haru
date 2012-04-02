srcdir = "."
blddir = "build"
VERSION = "0.0.1"

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")

def build(bld):
  bld.add_group("c++")

  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = [
    "-D_FILE_OFFSET_BITS=64",
    "-D_LARGEFILE_SOURCE"
  ]
  obj.target = "haru"
  obj.source = "src/haru.cc"