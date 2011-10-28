# This is an example of a mirror definition file. Change settings
# as appropriate and then delete the notes. If you would like to
# mirror an APT archive using HTTP or FTP, see the example at the
# end of the file.
#
# This name of this file should be the lowercase version of the
# archive name, matching the name of the class below. So if
# you're mirroring TerpLinux, your class will be called 
# TerpLinuxMirrorRunner, and your file will be terplinux.py.
# To run the script, you'd use `run_mirror.py [-v] [-n] terplinux'.

# Always use this:
from . import MirrorRunner

# If you're using files in extras/, you'll need these:
from . import EXTRAS 
import os

# Name this class to match your content.
class TerpLinuxMirrorRunner(MirrorRunner):
  # Note the slash at the end. If you don't include it, rsync
  # might do nasty things, like making a second copy of your archive.
  # It'd probably be safe to automate this, but no.
  source = 'rsync://rsync.terplinux.umd.edu/terplinux/'

  # You probably shouldn't set these: (the scripts will take care of that)
  #base_subdir = name_of_this_module
  #base = /path/to/pub/{base_subdir}

  # rsync options.
  #rsync_archive = True # You want to leave this set to true.
  #rsync_preserve_perm = False # Set this if the upstream does "bitflips"
  #rsync_delete = True # Whether to delete files that don't exist upstream
  #rsync_delete_excluded = False # Delete things even if they're excluded
  #rsync_delete_delay = False # Compute deletes during run, delete at the end
  #rsync_delay_updates = False # Delay any updates until the end
  #rsync_filter_from = None # Path to a file in the --filter-from format
  #                           e.g. os.path.join(EXTRAS, 'terplinux.excludes')
  #rsync_filter_list = None # List of exclusion rules
  #                           e.g. ['- DVD', '- /releases/old', ...]

  # Need to do something unusual before the rsync? Define this method
  #def pre_update(self, verbose, dry_run):
  #  pass

  # How about after rsync runs?
  #def post_update(self, verbose, dry_run):
  #  pass

# If your source doesn't provide an rsync server, APT might be appropriate.
# This uses the apt-mirror script.
#
# Delete this class if you're using rsync.
class TerpLinuxPackagesMirrorRunner(APTMirrorRunner):
  source = 'http://packages.terplinux.umd.edu/terplinux'

  # The archive will be downloaded to /.../pub/packages.terplinux.umd.edu.

  # What parts of the archive you want to mirror:
  apt_releases = ['dback', 'mangrove', 'pileata']
  apt_architectures = ['i386', 'amd64', 'src']
  apt_slots = ['', '-updates'] # default: ['']
  apt_parts = ['main', 'contrib', 'non-free']

  # As above, you may define pre_ and post_update, but make sure that you
  # call the corresponding methods in APTMirrorRunner.

