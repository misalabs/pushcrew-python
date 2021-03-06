from marshmallow import fields, post_load, Schema

from .base import BaseSchema
from .subscriber import SubscriberSchema


class SegmentSchema(Schema):
    """
    Segment Schema.
    """
    id = fields.Decimal(data_key='id')
    name = fields.String(data_key='name')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Segment', data)


class SegmentsSchema(Schema):
    """
    List of Segments schema.
    """
    status = fields.String(data_key='status')
    segment_list = fields.Nested(SegmentSchema, many=True)

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Segments', data)


class AddSegmentSchema(Schema):
    """
    Add Segment schema.
    """
    status = fields.String(data_key='status')
    segment_id = fields.Decimal(data_key='segment_id')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('AddSegment', data)


class StatusSchema(Schema):
    """
    Status schema
    """
    status = fields.String(data_key='status')
    message = fields.String(data_key='message')

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('SatusSegment', data)


class SegmentSubscribersSchema(Schema):
    status = fields.String(data_key='status')
    count_active = fields.Integer(data_key='count_active')
    count_total = fields.Integer(data_key='count_total')
    next_page = fields.String(data_key='next_page')
    subscriber_list = fields.Nested(SubscriberSchema, many=True)

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('SegmentSubscribers', data)
