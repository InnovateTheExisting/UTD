"""
Created on Sat Nov 17 15:23:07 2018

@author: rutujakaushike
"""

import json
import sys


# Find intersection to calculate Jaccard distance
def intersectionForJaccard(set_one, set_two):
    set_result = 0
    for w in set_one:
        while w in set_two and set_one[w] != 0 :
            if w in set_two:
                set_two[w] -= 1
                set_one[w] -= 1
                if set_two[w] == 0:
                    set_two.pop(w, None)
                set_result += 1
    return set_result

# Find union to calculate Jaccard distance
def unionForJaccard(set_one, set_two):
    set_result = 0
    for w in set_one:
        if w in set_two:
            set_result = set_result + max(set_one[w], set_two[w])
            set_two.pop(w, None)
        else:
            set_result = set_result + set_one[w]
    for w in set_two:
        set_result = set_result + set_two[w]
    return set_result

# Calculate Jaccard distance
def jaccard_distance(set_one, set_two):
    count1 = noOfWords(set_one)
    count2 = noOfWords(set_two)
    union = unionForJaccard(dict(count1), dict(count2))
    intersect = intersectionForJaccard(dict(count1), dict(count2))
    return 1.0 - ((intersect * 1.0)/ union)

# Sum of the squared error
def squaredErrorSum(clusters, centroid, tweet):
    sse = 0
    for c in clusters:
        for i in clusters[c]:
            sse += jaccard_distance(tweet[i], tweet[centroid[c]]) * jaccard_distance(tweet[i], tweet[centroid[c]])
    return sse


# Read the initial seed file
def getCentroidsFromInitialSeedFile(initialSeedsFile):
    with open(initialSeedsFile) as tweets_file_centroids:
        return tweets_file_centroids.read().rsplit(",\n")

# Read json file in a dictionary
def getDataFromTweetsJson(tweetsDataFileJson):
    # Declare a dictionary 'data' to read tweets from JSON file into it.
    data = {}
    # Getting data into 'data' from JSON file.
    with open(tweetsDataFileJson) as dataFromJson:
        for tweetRow in dataFromJson:
            tweet = json.loads(tweetRow)
            data[str(tweet["id"])] = tweet["text"]
    return data

# Count the number of words from the list of words
def noOfWords(listOfWords):
    no = {}
    for w in listOfWords:
        if w not in no:
            no[w] = 1
        else:
            no[w] += 1
    return no


# Get initial centroids into a dictionary
def getCentroidsIntoDictionary(centroid):
    dict = {}
    numberOfClusters = len(centroid)
    for i in range(0, numberOfClusters):
        dict[i] = centroid[i]
    return dict


# Creating clusters
def createClusters(tweet, centroid):
    clusters = {}
    for i in range(len(centroid)):
        clusters[i] = []

    for i in tweet:
        minDistance = 1
        cid = 0
        for j in centroid:
            jaccardDistance = jaccard_distance(tweet[centroid[j]], tweet[i], )
            if(jaccardDistance < minDistance):
                minDistance = jaccardDistance
                cid = j
        clusters[cid].append(i)
    return clusters

# Find new centroids using Jaccard distance
def calculteNewCentroids(cluster, tweets):
    min_distance = 1
    min_cid = cluster[0]
    for i in cluster:
        d = 0
        for j in cluster:
            d = d + jaccard_distance(tweets[i], tweets[j] )
        # Calculate mean
        m = d/len(cluster)
        if m < min_distance:
            min_distance = m
            min_cid = i
    return min_cid


# main method to execute the program
def main():
    if len(sys.argv) == 5:
        c = int(sys.argv[1])
        s = sys.argv[2]
        t = sys.argv[3]
        o = sys.argv[4]
    elif len(sys.argv) == 4:
        c = 25
        s = sys.argv[1]
        t = sys.argv[2]
        o = sys.argv[3]
    
    tweets = getDataFromTweetsJson(t)
    centroid = getCentroidsFromInitialSeedFile(s)
   

    if len(centroid) != c:
        print("Number of values from initial seed file and number of clusters entered do not match.")
        sys.exit(1)


    while True:
        NewCentroids = []
        centroidDictionary = getCentroidsIntoDictionary(centroid)
        clusters = createClusters(tweets, centroidDictionary)
        for cluster in clusters:
            NewCentroids.append(calculteNewCentroids(clusters[cluster], tweets))
        if NewCentroids == centroid:
            break
        else:
            centroid = NewCentroids

    o = open(o, 'w')
    o.write("\n\nClusters:\n")
    for cluster in clusters:
        o.write(str(cluster))
        o.write("\t")
        for tweet in clusters[cluster]:
            o.write(tweet)
            o.write(", ")
        o.write("\n")

    o.write("\n\n")
    o.write("SSE is: ")
    o.write(str(squaredErrorSum(clusters, centroid, tweets)))


main()