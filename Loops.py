#  Definite interation: The number of repititions is specified explicitly in advance -- For loop
#  Indefinite interation: The number of repeititions isn't specified in advance -- While loop

def main():
    #  List of AWS Services
    aws_services = ['S3', 'Lambda', 'EC2', 'RDS', 'DynamoDB']
    print(f"AWS services list: {aws_services}")
    #  Use a for loop to interate through the list
    print(f"\nUsing a for loop to iterate through the list:")
    for service in aws_services:
        print(f"Service: {service}")
    # Use a while loop to iterate through the list in reverse order
    print(f"\nUsing a while loop to iterate through the list in reverse order:")
    index = len(aws_services) - 1
    while index >= 0:
        print(aws_services[index])
        index -= 1
    #  Using enumerate() with a for loop to get both index and value
    print(f"\nUsing enumerate() with for loop to get both index and value:")
    for index, service in enumerate(aws_services):
        print(f"Service # {index + 1}: {service}") #  Add '+1' to index to make the list start at 1.






if __name__ == "__main__":
    main()