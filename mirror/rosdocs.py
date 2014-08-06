from . import RsyncMirrorRunner

class ROSDocsMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://docs.ros.org/mirror/'

  base_subdir = 'ros-docs'
