import pytest
import os,sys
print(sys.path)
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from test_data.before_testdta import Beforedata


@pytest.fixture(scope="class")
def ready_data():
    data = Beforedata.do_test_data('test_data', 'test_da.xlsx', 'login')
    yield data