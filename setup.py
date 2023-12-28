from instances import Instances
from utils import save_dict_to_file

def main():
    instances = Instances()
    vpc_id = instances.get_vpc_id()

    instances.create_security_group(vpc_id)
    instances.create_key_pair()

    security_groups = ["default", instances.security_group["name"]]
    instances.launch_instances(5, "t2.micro", security_groups)
    instances.wait_until_instances_are_running()

    instance_data = {
        "instance_ids": instances.instance_ids,
        "security_group": instances.security_group,
        "key": instances.key,
    }

    save_dict_to_file(instance_data, './data/aws_resources.json')

    with open("./data/key.pem", "w") as key_file:
        key_file.write(instances.key["KeyMaterial"])

if __name__ == "__main__":
    main()