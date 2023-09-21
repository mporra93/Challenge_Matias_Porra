

# Avoiding to use any external library like unittest as requested
from main import dict_processor  


def test_dict_processor():

    # Test with valid data
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 40},
        {'name': 'David', 'age': 35}
    ]
    filter_key = 'age'
    numeric_key = 'age'
    result = dict_processor(data, filter_key, numeric_key)
    if (result == 32.5):
        print("Test case 1 success")
    else:
        print("Test case 1 failed")


    # Test with invalid filter_key
    filter_key = 'non_existent_key'
    numeric_key = 'age'
    try:
        dict_processor(data, filter_key, numeric_key)
        print("Test case 2 failed")
    except AssertionError as e:
        if (str(e) == "both 'non_existent_key' and 'age' must be keys in at least one dictionary in the data list."):
            print("Test case 2 success")
        else:
            print("Test case 2 failed")


    # Test with invalid numeric_key
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 40},
        {'name': 'David', 'age': '35'},  # Age is not a numeric value
    ]
    filter_key = 'age'
    numeric_key = 'age'
    try:
        dict_processor(data, filter_key, numeric_key)
        print("Test case 3 failed")
    except Exception as e:
        if (str(e) == "There is a value that is not an instance of int neither float"):
            print("Test case 3 success")
        else:
            print("Test case 3 failed")

#just press run
if __name__ == '__main__':
    test_dict_processor()
