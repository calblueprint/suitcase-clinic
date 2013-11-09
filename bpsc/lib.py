import os
import yaml

from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, Template


EMAIL_TEMPLATE_PATH = os.path.join(settings.SETTINGS_PATH, 'templates', 'email_templates')
SUITCASE_EMAIL = 'bpsc@bpsc.com'

def send_suitcase_email(template_name, context_dict, recipient_list, from_address=SUITCASE_EMAIL):
    """ Templates for emails should be yaml files, with 'subject' and 'body' sections, so
    'template_name' should be something like 'foo.yml'.
    'context_dict' should be just a Python dictionary of all the context variables you want
    available in the email templates (e.g. {'client_name': 'Mr. Cient', 'resource_url': 'www.resource.com'})
    'recipient_list' must be a list of email addresse strings we are sending to, even if it
    there is only one email in the list. On the other hand, 'from_address' is just one
    email address string.
    """
    f = open(os.path.join(EMAIL_TEMPLATE_PATH, template_name))
    email_template = yaml.load(f)
    f.close()
    context = Context(context_dict)
    subject_template = Template(email_template['subject'])
    body_template = Template(email_template['body'])
    subject = subject_template.render(context)
    body = body_template.render(context)
    send_mail(subject, body, from_address, recipient_list)
