import os
import shutil
import tempfile

from . import MirrorRunner, EXTRAS

class MozillaMirrorRunner(MirrorRunner):
  source = 'rsync://mozilla-osl.osuosl.org/mozilla/'
  rsync_delete_excluded = True

  def pre_update(self, verbose, dry_run):
    # This stuff was from when I was just pulling some popular files.
    # (filter_file_fd, filter_path) = tempfile.mkstemp(prefix='mozilla')
    # filter_file = os.fdopen(filter_file_fd, 'w')
    
    # custom_path = os.path.join(EXTRAS, 'mozilla-custom.exclude')
    # distro_path = os.path.join(self.base, 'zz', 'rsyncd-mozilla-current.exclude')

    # shutil.copyfileobj(open(custom_path, 'rb'), filter_file)
    # shutil.copyfileobj(open(distro_path, 'rb'), filter_file)
    # filter_file.close()

    # self.rsync_filter_from = filter_path

    # if verbose:
    #   print ">>> Filter compiled at", filter_path
    pass

  def post_update(self, verbose, dry_run):
    # os.unlink(self.rsync_filter_from)
    pass

# $RSYNC $STOPTS $PATH $BASE/mozilla --filter=". $SCRIPTS/patterns/mozilla" --delete-excluded
