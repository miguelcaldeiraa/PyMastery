# The __name__ variable is a specific property of each Python module.
# When the module is imported, the value of __name__ is different from '__main__'.
# When the module is executed directly, the value of __name__ is '__main__'.

if __name__ == '__main__':
    print("I was executed directly, not imported")
