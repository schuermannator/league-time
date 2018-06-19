import os
import requests


API_KEY = os.environ["RIOT_API_KEY"]
summ_account = ["https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/", "?api_key=" + API_KEY]
match_hist = ["https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/", "?api_key=" + API_KEY]
match_data = ["https://na1.api.riotgames.com/lol/match/v3/matches/", "?api_key=" + API_KEY]


#req = requests.get(summ_account[0] + "Anim8tor" + summ_account[1])

def get_account_id(summoner):
	"""use summoner name to fetch account ID"""
	account_id = requests.get(summ_account[0] + summoner + summ_account[1])
	return account_id.json()["accountId"]

def get_matches(account_id):
    r = requests.get(match_hist[0] + str(account_id) + match_hist[1])
    print("Fetching match history...")
    if r.status_code == 200:
    	return r.json()
    else:
    	return -1

def get_match_lens(match_id):
	r = requests.get(match_data[0] + str(match_id) + match_data[1])
	if r.status_code == 200:
		return r.json()["gameCreation"], r.json()["gameDuration"]

id = get_account_id("Anim8tor")
print("Id: " + str(id))
matches = get_matches(id)

print(matches.keys())
print(matches["matches"])

lens = {}
for match in matches["matches"]:
	time, duration = get_match_lens(match["gameId"])
	lens[time] = duration
	print("getting len " + str(len(lens)))


print(lens)
