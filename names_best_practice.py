def main():
    names = ['Joe', 'Jane', 'Alice', 'Annie', 'Matt']
    for a_name in names:
        greet(a_name)
    print('END')

def greet(name):
    print(f'Hello, {name}')
    uppercase_name = name.upper()
    print(f'YOU ARE AWESOME, {uppercase_name}!')

if __name__ == "__main__":
    main()
