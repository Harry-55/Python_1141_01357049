def my_decorator(func): # func is the function being decorated
    def wrapper(*args, **kwargs): # wrapper is the new function
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs) # Call the original function
        print(f"After calling {func.__name__}")
        return result
    return wrapper # Return the new function
    # Step 2: Apply the Decorator
    # The @ syntax is equivalent to: greet = my_decorator(greet)
@my_decorator
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeting for {name}"
# Call decorated function
result = greet("Alice")
print(f"Result: {result}")
