import threat_intel.feeds as feeds


def query(config, search):

    results = []

    for name in feeds.__all__:
        feed = getattr(feeds, name)
        try:
            # see if the plugin has a 'register' attribute
            print(f"Searching {name}")

            feed_config = {}
            for feed_entry in config['feeds']:
                if feed_entry['name'] == name:
                    feed_config = feed_entry

            out_feed = feed.run(feed_config, search)

            results.append(out_feed)
        except AttributeError:
            # raise an exception, log a message, 
            # or just ignore the problem
            pass

    return results