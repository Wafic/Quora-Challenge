# Quora Upvote Challenge

The problem statement for this code can be found [here](https://www.quora.com/challenges). 

Below is a copy of the problem statement with some alterations to match my input and output format.

## Problem Statement

At Quora, we have aggregate graphs that track the number of upvotes we get each day.

As we looked at patterns across windows of certain sizes, we thought about ways to track trends such as non-decreasing and 
non-increasing subranges as efficiently as possible.

For this problem, you are given N days of upvote count data, and a fixed window size K. For each window of K days, 
from left to right, find the number of non-decreasing subranges within the window minus the number of non-increasing 
subranges within the window.

A window of days is defined as contiguous range of days. Thus, there are exactly N−K+1N−K+1 windows where this metric 
needs to be computed. A non-decreasing subrange is defined as a contiguous range of indices [a,b][a,b], a<ba<b, 
where each element is at least as large as the previous element. A non-increasing subrange is similarly defined, 
except each element is at least as large as the next. There are up to K(K−1)/2K(K−1)/2 of these respective subranges 
within a window, so the metric is bounded by [−K(K−1)/2,K(K−1)/2][−K(K−1)/2,K(K−1)/2].

## Constraints

- 1 ≤ N ≤ 100,000 days 
- 1 ≤ K ≤ N days

## Input Format

Input N, K and a list of N positive upvote counts into the 'Upvotes' module

## Output Format

A list of scores for each window of size K

## Explanation

For the first window of [1, 2, 3], there are 3 non-decreasing subranges and 0 non-increasing, so the answer is 3. 
For the second window of [2, 3, 1], there is 1 non-decreasing subrange and 1 non-increasing, so the answer is 0. 
For the third window of [3, 1, 1], there is 1 non-decreasing subrange and 3 non-increasing, so the answer is -2.

## Addition Notes

Some additions to the original challenge requirements were included:

- A final list of subranges called 'group_lists', whether non-decreasing or non-increasing is created.
- The list 'group_lists' also includes all repeated items that are to be counted for each subrange
- The list 'score_ninc' displays the triangular number score for each non increasing subrange
- The list 'score_ndec' displays the triangular number score for each non decreasing subrange
- the list 'treated_list' can be printed in every for loop iteration to display the window created as per the dimension of 'K' 
