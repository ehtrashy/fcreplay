from sqlalchemy import Column, String, Integer, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Job(Base):
    __tablename__ = 'job'

    id = Column(String, primary_key=True)
    start_time = Column(DateTime)
    instance = Column(String)


class Descriptions(Base):
    __tablename__ = 'descriptions'

    id = Column(String, primary_key=True)
    description = Column(Text)


class Replays(Base):
    __tablename__ = 'replays'

    id = Column(String, primary_key=True)
    p1_loc = Column(String)
    p2_loc = Column(String)
    p1_rank = Column(String)
    p2_rank = Column(String)
    p1 = Column(String)
    p2 = Column(String)
    date_replay = Column(DateTime)
    length = Column(Integer)
    created = Column(Boolean)
    failed = Column(Boolean)
    status = Column(String)
    date_added = Column(DateTime)
    player_requested = Column(Boolean)
    game = Column(String)
    emulator = Column(String)
    video_processed = Column(Boolean)
    video_youtube_uploaded = Column(Boolean)
    video_youtube_id = Column(String)
    fail_count = Column(Integer)


class Youtube_day_log(Base):
    __tablename__ = 'youtube_day_log'

    id = Column(String, primary_key=True)
    date = Column(DateTime)
    count = Column(Integer)
    # Need to init count somehow


class Character_detect(Base):
    __tablename__ = 'character_detect'

    id = Column(Integer, primary_key=True)
    challenge_id = Column(String)
    p1_char = Column(String)
    p2_char = Column(String)
    vid_time = Column(String)
    game = Column(String)
