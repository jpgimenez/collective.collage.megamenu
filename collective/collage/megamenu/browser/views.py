from Acquisition import aq_inner

from zope.interface import Interface, noLongerProvides, alsoProvides
from zope.component import getMultiAdapter

from Products.Five import BrowserView

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
        
### Menu Renderer view

class MenuRenderer(BrowserView):

    def __init__(self, context, request):
        self.context = aq_inner(context)
        self.request = request
        portal_state = getMultiAdapter((context, request), name="plone_portal_state")
        self.portal_url = portal_state.portal_url()

    def getItems(self):
        # TODO: Restrict items?
        contents = self.context.getFolderContents()
        
        # Before getting items (actually, before rendering them), remove ICollageEditLayer from request
        composing = ICollageEditLayer.providedBy(self.request)
        if composing:
            noLongerProvides(self.request, ICollageEditLayer)
            
        items = []
        for content in contents:
            item = {}
            item['object'] = content
            item['with_menu'] = content.meta_type == 'Collage'
            item['title'] = content.Title
            item['description'] = content.Description
            if content.meta_type == 'ATLink':
                item['url'] = '%s%s' % (self.portal_url, content.getRemoteUrl)
            else:
                item['url'] = content.getURL()

            if item['with_menu']:
                item['class'] = 'menu-dropdown'
                item['dropdown'] = content.getObject().restrictedTraverse('@@renderer')()
            else:
                item['class'] = ''
                item['dropdown'] = None
                
            items.append(item)

        if composing:
            alsoProvides(self.request, ICollageEditLayer)
            
        return items

