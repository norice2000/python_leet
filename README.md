# Leet code trials

Test bed for attempting leet code


pattern
```
try:
    # Attempt the risky operation
    result = risky_operation()
except SpecificError as e:
    # Handle specific errors
    logging.error(f"Specific error occurred: {e}")
    return None
else:
    # This runs ONLY if no exception occurred
    logging.info("Operation successful")
    return result
finally:
    # Always runs (cleanup code)
    cleanup_resources()
```
