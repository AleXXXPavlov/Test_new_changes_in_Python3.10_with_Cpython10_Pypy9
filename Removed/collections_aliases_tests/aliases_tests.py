import unittest

from collections import abc
from sys import version_info


class AliasExistTest(unittest.TestCase):
    def test_import_error(self):
        """
        Testing moving Collections Abstract Base Classes to the collections.abc module
        """
        with self.assertRaises(ImportError):
            from collections import Hashable

        with self.assertRaises(ImportError):
            from collections import Sized

        with self.assertRaises(ImportError):
            from collections import Callable

        with self.assertRaises(ImportError):
            from collections import Iterable

        with self.assertRaises(ImportError):
            from collections import Collection

        with self.assertRaises(ImportError):
            from collections import Iterator

        with self.assertRaises(ImportError):
            from collections import Reversible

        with self.assertRaises(ImportError):
            from collections import Generator

        with self.assertRaises(ImportError):
            from collections import Sequence

        with self.assertRaises(ImportError):
            from collections import MutableSequence

        with self.assertRaises(ImportError):
            from collections import ByteString

        with self.assertRaises(ImportError):
            from collections import Set

        with self.assertRaises(ImportError):
            from collections import MutableSet

        with self.assertRaises(ImportError):
            from collections import Mapping

        with self.assertRaises(ImportError):
            from collections import MutableMapping

        with self.assertRaises(ImportError):
            from collections import MappingView

        with self.assertRaises(ImportError):
            from collections import ItemsView

        with self.assertRaises(ImportError):
            from collections import KeysView

        with self.assertRaises(ImportError):
            from collections import ValuesView

        with self.assertRaises(ImportError):
            from collections import Awaitable

        with self.assertRaises(ImportError):
            from collections import Coroutine

        with self.assertRaises(ImportError):
            from collections import AsyncIterable

        with self.assertRaises(ImportError):
            from collections import AsyncIterator

        with self.assertRaises(ImportError):
            from collections import AsyncGenerator

    def test_not_import_error(self):
        """
        Testing moving Collections Abstract Base Classes to the collections.abc module
        """
        abc_classes = [
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'ByteString', 'Callable', 'Collection', 'Container',
            'Coroutine', 'Generator', 'Hashable', 'ItemsView',
            'Iterable', 'Iterator', 'KeysView', 'Mapping',
            'MappingView', 'MutableMapping', 'MutableSequence', 'MutableSet',
            'Reversible', 'Sequence', 'Set', 'Sized',
            'ValuesView'
        ]

        for abc_class in abc_classes:
            self.assertTrue(abc_class in dir(abc))

    # @unittest.skipIf(version_info.minor > 9, "check in Python 3.9")
    # def test_import_warn(self):
    #     """
    #     Testing that using ABC Classes from collections raise an DeprecationWarning
    #     """
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Hashable
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Sized
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Callable
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Iterable
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Collection
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Iterator
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Reversible
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Generator
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Sequence
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import MutableSequence
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import ByteString
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Set
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import MutableSet
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Mapping
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import MutableMapping
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import MappingView
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import ItemsView
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import KeysView
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import ValuesView
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Awaitable
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import Coroutine
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import AsyncIterable
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import AsyncIterator
    #
    #     with self.assertWarns(DeprecationWarning):
    #         from collections import AsyncGenerator
    #

if __name__ == "__main__":
    unittest.main()

