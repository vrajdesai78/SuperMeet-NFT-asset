import json

# Function to create a JSON file based on the given index
def create_json_file(index, name):
    data = {
        "name": f"{name}",
        "symbol": "SM",
        "description": f"Collection of SuperMeet NFTs",
        "image": "0.png",
        "attributes": [
            {
                "trait_type": "Name",
                "value": name
            }
        ],
        "properties": {
            "files": [
                {
                    "uri": "0.png",
                    "type": "image/png"
                }
            ]
        }
    }

    # Save the data to a JSON file
    with open(f"{index}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

# Generate 10 JSON files
names = [
        "Neon Cipher",
        "Vapor Byte",
        "Nova Shock",
        "Cyber Scribe",
        "Synth Viper",
        "Byte Blade",
        "Holo Phantom",
        "Quantum Pulse",
        "Matrix Renegade",
        "Pulsewave Nexus"
    ]

for i in range(10):
    create_json_file(i, names[i])
