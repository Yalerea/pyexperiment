"""
test_plo17
"""
import pytest
from plo17 import get_repos_info,get_response_dict

# 测试方法一：不使用夹具

def test_response_status_code():
    '''测试响应是否具有成功的状态代码。'''
    r = get_repos_info()
    assert r.status_code == 200

def test_response_dict():
    '''验证是否表示了适当数量的存储库，以及结果是否完整。'''
    r = get_repos_info()
    response_dict = get_response_dict(r)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 190
    assert complete_results


# 测试方法二；使用夹具
@pytest.fixture
def response():
    """获取一个响应对象。"""
    r = get_repos_info()
    return r

def test_response_status_code(response):
    """测试响应是否具有成功的状态代码。"""
    assert response.status_code == 200

def test_response_dict(response):
    """验证是否表示了适当数量的存储库，以及结果是否完整。"""
    response_dict = get_response_dict(response)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 190
    assert complete_results







