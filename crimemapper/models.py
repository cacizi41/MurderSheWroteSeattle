# -*- coding: utf-8 -*-
"""Entry Model defined."""
from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    DateTime,
    BigInteger
)
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    """Create New Crime Entry for crimedb database. Mimic Socrata Table."""

    __tablename__ = 'crimedb'
    id = Column(Integer, primary_key=True)
    rms_cdw_id = Column(Integer)
    general_offense_number = Column(BigInteger)
    offense_code = Column(Integer)
    offense_code_extension = Column(Integer)
    offense_type = Column(Text)
    summary_offense_code = Column(Integer)
    summarized_offense_description = Column(Text)
    date_reported = Column(DateTime)
    occurred_date_or_date_range_start = Column(Text)
    occurred_date_range_end = Column(Text)
    hundred_block_location = Column(Text)
    district_sector = Column(Text)
    zone_beat = Column(Text)
    census_tract_2000 = Column(Text)
    longitude = Column(Float)
    latitude = Column(Float)
    location = Column(JSON)
