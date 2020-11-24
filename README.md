# The Travelling Judges Problem

A group of judges must get together to judge a contest held in a particular city, and they need to figure out the cheapest way of renting cars in order to get everyone to the contest. They observed that it might be cheaper if several judges share a rental car during all or part of the trip, thus reducing the overall cost. Your task is to identify the routes the judges should take in order to minimize the total cost of their car rentals.

We will make the following assumptions:

- The cost of a rental car is proportional to the distance it is driven. There are no charges for more than one occupant in the car, fuel, insurance, or leaving the car in a city other than that in which it was rented.

- All rental cars are billed at the same rate per mile.

- A rental car can accommodate any number of passengers.

- At most one road directly connects any pair of cities. Each road is two-way and has an integer length greater than zero.

- There is at least one route from every judge’s starting city to the city in which the contest is held.

- All judges whose routes to the contest take them from or through the same city travel from that city to the contest together. (A judge might arrive at a city in one car and leave that city in a different car.)


## Input

The input contains several test cases. Each test case includes a route map, the destination city where the contest is being held, and the cities where the judges are initially located.
Each case appears in the input as a list of integers separated by blanks and/or ends of lines. The order and interpretation of the integers in each case is as follows:

- $n_c$: the number of cities that appear in the route map; this will be no larger than 20.

- $d_c$: the number of the destination city, assuming the cities are numbered 1 to $n_c$.

- $n_r$: the number of roads in the route map. Each road connects a distinct pair of cities.

- For each of the $n_r$ roads, three integers $c_1,~ c_2$ and $l$. $c_1$ and $c_2$identify two cities connected by a road, and $l$ gives the distance between these cities along that road.

- $n_j$: the number of judges. This number will be no larger than 10.

- $n_j$ integers, one for each judge – each of these is a city number identifying the initial location of that judge.

The data for the last case will be followed by a line consisting of the integer –1.


## Output

For each test case, display the case number (1, 2, ...) and the shortest total distance traveled by the rental cars conveying the judges to the contest. Then display the list of routes used by the judges, each route on a separate line, in the same order as the ordering of starting cities given in the input. Each route consists of the cities that the corresponding judge must visit, listed in the order in which they are visited, starting with the judge’s starting city and ending with the contest city. Any other cities along the route are listed in the order in which they are visited during the judge’s travels. Separate the numbers in the route with “–”, and precede each route by three spaces.

If multiple sets of routes have the same minimum distance, choose a set that requires the fewest number of cities. If several sets of cities of the same cardinality may be used, choose the set that comes lexicographically first when ordered by city number (e.g., $\{2, 3, 6]\}$ rather than $\{2, 10, 5\}$). If multiple routes are still available, output any set of routes that meets the requirements.

Follow the format of the sample output shown below for the corresponding input.


## Sample Input

    5 3 5 
    1 2 1
    2 3 2 
    3 4 3
    4 5 1
    2 4 2
    2 5 1

    4 4 3
    1 3 1
    2 3 2
    3 4 2
    2 1 2

    3 3 3
    1 2 2
    1 3 3
    2 3 1
    2 2 1
    -1


## Sample Output

    Case 1: 
    distance = 6 
        5-4-2-3
        1-2-3

    Case 2:
    distance = 5 
        1-3-4
        2-3-4

    Case 3: distance = 3 
        2-3
        1-2-3
