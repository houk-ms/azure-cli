# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JsonWebKey(Model):
    """As of http://tools.ietf.org/html/draft-ietf-jose-json-web-key-18.

    :param kid: Key identifier.
    :type kid: str
    :param kty: JsonWebKey Key Type (kty), as defined in
     https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40.
     Possible values include: 'EC', 'EC-HSM', 'RSA', 'RSA-HSM', 'oct',
     'oct-HSM'
    :type kty: str or ~keys.models.JsonWebKeyType
    :param key_ops:
    :type key_ops: list[str]
    :param n: RSA modulus.
    :type n: bytes
    :param e: RSA public exponent.
    :type e: bytes
    :param d: RSA private exponent, or the D component of an EC private key.
    :type d: bytes
    :param dp: RSA private key parameter.
    :type dp: bytes
    :param dq: RSA private key parameter.
    :type dq: bytes
    :param qi: RSA private key parameter.
    :type qi: bytes
    :param p: RSA secret prime.
    :type p: bytes
    :param q: RSA secret prime, with p < q.
    :type q: bytes
    :param k: Symmetric key.
    :type k: bytes
    :param t: Protected Key, used with 'Bring Your Own Key'.
    :type t: bytes
    :param crv: Elliptic curve name. For valid values, see
     JsonWebKeyCurveName. Possible values include: 'P-256', 'P-384', 'P-521',
     'P-256K'
    :type crv: str or ~keys.models.JsonWebKeyCurveName
    :param x: X component of an EC public key.
    :type x: bytes
    :param y: Y component of an EC public key.
    :type y: bytes
    """

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'n': {'key': 'n', 'type': 'base64'},
        'e': {'key': 'e', 'type': 'base64'},
        'd': {'key': 'd', 'type': 'base64'},
        'dp': {'key': 'dp', 'type': 'base64'},
        'dq': {'key': 'dq', 'type': 'base64'},
        'qi': {'key': 'qi', 'type': 'base64'},
        'p': {'key': 'p', 'type': 'base64'},
        'q': {'key': 'q', 'type': 'base64'},
        'k': {'key': 'k', 'type': 'base64'},
        't': {'key': 'key_hsm', 'type': 'base64'},
        'crv': {'key': 'crv', 'type': 'str'},
        'x': {'key': 'x', 'type': 'base64'},
        'y': {'key': 'y', 'type': 'base64'},
    }

    def __init__(self, **kwargs):
        super(JsonWebKey, self).__init__(**kwargs)
        self.kid = kwargs.get('kid', None)
        self.kty = kwargs.get('kty', None)
        self.key_ops = kwargs.get('key_ops', None)
        self.n = kwargs.get('n', None)
        self.e = kwargs.get('e', None)
        self.d = kwargs.get('d', None)
        self.dp = kwargs.get('dp', None)
        self.dq = kwargs.get('dq', None)
        self.qi = kwargs.get('qi', None)
        self.p = kwargs.get('p', None)
        self.q = kwargs.get('q', None)
        self.k = kwargs.get('k', None)
        self.t = kwargs.get('t', None)
        self.crv = kwargs.get('crv', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
