from pathlib import Path
import json

def ParseMicrConfig():
    base_dir = Path(__file__).parent.parent.resolve()
    cur_path = base_dir.joinpath('configs', 'microservices.json')
    with open(cur_path) as config:
        json_config = json.load(config)
    return json_config