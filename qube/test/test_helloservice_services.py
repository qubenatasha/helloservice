#!/usr/bin/python
"""
Add docstring here
"""
import os
import time
import unittest

import mock
from mock import patch
import mongomock


with patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient):
    os.environ['HELLOSERVICE_MONGOALCHEMY_CONNECTION_STRING'] = ''
    os.environ['HELLOSERVICE_MONGOALCHEMY_SERVER'] = ''
    os.environ['HELLOSERVICE_MONGOALCHEMY_PORT'] = ''
    os.environ['HELLOSERVICE_MONGOALCHEMY_DATABASE'] = ''

    from qube.src.models.helloservice import HelloService
    from qube.src.services.helloserviceservice import HelloServiceService
    from qube.src.commons.context import AuthContext
    from qube.src.commons.error import ErrorCodes, HelloServiceServiceError


class TestHelloServiceService(unittest.TestCase):
    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def setUp(self):
        context = AuthContext("23432523452345", "tenantname",
                              "987656789765670", "orgname", "1009009009988",
                              "username", False)
        self.helloserviceService = HelloServiceService(context)
        self.helloservice_api_model = self.createTestModelData()
        self.helloservice_data = self.setupDatabaseRecords(self.helloservice_api_model)
        self.helloservice_someoneelses = \
            self.setupDatabaseRecords(self.helloservice_api_model)
        self.helloservice_someoneelses.tenantId = "123432523452345"
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            self.helloservice_someoneelses.save()
        self.helloservice_api_model_put_description \
            = self.createTestModelDataDescription()
        self.test_data_collection = [self.helloservice_data]

    def tearDown(self):
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            for item in self.test_data_collection:
                item.remove()
            self.helloservice_data.remove()

    def createTestModelData(self):
        return {'name': 'test123123124'}

    def createTestModelDataDescription(self):
        return {'description': 'test123123124'}

    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def setupDatabaseRecords(self, helloservice_api_model):
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            helloservice_data = HelloService(name='test_record')
            for key in helloservice_api_model:
                helloservice_data.__setattr__(key, helloservice_api_model[key])

            helloservice_data.description = 'my short description'
            helloservice_data.tenantId = "23432523452345"
            helloservice_data.orgId = "987656789765670"
            helloservice_data.createdBy = "1009009009988"
            helloservice_data.modifiedBy = "1009009009988"
            helloservice_data.createDate = str(int(time.time()))
            helloservice_data.modifiedDate = str(int(time.time()))
            helloservice_data.save()
            return helloservice_data

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_post_helloservice(self, *args, **kwargs):
        result = self.helloserviceService.save(self.helloservice_api_model)
        self.assertTrue(result['id'] is not None)
        self.assertTrue(result['name'] == self.helloservice_api_model['name'])
        HelloService.query.get(result['id']).remove()

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_put_helloservice(self, *args, **kwargs):
        self.helloservice_api_model['name'] = 'modified for put'
        id_to_find = str(self.helloservice_data.mongo_id)
        result = self.helloserviceService.update(
            self.helloservice_api_model, id_to_find)
        self.assertTrue(result['id'] == str(id_to_find))
        self.assertTrue(result['name'] == self.helloservice_api_model['name'])

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_put_helloservice_description(self, *args, **kwargs):
        self.helloservice_api_model_put_description['description'] =\
            'modified for put'
        id_to_find = str(self.helloservice_data.mongo_id)
        result = self.helloserviceService.update(
            self.helloservice_api_model_put_description, id_to_find)
        self.assertTrue(result['id'] == str(id_to_find))
        self.assertTrue(result['description'] ==
                        self.helloservice_api_model_put_description['description'])

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_get_helloservice_item(self, *args, **kwargs):
        id_to_find = str(self.helloservice_data.mongo_id)
        result = self.helloserviceService.find_by_id(id_to_find)
        self.assertTrue(result['id'] == str(id_to_find))

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_get_helloservice_item_invalid(self, *args, **kwargs):
        id_to_find = '123notexist'
        with self.assertRaises(HelloServiceServiceError):
            self.helloserviceService.find_by_id(id_to_find)

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_get_helloservice_list(self, *args, **kwargs):
        result_collection = self.helloserviceService.get_all()
        self.assertTrue(len(result_collection) == 1,
                        "Expected result 1 but got {} ".
                        format(str(len(result_collection))))
        self.assertTrue(result_collection[0]['id'] ==
                        str(self.helloservice_data.mongo_id))

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_delete_toolchain_not_system_user(self, *args, **kwargs):
        id_to_delete = str(self.helloservice_data.mongo_id)
        with self.assertRaises(HelloServiceServiceError) as ex:
            self.helloserviceService.delete(id_to_delete)
        self.assertEquals(ex.exception.errors, ErrorCodes.NOT_ALLOWED)

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_delete_toolchain_by_system_user(self, *args, **kwargs):
        id_to_delete = str(self.helloservice_data.mongo_id)
        self.helloserviceService.auth_context.is_system_user = True
        self.helloserviceService.delete(id_to_delete)
        with self.assertRaises(HelloServiceServiceError) as ex:
            self.helloserviceService.find_by_id(id_to_delete)
        self.assertEquals(ex.exception.errors, ErrorCodes.NOT_FOUND)
        self.helloserviceService.auth_context.is_system_user = False

    @patch('mongomock.write_concern.WriteConcern.__init__', return_value=None)
    def test_delete_toolchain_item_someoneelse(self, *args, **kwargs):
        id_to_delete = str(self.helloservice_someoneelses.mongo_id)
        with self.assertRaises(HelloServiceServiceError):
            self.helloserviceService.delete(id_to_delete)
