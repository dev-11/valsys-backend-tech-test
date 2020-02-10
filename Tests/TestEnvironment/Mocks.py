from unittest.mock import Mock
from Services import CompanyRegistry


def get_company_registry_mock():
    cr = CompanyRegistry()
    cr.is_company_unseen = Mock(name='is_company_unseen')
    cr.is_company_unseen.return_value = True
    return cr
