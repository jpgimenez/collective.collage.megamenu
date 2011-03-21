from Acquisition import aq_inner

from zope.interface import Interface
from zope.component import getMultiAdapter

from Products.Collage.browser.views import BaseView, RowView
from Products.Collage.interfaces import ICollageEditLayer
from Products.ATContentTypes.interfaces import IATLink

from plone.memoize.instance import memoize


class IMenuLayoutSkin(Interface):
    """Interface for skinable views."""
    pass

class BasicMenuLayout(BaseView):
    skinInterfaces = (IMenuLayoutSkin, )
    
    title = "Menu"
    
    @memoize
    def object(self):
        return aq_inner(self.context)
        
    def url(self):
        object = self.object()
        # If it's a link
        if IATLink.providedBy(object):
            remoteUrl = object.getRemoteUrl()
            # If it's a local link
            if remoteUrl[0] == '/':
                # Get portal object and re-create link
                context = aq_inner(self.context)
                request = self.request
                portal_state = getMultiAdapter((context, request), name="plone_portal_state")
                return '%s%s' % (portal_state.portal_url(), remoteUrl)
            else:
                return remoteUrl
        else:
            # Otherwise, return object's url
            return object.absolute_url()
    
### Skins

class TitleSkin(object):
    title = "Title"

class LinkSkin(object):
    title = "Link"

class HighlightedLinkSkin(object):
    title = "Highlight"

### MenuRow

class MenuRowLayout(RowView):
    """ Special RowView """

    def inComposeView(self):
        return ICollageEditLayer.providedBy(self.request)
 
