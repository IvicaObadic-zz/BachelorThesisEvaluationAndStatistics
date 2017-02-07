import json
import numpy as np
import matplotlib.pyplot as plt
import visualizer
from collections import Counter

plots_source_file = 'C:\\Users\\ivicaobadic\\Desktop\\Diplomska\\Plots\\Dataset statistsics\\'

def generate_barplot_from_ratings(ratings):
    ratings_by_categories = np.bincount(ratings)
    ratings_by_categories_scaled = []
    for rating in ratings_by_categories:
        ratings_by_categories_scaled.append((1.0*rating)/len(ratings))

    outputfilename = plots_source_file + 'ratings_distribution.jpg'
    visualizer.generate_bar_plot(
        'Dataset ratings distribution',
        'Stars',
        'Frequency',
        range(1, 6),
        ratings_by_categories_scaled[1:],
        outputfilename
    )

def filter_by_count_threshold(counts, threshold):
    counts_filtered = {id: counts[id] for id in counts if counts[id] <= threshold}
    return counts_filtered

def generate_histogram_for_count_of_entity_reviews(ids, title, xlabel, ylabel, outputfilename, filter=None):
    entity_counts_by_id = Counter(ids)
    if filter is not None:
        entity_counts_by_id = filter(entity_counts_by_id, 100)

    counts = list(entity_counts_by_id.values())
    bins = np.linspace(min(counts), max(counts), 40, endpoint=True)
    visualizer.generate_histogram(title, xlabel, ylabel, counts, bins, outputfilename)

def get_counts(businesses_votes_counts):
    all_votes_counts = []
    for business_counts in businesses_votes_counts.values():
        for count in business_counts:
            all_votes_counts.append(count)
    return all_votes_counts

def generate_histogram_from_review_votes(businesses_votes_counts, title, xlabel, ylabel, outputfilename):
    all_votes_counts = get_counts(businesses_votes_counts)

    print(min(all_votes_counts), max(all_votes_counts))
    bins = np.linspace(min(all_votes_counts), max(all_votes_counts), 40, endpoint=True)
    visualizer.generate_histogram(title, xlabel, ylabel, all_votes_counts, bins, outputfilename)

def add_rating_to_dictionary(rating_dict, entity_id, rating):
    already_added_ratings = rating_dict.get(entity_id, [])
    already_added_ratings.append(rating)
    rating_dict[entity_id] = already_added_ratings

def generate_pairwise_histogram(businesses, businesses_votes_counts):
    businesses_counts = Counter(businesses)
    most_common_bussinesses_ids = [business_with_count[0] for business_with_count in  businesses_counts.most_common(1154)]
    most_common_businesses_votes = {business:counts for business, counts in businesses_votes_counts.items() if business in most_common_bussinesses_ids}
    most_common_counts = get_counts(most_common_businesses_votes)

    least_common_businesses_ids = [business_with_count[0] for business_with_count
                                   in businesses_counts.most_common()[9500:]]
    least_common_businesses_votes = {business:counts for business, counts in businesses_votes_counts.items() if business in least_common_businesses_ids}
    least_common_counts = get_counts(least_common_businesses_votes)
    visualizer.plot_two_histograms_together(
        'Pairwise businesses distribution',
        'Votes',
        'Reviews',
        least_common_counts,
        most_common_counts,
        np.linspace(0, 100, 50, endpoint=True),
        output_filename=plots_source_file + 'pairwise_votes_distribution.jpg'
    )


#Read review ratings from filepath. If ratingsToTake is not specified, then read the whole dataset in the memory.
def get_businesses_categories(filepath='dataset/yelp_training_set_business.json'):
    all_businesses_categories = []
    for line in open(filepath):
        business = json.loads(line.strip())
        categories_for_business = business['categories']
        for category in categories_for_business:
            all_businesses_categories.append(category)

    businesses_counts = Counter(all_businesses_categories)
    print(businesses_counts.most_common(10))


def parseReviewsDataset(filepath):

    reviewsFile = open(filepath, mode='r')

    users = []
    business = []
    business_votes_counts = {}
    ratings = []
    for line in reviewsFile:
        review = json.loads(line.strip())
        user_id = review['user_id']
        business_id = review['business_id']
        rating = review['stars']
        votes = review['votes']
        votes_total = int(votes['funny']) + int(votes['useful']) + int(votes['cool'])

        ratings.append(rating)
        users.append(user_id)
        business.append(business_id)
        add_rating_to_dictionary(business_votes_counts, business_id, votes_total)

    reviewsFile.close()

    item_counts = Counter(business)
    most_common_items = [item_with_count[1] for item_with_count in item_counts.most_common(1154)]
    print(sum(most_common_items))

    #this section generates the plots from the dataset.

    generate_barplot_from_ratings(ratings)

    generate_histogram_for_count_of_entity_reviews(
        users,
        'Users review distribution',
        'Reviews',
        'Users',
        plots_source_file + 'num_user_reviews_histogram.jpg'
        )

    generate_histogram_for_count_of_entity_reviews(
        business,
        'Businesses review distribution',
        'Reviews',
        'Businesses',
        plots_source_file + 'num_businesses_reviews_histogram.jpg'
    )

    generate_histogram_for_count_of_entity_reviews(
        business,
        'Review distribution for businesses with less than 100 reviews',
        'Reviews',
        'Businesses',
        plots_source_file + 'num_businesses_reviews_histogram_less_than_100.jpg',
        filter_by_count_threshold
    )
    generate_histogram_from_review_votes(
        business_votes_counts,
        'Votes distribution',
        'Votes',
        'Reviews',
        plots_source_file + 'votes_distribution.jpg'
    )
    generate_pairwise_histogram(business, business_votes_counts)

parseReviewsDataset('dataset/yelp_training_set_review.json')
