Etude 8, Drawing Bus Routes

Brodie Bosecke, 5471718

Download the attached files into the same folder

To run the program, cd into the directory where the downloads are. In your terminal type the command
    Python3 draw.py < filename.txt

RESUB 1: added another draw_network_edges list, and draw with specified alpha values according to 'in path' or 'not in path'
The file now also uses the correct shortest path first by using the weighting as values. I did a new test case with the 
Chch->Palmerston->Dunedin test case, and changed all the values to 1, or 2 (apart from Palmerston->Dunedin), and it showed the
correct path.

To see the alpha work (as I find it hard to distinguish for the node alpha), you can change line 293 float values, and
you will see that it does work, and draws differing alpha values.


I ran my drawing program with the following cases
____
Christchurch, Dunedin
Christchurch, Rolleston, 5.5
Rolleston, Temuka, 15
Temuka, Timaru, 16.5
Timaru, Oamaru, 27
Oamaru, Palmerston, 21.5
Palmerston, Dunedin, 23
Christchurch, Palmerston, 85.5
Shortest Path: Christchurch->Palmerston->Dunedin
____
Christchurch, Dunedin
Christchurch, Rolleston, 1
Rolleston, Temuka, 2
Temuka, Timaru, 2
Timaru, Oamaru, 1
Oamaru, Palmerston, 1
Palmerston, Dunedin, 23
Christchurch, Palmerston, 85.5
Shortest Path:Christchurch->Rolleston->Temuka->Timaru->Oamaru->Palmerston->Dunedin
___
A, E
A, B, 2
B, C, 4
D, E, 2
A, F, 2
F, G, 1
F, C, 10
G, E, 3
G, D, 10
Shortest Path: a->f->g->e
____
A, E
A, B, 2
B, C, 4
D, E, 1
A, F, 2
F, G, 1
F, C, 10
G, E, 3
G, D, 1
Shortest Path: a->f->g->d->e
____
Texas, New York
Texas, Mississippi, 20
Mississippi, North_Carolina, 20
North_Carolina, Boston, 30
Boston, New York, 10
Texas, South_Carolina, 40
South_Carolina, Indiana, 10
Indiana, New York, 5
OUTPUT: texas-south_carolina-indiana-new-york
____
Japan, USA
Japan,Rolleston, 135
Rolleston ,China, 15
China , USA, 222
Russia, Australia, 5
Australia, India, 12
India, USA, 23
Japan, India, 85.5
Shortest Path: japan->india->usa
____

The following test cases show the output errors expected. This is the outputs our program gave
____
DUPLICATE ROUTE:
Japan, USA
Japan,Rolleston, 135
Rolleston ,China, 15
China , USA, 222
Russia, Australia, 5
Australia, India, 12
India, USA, 23
Japan, India, 85.5
USA, India, 40050
OUTPUT: Invalid: Non-unique routes
_____

Japan, USA
Japan,Rolleston, 135, 200
Rolleston ,China, 15
China , USA, 222
Russia, Australia, 5
Australia, India, 12
India, USA, 23
Japan, India, 85.5
USA, India, 40050
OUTPUT: Invalid: route set
____
Japan, USA, 200
Japan,Rolleston, 135, 200
Rolleston ,China, 15
China , USA, 222
Russia, Australia, 5
Australia, India, 12
India, USA, 23
Japan, India, 85.5
USA, India, 40050
OUTPUT: Invalid: route