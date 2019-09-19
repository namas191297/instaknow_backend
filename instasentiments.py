import instaloader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
from instaloader import Profile, Post


def getPublicProfileCaptions(profile_id):
    profilename = profile_id
    loader = instaloader.Instaloader()
    profile = Profile.from_username(loader.context,profilename)
    profile_pic = profile.get_profile_pic_url()
    full_name = profile.full_name

    posts = profile.get_posts()
    captions = []
    for post in posts:
        if post.caption != None:
            captions.append(post.caption)
    if len(captions) < 1:
        loader.close()
        return "No captions found! Are you sure this profile is public and has posted?", "Empty", "Empty"
    else:
        loader.close()
        return captions, profile_pic, full_name

def getPrivateProfileCaptions(profile_id, login, password):
    profilename = profile_id
    loader = instaloader.Instaloader()
    try:
        loader.login(login,password)
    except:
        return "Failed to login!", "Empty", "Empty"

    profile = Profile.from_username(loader.context, profilename)
    posts = profile.get_posts()
    profile_pic = profile.get_profile_pic_url()
    full_name = profile.full_name
    captions = []
    for post in posts:
        if post.caption != None:
            captions.append(post.caption)
    if len(captions) < 1:
        loader.close()
        return "No captions found! Are you sure this profile has posted?", "Empty", "Empty"
    else:
        loader.close()
        return captions, profile_pic, full_name

def getSentiments(captions):
    if len(captions) > 0 and type(captions) == list:
        analyser = SentimentIntensityAnalyzer()
        neutral = []
        positive = []
        negative = []
        compound = []

        for caption in captions:
            neutral.append(analyser.polarity_scores(caption)['neu'])
            positive.append(analyser.polarity_scores(caption)['pos'])
            negative.append(analyser.polarity_scores(caption)['neg'])
            compound.append(analyser.polarity_scores(caption)['compound'])

        positive = np.array(positive)
        negative = np.array(negative)
        neutral = np.array(neutral)
        compound = np.array(compound)

        return {
            'Neutral':round(neutral.mean(),2)*100.0,
            'Positive':round(positive.mean(),2)*100.0,
            'Negative':round(negative.mean(), 2) * 100.0,
            'Overall':round(compound.mean(), 2) * 100.0
                }
    else:
        return captions

