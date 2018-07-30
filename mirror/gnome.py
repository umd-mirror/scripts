from . import RsyncMirrorRunner, EXTRAS
import os

class GNOMEMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://master.gnome.org/gnomeftp/'
  rsync_delete_delay = True
  rsync_preserve_perm = True

  def pre_update(self, verbose, dry_run):
    os.environ['RSYNC_PASSWORD'] = open(os.path.join(EXTRAS, 'gnome-rsync.password'), "r").read().strip()

