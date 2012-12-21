from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implements

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content

from kotti_link import _


class Link(Content):
    """Link content type"""

    implements(IDefaultWorkflow)

    id = Column(
        Integer(),
        ForeignKey('contents.id'),
        primary_key=True
    )

    link = Column(Unicode())

    type_info = Content.type_info.copy(
        name=u'Link',
        title=_(u'Link'),
        add_view=u'add_link',
        addable_to=['Document', ],
        selectable_default_views=[
            ('redirect', _(u"Redirect View")),
            ('popup', _(u"Popup View")),
        ],
    )

    def __init__(self, link, **kwargs):
        super(Link, self).__init__(**kwargs)
        self.link = link
