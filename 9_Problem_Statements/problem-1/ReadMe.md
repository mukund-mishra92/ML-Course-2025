#### Data
#### Two data sets are provided, both in the same format:
#### common.csv -- this contains 10000 examples from a home where leaks are common so that we have about 100 examples of leaks
#### rare.csv -- this contains 50000 examples from a home where leaks are rare so that we have only 3 examples of a leak.

#### Each row of data is an example of an event where water was flowing. The data in each column contains aggregated information about the event.


#### The data set has the following attributes:
#### 1. time --  wall time for the start of the event (in UTC)
#### 2. day -- day of the week for the start of the event
#### 3. duration -- total number of seconds of water flow
#### 4. flow_rate -- average gallons per minute
#### 5. variability -- a unitless normalized measure of the variability of the flow rate
#### 6. isleak -- ground-truth label

 
#### Hints:
#### 1. You may assume that the rows are statistically independent from each other.
#### 2. The home in common.csv has a different behavior pattern than rare.csv

#### Task 1
#### Explore the data and produce a couple plots that visualize it in an informative way.  Document your approach to feature engineering: what preprocessing, if any, will you do with the data?

#### Task 2
#### Build a leak-detector for the data in common.csv. Please provide source code which does the following: 
#### trains on the data in common.csv as needed
#### reads a second csv file in the same format, and labels that data using the trained model
#### prints out metrics indicating the performance of the leak detector on the second csv input data


#### Task 3
#### Build a leak-detector for the data in rare.csv. Provide source code in the same format as in Task 2.


