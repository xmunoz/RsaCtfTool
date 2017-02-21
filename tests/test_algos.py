import pytest
from factorize import RSAAttack
import os.path
import inspect


TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(
    inspect.currentframe()))), "data")


class Args(object):
    def __init__(self, *args, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

'''
def test_hastads():
    pubkey_f = os.path.join(TEST_DATA_PATH, "small_exponent.pub")
    cipher_f = os.path.join(TEST_DATA_PATH, "small_exponent.cipher")
    args = Args(publickey=pubkey_f, uncipher=cipher_f)
    a = RSAAttack(args)
    a.attack("hastads")
    cleartext = "\nDidn't I tell you everything would work out in the end? Brixby gave me the "\
"password to the secure server: 56c812da9a3955e3c81453eb035b3d37b3f1bfe407ef701d09cf68dd4bb335b1\n"
    assert a.unciphered ==  cleartext
'''

def test_noveltyprimes():
    pubkey_f = os.path.join(TEST_DATA_PATH, "elite_primes.pub")
    args = Args(publickey=pubkey_f, uncipher=None, private=True)
    a = RSAAttack(args)
    a.attack("noveltyprimes")
    private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIFLAIBAAKCAQMlsYv184kJfRcjeGa7Uc/43pIkU3SevEA7CZXJfA44bUbBYcrf
93xphg2uR5HCFM+Eh6qqnybpIKl3g0kGA4rvtcMIJ9/PP8npdpVE+U4Hzf4IcgOa
OmJiEWZ4smH7LWudMlOekqFTs2dWKbqzlC59NeMPfu9avxxQ15fQzIjhvcz9GhLq
b373XDcn298ueA80KK6Pek+3qJ8YSjZQMrFT+EJehFdQ6yt6vALcFc4CB1B6qVCG
O7hICngCjdYpeZRNbGM/r6ED5Nsozof1oMbtSi8mZEJ/Vlx3gathkUVtlxx/+jlS
cjdM7AFV5fkRidt0LkwosDoPoRz/sDFz0qTM5q5TAgMBAAECggECMS1yZh8MG3FG
nKTITEilsh3FOI+PY1kWgrKszzruEbGDNZOsS2BMJ62DF0DFTXhzeFbQqrJtyDDT
ruQnfH6IOpGnigm9QPjuNwoGi++NL0qOlTXq3V6wHSyofVZAxBoYFlw3/ZCg90nz
xKbPLB/l7VDigd4Q0CJ4XbQlchZ+ZFtSqMd/XexU4iRJKA20mOjzAIa/yJkpdJzC
j4rd/iKxDDDR70CEF/hT0md4Zyv8J6gsiwGvIG3i2GOGt7/HwL/SQEYfhNkqniM3
tltxP9tVu9Ke19bwJRQ8F9GuauxYIOCNaadi7vB6yZQJ4cCH2Olu1/dUv3rkloyZ
hFXelOxjpq8hAoIBAQDJ08SlePbnv2FpQcIxALRf20m8srA+RHX5FAQG5Sp4f8Zf
7dWuhk8CASkXvZ9Gm2BQjXMws1tiRI8/xK2jwJT1/wm912htUZu3+TrGxoaPhY8K
rbJ9xClpXwj9+KQwApIzbuXm7POOazPwLi/7g3HCRcb6BKRc+OzHbAGdo/WZYgBo
lIR61GvQOLhb/D1CW3WatV8BaZshQXP8pqvShuxtyoK9Ymp9PVH0HrR2zlf9lr7L
IOI6CKauzE4czjePRD6d+8AVSifr0LY/vvzkvOH+LsZXd8t4/4sCD+u2PCV5sAfR
bhEvwHMvvER9RW1FHtWTX0GsaozaLl00XWWCT5DLAgMvz5kCggEAeVxNsvK6BUCf
YpuYGb9CtyE1hbItKEQibFQM19iVYT/0GVr6UqeQerQX8Z6kV+C2Wbm0umQfX0e6
m624e+8ho4poYS9WK+YWrNnA7iYSY9r72H/6BIYgIKx0y8Lnd7cUErlspR92lP0B
jjs3vxWbIiazL0P7UaydNI1Nq20cEc9MT5Z+0x1IdzykHyvd6jj0zsKhDkhib+zb
weC3ETDwmlRbqWW0gvqMfS65dXc+kc5DjAGKBzuMfy97CPc3kX6H6JepOSQOPU6T
SGGf0CuD+URHH/F4+JkxDVxlcH9aSYIAMX7t9rjSirG6vVkyC44u/x8YboTjjY6z
nPlMQL93YQIDDHqxAoIBAAbrY43HVGPxreTAEnjzpgRhSb53AddLmWr7rjrU+qJF
hBbSObmLzsbQttFBw9dhjLdgM5xkOR5ot/+vUrY/9J7E5S2C6ww69KJ3Ey0xaJmk
yr+HR21zh0aKqYOrrzr+uSCAufaz4Lvv5bMzIhyj8y9/CEpfM183kV6TOw0b8hsl
kTwV/qFS2g0HPbj25ZbtsnP2t83GiVLbl5gdd55Jb0kaYk3fHeukC8OQ87MPShV0
rpDl8QLPUlBdHPeloSjz57kuNRbNgg61VNMv0foZrZm1ARTCaDjZnZx6twJOJObe
iYC1+mXOks0OC0LPc8Is1mW6z9uFgrc7GvHrhcyaP4k=
-----END RSA PRIVATE KEY-----'''
    assert str(a.priv_key) == private_key

def test_smallq():
    pubkey_f = os.path.join(TEST_DATA_PATH, "small_q.pub")
    cipher_f = os.path.join(TEST_DATA_PATH, "small_q.cipher")
    args = Args(publickey=pubkey_f, uncipher=cipher_f, private=True)
    a = RSAAttack(args)
    a.attack("smallq")
    private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICpwIBAAKBgwC60gz5ftUELfaWzk3z5aZ4z0+zaT098S3+n9P9jMiquLlVM+QU
4/wMN39O5UgnEYsdMFYaPHQb6nx2iZeJtRdD4HYJLfnrBdyX6xUFzp6xK1q54Qq/
VvkgpY5+AOzwWXfocoNN2FhM9KyHy33FAVm9lix1y++2xqw6MadOfY8eTBDVAgMB
AAECgYJFlcHtNhAA2W3vKuk23oB3M4+IAe+hIy0nl5KjuDx6xtWYbcucckvIX+dG
WRVgvQDlnQ+OZI3zYeWb1Wxmt52woJeq0uo2nUCavzOVlPtxfUqF5waZdYOR9Xjj
Dg2/68dh3KdSOxKYq/OoyzjJRml3fNcwRG6nGhI1HC7WzaXo/4BFAoGBAOFuvbXZ
g3okp9rZULhFhxmiTUDGfGHNnv9HK6aFVPTdfRceok/lNUnHjmDZ/rkSiM2z7E7G
lY/bQUf15FIFjJUVbtFDvRmeI5/9O7TIjD6OR06Cg3WCgEwyp5PktArF1EAitSbw
zNHQjjLgSmKfyiP5l3hq+ncWYGJteYOYxKSjAgMA1CcCgYAuOGNjLpa7a1qTD21y
aqb5hYJrXobQErWfx3rWqI2zqtnj7J8A3JDhcK3rg6arUXaFHne76xFtLlojI/JN
MuARDRTsiQPzha3uNqCQP3IpvUg3e6DybfBaLySWuRSFBOywva0Ar+x+tFEDc2Ms
93AdkiYRRXXXBtp6M9HvPlpLGwICDQUCgYEA1910Fo1Ui3ZH4TbxYjXD77xbW6uF
/lCx4bnkDjpMaTnm8StzfDONy9mGgIk/UgRvxBnCng/M4eLIKpOJv+9/xsl3/ILJ
wf0pPqMIkgH0vvUnBelapUvETfXbtfNtcQUi4xPctU6eaKFOqZ7ffJ6gamCqyZqO
bJMtE+mGE0btphU=
-----END RSA PRIVATE KEY-----'''
    cleartext = "hQdK+dKleMJqth/dofWyFaiWp3PW7jil"
    assert a.unciphered == cleartext
    assert str(a.priv_key) == private_key

def test_wiener():
    pubkey_f = os.path.join(TEST_DATA_PATH, "new_wiener.pub")
    cipher_f = os.path.join(TEST_DATA_PATH, "new_wiener.cipher")
    args = Args(publickey=pubkey_f, uncipher=cipher_f, private=True)
    a = RSAAttack(args)
    a.attack("wiener")
    cleartext = "The code word is `donut`."
    private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICOgIBAAKBgQKFzuYDNkcg8cV1poJq6cHuNoH95Ht34qBwf6k3TpdeT4NdNsNr
lZmMU4hu+/SAN7Md5B4RG9jG6YnpkLxQPiRH0m30f7uUj7fo+2xkcNg6uWtNNiuv
vdfzQUbGd/xtHBiyE3CJJ0GeRi0VZQciYqnjfCI/ztEfjezF9cnZWQVTNQKBgQJv
QGdFHgC3foryJMAl4yBpwTzGKp69OPLzdfoJ+SpxJOCf4lJq5vC7ZPJCBGgpBVmm
1OqEKcvtRlH54ySXhiqPgA4H1/3L/hOir7jECy9xoPfRY55ueJ1mdqwsfhzzYYBw
rqMQ/h/VKaEMi33MKpvE5xKwuJAEhIqGkwJXBMMBWwIgCRaKoJy7gLcSlm4yuYXz
yj8wEteHVM4K3opDgpUeH5MCQQFQE7s9ZQJTSY5pO0Pl0J+qni4YIhKJ9kf5vQvW
7ny3S5JynCY61EiPEjqErMNMulEGR3S9ZdgJjQ667rFQ+msNAkEB6+52fGH2QuhR
gFSrbFYXXs5SWmiWU6zxTYy5Fgp4jEDToyiVEufdsVwwPnM325I+VQMMfxKeb+Wn
dGnTnVreyQIgCRaKoJy7gLcSlm4yuYXzyj8wEteHVM4K3opDgpUeH5MCIAkWiqCc
u4C3EpZuMrmF88o/MBLXh1TOCt6KQ4KVHh+TAkEArtTziWW55V1XPxOKj+EKDJ+7
oI+OCu+9nE8kWP0sMSwDtaYo1AoOtJrYhh1RDvAe0YYK1Pf6MszegIDTNp43aA==
-----END RSA PRIVATE KEY-----'''
    assert str(a.unciphered) == cleartext
    assert str(a.priv_key) == private_key

def test_common_factors():
    pass

def test_fermat():
    pass

def test_fermat2():
    pass

def test_siqs():
    pass

def test_createpub():
    pass

def test_createpub_exception():
    pass

def test_createpub_crack():
    pass
