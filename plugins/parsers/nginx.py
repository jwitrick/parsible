import re

def parse_nginx(line):
#    regex = re.compile("(?P<ip_address>\S*)\s-\s(?P<requesting_user>\S*)\s-\s\[(?P<timestamp>.*?)\]\s{1,2}(?P<method>\S*)\s*(?P<request>\S*)\s*(HTTP\/)*(?P<http_version>.*?)\s\"(?P<response_code>\d{3})\"\s(?P<size>\S*)\s\"-\"\s\"-\"\s\"-\"\s-\s(?P<service_time>\S*)")
    regex = re.compile("(?P<ip_address>\S*)\s-\s-\s\[(?P<timestamp>.*?)\]\s{1,2}(?P<method>\S*)\s*(?P<request>\S*)\s*(HTTP\/)*(?P<http_version>.*?)\s\"(?P<response_code>\d{3})\"\s(?P<size>\S*)\s\"-\"\s\"-\"\s\"-\"\s-\s(?P<service_time>\S*)")
#10.130.0.55:35357 - - [14/May/2014:08:52:44 -0400] GET /v2.0/tokens/769ad89c77f14ea2a81eead9c09471c5 HTTP/1.1 "200" 1270 "-" "-" "-" - 0.000
    r = regex.search(line)
    result_set = {}
    if r:
        for k, v in r.groupdict().iteritems():
            if v is None or v is "-":
                continue
            if "request" in k:
                if "?" in v:
                    request = v.partition("?")
                    path = request[0]
                    query = request[2]
                    result_set["path"] = path
                    result_set["query"] = query
                    r.groupdict().pop(k)
                    continue
                else:
                    result_set["path"] = r.groupdict().pop(k)
                    continue
            result_set[k] = r.groupdict().pop(k)
    return result_set




