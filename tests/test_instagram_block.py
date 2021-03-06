from threading import Event
from unittest.mock import patch, Mock

from nio.testing.block_test_case import NIOBlockTestCase
from nio.util.discovery import not_discoverable

from ..rest_polling.rest_block import RESTPolling
from ..instagram_block import Instagram


@not_discoverable
class InstagramEpilogueEvent(Instagram):

    def __init__(self, event):
        super().__init__()
        self._event = event

    def _epilogue(self):
        super()._epilogue()
        self._event.set()


class TestInstagram(NIOBlockTestCase):

    @patch.object(RESTPolling, "_retry")
    @patch.object(RESTPolling, "_authenticate")
    @patch("requests.get")
    def test_private_user(self, mock_get, mock_auth, mock_retry):
        e = Event()
        blk = InstagramEpilogueEvent(e)
        self.configure_block(blk, {
            "queries": [
                "hashtag1",
                "hashtag2"
            ]
        })
        mock_get.return_value = Mock()
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = \
            {
                "data": [],
                "pagination": {"next_url": "the_url"}
            }
        blk.poll()
        e.wait(2)
        self.assertEqual(blk.page_num, blk.polling_interval().total_seconds())
