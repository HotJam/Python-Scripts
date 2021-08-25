# tree = ET.parse('Filename.xml')
# root = tree.getroot() 

# root toma o valor de <Inventory>
# root.tag >>> Inventory
# root.attribute >>> {}

# children nodes
# for child in root:
#     print(child.tag, child.attrib)

# >>> Movie {}
# ... 


##############################################
# CSV fields

# title, description, year, duration, genre
# Coluna: 2, 14, 4, 7, 6

# python script.py -h       --> Mostra o formato para executar script
# python script.py <inputfile.csv> <outputfile>

import random 
import xml.etree.ElementTree as ET
import csv
import sys
import time

inputfile = ''
outputfile = ''
help_string = '\n\tFORMAT: script.py <inputfile> <outputfile>\n\tinputfile must be .csv\n\tDO NOT add extension to outputfile\n'

if sys.argv[1] == '-h':
    print(help_string) 
else:
    
    start = time.time()

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    print('Output File is "' + outputfile + '.xml"');

    entry = 1
    with open(inputfile, newline='\n', encoding='utf8') as csvfile:
        stream = csv.DictReader(csvfile)
        # stream = pd.read_csv(
        #     csvfile, 
        #     encoding='utf-8',
        #     usecols=[2,14,4,7,6],
        #     names=["Title","Description","ReleaseDate","Length","Genre"] 
        #     )
        root = ET.Element('Inventory')
        for row in stream:
            
            # Sequencia tem de coincidir com a sequencia de campos da xml port do nav
            # XML Port - Element Tree Structure
            movie = ET.SubElement(root, 'Movie')
            code = ET.SubElement(movie, 'Code')
            title = ET.SubElement(movie, 'Title')
            desc = ET.SubElement(movie, 'Description')
            year = ET.SubElement(movie, 'ReleaseDate')
            length = ET.SubElement(movie, 'Length')
            available = ET.SubElement(movie, 'Available')
            units = ET.SubElement(movie, 'Units')
            rate = ET.SubElement(movie, 'RentalRate')
            unitCheck = ET.SubElement(movie, 'UnitCheck')
            genre = ET.SubElement(movie, 'Genre')
            

            # Sub Element values
            code.text = str(entry)
            entry += 1
            title.text = row['title']
            limiter = row['description']
            desc.text = limiter[:250]
            year.text = str(row['year'])
            length.text = str(row['duration'])
            available.text = 'true'
            units.text = str(random.randint(1,10))
            rate.text = str(round(random.uniform(1,6), 2))
            unitCheck.text = str(0)
            genre.text = row['genre']

        # Write root element, containing all the sub element values to file
        mydata = ET.tostring(root, "utf-8")
        myfile = open(outputfile + '.xml', "wb")
        myfile.write(mydata)

    end = time.time()
    execution_time = end - start
        
    print('Done!')
    print('Execution Time: ' + str(round(execution_time,3)) + 's')