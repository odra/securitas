import pytest

from securitas.representation.user import User


@pytest.fixture
def dummy_user_dict():
    return {
        'cn': ['Dummy User'],
        'displayname': ['Dummy User'],
        'dn': 'uid=dummy,cn=users,cn=accounts,dc=example,dc=com',
        'fascreationtime': ['20200122162312Z'],
        'fasgithubusername': ['dummy'],
        'fasgitlabusername': ['dummy'],
        'fasgpgkeyid': ['key1', 'key2'],
        'fasircnick': ['dummy'],
        'faslocale': ['en-US'],
        'fasrhbzemail': ['dummy@example.com'],
        'fastimezone': ['UTC'],
        'gecos': ['Dummy User'],
        'gidnumber': ['158200186'],
        'givenname': ['Dummy'],
        'has_keytab': True,
        'has_password': True,
        'homedirectory': ['/home/dummy'],
        'initials': ['DU'],
        'ipauniqueid': ['7ce42ff4-3d33-11ea-9ce7-52540019b1a3'],
        'ipasshpubkey': [
            'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtX/SK86GrOa0xUadeZVbDXCj6wseamJQTpvjzNdKLgIBuQnA2dnR+jBS54rxUzHD1In/yI9r1VXr+KVZG4ULHmSuP3Icl0SUiVs+u+qeHP77Fa9rnQaxxCFL7uZgDSGSgMx0XtiQUrcumlD/9mrahCefU0BIKfS6e9chWwJnDnPSpyWf0y0NpaGYqPaV6Ukg2Z5tBvei6ghBb0e9Tusg9dHGvpv2B23dCzps6s5WBYY2TqjTHAEuRe6xR0agtPUE1AZ/DvSBKgwEz6RXIFOtv/fnZ0tERh238+n2nohMZNo1QAtQ6I0U9Kx2gdAgHRaMN6GzmbThji/MLgKlIJPSh',  # noqa: E501
            'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDuxGxBwWH5xMLAuIUAVU3O8ZViYWW64V3tJRob+eZngeR95PzUDeH0UlZ58bPyucpMowZNgJucsHyUjqal5bctv9Q5r224Of1R3DJqIViE16W3zncGNjbgiuc66wcO2o84HEm2Zi+v4cwU8ykM0m9zeG0257aVW4/L/fDAyR55NRJ7zLIyRmGMcjkN6j02wbGK89xXJKHMtRKa5Kg4GJx3HUae79C3B7SyoRAuyzLT6GmpMZ3XRa/khZ3t4xfUtSMV6DuvR5KJ9Wg5B20ecua1tNXOLHC3dU5L+P6Pb7+HL1sxHiYbaiBPJbosMkM2wqd3VyduQDQTO4BJyly/ruIN',  # noqa: E501
        ],
        'krbcanonicalname': ['dummy@EXAMPLE.COM'],
        'krblastpwdchange': ['20200122162313Z'],
        'krbpasswordexpiration': ['20200421162313Z'],
        'krbprincipalname': ['dummy@EXAMPLE.COM'],
        'loginshell': ['/bin/bash'],
        'mail': ['dummy@example.com'],
        'memberof_group': ['ipausers'],
        'nsaccountlock': False,
        'objectclass': [
            'top',
            'person',
            'organizationalperson',
            'inetorgperson',
            'inetuser',
            'posixaccount',
            'krbprincipalaux',
            'krbticketpolicyaux',
            'ipaobject',
            'ipasshuser',
            'fasuser',
            'ipaSshGroupOfPubKeys',
            'mepOriginEntry',
        ],
        'preserved': False,
        'sn': ['User'],
        'uid': ['dummy'],
        'uidnumber': ['158200186'],
    }


def test_user(dummy_user_dict):
    """Test the User representation"""
    user = User(dummy_user_dict)
    assert user.username == "dummy"
    assert user.firstname == "Dummy"
    assert user.lastname == "User"
    assert user.name == "Dummy User"
    assert user.mail == "dummy@example.com"
    assert user.sshpubkeys == [
        'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtX/SK86GrOa0xUadeZVbDXCj6wseamJQTpvjzNdKLgIBuQnA2dnR+jBS54rxUzHD1In/yI9r1VXr+KVZG4ULHmSuP3Icl0SUiVs+u+qeHP77Fa9rnQaxxCFL7uZgDSGSgMx0XtiQUrcumlD/9mrahCefU0BIKfS6e9chWwJnDnPSpyWf0y0NpaGYqPaV6Ukg2Z5tBvei6ghBb0e9Tusg9dHGvpv2B23dCzps6s5WBYY2TqjTHAEuRe6xR0agtPUE1AZ/DvSBKgwEz6RXIFOtv/fnZ0tERh238+n2nohMZNo1QAtQ6I0U9Kx2gdAgHRaMN6GzmbThji/MLgKlIJPSh',  # noqa: E501
        'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDuxGxBwWH5xMLAuIUAVU3O8ZViYWW64V3tJRob+eZngeR95PzUDeH0UlZ58bPyucpMowZNgJucsHyUjqal5bctv9Q5r224Of1R3DJqIViE16W3zncGNjbgiuc66wcO2o84HEm2Zi+v4cwU8ykM0m9zeG0257aVW4/L/fDAyR55NRJ7zLIyRmGMcjkN6j02wbGK89xXJKHMtRKa5Kg4GJx3HUae79C3B7SyoRAuyzLT6GmpMZ3XRa/khZ3t4xfUtSMV6DuvR5KJ9Wg5B20ecua1tNXOLHC3dU5L+P6Pb7+HL1sxHiYbaiBPJbosMkM2wqd3VyduQDQTO4BJyly/ruIN',  # noqa: E501
    ]
    assert user.timezone == "UTC"
    assert user.locale == "en-US"
    assert user.ircnick == "dummy"
    assert user.gpgkeys == ["key1", "key2"]
    assert user.groups == ["ipausers"]
    assert user.github == "dummy"
    assert user.gitlab == "dummy"
    assert user.rhbz_mail == "dummy@example.com"


def test_user_no_displayname(dummy_user_dict):
    """Test that we fallback to gecos if there is no displayname"""
    del dummy_user_dict["displayname"]
    dummy_user_dict["gecos"] = ["GCOS"]
    user = User(dummy_user_dict)
    assert user.name == "GCOS"


def test_user_no_displayname_no_gcos(dummy_user_dict):
    """Test that we fallback to cn if there is no displayname nor gcos"""
    del dummy_user_dict["displayname"]
    del dummy_user_dict["gecos"]
    dummy_user_dict["cn"] = ["CN"]
    user = User(dummy_user_dict)
    assert user.name == "CN"


def test_user_no_displayname_no_gcos_no_cn(dummy_user_dict):
    """Test that we fallback to cn if there is no displayname nor gcos"""
    del dummy_user_dict["displayname"]
    del dummy_user_dict["gecos"]
    del dummy_user_dict["cn"]
    user = User(dummy_user_dict)
    assert user.name is None
