# Lists are ordered collection of items
def main():
    # Create a list of AWS services
    aws_services = ['S3', 'EC2', 'Lambda', 'RDS', 'DynamoDB']
    print(f"AWS services list: {aws_services}")
    #  Access first service
    first_service = aws_services[0]
    print(f"First service: {first_service}")
    #  Access last service
    last_service = aws_services[-1]
    print(f"Last service: {last_service}")
    # Modify last service in the list
    aws_services[-1] = 'SNS'
    print(f"AWS services list: {aws_services}")
    # Add new service to the list
    aws_services.append('SQS')
    # Remove the second service from the list
    aws_services.pop(1)
    print(f"AWS services list: {aws_services}")
    # Slice the list to get services from index 1 to 3 (inclusive of 1 and exclusive of 3)
    sliced_services = aws_services[1:5]
    print(f"AWS services list: {sliced_services}")
    # Find the length of the list
    list_length = len(aws_services)
    print(f"The length of our AWS services is: {list_length}")


if __name__ == '__main__':
    main()
