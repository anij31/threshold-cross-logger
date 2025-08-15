## Project Context

For any sensor, there are domain-defined erroneous readings that have to be discussed in a sensor-fusion or IOT system. Any sensor can be polled with a defined periodicity, and readings must be logged, however, it is almost always beneficial to have a separate log of erroenous readings. Our ability to troubleshoot the system absolutely comes from recognizing that systematic errors can occur. 

Once erroneous readings are logged, they serve as important data points to sample for neighboring data points with past and future timestamp values. Erroneuous readings can then be correlated with other readings from other sensors downstream, if connected in such a way. We must take into consideration any dependency graph of sensor units involved in our system. That dependency graph becomes crucial in any troubleshooting. Sometimes, in a system, one can get completely fine reading in one sensor, but a disaster could be happening in that system. In such cases, a dependency graph can help for sanity checking of the entire system. 

It is important to not rely on any single sensor, but to see the system as a flow of information from sensor to sensor in a graph. You should always aim to have a graph of sensors in a system if you want aid in troubleshooting. For large industrial systems, this is no-brainer. Even if it become a multi-year project, the long term benefits of such a system always ends up on the side of safety, cost-savings and time-saving. 

### Repository 
This repository aims to demonstrate modeling of a sensor system as a graph problem, and logging as its foundation.

