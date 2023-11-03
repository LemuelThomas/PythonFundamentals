def main():
    user_requirement = 'serverless_computing'

    if user_requirement == 'file_storage':
        aws_service = 'S3'
    elif user_requirement == 'virtual_server':
        aws_service = 'EC2'
    elif user_requirement == 'serverless_computing':
        aws_service = 'Lambda'
    else:
        print("Unknown")

    if user_requirement != 'Unknown':
        print(f"AWS service required is {aws_service}")

if __name__ == '__main__':
    main()
