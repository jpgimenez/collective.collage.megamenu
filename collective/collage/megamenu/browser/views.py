from Acquisition import aq_inner

from zope.interface import noLongerProvides, alsoProvides
from zope.component import queryUtility, getMultiAdapter
from zope.interface import providedBy

from Products.Five import BrowserView

from Products.statusmessages.interfaces import IStatusMessage
from plone.registry.interfaces import IRegistry

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode

from collective.collage.megamenu.interfaces import IMegamenuCapable, IMegamenuEnabled, IMegamenuSettings
from collective.collage.megamenu import message_factory as _

from plone.memoize.instance import memoize

## Enabler/Disabler View
class EnablerView(BrowserView):

    def __init__(self, context, request):
        self.context = aq_inner(context)
        self.request = request
        self.globals_view = getMultiAdapter((self.context, self.request), name="plone")

    def enable(self):
        message = ""

        if not self.is_enabled():
            alsoProvides(self.context, IMegamenuEnabled)
            message = _(u"Folder can now be used as megamenu")

        self.return_with_message(message)


    def disable(self):
        message = ""

        if self.is_enabled():
            noLongerProvides(self.context, IMegamenuEnabled)
            message = _(u"Folder can no longer be used as megamenu")

        self.return_with_message(message)

    @memoize
    def is_capable(self):
        return IMegamenuCapable in providedBy(self.context)

    @memoize
    def is_enabled(self):
        globals = self.globals_view
        if globals.isFolderOrFolderDefaultPage():
            folder = globals.getCurrentFolder()
            return IMegamenuEnabled in providedBy(folder)
        else:
            return False

    @memoize
    def is_disabled(self):
        globals = self.globals_view
        if globals.isFolderOrFolderDefaultPage():
            folder = globals.getCurrentFolder()
            return not IMegamenuEnabled in providedBy(folder)
        else:
            return False

    def return_with_message(self, message):
        request = self.request

        if message:
            self.context.reindexObject(idxs=['object_provides', ])
            IStatusMessage(request).addStatusMessage(message, type="info")

        return request.response.redirect(request.HTTP_REFERER)

    def set_as_current(self):
        request = self.request
        context = self.context
        title = safe_unicode(context.Title())
        message = _(u"Press 'Save' button to select '${title}' as Megamenu folder", mapping={'title': title})
        IStatusMessage(request).addStatusMessage(message, type="info")
        utool = getToolByName(context, 'portal_url')
        portal_url = utool.getPortalObject().absolute_url()
        uid = context.UID()
        url = '%s/@@megamenu-controlpanel?form.widgets.megamenu_folder:list=%s' % (portal_url, uid)
        return request.response.redirect(url)

## Configuration options View
class SettingsView(BrowserView):

    def __init__(self, context, request):
        self.context = aq_inner(context)
        self.request = request
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IMegamenuSettings)
        self.enabled = settings.enabled and settings.megamenu_folder
        self.menufolder = None
        if self.enabled:
            catalog = getToolByName(self.context, 'portal_catalog')
            brain = catalog(UID=settings.megamenu_folder)
            if len(brain)>0:
                try:
                    self.menufolder = brain[0].getObject()
                except:
                    pass

        self.ajax = settings.deferred_rendering

