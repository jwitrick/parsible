from plugins.outputs.statsd import output_statsd_count, output_statsd_timer

def process_ajax(line):
    if 'path' in line.keys():
        if line['path'].startswith('/ajax/'):
            output_statsd_count('call.ajax')

def process_status(line):
    if 'path' in line.keys():
        if line['path'].startswith('/v2.0/status/'):
            output_statsd_count("sp.nginx.ord1a.status.total")
            if line['response_code'] == "200":
                output_statsd_count("sp.nginx.ord1a.status.successful")
            else:
                output_statsd_count("sp.nginx.ord1a.status.failure")
           
            output_statsd_timer("sp.nginx.ord1a.status.service_time", line['service_time'])


def process_tokens(line):
    if 'path' in line.keys():
        if line['path'].startswith('/v2.0/tokens/'):
            output_statsd_count("sp.nginx.ord1a.tokens.{0}.total".format(line['method'].lower()))
            if line['response_code'] != "200":
                output_statsd_count("sp.nginx.ord1a.tokens.{0}.failure".format(line['method'].lower()))
            output_statsd_timer("sp.nginx.ord1a.tokens.{0}.service_time".format(line['method'].lower()), line['service_time'])

