#!/usr/bin/python
"""
Add docstring here
"""
import time
import unittest

import mock

from mock import patch
import mongomock


class TestHelloServiceModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("before class")

    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def test_create_helloservice_model(self):
        from qube.src.models.helloservice import HelloService
        helloservice_data = HelloService(name='testname')
        helloservice_data.tenantId = "23432523452345"
        helloservice_data.orgId = "987656789765670"
        helloservice_data.createdBy = "1009009009988"
        helloservice_data.modifiedBy = "1009009009988"
        helloservice_data.createDate = str(int(time.time()))
        helloservice_data.modifiedDate = str(int(time.time()))
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            helloservice_data.save()
            self.assertIsNotNone(helloservice_data.mongo_id)
            helloservice_data.remove()

    @classmethod
    def tearDownClass(cls):
        print("After class")


if __name__ == '__main__':
    unittest.main()
