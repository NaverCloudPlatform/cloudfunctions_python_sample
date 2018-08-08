class BaseAuthInfo:

    # Base Auth Info #

    # API Gateway api key
    api_key = ""
    # NCP Access key
    access_key = ''
    # NCP Access secrete
    access_secrete = ''

    # SENS #

    # SENS REST End-point
    sens_ep_path = 'https://api-sens.ncloud.com'
    # SENS project name
    sens_project_name = ''
    # SENS service id
    sens_service_id = ''
    # SENS project secret key
    sens_service_secrete = ''

    # Cloud OutBound Mailer #

    # Outbound Mailer REST End-point
    mail_ep_path = 'https://mail.apigw.ntruss.com/api/v1/mails'

    def get_api_key(self):
        return self.api_key

    def get_access_key(self):
        return self.access_key

    def get_access_secrete(self):
        return self.access_secrete

    def get_sens_service_id(self):
        return self.sens_service_id

    def get_sens_project_name(self):
        return self.sens_project_name

    def get_sens_service_secrete(self):
        return self.sens_service_secrete

    def get_mail_ep_path(self):
        return self.mail_ep_path

    def get_sens_ep_path(self):

        ep_full_path = self.sens_ep_path + '/v1/sms/services/' + self.sens_service_id + '/messages'

        return ep_full_path
