"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, list(fieldnames))
        writer.writeheader()
        for approach in results:
            approach_s = approach.serialize()
            approach_d = {
                'datetime_utc' : approach_s['datetime_utc'],
                'distance_au' : approach_s['distance_au'],
                'velocity_km_s' : approach_s['velocity_km_s'],
                'designation' : (approach_s['neo'])['designation'],
                'name' : (approach_s['neo'])['name'],
                'diameter_km' : (approach_s['neo'])['diameter_km'],
                'potentially_hazardous' : (approach_s['neo'])['potentially_hazardous']
            }
            writer.writerow(approach_d)    

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    approach_list = []
    with open(filename, "w") as outfile:
        for approach in results:
            approach_list.append(approach.serialize())
        
        outfile.write(json.dumps(approach_list))
        