from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.actions.discord.notifiers import SendDiscordMessageSpiderFinished
from spidermon.contrib.monitors.mixins import StatsMonitorMixin, ValidationMonitorMixin
from spidermon.contrib.scrapy.monitors import FinishReasonMonitor

@monitors.name("SKU validation")
class SkuValidationMonitor(Monitor, ValidationMonitorMixin):
    @monitors.name("Maximum sku missing")
    def test_maximum_sku_missing(self):
        self.check_missing_required_fields_percent(field_names=['sku', 'price'], allowed_percent=0.10)

@monitors.name('Item validation')
class ItemValidationMonitor(Monitor, StatsMonitorMixin):
    @monitors.name('No item validation errors')
    def test_no_item_validation_errors(self):
        validation_errors = getattr(
            self.stats, 'spidermon/validation/fields/errors', 0
        )
        self.assertEqual(validation_errors, 0, msg='Found validation errors in {} fields'.format(validation_errors))



class SpiderCloseMonitorSuite(MonitorSuite):
    monitors = [SkuValidationMonitor, ItemValidationMonitor, FinishReasonMonitor]

    monitors_failed_actions = [SendDiscordMessageSpiderFinished]