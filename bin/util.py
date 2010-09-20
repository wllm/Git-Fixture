#!/usr/bin/python
import sys, os

def nextArg(args):
  if len(args) > 0:
    return args.pop(0)

def __main():
  args = sys.argv
  
  # The first arg should be the name of this script
  assert(args.pop(0) == __file__)
  
  command = nextArg(args)
  
  env = {}
  env['start'] = start = nextArg(args)
  env['stop']  = stop = nextArg(args)
  
  for i in range(int(start), int(stop) + 1):
    env['current'] = i 
    execStr = command % env
    print('executing: ' + execStr)
    os.system(execStr)
    
if __name__ == "__main__":
  __main()