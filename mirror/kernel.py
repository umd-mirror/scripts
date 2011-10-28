from . import MirrorRunner

class KernelMirrorRunner(MirrorRunner):
  base_subdir = 'kernel.org'
  source = 'rsync://rsync.kernel.org/pub/'

