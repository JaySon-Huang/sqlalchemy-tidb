# Copyright 2021 PingCAP, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# See the License for the specific language governing permissions and
# limitations under the License.
from sqlalchemy.dialects import registry as _registry

from .ddl import VectorIndex, TiFlashReplica, Table, MetaData
from .ext.declarative import get_declarative_base

__version__ = "1.0.0"

_registry.register(
    "tidb",
    "sqlalchemy_tidb.dialect.mysqldb",
    "TiDBDialect_mysqldb"
)

_registry.register(
    "tidb.cmysql",
    "sqlalchemy_tidb.dialect.cmysql",
    "TiDBDialect_cmysql",
)

_registry.register(
    "tidb.mysqlconnector",
    "sqlalchemy_tidb.dialect.mysqlconnector",
    "TiDBDialect_mysqlconnector",
)

_registry.register(
    "tidb.mysqldb",
    "sqlalchemy_tidb.dialect.mysqldb",
    "TiDBDialect_mysqldb",
)

_registry.register(
    "tidb.pymysql",
    "sqlalchemy_tidb.dialect.pymysql",
    "TiDBDialect_pymysql",
)

__all__ = (
    "get_declarative_base",
    "MetaData",
    "Table",
    "VectorType",
    "VectorIndex",
    "TiFlashReplica",
)
