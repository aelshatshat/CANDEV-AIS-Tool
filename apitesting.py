import urllib.request, json 
with urllib.request.urlopen("https://data.tc.gc.ca/v1.3/api/eng/vessel-registration-query-system/canadian-registry-large-vessels/official-number/316020871?format=json"
) as url:
    data = json.loads(url.read().decode())
    print(data)
#http://data.tc.gc.ca/v1.3/api/eng/vessel-registration-query-system/canadian-registry-large-vessels/official-number/259385000?format=json
