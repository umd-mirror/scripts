from . import RsyncMirrorRunner

class ArchStrikeMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://149.56.97.241/archstrike-pull'
  rsync_delete_delay = True
  rsync_delay_updates = True

