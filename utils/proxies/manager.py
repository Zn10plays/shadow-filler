import os
import dotenv
import random

dotenv.load_dotenv()

PROXY_SERVER = os.getenv("PROXY_SERVER", "")
PROXY_USERNAME = os.getenv("PROXY_USERNAME", "")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD", "")

# proxy ranges form 30000-30999
proxy_ports = [str(port) for port in range(30000, 31000)]    

instances = {}

def get_proxy(instance_id: str | None = None) -> str | None:
    global instances

    if instance_id is not None and instance_id in instances:
        return instances[instance_id]
    elif instance_id is None:
        instance_id = str(random.randint(1000, 9999))

    if PROXY_SERVER and PROXY_USERNAME and PROXY_PASSWORD:
        proxy = f'{PROXY_SERVER}:{random.choice(proxy_ports)}:{PROXY_USERNAME}:{PROXY_PASSWORD}'
        instances[instance_id] = proxy
        return proxy

def terminate_proxy(instance_id: str) -> bool:
    global instances

    # remove the instance from the dictionary
    if instance_id in instances:
        del instances[instance_id]
        return True
    return False