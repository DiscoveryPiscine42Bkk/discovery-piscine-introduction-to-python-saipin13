def array_of_names(name_dict):
    """Builds a list of full names with capitalized first and last names."""
    full_names = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

# Test data
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# Output the result
print(array_of_names(persons))