spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# func to accept list
# returns string all items
# split to seperate by comma 
# and remoce space
# insert before the last item
# e.g.
# spa list returns 'apples, bananas, tofy, and cats'
# before to test case where an empty list [] is passed

def main():
    test_cases = [
        [],
        ['apples'], 
        ['apples', 'bananas'],
        ['apples', 'bananas', 'tofu'],
        ['apples', 'bananas', 'tofu', 'cats']
    ]
    for test_list in test_cases:
        result = tidy_output(test_list)
        print(f"Input: {test_list}")
        print(f"Output: '{result}'")
        print()
    # tidy_output(spam)


def tidy_output(inputs: list) -> str:

    if len(inputs) > 0:
        construct_word = ''
        for item in inputs[:-1]:
            construct_word = construct_word + item + ', '
        return f"{construct_word}and {inputs[-1]}"

if __name__ == "__main__":
    main()

