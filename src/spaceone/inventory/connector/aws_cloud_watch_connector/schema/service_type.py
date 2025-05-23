from spaceone.inventory.conf.cloud_service_conf import ASSET_URL
from spaceone.inventory.libs.schema.dynamic_field import (
    TextDyField,
    SearchField,
    DateTimeDyField,
    EnumDyField,
)
from spaceone.inventory.libs.schema.resource import (
    CloudServiceTypeResponse,
    CloudServiceTypeResource,
    CloudServiceTypeMeta,
)

"""
ALARMS
"""
cst_alarms = CloudServiceTypeResource()
cst_alarms.name = "Alarms"
cst_alarms.provider = "aws"
cst_alarms.group = "CloudWatch"
cst_alarms.labels = ["Monitoring"]
cst_alarms.service_code = "AWSCloudWatch"
cst_alarms.is_primary = True
cst_alarms.is_major = True
cst_alarms.tags = {
    "spaceone:icon": f"{ASSET_URL}/AWS-Cloud-Watch.svg",
}

cst_alarms._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        EnumDyField.data_source(
            "State",
            "data.state_value",
            default_state={
                "safe": ["OK"],
                "disable": ["INSUFFICIENT_DATA"],
                "alert": ["ALARM"],
            },
        ),
        DateTimeDyField.data_source(
            "Last State Update", "data.state_updated_timestamp"
        ),
        TextDyField.data_source("Conditions", "data.conditions"),
        EnumDyField.data_source(
            "Actions",
            "data.actions_enabled",
            default_badge={
                "gray.500": ["No actions"],
                "green.500": ["Actions enabled"],
            },
        ),
        TextDyField.data_source(
            "MetricName", "data.metric_name", options={"is_optional": True}
        ),
        TextDyField.data_source(
            "Namespace", "data.namespace", options={"is_optional": True}
        ),
        TextDyField.data_source(
            "Statistic", "data.statistic", options={"is_optional": True}
        ),
        TextDyField.data_source("Period", "data.period", options={"is_optional": True}),
    ],
    search=[
        SearchField.set(name="Alarm ARN", key="data.alarm_arn"),
        SearchField.set(name="Alarm Name", key="name"),
        SearchField.set(name="State", key="data.state_value"),
        SearchField.set(name="Actions", key="data.actions_enabled"),
        SearchField.set(name="MetricName", key="data.metric_name"),
        SearchField.set(name="Namespace", key="data.namespace"),
        SearchField.set(name="Statistic", key="data.statistic"),
        SearchField.set(name="Period", key="data.period"),
    ],
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({"resource": cst_alarms}),
]
