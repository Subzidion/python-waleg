class Amendment(object):
    """
    <BillNumber>int</BillNumber>
    <Name>string</Name>
    <BillId>string</BillId>
    <LegislativeSession>string</LegislativeSession>
    <Type>string</Type>
    <FloorNumber>int</FloorNumber>
    <SponsorName>string</SponsorName>
    <Description>string</Description>
    <Drafter>string</Drafter>
    <FloorAction>string</FloorAction>
    <FloorActionDate>dateTime</FloorActionDate>
    <DocumentExists>boolean</DocumentExists>
    <HtmUrl>string</HtmUrl>
    <PdfUrl>string</PdfUrl>
    <Agency>string</Agency>
    """
    def __init__(self, name, bill_id, legislative_sesion, amendment_type, floor_number, 
                 sponsor_name, description, drafter, floor_action, floor_action_date, 
                 document_exists, htm_url, pdf_url, agency):
        self._name = name
        self._bill_id = bill_id
        self._legislative_session = legislative_sesion
        self._amendment_type = amendment_type
        self._floor_number = floor_number
        self._sponsor_name = sponsor_name
        self._description = description
        self._drafter = drafter
        self._floor_action = floor_action
        self._floor_action_date = floor_action_date
        self._document_exists = document_exists
        self._htm_url = htm_url
        self._pdf_url = pdf_url
        self._agency = agency

    @property
    def name(self):
        return self._name

    @property
    def bill_id(self):
        return self._bill_id

    @property
    def legislative_session(self):
        return self._legislative_session

    @property
    def amendment_type(self):
        return self._amendment_type

    @property
    def floor_number(self):
        return self._floor_number

    @property
    def sponsor_name(self):
        return self._sponsor_name

    @property
    def description(self):
        return self._description

    @property
    def drafter(self):
        return self._drafter

    @property
    def floor_action(self):
        return self._floor_action

    @property
    def floor_action_date(self):
        return self._floor_action_date

    @property
    def document_exists(self):
        return self._document_exists

    @property
    def html_url(self):
        return self._htm_url

    @property
    def pdf_url(self):
        return self._pdf_url

    @property
    def agency(self):
        return self._agency