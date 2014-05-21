import urllib2
import json
import matplotlib.pyplot as plt

def getUser(username):
    """
    function getUser parses json page with user information
    returns page content in string format
    """
    url = "http://forum.toribash.com/tori_stats.php?username=%26%2312579%3B"+username+"&format=json"
    response = urllib2.urlopen(url)
    html = response.read()
    print username
    return html


def getTC(inputFile, outputFile):
    """
    function getTC converts string to json string, and finds tc balance for each user
    takes txt file with usernames, one in a line 
    """
    stats_tc = open(outputFile, 'w')
    usernamesFile = open(inputFile, 'r')
    usernames = usernamesFile.readlines()
    for username in usernames:
        username = username.replace('\n','')
        user_string = getUser(username)
        user_json = json.loads(user_string)
        stats_tc.write(str(user_json["tc"])+"\n")
getTC('usernamesR2R.txt', 'tc-stats.txt')

#reminder1: configure gathering stats for the plot from getTC outputs
#reminder2: split into 2 different modules
def plotTC():
    """
    returns diagram of top 5 players for the first len(user<x>) days
    """
    user1 = [5000, 8620, 9100, 12020, 17020, 25020, 33002, 44435, 55001, 68260, 99444, 102322, 101023, 111056, 123456]
    user2 = [5000, 1220, 2000, 1100, 7020, 5000, 19002, 18435, 32001, 43260, 80444, 66322, 86123, 96056, 112345]
    user3 = [5000, 12220, 19800, 22050, 43020, 42020, 39002, 45435, 3001, 8260, 9944, 56002, 54023, 62017, 73456]
    user4 = [5000, 2900, 6700, 2020, 2020, 2020, 3300, 4999, 5501, 6860, 9944, 22322, 28023, 33156, 53456]
    user5 = [5000, 6080, 7000, 14020, 15000, 4500, 17200, 14435, 15001, 18260, 19444, 22322, 21023, 31056, 33456]
    user6 = [5000, 2343, 7235, 4020, 5000, 1400, 1200, 1445, 1501, 1860, 1944, 2222, 2103, 3156, 29456]
    #user6 = [5000, 5000, 4000, 5020, 3000, 4400, 2200, 8445, 11501, 18860, 1944, 22222, 24003, 24003, 24003]

    plt.plot(user1)
    plt.plot(user2)
    plt.plot(user3)
    plt.plot(user4)
    plt.plot(user5)
    #plt.plot(user6)
    plt.ylabel('Toricredits')
    plt.xlabel('Days')
    plt.title('Top 5 Earnings for the first 2 weeks')
    plt.text(130, 10, r'$shevaroller$')
    plt.axis([0, 14, 0, 150000])
    plt.show()



