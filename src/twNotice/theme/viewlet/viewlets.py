# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from plone import api
from DateTime import DateTime


class BodyBottomScript(base.ViewletBase):
    """ Body Bottom Script  """


class ContactUsInHeader(base.ViewletBase):
    """  """


class D3PieScript(base.ViewletBase):
    """  """


class CountDown(base.ViewletBase):
    """  """

    def get_deadline(self):
        context = self.context
        request = self.request

        notice_view = api.content.get_view(
            name='notice_view',
            context=context,
            request=request,
        )

        result = {}
        try:
            deadline = notice_view.get_deadline()
            result['year'] = str(int(deadline.split('/')[0]) + 1911)
            result['month'] = deadline.split('/')[1]
            result['day'] = deadline.split('/')[2].split()[0]
            result['hour'], result['minute'] = deadline.split()[1].split(':')[0:2]
        except:
            return None

        if DateTime('%s/%s/%s %s:%s' % (result['year'], result['month'], result['day'], result['hour'], result['minute'])) < DateTime():
            return None

        return result


