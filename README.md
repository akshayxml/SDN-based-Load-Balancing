# SDN Ryu-Controller -- Load-Balancing with Dynamic-Routing

## Commands
- ryu-manager --observe-links multipath.py (for initializing the RYU controller)

- sudo mn -c
- sudo python topology.py (For initializing the topology of the network)

## Project Details: 

``OpenFlow version used:`` OpenFlow 1.3 


``Description:`` This project is created using Ryu controller which performs DIJKSTRA algorithm to find best paths, based on traffic flowing through links. Optimal path is being choosen from possible paths. The costs are being calculated in the background (action performed by thread and the path cost is calculated via network bandwidth calculation.) and optimal path is being updated every second based on the gathered stats. Discover of topology is done automatically so we don't have to have specially prepared topology. 


``DIJKSTRA ALOGRITHM USED:``
We have used Dijkstra algorithm to find the shortest available path from H1 to H2. The algorithm uses min heap functionality to calculate the smallest path cost. Following is the screenshot of the code.


