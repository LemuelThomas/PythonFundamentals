# Dictionaries is an unordered collection of key-value pairs
def main():
    #  Create a dictionary of AWS services and their descriptions
    aws_services = {
        'S3': "Amazon S3 is a object storage service provided by AWS",
        'Lambda': "AWS Lambda is a serverless computing service provided by AWS",
        'EC2': "Amazon EC2 is a web service provided by AWS"
    }
    #  Print the dictionary
    print(aws_services)

    #  Access the description of an item in the dictionary
    lambda_description = aws_services['Lambda']
    print(f"\nDescription of lambda: {lambda_description}")

    #  Modify the description of a service of a service
    aws_services['Lambda'] = "AWS Serverless compute service"
    print(f"\nUpdated Description of lambda: {aws_services}")

    # Add a new service and its description to the dictionary
    aws_services['SNS'] = "Simple notification service"
    print(f"\nAdded SNS: {aws_services['SNS']}")

    # Remove a service from the dictionary
    del aws_services['Lambda']
    print(f"\nRemoved Lamda: {aws_services}")
    # Use the keys(), values(), and items() methods to display different aspects of the dictionary
    print()
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items())

    # Modify the dictionary to add a nested structure with additional information (launch_year)
    aws_services['EC2'] = {
        'description': "Elastic Compute Cloud",
        'launch_year': 2006
    }
    print("\nModified dictionary with nested structure:")
    print(aws_services)


if __name__ == "__main__":
    main()