import requests
from HTMLParser import HTMLParser

CATALOGUE_URL = 'https://go.sfu.ca/psp/paprd/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL'
REDIR_CATALOGUE = 'https://go.sfu.ca/psp/paprd/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?&'
SECOND_REDIR = 'https://go.sfu.ca/psp/paprd/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL'
AUTHENTICATION_URL = 'https://sims-prd.sfu.ca/psc/csprd/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL?PortalActualURL=https%3a%2f%2fsims-prd.sfu.ca%2fpsc%2fcsprd%2fEMPLOYEE%2fHRMS%2fc%2fCOMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL&PortalContentURL=https%3a%2f%2fsims-prd.sfu.ca%2fpsc%2fcsprd%2fEMPLOYEE%2fHRMS%2fc%2fCOMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL&PortalContentProvider=HRMS&PortalCRefLabel=Browse%20Course%20Catalog&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fgo.sfu.ca%2fpsp%2fpaprd%2f&PortalURI=https%3a%2f%2fgo.sfu.ca%2fpsc%2fpaprd%2f&PortalHostNode=EMPL&NoCrumbs=yes&PortalKeyStruct=yes'

class AuthParser(HTMLParser):
    inputs = []
    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            self.inputs.append(attrs)
        else:
            pass
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        pass


def get_session(url):
    session = requests.Session()
    session.get(url)
    return session

def get_auth_info(session):
    session.get(REDIR_CATALOGUE)
    session.get(SECOND_REDIR)
    response = session.get(AUTHENTICATION_URL)
    request_fields = response_parser(response.text)
    print request_fields
    return response

def response_parser(response_text):
    parser = AuthParser()
    parser.feed(response_text)
    return parser.inputs

#TODO: convert stuff in request_fields into proper form data, remember to increment state
def create_form_data():
     pass

# TODO: server architecture is SOAP, iterate your session over all alphanumeric possibilities from a-z0-9
# TODO: access each class on the list from 0-max and parse data in each class, last request is generic
def get_classid_mapping(session):
    pass

# TODO: db probably contains one entry per section of class, each db entry will probably contain
# TODO: the mapping of course to ID and maybe vice-versa, will also contain a list of users in line
# TODO: This function probably shouldn't know about the users associated with each section
def check_class_availability():
    pass

get_auth_info(get_session(CATALOGUE_URL))


