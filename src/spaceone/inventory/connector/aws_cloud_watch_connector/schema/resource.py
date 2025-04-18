from schematics.types import PolyModelType, StringType, ModelType

from spaceone.inventory.connector.aws_cloud_watch_connector.schema.data import Alarms
from spaceone.inventory.libs.schema.dynamic_field import TextDyField, DateTimeDyField
from spaceone.inventory.libs.schema.dynamic_layout import TableDynamicLayout
from spaceone.inventory.libs.schema.resource import CloudServiceResponse, CloudServiceResource, CloudServiceMeta


cw_actions = TableDynamicLayout.set_fields(
    "Actions", "data.actions",
    fields=[
        TextDyField.data_source("Type", "type"),
        TextDyField.data_source("ARN", "arn"),
    ],
)

cw_history = TableDynamicLayout.set_fields(
    "History", 'data.history',
    fields=[
        DateTimeDyField.data_source("Date", "date"),
        TextDyField.data_source("Type", "type"),
        TextDyField.data_source("Description", "description"),
    ],
)

cloud_watch_metadata = CloudServiceMeta.set_layouts(layouts=[cw_actions,cw_history])


class CloudWatchResource(CloudServiceResource):
    cloud_service_group = StringType(default="CloudWatch")


class AlarmsResource(CloudWatchResource):
    cloud_service_type = StringType(default="Alarms")
    data = ModelType(Alarms)
    _metadata = ModelType(
        CloudServiceMeta, default=cloud_watch_metadata, serialized_name="metadata"
    )


class AlarmsResponse(CloudServiceResponse):
    resource = PolyModelType(AlarmsResource)