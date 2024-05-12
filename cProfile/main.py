import cProfile

def sum ():
    print(1, 3)

cProfile.run('sum()')

"""
Ordered by: standard name:

For example, if there are functions named function_A,
function_B, and function_C, they will appear in 
the profiling results in alphabetical order: 
function_A, function_B, function_C.

-----------------------------------------------

<string>:1(<module>): This is the call to the module's 
main code block, where sum() is invoked. 

main.py:3(sum): This is the call to the sum() function
itself.

built-in method builtins.exec: This is the call to 
execute the code inside the cProfile.run() function, 
which includes the calls mentioned above.

built-in method builtins.print: This is the call to 
the print() function within your sum() function.

method 'disable' of '_lsprof.Profiler' objects: 
This is an internal call to disable the profiler 
after it has completed its profiling.

-----------------------------------------------

There can be other options for "Ordered by" :

'calls': Sorts the output by the number of calls 
to each function.
'cumulative': Sorts the output by cumulative time, 
which includes the time spent in the function itself 
plus the time spent in all functions called from it.
'file': Sorts the output by filename.
'line': Sorts the output by line number.
'module': Sorts the output by module name.
'name': Sorts the output by function name.
'nfl': Sorts the output by name, file, and line.
'stdname': Sorts the output by standard name, which 
is similar to 'name' but avoids displaying the module 
name in the function name.
"""