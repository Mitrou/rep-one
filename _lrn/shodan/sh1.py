import shodan

SHODAN_API_KEY = "2Yz6rpFRqSRAieCld3iSxIN9FbE0b2Mz"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
	# Lookup the host
	host = api.host('104.25.87.11')

	# Print general info
	print("""
                IP: {}
                Organization: {}
                Operating System: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

	# Print all banners
	for item in host['data']:
		print("""
                        Port: {}
                        Banner: {}

                """.format(item['port'], item['data']))
except shodan.APIError as e:
        print('Error: {}'.format(e))
