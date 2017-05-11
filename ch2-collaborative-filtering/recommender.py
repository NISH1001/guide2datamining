#!/usr/bin/env python3

import json

from dist_metric import minkowski

from mathutils import pearson_coefficient, cosine_similarity
from dsutils import convert_to_sparse

def load_data(filename="ratings.json"):
    """
    load json data
    """
    data = None
    with open(filename, 'r') as fp:
        data = json.load(fp)
    return data

def get_common_keys(rating1, rating2):
    """
    get common keys between two dictionary
    """
    return list(rating1.keys() & rating2.keys())

def filter_by_keys(rating, keys):
    """
    filter a dictionary by list of keys
    """
    return { key : rating[key] for key in keys }

def get_dict_values_list(d):
    """
    get all the values of the dict as list
    """
    return list(d.values())

def KNN(username, users, k=None):
    """
        Compute K Nearest Neighbours for the given username.
        
        return list of tuple ('the name of the neighbour user', 'username')

    """
    if k is not None and k < 1:
        raise ValueError("K should be greater than or equal to 1")

    distances = []
    rating_by_username = users[username]
    for user in users:
        if user != username:
            common = get_common_keys(rating_by_username, users[user])
            rating1 = filter_by_keys(rating_by_username, common)
            rating2 = filter_by_keys(users[user], common)
            distance = minkowski(get_dict_values_list(rating1), get_dict_values_list(rating2), r=2)
            distances.append((user, distance))
    distances.sort(key = lambda x:x[1])
    if k is None or k >= len(distances):
        k = len(distances)
    return distances[:k]

def recommend(username, users):
    """
        This method recommends the list of book to the username.
        The recommendation is based on the nearest neighbour/user.
    """

    # find knn
    knn = KNN(username, users)
    print(knn)

    # get the nearest user
    nearest_user = knn[0][0]

    # get ratings accordingly
    neighbour_ratings = users[nearest_user]
    user_ratings = users[username]

    recommendations = []

    """
        now search those item in neighbour 
        that are not in our user
    """
    for item in neighbour_ratings:
        if not item in user_ratings:
            recommendations.append( (item, neighbour_ratings[item]) )

    recommendations.sort(key=lambda x : x[1], reverse = True)
    return recommendations


def pearson(users, username1, username2):
    """
        This finds the correlation between two users
    """
    rating1 = users[username1]
    rating2 = users[username2]
    common_keys = get_common_keys(rating1, rating2)
    r1 = filter_by_keys(rating1, common_keys)
    r2 = filter_by_keys(rating2, common_keys)
    r = pearson_coefficient(get_dict_values_list(r1), get_dict_values_list(r2))
    return r

def cosine_similairty_ratings(users, username1, username2):
    """
        This finds the cosine similarity between two users
    """
    rating1 = users[username1]
    rating2 = users[username2]
    r1, r2 = convert_to_sparse(rating1, rating2)
    c = cosine_similarity(get_dict_values_list(r1), get_dict_values_list(r2))
    return c

def main():
    #users = load_data("ratings2.json")
    users = load_data("ratings2.json")

    #recommendations = recommend("Barsha", users)
    #print(recommendations)
    r = pearson(users, "Angelica", "Veronica")
    print(r)
    c = cosine_similairty_ratings(users, "Angelica", "Veronica")
    print(c)

if __name__ == "__main__":
    main()

