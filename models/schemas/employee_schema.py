from marshmallow import Schema, fields

class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)
    role = fields.Str()