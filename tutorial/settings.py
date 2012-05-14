BOT_NAME = 'tutorial'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
ITEM_PIPELINES = [
'tutorial.pipelines.FicheroJsonTagsPipeline',
'tutorial.pipelines.FicheroJsonPipeline',
]
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

