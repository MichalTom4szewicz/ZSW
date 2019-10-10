import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(" ",
                           " ")
auth.set_access_token(" ",
                      " ")


def auth_twitter():
    api = tweepy.API(auth)

    # Verify all's ok
    try:
        api.verify_credentials()
        print("Lookin' good sire!")
        return True
    except:
        print("Yer effed up mate!")
        return False


def init_twitter():
    # Create API object
    return tweepy.API(auth, wait_on_rate_limit=True,
                      wait_on_rate_limit_notify=True)


def post_update(api):
    message_body = "Today's temperature: 23°C\n" \
                   "Humidity: Kinda wet\n" \
                   "Loudness: ---|-------------"  # TODO: get sensor data
    api.update_status(message_body)


if __name__ == "__main__":
    auth_twitter()
    api = init_twitter()
    post_update(api)