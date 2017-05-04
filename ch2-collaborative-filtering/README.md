# Chapter 2 - Collaborative Filtering
It is the recommendation method where a user is recommended about items based on tastes of similar users.  
The similarity is measured using certain distance metrics like Euclidean, Manhattan or Minkowski.  
It is a rating-based recommendation method where distance between items are found using the distance metrics. And 
this is used for finding the similarity between the users.

## Example

Say a user **A** and **B** have rated items like:
```json
{
    "A" : {
        "a" : 4.0,
        "b" : 5.0
    },

    "B" : {
        "a" : 5.0,
        "b" : 2.5,
        "c" : 3.0
    },

    "C" : {
        "a" : 4.0,
        "c" : 3.0,
        "d" : 3.0
    }
}
```

So, we find the similarity between the users using the ratings provided on same items.  

### A and B
```bash
distance = |4.0 - 5.0| + |5.0 - 2.5| = 1.5
```

### A and C
```bash
distance = |4.0 - 4.0| = 0.0
```

Here, A is similar to C than to B

> **Note** : Normally, Euclidean distance is used for most of the cases. There are other metrics too

---------------

## References:
[K-Nearest-Neighbour](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)  
[Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance)
[Manhattan Distance](https://en.wiktionary.org/wiki/Manhattan_distance)
[Minkowski Distance](https://en.wikipedia.org/wiki/Minkowski_distance)
