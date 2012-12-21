from mock import patch
from pyramid.httpexceptions import HTTPFound

from kotti.resources import get_root
from kotti.testing import testing_db_url

from kotti_link.resources import Link
from kotti_link.views import LinkView


def test_view_view(db_session, dummy_request):
    root = get_root()
    link = root['link'] = Link(link=u'/', title=u'Test Link')
    view = LinkView(link, dummy_request)
    assert(isinstance(view.view(), dict))


def test_redirect_view(db_session, dummy_request, extra_principals):
    from kotti import main
    from kotti.security import get_principals

    settings = {'sqlalchemy.url': testing_db_url(),
                'kotti.secret': 'dude'}
    with patch('kotti.resources.initialize_sql'):
        main({}, **settings)

    root = get_root()
    link = root['link'] = Link(link=u'/', title=u'Test Link')
    view = LinkView(link, dummy_request)
    assert(isinstance(view.redirect(), HTTPFound))

    bob = get_principals()[u'bob']
    dummy_request.user = bob
    acl = [('Allow', 'system.Everyone', 'edit')]
    link.__acl__ = acl
    view = LinkView(link, dummy_request)
    assert(isinstance(view.redirect(), dict))


def test_popup_view(db_session, dummy_request):
    pass
