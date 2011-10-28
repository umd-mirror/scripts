from . import MirrorRunner

class OpenSUSEMirrorRunner(MirrorRunner):
  source = 'rsync://rsync.opensuse.org/opensuse-hotstuff-160gb/'
  rsync_preserve_perm = True

