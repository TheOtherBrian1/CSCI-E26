#!/bin/sh

# Question 3:
    # Write a shell script called busiest-hour that contains 
    # one pipeline to find which hour of the day has the most 
    # train stop events on a given day: m-f, sa, or su. 
    # The script should take an argument of m-f, sa, or su 
    # and print out the hour of the day which contains 
    # the largest number of records in the sched file and 
    # the number of records for that hour.

#Example of file being analyzed:
    #TR=002;dir=i;day=m-f;TI=04:50;stn=middleborough/lakeville;Line=middleborough;zn=8
    #TR=002;dir=i;day=m-f;TI=05:00;stn=bridgewater;Line=middleborough;zn=6

#References used:
    # https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-5.html
    # https://www.redhat.com/sysadmin/uniq-command-lists
    # https://unix.stackexchange.com/questions/170043/sort-and-count-number-of-occurrence-of-lines
    # https://www.geeksforgeeks.org/head-command-linux-examples/
    # https://www.hostinger.com/tutorials/bash-concatenate-strings


#Find lines with user inputted days and then finds out which hours have the most 

grep day="$1" sched | 
    \cut -d";" -f4 | #Isolate time section
    \cut -d"=" -f2 | #Isolate time from time section
    \cut -d":" -f1 | #Isolate hour from time section 
    \uniq -c | #Count unique occurences of each hour
    \sort -r | #Sort the occurences from most common to least
    \head -n 1 #Return the first line, which should contain the 
               #occurences of the most common hour followed by the most common hour