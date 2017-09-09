def varargs(*args):
    return args

varargs(1, 2, 3)
    
def keyword_args(**kwargs):
    return kwargs
    print kwargs

keyword_args(big="foot", loch="ness")

def all_the_args(*args, **kwargs):
    print args
    print kwargs

a = 6
print a

while True:
    if a >= 1:
        all_the_args(1, 2, a=3, b=4)
        a -= 1
        print a

    else:
        kwargs= {"c": 5, "d": 6}
        all_the_args(**kwargs)
        break

