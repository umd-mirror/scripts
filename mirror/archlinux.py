from . import RsyncMirrorRunner

class ArchLinuxMirrorRunner(RsyncMirrorRunner):
  #source = 'rsync://mirror.rit.edu/archlinux/'
  # rit is often over capacity (too many connections) or drops connections (5/11/2012)
  #source = 'rsync://rsync.gtlib.gatech.edu/archlinux/'
  # gatech times out frequently and has a poor mirror score (9/28/2013)
  source = 'rsync://mirror.us.leaseweb.net/archlinux/'
  #rsync_filter_list = ['- iso/2007.*', '- iso/2008.*', '- iso/2009.*']
  rsync_delete_delay = True
  rsync_delay_updates = True

