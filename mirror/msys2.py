from . import RsyncMirrorRunner

class ArchLinuxMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://repo.msys2.org/builds/'
  rsync_delete_delay = True
  rsync_delay_updates = True
