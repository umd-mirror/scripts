from . import RsyncMirrorRunner

class OpenSUSEMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.opensuse.org/opensuse-hotstuff-160gb/'
  rsync_preserve_perm = True

