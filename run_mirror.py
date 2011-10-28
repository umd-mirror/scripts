#!/usr/bin/env python
import sys
#sys.path.append('/home/blah/libexec') ...

import inspect
import mirror

if __name__ == '__main__':
  invalid_args = False
  verbose = False
  dry_run = False

  modules = []
  for arg in sys.argv[1:]:
    if arg == '-v':
      verbose = True
    elif arg == '-n':
      dry_run = True
    elif arg[0] == '-':
      invalid_args = True
    else:
      modules.append(arg)

  if len(modules) == 0 or invalid_args:
    print "USAGE: %s [-v] [-n] <mirror names>" % sys.argv[0]
  else:
    for name in modules:
      if mirror.get_lock(name):
        mirror_imp = __import__("mirror", fromlist=[name])

        runner_module = getattr(mirror_imp, name)

        for module_name in dir(runner_module):
          item = getattr(runner_module, module_name)
          if inspect.isclass(item) and item != mirror.MirrorRunner and issubclass(item, mirror.MirrorRunner):
            if item != mirror.APTMirrorRunner:
              if verbose:
                print "Running", item
              runner = item()
              runner.run(verbose=verbose, dry_run=dry_run)
      else:
        print "Skipping", name


