import tweepy
import Adafruit_DHT
import sounddevice as sd
from scipy.io.wavfile import write
from time import gmtime, strftime
from scipy.io import wavfile as wav
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Y509knpZaOHKERLudDQ5yCa1a",
                           "WOpjxR4FFAuEXgTvZ5gSqPBWAkgem8r82XyKnyV4kfAjOPxvh0")
auth.set_access_token("1182367262453518336-C50nxYQTZwKZrmLuHleyorIvSVUO95",
                      "wvRMz5fqiHGhS6JOQqXDt5l40cw5yrA1IBfJNZV3vQHYg")

def get_sound():
	timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())

	ts = str(timestamp)+".wav"
	print(ts)


	fs = 44100  # Sample rate
	seconds = 5  # Duration of recording


	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	sd.wait()  # Wait until recording is finished
	write(ts, fs, myrecording)  # Save as WAV file

	rate, data = wav.read(ts)

	min = 0
	max = 0

	print(int(data[10][0]))
	for i in data:
	    for j in i:
	        a = float(j)
	        if a < min:
	            min = a
	        if a > max:
	            max = a

	print("minimum: " + str(min))
	print("maximum: " + str(max))

	list = os.listdir(r".")

	nazwa = "dane.txt"


	#jakiestam przetwarzanie ocena tego czy jest glosno czy cicho, najlepiej w dB
	# moze cos takiego https://github.com/SuperShinyEyes/spl-meter-with-RPi

	if nazwa in list:
	    f = open("dane.txt", "a")
	    f.write(str(timestamp) + " " + str(min) + " " + str(max)+"\n")
	    f.close()
	else:
	    f = open("dane.txt", "x")
	    f.write(str(timestamp) + " " + str(min) + " " + str(max)+"\n")
	    f.close()

	os.remove(ts)
	return (min+max)/2



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
