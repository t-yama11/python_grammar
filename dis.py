import dis

def func(name):
    return f'Hello, {name}'

if __name__ == "__main__":
    dis.dis(func)
