[![GitHub stars](https://img.shields.io/github/stars/jkerai1/ScrapWebsiteForTopKeywords?style=flat-square)](https://github.com/jkerai1/ScrapWebsiteForTopKeywords/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/jkerai1/ScrapWebsiteForTopKeywords?style=flat-square)](https://github.com/jkerai1/ScrapWebsiteForTopKeywords/network)
[![GitHub issues](https://img.shields.io/github/issues/jkerai1/ScrapWebsiteForTopKeywords?style=flat-square)](https://github.com/jkerai1/ScrapWebsiteForTopKeywords/issues)
[![GitHub pulls](https://img.shields.io/github/issues-pr/jkerai1/ScrapWebsiteForTopKeywords?style=flat-square)](https://github.com/jkerai1/ScrapWebsiteForTopKeywords/pulls)


# Scrape Websites For Top Keywords  

Scrape website for top keywords then use word association to generate new keywords.

The intention of this project will be to scrape websites for keywords for usage in banned password lists however this could have other uses.

An Output txt file is created in the same directory with as a script with the keywords.  

# Requirements
pip install scipy==1.12
pip install gensim  
pip install BeautifulSoup

Google's Word Vectors Model : https://drive.usercontent.google.com/download?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download&confirm=t&uuid=7b93067e-638f-45f2-9f6c-61db0e0f77b7  

Model must be in path './model/'  

# Example usage

As you can see example.com does not reach 30 words but results are still returned:    


![344489036-477f00b0-7d7f-4c05-879c-3888ead313f4](https://github.com/jkerai1/ScrapWebsiteForTopKeywords/assets/55988027/c9c9f1b6-f888-469e-bee5-5ca13f5140f5)


![image](https://github.com/jkerai1/ScrapWebsiteForTopKeywords/assets/55988027/76a92e9b-41fd-478d-94c0-7815284a37f9)


# See More  

https://github.com/jkerai1/AzurePasswordProtectionCalculator  
https://learn.microsoft.com/en-us/entra/identity/authentication/concept-password-ban-bad
