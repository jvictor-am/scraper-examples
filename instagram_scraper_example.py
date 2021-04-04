from instascrape import Profile
import pandas as pd

name = input('Enter profile name:')
profile = Profile(name)
profile.scrape()
recent_posts = profile.get_recent_posts()

posts_data = [post.to_dict() for post in recent_posts]
posts_df = pd.DataFrame(posts_data)

print(posts_df[['upload_date', 'comments', 'likes']])
