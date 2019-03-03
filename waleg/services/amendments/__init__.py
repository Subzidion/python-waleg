from .amendment import Amendment

def get_amendments(year):
    SERVICE_URL = "/amendmentservice.asmx/GetAmendments?year={}"

    amendments = {}
    request_url = WSL_WEB_SERVICES_HOST + SERVICE_URL.format(year)
    response = requests.get(request_url)
    namespace = {"waleg": "http://WSLWebServices.leg.wa.gov/"}
    tree = ElementTree.ElementTree(ElementTree.fromstring(response.text))
    amendment_tree = tree.getroot()
    for amendment in amendment_tree:
        amendments[amendment.find("waleg:BillId", namespace).text] = Amendment(
                getattr(amendment.find("waleg:Name", namespace), "text", None),
                getattr(amendment.find("waleg:BillId", namespace), "text", None),
                getattr(amendment.find("waleg:LegislativeSession", namespace), "text", None),
                getattr(amendment.find("waleg:Type", namespace), "text", None),
                getattr(amendment.find("waleg:FloorNumber", namespace), "text", None),
                getattr(amendment.find("waleg:SponsorName", namespace), "text", None),
                getattr(amendment.find("waleg:Description", namespace), "text", None),
                getattr(amendment.find("waleg:Drafter", namespace), "text", None),
                getattr(amendment.find("waleg:FloorAction", namespace), "text", None),
                getattr(amendment.find("waleg:FloorActionDate", namespace), "text", None),
                getattr(amendment.find("waleg:DocumentExists", namespace), "text", None),
                getattr(amendment.find("waleg:HtmUrl", namespace), "text", None),
                getattr(amendment.find("waleg:PdfUrl", namespace), "text", None),
                getattr(amendment.find("waleg:Agency", namespace), "text", None)
            )

    return amendments