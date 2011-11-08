from . import RsyncMirrorRunner

class ArchLinuxMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://mirror.rit.edu/archlinux/'
  #rsync_filter_list = ['- iso/2007.*', '- iso/2008.*', '- iso/2009.*']
  rsync_delete_delay = True
  rsync_delay_updates = True

