from . import MirrorRunner
import subprocess

class RosWikiMirrorRunner(MirrorRunner):
  def update(self, verbose, dry_run):
    if not dry_run:
      subprocess.check_call(['/export/btr0/ros.org/wiki.sh'])

