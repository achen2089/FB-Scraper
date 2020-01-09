
from fb_engage import scrape_FB
import numpy as np


def post_type_breakdown_graph(url):
    post_data = scrape_FB(url)
    num_video = 0
    num_post = 0
    num_photo = 0
    for i in post_data.content_type:
        if i == 'video':
            num_video +=1
        elif i == 'post':
            num_post += 1
        else :
            num_photo += 1

    # print("number of videos " , num_video)
    # print("number of posts " , num_post)
    # print("number of photos " , num_photo)

    types = ('videos', 'posts', 'photos')
    y_pos = np.arange(len(types))
    num_breakdown = [num_video, num_post, num_photo]

    plt.bar(y_pos, num_breakdown, align='center', alpha=0.5)
    plt.xticks(y_pos, types)
    plt.ylabel('Number of Posts')
    plt.title('Post Type Breakdown')

    plt.savefig('post_type_breakdown.png')

# def average_engagement_month_a_year(url, year)
#     post_data = scrape_FB(url)

# post_type_breakdown_graph("https://www.facebook.com/pg/DukeUniv/posts/?ref=page_internal")
    

