# IP Checker
Inspired by security requirements for web applications and public-facing infrastructure this library assists with the 
management of white/blacklists of IP addresses.

Options available:

* Checking against known [TOR exit nodes](https://check.torproject.org/cgi-bin/TorBulkExitList.py)
* Checking against [x] built-in blacklist providers
* Ability to add your own lists / providers

Thanks to the [iptools](http://python-iptools.readthedocs.io/en/latest/) library, which this makes heavy use of.
