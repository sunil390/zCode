# Create a dictionary to store tasks and their dependencies
tasks = {}

# Add tasks to the dictionary
tasks["create_project_plan"] = {"completed": False, "dependencies": []}
tasks["gather_requirements"] = {"completed": False, "dependencies": ["create_project_plan"]}
tasks["design_system"] = {"completed": False, "dependencies": ["gather_requirements"]}
tasks["develop_features"] = {"completed": False, "dependencies": ["design_system"]}
tasks["test_features"] = {"completed": False, "dependencies": ["develop_features"]}
tasks["deploy_features"] = {"completed": False, "dependencies": ["test_features"]}

# Check the status of tasks
for task in tasks:
    if tasks[task]["completed"]:
        print(f"{task} is completed")
    else:
        print(f"{task} is not completed")

# Check the dependencies of tasks
for task in tasks:
    if tasks[task]["dependencies"]:
        print(f"{task} has dependencies: {tasks[task]['dependencies']}")
    else:
        print(f"{task} does not have dependencies")
# Import the json module
import json

# Write the dictionary to a file
with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)

# Read the dictionary from a file
with open("tasks.json", "r") as f:
    tasks_from_file = json.load(f)

# Check if the dictionaries are equal
assert tasks == tasks_from_file
