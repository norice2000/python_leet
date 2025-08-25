class AWSInstance:
    def __init__(self, instance_id, instance_type, region):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region = region
        self.state = "stopped"
        self.tags = {}
        self.security_groups = []

    def start_instance(self):
        """Start the EC2 instance"""
        if self.state == "stopped":
            self.state = "running"
            print(f"Starting {self.instance_id} ({self.instance_type}) in {self.region}")
            return True
        else:
            print(f"Instance {self.instance_id} is already {self.state}")
            return False

    def stop_instance(self):
        """Stop the EC2 instance"""
        if self.state == "running":
            self.state = "stopped"
            print(f"Stopping {self.instance_id}")
            return True
        else:
            print(f"Instance {self.instance_id} is not running")
            return False

    def add_tag(self, key, value):
        """Add a tag to the instance"""
        self.tags[key] = value
        print(f"Added tag {key}={value} to {self.instance_id}")

    def add_security_group(self, sg_id):
        """Attach a security group"""
        if sg_id not in self.security_groups:
            self.security_groups.append(sg_id)
            print(f"Added security group {sg_id} to {self.instance_id}")

    def get_status(self):
        """Get comprehensive instance status"""
        return {
            "instance_id": self.instance_id,
            "type": self.instance_type,
            "region": self.region,
            "state": self.state,
            "tags": self.tags,
            "security_groups": self.security_groups
        }

# Create instances
web_instance = AWSInstance("i-1234567890abcdef0", "t3.medium", "ap-southeast-1")
db_instance = AWSInstance("i-0987654321fedcba0", "r5.large", "ap-southeast-2")

# Use the instances
web_instance.add_tag("Name", "WebServer")
web_instance.add_tag("Environment", "Production")
web_instance.add_security_group("sg-web-80-443")
web_instance.start_instance()

db_instance.add_tag("Name", "DatabaseServer")
db_instance.add_security_group("sg-db-3306")
db_instance.start_instance()

# Check status
print("\n Instance Status:")
print(web_instance.get_status())
print(db_instance.get_status())