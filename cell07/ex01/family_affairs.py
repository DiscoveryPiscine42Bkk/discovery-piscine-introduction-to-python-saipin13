def find_the_redheads(family_dict):
    """Returns a list of first names with red hair using the filter function."""
    return list(filter(lambda name: family_dict[name] == "red", family_dict))

# Example dictionary
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# Output the result
print(find_the_redheads(dupont_family))