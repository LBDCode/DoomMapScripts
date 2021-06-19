
import requests
import io

def getStateData():
    print("geting state data")

    states = ['AZ','AR','CA','CO','CT','DE','DC','FL','GA','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

    print(len(states))

    for state in states:
        print("getting data for " + state)
        url = "https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd=" + state + "&parameterCd=00060,00065&siteStatus=active&hasDataTypeCd=iv"
        response = requests.get(url).content
        encoding = 'utf-8'
        strResponse = str(response, encoding)
        

        tempFile = open("temp_data.txt","w")
        tempFile.write(strResponse)
        

        tempDataFile = open('temp_data.txt',
                'r')

        cleanDataFile = open('clean_data.txt',
                'a')
    
        for line in tempDataFile.readlines():    
            if (line.startswith('USGS')):
                line = state + '\t' + line
                cleanDataFile.write(line)
            
   

getStateData()
