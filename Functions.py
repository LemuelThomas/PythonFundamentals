def main():
    #  Determine the shoe types based on the materials provided
    materials_1 = ['leather', 'rubber']
    materials_2 = ['canvas', 'rubber']
    materials_3 = ['mesh', 'rubber']
    #  Use the create_shoe function and check the result
    shoe1 = create_shoe(materials_1)
    shoe2 = create_shoe(materials_2)
    shoe3 = create_shoe(materials_3)

    shoes = [shoe1, shoe2, shoe3]
    for shoe in shoes:
        if shoe['type'] == 'Unknown':
            print(f"WARNING: You have an unknown shoe containing materials: {shoe['materials']}")
        else:
            print(f"Shoes created of type: {shoe1['type']}")

    print(f"\nShoe 1 is of type: {shoe1['type']}")
    print(f"Shoe 2 is of type: {shoe2['type']}")
    print(f"Shoe 3 is of type: {shoe3['type']}")

def create_shoe(materials_list):
    shoe_type = ''

    if 'leather' in materials_list and 'rubber' in materials_list:
        shoe_type = 'Boots'
    elif 'mesh' in materials_list and 'rubber' in materials_list:
        shoe_type = 'Sneakers'
    else:
        shoe_type = 'Unknown'
    return {'type': shoe_type, 'materials': materials_list}








if __name__ == "__main__":
    main()