from . import RsyncMirrorRunner

class MxLinuxISOMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://downstreamtestuser@rsync-mxlinux.org/MX-Linux'

  rsync_delete_delay = True
  rsync_delay_updates = True
  rsync_password_file = '/home/mirror/scripts/mirror/extras/mx_isos_rsync.password'
