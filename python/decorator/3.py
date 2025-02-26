def greet(*args, **kwargs):
    name ,message ,*other = args
    print(f"Hello {name}, i wish u {message} and {other[0]}")
    print(kwargs)
    
    
greet("sam", "Goodluvk", "R", age=22)