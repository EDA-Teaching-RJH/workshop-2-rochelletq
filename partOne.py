def main():
    slow = input(" press enter ")
    myFunction(slow)

def myFunction(slow):
    name = input("What's your name? ")
    name=name.strip().title()
    name = name.replace(" ", "...")
    print(f" {name}")
          
main()
          



