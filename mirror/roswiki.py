from . import MirrorRunner
import subprocess

class RosWikiMirrorRunner(MirrorRunner):
  def update(self, verbose, dry_run):
    if not dry_run:
      subprocess.check_call(['/export/vg2/mirror_ros-www/wiki.sh'])

