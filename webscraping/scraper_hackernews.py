# -*- coding: utf-8 -*-
"""
Scrap Hckernews website and display all news with scores 100 and above.

Read about selectors at:
   https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
Created on Sat Jan 29 11:49:25 2022

@author: Farid
"""
import requests
from bs4 import BeautifulSoup
import pprint


def extract_links_subtexts(url, n_pages=1):
    """
    Scraps provided url to extract links and subtexts.

    Parameters
    ----------
    url : string
        url.
    n_pages : int, optional
        Number of pages to scrap. The default is 1.

    Returns
    -------
    links : list
        Scrapped links.
    subtexts : list
        List of subtexts.

    """
    # Prepare urls
    urls = [url]
    for i in range(1, int(n_pages)):
        urls.append(f'{url}?p={i+1}')
    # Extract links and subtexts
    links = []
    subtexts = []
    for url in urls:
        res = requests.get(url)
        # Parse
        soup = BeautifulSoup(res.text, 'html.parser')
        # Links for each items
        links.extend(soup.select('.titlelink'))
        subtexts.extend(soup.select('.subtext'))
    return links, subtexts


def sort_stories_by_votes(hnlist):
    """
    Sorts the hnlist of dictionaries based on their votes.

    Parameters
    ----------
    hnlist : list
        List of dictionaries.

    Returns
    -------
    list
        Sorted list of dictionaries.

    """
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    """
    Creates list of dicrionaries including title, link and votes.

    Parameters
    ----------
    links : list
        List of links.
    subtext : list
        List of subtexts.

    Returns
    -------
    list
        List of dictionaries.

    """
    hn = []
    for i, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'title': title, 'link': href, 'votes': score})
    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    # Url of the hackernews website
    url = 'https://news.ycombinator.com/news'
    # Number of pages to scrap
    n_pages = 3
    # Extract links and subtexts
    links, subtexts = extract_links_subtexts(url, n_pages)
    # Create customized list of news based on scores (>100)
    hn = create_custom_hn(links, subtexts)
    # Print the links
    pprint.pprint(hn)
