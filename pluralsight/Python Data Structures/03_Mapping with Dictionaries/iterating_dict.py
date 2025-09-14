# Iterating over Dictionary Keys
status_messages = {
    200: "OK",
    404: "Not Found",
    500: "Server Error",
    403: "Forbidden"
}

# iterate over keys
for code in status_messages:
    print(f"code: {code}")

# iterate over values
for msg in status_messages.values():
    print(f"message: {msg}")

# iterate over items as key value
for k, v in status_messages.items():
    print(f"key: {k}\t value: {v}")


# prior to dict comprehension
file_sizes = {
    "report.pdf": 4,
    "photo.png": 2,
    "data.csv": 12
}

size_kb = {}
for filename, size in file_sizes.items():
    size_kb[filename] = size * 1024
print(size_kb)

# dict comprehension
compre_size = {}
size_kb = {filename: size * 1024 for filename, size in file_sizes.items()}
print(size_kb)