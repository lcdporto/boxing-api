from django.conf import settings

from post_office import mail
from post_office.models import EmailTemplate

from boxing.api.models import Lending
from boxing.api import utils

class BoxingEmail(object):

    template = None
    context = None
    context_data = {}
    data = None

    def __init__(self):
        self.validate_context()
        assert self.template, 'Must set template attribute on subclass.'

    def validate_context(self):
        """
        Make sure there are no duplicate context objects
        or we might end up with switched data

        Converting the tuple to a set gets rid of the
        eventual duplicate objects, comparing the length
        of the original tuple and set tells us if we
        have duplicates in the tuple or not
        """
        if self.context and len(self.context) != len(set(self.context)):
            raise Exception('Cannot have duplicated context objects.')

    def get_instance_of(self, model_cls):
        """
        Search the data to find a instance
        of a model specified in the template
        """
        for obj in self.data.values():
            if isinstance(obj, model_cls):
                return obj
        raise Exception('Context Not Found')

    def get_context(self):
        """
        Create a dict with the context data
        """
        if not self.context:
            return
        for model_cls in self.context:
            key = utils.camel_to_snake(model_cls.__name__)
            self.context_data[key] = self.get_instance_of(model_cls)

    def send(self, to, **data):
        """
        This is the method to be called
        """
        self.data = data
        self.get_context()
        if settings.EMAIL_SEND_EMAILS:
            try:
                mail.send(to, template=self.template, context=self.context_data)
            except EmailTemplate.DoesNotExist:
                msg = 'Trying to use a non existent email template {0}'.format(self.template)
                logger.error(msg)

class LendingCreated(BoxingEmail):
    """
    Email sent to staff when lending has been created
    """
    template = 'LENDING_CREATED'
    context = (Lending, )

class LendingPending(BoxingEmail):
    """
    Email sent to user when lending has been created
    and waits staff approval
    """
    template = 'LENDING_PENDING'
    context = (Lending, )

class LendingApproved(BoxingEmail):
    """
    Email sent to user when lending has been approved
    """
    template = 'LENDING_APPROVED'
    context = (Lending, )

class LendingRefused(BoxingEmail):
    """
    Email sent to user when lending has been refused
    """
    template = 'LENDING_REFUSED'
    context = (Lending, )

class LendingReturned(BoxingEmail):
    """
    Email sent to user when item returned
    """
    template = 'LENDING_RETURNED'
    context = (Lending, )
