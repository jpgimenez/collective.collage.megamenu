from collective.collage.megamenu.interfaces import IMegamenuEnabled
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.BaseContent import BaseContent

def getIcon(self, relative_to_portal=0):
    utool = getToolByName(self, 'portal_url')
    portal_url = utool()
    
    if IMegamenuEnabled.providedBy(self):
        if not relative_to_portal:
            return '%s++resource++collective.collage.megamenu/megamenu.gif' % (relative_to_portal and '' or portal_url + '/')
    else:
        return BaseContent.getIcon(self, relative_to_portal)
