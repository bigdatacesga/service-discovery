"""Tests for the service discovery API"""
import unittest
import consul


class consulTestCase(unittest.TestCase):

    def setUp(self):
        self.service = consul.Client()

    def tearDown(self):
        pass

    def test_register_new_service(self):
        service_name = 'unittest'
        service_id = 'unittest1'
        service_address = '9.9.9.9'
        self.service.register(id=service_id, name=service_name, address=service_address)
        returned = self.service.info(name=service_name)
        # Clean up
        self.service.deregister(service_id)

        self.assertEqual(returned[0]['ServiceID'], service_id)
        self.assertEqual(returned[0]['ServiceName'], service_name)
        self.assertEqual(returned[0]['ServiceAddress'], service_address)

    def test_deregister_service(self):
        service_name = 'unittest'
        service_id = 'unittest1'
        service_address = '9.9.9.9'
        self.service.register(id=service_id, name=service_name, address=service_address)
        returned = self.service.deregister(service_id)

        self.assertEqual(returned.status_code, 200)

    def test_deregister_nonexistent_service(self):
        service_id = 'non_existing_service'
        returned = self.service.deregister(service_id)

        # In consul deregistering a nonexistent service also returns exit status 200
        self.assertEqual(returned.status_code, 200)

    def test_list_services(self):
        returned = self.service.list()

        self.assertTrue(isinstance(returned, dict))

    def test_info_service(self):
        service_name = 'unittest-info'
        service_id = 'unittest1'
        service_address = '9.9.9.9'
        self.service.register(id=service_id, name=service_name, address=service_address)
        returned = self.service.info(name=service_name)
        # Clean up
        self.service.deregister(service_id)

        self.assertEqual(returned[0]['ServiceID'], service_id)
        self.assertEqual(returned[0]['ServiceName'], service_name)
        self.assertEqual(returned[0]['ServiceAddress'], service_address)

    def test_info_nonexistent_service(self):
        returned = self.service.info(name='nonexistent_service_ABC')
        self.assertEqual(returned, [])


if __name__ == '__main__':
    unittest.main()
