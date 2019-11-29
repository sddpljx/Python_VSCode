# import module as namespace
import helper # helper is a namespace
helper.display('Not a warning')

# import all into current namespace
from helper import * # helper is a module
display('bbb')

# import 
from helper import helper
display('ccc')