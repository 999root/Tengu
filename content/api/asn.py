
# /content/lists
import os

#
def pull_user_agent_contents() -> list:
    """
    Pull the contents of User Agents
    """

    # Folder Path to the User Agents
    folder_path = os.path.join(os.path.dirname(__file__), 'lists', 'uas')

    # List to User Agents
    user_agents = []

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Only process .txt files
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            # Read the Content of the File
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Add each line (assumked to be user-agents) to the list
                user_agents.extend([line.strip() for line in lines if line.strip()])

    # Remove Duplicates
    user_agents = list(set(user_agents))

    # Return User Agents to the Function
    return user_agents