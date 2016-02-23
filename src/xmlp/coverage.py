#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom, os


current_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_directory, '../data')
        
file_path = os.path.join(data_directory, 'coverages.xml')
    

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse(file_path)

collection = DOMTree.documentElement
items = collection.getElementsByTagName("GIOSXMLEntry")

for item in items:
    type_code = item.getElementsByTagName('GIOSXMLCd')[0]
    occ_ind = item.getElementsByTagName('OccasionalDriverInd')
    if occ_ind:
        description = item.getElementsByTagName('EnglishDesc')[0]
        print "TypeCode: {0} OCC: {1} desc: {2}".format(type_code.childNodes[0].data, occ_ind[0].childNodes[0].data, description.childNodes[0].data)   


# 
# <collection shelf="New Arrivals">
# <movie title="Enemy Behind">
#    <type>War, Thriller</type>
#    <format>DVD</format>
#    <year>2003</year>
#    <rating>PG</rating>
#    <stars>10</stars>
#    <description>Talk about a US-Japan war</description>
# </movie>
# <movie title="Transformers">
#    <type>Anime, Science Fiction</type>
#    <format>DVD</format>
#    <year>1989</year>
#    <rating>R</rating>
#    <stars>8</stars>
#    <description>A schientific fiction</description>
# </movie>
#    <movie title="Trigun">
#    <type>Anime, Action</type>
#    <format>DVD</format>
#    <episodes>4</episodes>
#    <rating>PG</rating>
#    <stars>10</stars>
#    <description>Vash the Stampede!</description>
# </movie>
# <movie title="Ishtar">
#    <type>Comedy</type>
#    <format>VHS</format>
#    <rating>PG</rating>
#    <stars>2</stars>
#    <description>Viewable boredom</description>
# </movie>
# </collection>
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")

# Get all the movies in the collection
# movies = collection.getElementsByTagName("movie")


# Print detail of each movie.
# for movie in movies:
#    print "*****Movie*****"
#    if movie.hasAttribute("title"):
#       print "Title: %s" % movie.getAttribute("title")
# 
#    type = movie.getElementsByTagName('type')[0]
#    print "Type: %s" % type.childNodes[0].data
#    format = movie.getElementsByTagName('format')[0]
#    print "Format: %s" % format.childNodes[0].data
#    rating = movie.getElementsByTagName('rating')[0]
#    print "Rating: %s" % rating.childNodes[0].data
#    description = movie.getElementsByTagName('description')[0]
#    print "Description: %s" % description.childNodes[0].data