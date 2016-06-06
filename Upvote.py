# function to calculate triangular number for a complete subrange
def triangular_number(num):
    return num * (num + 1) / 2

# function to identify non increasing or decreasing subranges and calculate difference
def get_count(days):
    
    # Setup lists and variables
    non_dec = []
    non_inc = []
    match = []
    group_lists= []
    index = 0
    ahead = 1
    score_ndec = []
    score_ninc = []
    non_dec.append(days[0])
    non_inc.append(days[0])
 
    # loop through a window to identify non-increasing and non-decreasing elements 
    # and get the difference between the two
    for i in days:
        index += 1
        ahead += 1
        
        # Identify non-decreasing elements by comparing with next list element
        if index < len(days) and days[index] > i:
            
            # calculate and append score of non increasing subrange
            if len(non_inc) > 1:
                group_lists.append(non_inc)
                score_ninc.append(triangular_number(len(non_inc)-1))
            
            # start non decreasing subrage with last element from non increasing subrange
            if len(non_dec) == 0:
                non_dec.append(non_inc[-1])
            
            # extend repeated items to current subrange
            if (len(match) != 0) and (non_dec[0] == match[0]) and (len(non_dec)!= len(non_inc)):
                non_dec.extend(match)
            
            # append and reset
            non_dec.append(days[index])   
            non_inc = []
            match = [] 
        
        # Identify non-decreasing elements by comparing with next list element
        elif index < len(days) and days[index] < i:
            
            # calculate and append score of non decreasing subrange
            if len(non_dec) > 1:
                group_lists.append(non_dec)
                score_ndec.append(triangular_number(len(non_dec)-1))
           
            # start non increasing subrage with last element from non decreasing subrange
            if len(non_inc) == 0:
                non_inc.append(non_dec[-1])
            
            # extend repeated items to current subrange
            if (len(match) != 0) and (non_inc[0] == match[0]) and (len(non_dec)!= len(non_inc)):
                non_inc.extend(match)
            
            # append and reset
            non_inc.append(days[index])
            non_dec = []
            match = []
         
        # Identify repetitions in subranges
        elif index < len(days) and days[index] == i:
            match.append(days[index])
            
            # append repetitions to non increasing subrange
            if len(non_inc) != 0:
                non_inc.append(days[index])
                
                # Check whether repetitions should be treated as both non decreasing
                # and non increasing and append score accordingly
                if ahead < len(days):
                    if days[ahead] < non_inc[-1] and (non_inc[0] != match[0]):
                        match.append(match[0])
                        group_lists.append(match)
                        score_ndec.append(triangular_number(len(match)-1))
            
            # append repetitions to non decreasing subrange
            if len(non_dec) != 0:
                non_dec.append(days[index])
                
                # Check whether repetitions should be treated as both non decreasing
                # and non increasing and append score accordingly
                if ahead < len(days):
                    if days[ahead] > non_dec[-1] and (non_dec[0] != match[0]):
                        match.append(match[0])
                        group_lists.append(match)
                        score_ninc.append(triangular_number(len(match)-1))
    
    # Check if there any remaining subrange and append score accordingly
    if len(non_dec) != 0:
        group_lists.append(non_dec)
        score_ndec.append(triangular_number(len(non_dec)-1))
    else:
        group_lists.append(non_inc)
        score_ninc.append(triangular_number(len(non_inc)-1))
    
    # Check if there is a list of repeated elements at the end and append score
    # to the inactive subrange
    if len(match) != 0:
        match.append(match[0])
        group_lists.append(match)
        if len(non_dec)!=0:
            score_ninc.append(triangular_number(len(match)-1))
        else:
            score_ndec.append(triangular_number(len(match)-1))
    
    # Calculate upvote difference
    upvote_diff = sum(score_ndec) - sum(score_ninc)
        
    return upvote_diff

# fuction to move through provided list of upvote days and 
# calculate difference in every window
def Upvotes(N, K, list_counts):
    scores = []
    windows = N - K + 1
    for row in range(windows):
        period = row + K
        treated_list = list_counts[row:period]
        #print treated_list
        #print "%d" % GetCount10(treated_list)
        scores.append(get_count(treated_list))
    return scores

print Upvotes(5,3,[1,2,3,1,1])