import os
import subprocess

from . import MirrorRunner, EXTRAS

class FedoraMirrorRunner(MirrorRunner):
  source = 'rsync://archive.linux.duke.edu:874/fedora/linux/'
  rsync_preserve_perm = True

  def post_update(self, verbose, dry_run):
    if not dry_run:
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')])

#$RSYNC $STOPTS -H \
#$HOST \
#$BASE/fedora/linux \
#--filter=". $PATTERNS/fedora" \
#-m --partial --delete-excluded

#date -u > $BASE/fedora/mirror.umoss.org.txt

#$RSYNC $STOPTS rsync://download.wpi.edu:874/fedora-epel/ $BASE/fedora/epel --exclude={debug,repoview,/testing,SRPMS}

#$SCRIPTS/report_mirror -c $SCRIPTS/report_mirror.conf
## $SCRIPTS/report_mirror -c $SCRIPTS/report_mirror-oncampus.conf

