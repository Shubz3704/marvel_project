def apply_function(function, *args, **kwargs):
    """
    Apply a given function with arguments and keyword arguments.
    """
    try:
        return function(*args, **kwargs)
    except Exception as e:
        return {"error": str(e)}
