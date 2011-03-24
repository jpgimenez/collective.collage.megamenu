from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.site.hooks import getSite
from Products.CMFCore.utils import getToolByName
from collective.collage.megamenu.interfaces import IMegamenuEnabled

class MegamenuesVocabulary(object):
    """
    Returns a list of all megamenu enabled objects in site
    """
    
    implements(IVocabularyFactory)

    def __call__(self, context):
        site = getSite()
        catalog = getToolByName(site, 'portal_catalog', None)
        if catalog is None:
            return SimpleVocabulary([])

        megamenues = catalog(object_provides=IMegamenuEnabled.__identifier__)

        terms = []

        for menu in megamenues:
            terms.append(SimpleTerm(value=menu.UID, token=menu.UID, title=menu.Title))

        return SimpleVocabulary(terms)

MegamenuesVocabularyFactory = MegamenuesVocabulary()
