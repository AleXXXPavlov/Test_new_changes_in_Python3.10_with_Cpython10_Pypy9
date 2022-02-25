import asyncio
from inspect import getfullargspec
import unittest


class AsyncioLoopTest(unittest.TestCase):
    def test_removing_loop(self):
        """
        Testing that the loop parameter has been removed from most of asyncio‘s
         high-level API.
        """
        self.assertFalse('loop' in getfullargspec(asyncio.sleep).kwonlyargs)
        self.assertFalse('loop' in getfullargspec(asyncio.gather).kwonlyargs)
        self.assertFalse('loop' in getfullargspec(asyncio.shield).kwonlyargs)
        self.assertFalse('loop' in getfullargspec(asyncio.wait_for).kwonlyargs)
        self.assertFalse('loop' in getfullargspec(asyncio.wait).kwonlyargs)
        self.assertFalse('loop' in getfullargspec(asyncio.as_completed).kwonlyargs)

        # still exist loop-argument
        self.assertTrue('loop' in getfullargspec(asyncio.run_coroutine_threadsafe).args)
        self.assertTrue('loop' in getfullargspec(asyncio.all_tasks).args)
        self.assertTrue('loop' in getfullargspec(asyncio.current_task).args)


if __name__ == '__main__':
    unittest.main()
