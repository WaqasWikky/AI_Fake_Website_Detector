import re
import socket
import tldextract
from urllib.parse import urlparse

def extract_features(url: str) -> dict:
    """
    Extracts key features from a URL for fake/phishing detection.
    Returns a dictionary of numeric and boolean values.
    """
    features = {}
    try:
        parsed = urlparse(url)
        hostname = parsed.netloc
        path = parsed.path

        # Basic features
        features['length_url'] = len(url)
        features['length_hostname'] = len(hostname)
        features['nb_dots'] = url.count('.')
        features['nb_hyphens'] = url.count('-')
        features['nb_at'] = url.count('@')
        features['nb_qm'] = url.count('?')
        features['nb_and'] = url.count('&')
        features['nb_eq'] = url.count('=')
        features['nb_underscore'] = url.count('_')
        features['nb_tilde'] = url.count('~')
        features['nb_percent'] = url.count('%')
        features['nb_slash'] = url.count('/')
        features['nb_colon'] = url.count(':')
        features['nb_www'] = url.lower().count('www')
        features['https_token'] = int('https' in path or 'https' in hostname)

        # Domain and TLD features
        ext = tldextract.extract(url)
        features['nb_subdomains'] = len(ext.subdomain.split('.')) if ext.subdomain else 0
        features['tld_length'] = len(ext.suffix)
        features['prefix_suffix'] = int('-' in ext.domain)

        # Suspicious keywords
        suspicious_words = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'ebay', 'paypal']
        features['phish_hints'] = sum(word in url.lower() for word in suspicious_words)

        # Digit ratios
        digits = sum(c.isdigit() for c in url)
        features['ratio_digits_url'] = digits / len(url) if len(url) > 0 else 0

        # IP address presence
        try:
            socket.inet_aton(hostname)
            features['ip'] = 1
        except:
            features['ip'] = 0

        # Use of shortening services
        shortening_services = [
            'bit.ly', 'goo.gl', 'shorte.st', 'tinyurl', 'ow.ly',
            't.co', 'is.gd', 'buff.ly', 'adf.ly'
        ]
        features['shortening_service'] = int(any(s in url for s in shortening_services))

    except Exception as e:
        print(f"[!] Feature extraction failed for {url}: {e}")
        return {}

    return features
