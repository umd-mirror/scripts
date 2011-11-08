from . import RsyncMirrorRunner

class KernelMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'kernel.org'
  source = 'rsync://rsync.kernel.org/pub/'

