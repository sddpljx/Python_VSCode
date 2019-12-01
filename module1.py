# import module as namespace
from helper import display
import helper  # helper is a namespace
helper.display('Not a warning')

# import all into current namespace
# from helper import * # helper is a module
#display('bbb', True)

# import
display('bbb', True)
display('ccc', False)
