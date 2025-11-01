# Exercise
# Handle all the exception! Think back to the previous lessons to return the last name of the actor.

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}


# Function to modify!!!
def get_last_name():
    try:
        # Try to get last_name directly first
        return actor["last_name"]
    except KeyError:
        # If last_name key doesn't exist, extract it from the name
        try:
            full_name = actor["name"]
            return full_name.split()[-1]  # Get the last part of the name
        except (KeyError, IndexError, AttributeError):
            # Handle cases where name doesn't exist or can't be split
            return "Unknown"


# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
