
from fb_engage import scrape_FB
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#years should all be the last two digits



def generate_graphs(url, year):
  post_data = scrape_FB(url)
  print(post_data)
  post_data.dropna(inplace = True)
  num_photo = post_data.groupby('content_type').content_type.count()[0]
  num_post = post_data.groupby('content_type').content_type.count()[1]
  num_video = post_data.groupby('content_type').content_type.count()[2]
   
    # print("number of videos " , num_video)
    # print("number of posts " , num_post)
    # print("number of photos " , num_photo)

  labels = ['Photos', 'Posts', 'Videos']
  sizes = [num_photo, num_post, num_video]
  colors = ['#adff7a', '#ffa27a', '#cc7aff']
  explode = (0, 0, 0)
  # plt.title('Post breakdown', year)
  plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=140)
  plt.axis('equal')
  plt.savefig('post_type_breakdown.png')


  df= post_data

  df.date = pd.to_datetime(df.date)
  # df.likes = pd.to_numeric(df.likes)
  df.comments = pd.to_numeric(df.comments)
  df.shares = pd.to_numeric(df.shares)
  df.fillna(0, inplace = True)

  df = df[df.date.dt.year==2019]


  df.groupby(df.date.dt.month).sum()[["comments","shares"]].plot()
  plt.title("Comments and Shares by Month", size=15)
  plt.xlabel("Month", size=15)
  plt.ylabel("Amount", size=15);

  plt.savefig("comments_shares.png")
  plt.clf()



#generate pie chart
def post_type_breakdown_graph(url, year):
  post_data = scrape_FB(url)
  print(post_data)
  post_data.dropna(inplace = True)
  num_photo = post_data.groupby('content_type').content_type.count()[0]
  num_post = post_data.groupby('content_type').content_type.count()[1]
  num_video = post_data.groupby('content_type').content_type.count()[2]
   
    # print("number of videos " , num_video)
    # print("number of posts " , num_post)
    # print("number of photos " , num_photo)

  labels = ['Photos', 'Posts', 'Videos']
  sizes = [num_photo, num_post, num_video]
  colors = ['#adff7a', '#ffa27a', '#cc7aff']
  explode = (0, 0, 0)
  # plt.title('Post breakdown', year)
  plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=140)
  plt.axis('equal')
  plt.savefig('post_type_breakdown.png')


#generates two line graphs
def average_engagement_month_a_year(url, year_need):
  post_data = scrape_FB(url)
  post_data.dropna(inplace = True)
  likes_month = post_data.groupby('month').likes.sum()
  shares_month = post_data.groupby('month').shares.sum()
  comments_month = post_data.groupby('month').comments.sum()
  # total_month = likes_month + shares_month + comments_month
  # plt.title("Total Engagement by Month")
  # plt.plot(total_month)
  # plt.ylabel('Engagements')
  # plt.xlabel('Months')
  # plt.savefig('total_engagement_month_year.png')

  # plt.clf()
  plt.plot(likes_month, color = "blue")
  plt.plot(shares_month, color = 'red')
  plt.plot(comments_month, color = 'green')
  blue_patch = mpatches.Patch(color='blue', label='Likes')
  red_patch = mpatches.Patch(color='red', label='Shares')
  green_patch = mpatches.Patch(color='green', label='Comments')
  plt.legend(handles = [blue_patch, red_patch, green_patch])
  plt.savefig('engagement_type_comparison_year.png')
  
def type_of_post_by_month_a_year(url, year):
  post_data = scrape_FB(url)
  post_data.dropna(inplace = True)
  photos = post_data.loc[post_data.content_type == 'photo'].groupby(['content_type', 'month']).content_type.count()
  posts = post_data.loc[post_data.content_type == 'post'].groupby(['content_type', 'month']).content_type.count()
  videos = post_data.loc[post_data.content_type == 'video'].groupby(['content_type', 'month']).content_type.count()
  plt.title('Types of Post By Month')
  photos.plot()
  posts.plot()
  videos.plot()
  plt.ylabel('Number of Content Type')
  plt.xlabel('Months')
  plt.savefig('type_of_post_by_month_a_year.png')


# type_of_post_by_month_a_year('https://www.facebook.com/pg/SantaClaraUniversity/posts/?ref=page_internal',19)
# average_engagement_month_a_year('https://www.facebook.com/pg/SantaClaraUniversity/posts/?ref=page_internal',19)
# post_type_breakdown_graph('https://www.facebook.com/pg/SantaClaraUniversity/posts/?ref=page_internal', 19)




  


    

