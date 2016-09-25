import json
from scipy.sparse import *

#Read review ratings from filepath. If ratingsToTake is not specified, then read the whole dataset in the memory.
def getItemUserMatrix(filepath, ratingsToTake=None):

    reviewsFile = open(filepath, mode='r')
    users = set()
    business = set()
    businessUsers = {}
    count = 0
    for line in reviewsFile:

        if ratingsToTake == None or count < ratingsToTake:
            review = json.loads(line.strip())
            user_id = review['user_id']
            business_id = review['business_id']
            rating = review['stars']
            users.add(user_id)
            business.add(business_id)
            businessUsers.setdefault(business_id, {})
            businessUsers[business_id][user_id] = rating

        if count >= ratingsToTake: break
        count+=1

    reviewsFile.close()
    return users, business, businessUsers


def printDatasetStats(users, business, businessUsers):
    minimumRatingsForBusiness = min([len(numUsers) for numUsers in businessUsers.values()])
    maximumRatingsForBusiness = max([len(numUsers) for numUsers in businessUsers.values()])
    totalVotes = sum([len(numUsers) for numUsers in businessUsers.values()])
    totalRatingsSum = sum([sum(list(businessUsers[business_id].values())) for business_id in businessUsers.keys()])
    print('Min ratings for business:{0}, Max ratings for business: {1}, Total ratings in dataset: {2}'.format(
          minimumRatingsForBusiness, maximumRatingsForBusiness, totalVotes))

    print('Min ratings for business:{0}, Max ratings for business: {1}, Total ratings in dataset: {2}'.format(
          minimumRatingsForBusiness, maximumRatingsForBusiness, totalVotes))

    print('Average rating in dataset: {}'.format(totalRatingsSum/(1.0 * totalVotes)))


def invertDict(businessUsers):
    usersBusiness = {}

    for (business, userVotes) in businessUsers.items():
        for (user, vote) in userVotes.items():
            usersBusiness.setdefault(user, {})
            usersBusiness[user][business] = vote

    return usersBusiness


#rating dictionary is of type: 'user': {'item': value}
def convertToSparse(ratingDictionary):
    data = []
    indices = []
    indptr = [0]
    businessMappings = {}
    count = 0
    for ratings in ratingDictionary.values():
        for (business, rating) in ratings.items():
            businessColumnIndex = businessMappings.setdefault(business, len(businessMappings))
            indices.append(businessColumnIndex)
            data.append(rating)
        indptr.append(len(indices))

    return csr_matrix((data, indices, indptr), dtype=int)

def getSparseRatingsMatrix(filepath, ratingsToTake):
    users, business, ratingsForBusiness = getItemUserMatrix(filepath, ratingsToTake)
    ratingsByUsers = invertDict(ratingsForBusiness)
    return convertToSparse(ratingsByUsers)

