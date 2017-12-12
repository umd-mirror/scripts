from . import RsyncMirrorRunner

class ROSDocsMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.osuosl.org/ros_docs_mirror/'

  base_subdir = 'ros-docs'
