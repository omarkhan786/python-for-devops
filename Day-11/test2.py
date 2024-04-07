ec2_instances = [
    {
        'image_id': 'ami',
        'ec2_id': 'ec2001',
        'ec2_instance_type': 't2.micro',
        'ec2_security_group_id': 'abc',
        'ec2_security_group_name': 'xyz'
    },

    {
        'image_id': 'ami',
        'ec2_id': 'ec2002',
        'ec2_instance_type': 't2.medium',
        'ec2_security_group_id': 'abc',
        'ec2_security_group_name': 'xyz'
    },
]

#print(ec2_instances)
print(ec2_instances[0]['image_id'])

