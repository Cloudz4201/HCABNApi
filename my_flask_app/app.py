from flask import Flask, render_template, request
import urllib.request as req
import xml.etree.ElementTree as ET  # Import the XML parsing library

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        postcode = request.form['postcode']

        authenticationGuid = 'cfda0a08-1907-4804-9536-d5faaa35ce73'  # Your provided GUID

        # Other parameters with default values
        legalName = ''
        tradingName = ''
        NSW = ''
        SA = ''
        ACT = ''
        VIC = ''
        WA = ''
        NT = ''
        QLD = ''
        TAS = ''

        # Construct URL
        url = f'https://abr.business.gov.au/abrxmlsearchRPC/AbrXmlSearch.asmx/ABRSearchByNameSimpleProtocol?name={name}&postcode={postcode}&legalName={legalName}&tradingName={tradingName}&NSW={NSW}&SA={SA}&ACT={ACT}&VIC={VIC}&WA={WA}&NT={NT}&QLD={QLD}&TAS={TAS}&authenticationGuid={authenticationGuid}'

        # Make API request
        try:
            conn = req.urlopen(url)
            returnedXML = conn.read().decode("utf-8")

            # Parse the XML response
            root = ET.fromstring(returnedXML)
            abn_status = root.find('.//{http://abr.business.gov.au/ABRXMLSearchRPC/literalTypes}identifierStatus').text

            return render_template('results.html', abn_status=abn_status)
        except Exception as e:
            return str(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
