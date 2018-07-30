import os
import subprocess

from . import RsyncMirrorRunner, EXTRAS

class FedoraLinuxMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'fedora/alt'
  # Haven't found other mirrors yet, but would like to. RIT frequently refuses
  # our connection due to too many connections.
  source = 'rsync://mirror.rit.edu/fedora-alt/'

  rsync_filter_list = ['+ live-respins/', '- /*']
  rsync_preserve_hardlinks = True
  rsync_preserve_perm = True
  rsync_delete_excluded = True

