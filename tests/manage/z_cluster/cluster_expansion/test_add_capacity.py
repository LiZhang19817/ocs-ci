import logging
import pytest

from ocs_ci.framework.testlib import ignore_leftovers, ManageTest, tier1
from ocs_ci.ocs.resources import storage_cluster

logger = logging.getLogger(__name__)


@ignore_leftovers
@tier1
class TestAddCapacity(ManageTest):
    """
    Automates adding variable capacity to the cluster while IOs running
    """
    def test_add_capacity(self):
        """
        Test to add variable capacity to the OSD cluster while IOs running
        """
        osd_size = storage_cluster.get_osd_size()
        result = storage_cluster.add_capacity(osd_size)
        assert result, logger.info("Test Failed, new pods failed reaching running state")