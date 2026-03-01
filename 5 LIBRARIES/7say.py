import sys
# import cowsay
from sayings import hello, goodbye
# import sayings

if len(sys.argv) != 2:
    sys.exit()

name = sys.argv[1]

# sayings.hello(name)
# sayings.goodbye(name)
hello(name)
goodbye(name)
