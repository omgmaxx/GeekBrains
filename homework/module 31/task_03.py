import requests
import json


if __name__ == '__main__':
    episodes_req = requests.get('https://www.breakingbadapi.com/api/episodes')
    deaths_req = requests.get('https://www.breakingbadapi.com/api/deaths')

    episodes_json = json.loads(episodes_req.text)
    deaths_json = json.loads(deaths_req.text)

    new_json = []
    for key in episodes_json:
        if 'Breaking Bad' in key.values():
            ep_dict = dict()
            ep_dict['episode_id'] = int(key['episode_id'])
            ep_dict['season'] = int(key['season'])
            ep_dict['episode'] = int(key['episode'])
            new_json.append(ep_dict)

    for key in deaths_json:
        for new_key in new_json:
            if key['episode'] == new_key['episode'] and \
                    key['season'] == new_key['season']:

                if new_key.get('death_toll'):
                    new_key['death_toll'] += 1
                else:
                    new_key['death_toll'] = 1

                if new_key.get('death_list'):
                    new_key['death_list'].append(key['death'])
                else:
                    new_key['death_list'] = list()
                    new_key['death_list'].append(key['death'])

    for ep in new_json:
        print(ep)

    with open('Breaking_bad_new.json', 'w') as file:
        json.dump(new_json, file, indent=4)
