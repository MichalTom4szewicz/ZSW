import tweepy
import Adafruit_DHT

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Y509knpZaOHKERLudDQ5yCa1a",
                           "WOpjxR4FFAuEXgTvZ5gSqPBWAkgem8r82XyKnyV4kfAjOPxvh0")
auth.set_access_token("1182367262453518336-C50nxYQTZwKZrmLuHleyorIvSVUO95",
                      "wvRMz5fqiHGhS6JOQqXDt5l40cw5yrA1IBfJNZV3vQHYg")

def get_sound():
        # here


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


def post_update(api, sensor_data):
    message_body = "Today's temperature: " + str(sensor_data["temperature"]) + "°C\n" \
                   "Humidity: " + str(sensor_data["humidity"]) + "%\n" \
                   "Loudness: " + str(sensor_data["loudness"])  # TODO: get sensor data
    api.update_status(message_body)
    print("Status uploaded!")


def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return temperature


def get_humi():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return humidity


if __name__ == "__main__":
    sensor_data = {"temperature": get_temp(), "humidity": get_humi(), "loudness": get_sound()}
    auth_twitter()
    api = init_twitter()
    post_update(api, sensor_data)
