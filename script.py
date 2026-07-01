if len(__import__('sys').argv) < 2:
    print(f"Usage: {__import__('sys').argv[0]} <name>")
    __import__('sys').exit(1)

print(f"Hello {__import__('sys').argv[1]}, right now the time is {__import__('time').strftime('%Y-%m-%d %H:%M:%S %Z')}")
