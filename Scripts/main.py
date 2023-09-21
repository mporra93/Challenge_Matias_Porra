

def dict_processor(data: dict, filter_key: str, numeric_key: str) -> float:
    '''Process a dictionary by filtering, calculating the average of specified keys.'''

    def _filterDict(data: dict, filter_key: str) -> dict:
        '''Filter a dictionary by removing entries with a specified key's None values.'''
        filtered_data = [d for d in data if d.get(filter_key) is not None]
        return filtered_data
    
    def _calculateAverage(data: dict, numeric_key: str) -> float:
        '''Calculate the average value of a specified numerical key in a dictionary, raising an exception for non-numeric values.'''
        total = 0
        count = 0
        for d in data:
            if isinstance(d.get(numeric_key), (int, float)):
                total += d[numeric_key]
                count += 1
            else:
                raise Exception('There is a value that is not an instance of int neither float')

        # Calculate the average value
        if count == 0:
            return None
        else:
            return total / count

    # Checking if keys are part of at least one dictionary
    assert any(filter_key in d and numeric_key in d for d in data), f"both '{filter_key}' and '{numeric_key}' must be keys in at least one dictionary in the data list."

    filtered_dict = _filterDict(data, filter_key)
    average = _calculateAverage(filtered_dict, numeric_key)
    return average

