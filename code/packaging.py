'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''
    output = []
    #credit to chatgpt for this idea
    segments = packaging_data.split(" / ")
    
    #remember that the for loop program repeats this process 
    #for each section of the input separated by a /
    #so ideally if u work on the first section it your code should make it
    #so that it is reflected on the rest of the input sections
    for section in segments:
        item_container_split = section.split(" in ")
        item_pieces = item_container_split[0].split()
        container_pieces = item_container_split[1].split()

        #remember item in one section becomes container in the next
    #items labeling:
        item_no = int(item_pieces[0])
        item = item_pieces[1]

    #container labeling:
        container_no = int(container_pieces[0])
        container = container_pieces[1]

        output.append({item: item_no}) 
        if section == segments[-1]:
            output.append({container: container_no})
        
    #  print(item_pieces, container_pieces, item_no, item, container_no, container)
    return output

#testing function out
#parse_packaging("6 bars in 1 pack / 12 packs in 1 carton")

def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''

    #code cleaned up (without the need to add to list then multiply:)
    total = 1
    for element in package: 
        unit = (list(element.values())[0])
        total *= unit
    return total
   # output = parse_packaging(package)
  #  if value in output == int:

#append every unit to a list, then multiply everything withiin list
# then parse to int when you get final product
        #return len()

#package = [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
#units = []

#for element in package:
    #units.append(list(element.values())[0])

#total = 1
#for int in units: 
   # total *= int # same as total = total * int

#print(total)

#for element in package:
    #units.append(list(element.values()))
    
#print(int(units))

def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    return list(package[0].keys())[0]
    #leaving out the second 0 returns all keys in the selected element
    #putting [0] inside parentheses is incorrect since that would be indexing keys
    #before converting to a list, 
    #which would give an error bc object view of keys is not indexable

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")

    #for sanity checks rather than writing a full test
    #name = main 
    #python has internaal variable called name of what runs, if you run the file the name of it is main