#!/usr/bin/python

# Although this script was written to generate directories, files, and commits for testing
# DVCSs, it can be used for any repeated command.
# Why Python and not Bash? a) I actually know how to code in Python and b) this script should
# work on Windows, but I haven't tested it on anything other than OSX. YMMV

# Examples:
# 
# util.py 'mkdir dir%(current)s; cd dir%(current)s; touch empty-file;' 1 100
# creates 100 flat directories, each with one empty file. Nice for testing Git.
#
# 

import sys, os

def nextArg(pop = False):
  args = sys.argv
  if len(args) > 0:
    if(pop):
      return args.pop(0)
    else:
      return args[0]

def appendCommand(command, env):
  execStr = ''
  for i in range(int(env['start']), int(env['stop']) + 1):
    execStr = execStr + command % env
    env['current'] = str(int(env['current']) + 1)
  print('Executing: ' + execStr)
  os.system(execStr)

def loopCommand(command, env):
  for i in range(int(env['start']), int(env['stop']) + 1):
    execStr = command % env
    env['current'] = str(int(env['current']) + 1)
    print('Executing: ' + execStr)
    os.system(execStr)

def __main():
  # The first arg should be the name of this script
  assert(nextArg(pop = True) == __file__)
  
  # Check for the append option
  if(nextArg() == '-a' or nextArg() == '--append'):
    append = True
    nextArg(pop = True)
  else:
    append = False
  
  env = {}
  env['command'] = command = nextArg(pop = True)
  env['start'] = env['current'] = nextArg(pop = True)
  env['stop']  = nextArg(pop = True)
  
  if(append):
    appendCommand(command, env)
  else:
    loopCommand(command, env)


if __name__ == "__main__":
  __main()
  
