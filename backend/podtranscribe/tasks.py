# todo: setup celery app

def _download_episode(episode_url):
    """async task to download episodes from a URL, 
    save them in a temporary folder

    Parameter: episode_url {string}
      a URL to a CDN download for a podcast

    Return: file_name {string}
      a file_name string for the download location
    """

    return None


def parse_RSS_feed(rss_feed):
    """asynchronous task for parsing an RSS feed

    Parameter: rss_feed {string}
      a RSS URL for fetching and parsing the RSS feed

    Return: None
    """
    return None


def transcribe_episode(episode_url):
    """async task to download and transcribe a podcast episode.

    Parameter: episode_url:
      a URL to a CDN download for a podcast 

    Return: None
      returns None if things work as expected.
    """

    return None
