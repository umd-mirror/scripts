from . import RsyncMirrorRunner, APTMirrorRunner

class MxLinuxMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsuser@iso.mxrepo.com/workspace'

  rsync_delete_delay = True
  rsync_delay_updates = True
  rsync_password_file = '/home/mirror/scripts/mirror/extras/mx_packages_rsync.password'
