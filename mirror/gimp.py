from . import RsyncMirrorRunner, EXTRAS
import os

class GIMPMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://mirror-mdu-edu@download.gimp.org/gimp/pub'
  rsync_delete_delay = True
  rsync_preserve_perm = True

  def pre_update(self, verbose, dry_run):
    os.environ['RSYNC_PASSWORD'] = open(os.path.join(EXTRAS, 'gimp-rsync.password'), "r").read().strip()

