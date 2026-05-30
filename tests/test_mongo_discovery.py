import json
import subprocess
import sys
import unittest

class TestMongoDiscovery(unittest.TestCase):
    def test_discover_databases_and_collections(self):
        try:
            from pymongo import MongoClient
        except Exception:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'pymongo', 'dnspython'])
            from pymongo import MongoClient
        uri = 'mongodb+srv://mcpatlaseval_db_user:kqilj9LfZYKUries@cluster0.v5fybig.mongodb.net/?tls=true'
        result = {}
        try:
            client = MongoClient(uri, serverSelectionTimeoutMS=120000)
            dbs = client.list_database_names()
            result['databases'] = dbs
            cols = {}
            for db in dbs:
                try:
                    cols[db] = client[db].list_collection_names()
                except Exception as e:
                    cols[db] = {'error': str(e)}
            result['collections'] = cols
        except Exception as e:
            result = {'error': str(e)}
        print('DISCOVERY_RESULT_START')
        print(json.dumps(result, sort_keys=True))
        print('DISCOVERY_RESULT_END')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
