"""
Problem 3: Logica bypassTime Left: 
02:21:51
King Lear's wants to increase security in his kingdom, but not at the cost of time. Help him out 
with your programming skills.You'll need to write a program to return the same security checksum 
that the royal guards would have after they would have checked all the workers through. 
Fortunately, King Lear's desire for efficiency won't allow for hours-long lines, so 
the checkpoint royal guards have found ways to quicken the pass-through rate. 
Instead of checking each and every worker coming through, the royal guards instead go over 
everyone in line while noting their security IDs, then allow the line to fill back up. 
Once they've done that they go over the line again, this time leaving off the last worker. 
They continue doing this, leaving off one more worker from the line each time but recording 
the security IDs of those they do check, until they skip the entire line, at which point they XOR 
the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the workers' orderly 
nature causes them to always line up in numerical order without any gaps.For example, if the first worker
 in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:

0   1   2   /
3   4   /   5
6   /   7   8

Where the royal guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.Likewise, if the first worker has ID 17, and
 the checkpoint holds four workers, the process would look like:

17   18   19   20   /
21   22   23   /   24
25   26   /   27   28
29   /   30   31   32

which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.All worker 
IDs (including the first worker) are between 0 and 3,000,000,000 inclusive, and the checkpoint line length
 will always be at least 1 worker long.
With this information, write a function checksum(start, length) that will cover for the missing security checkpoint
 by outputting the same checksum the royal guards would normally submit before lunch. You have just enough 
time to find out the ID of the first worker to be checked (start) and the length of the line (length) before 
the automatic review occurs, so your program must generate the proper checksum with just those two values. 

Test Case 1:
Input:
(int) start = 0, (int) length = 3
Output:
(int) 2Test Case 2:
Input:
(int) start = 17, (int) length = 4
Output:
(int) 14
If your code is taking more than a second to execute, you are not doing it right. Think smarter!


"""