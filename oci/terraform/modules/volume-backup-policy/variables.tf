variable "compartment_id" {}
variable "display_name" {}
variable "freeform_tags" {}
variable "volume_backup_policy_destination_region" {
    type              = string
    default           = "eu-frankfurt-1"
}

variable "volume_backup_policy_schedules_backup_type" {
    type              = string
    default           = "FULL"
}
variable "volume_backup_policy_schedules_period" {
    type              = string
    default           = "ONE_DAY"
}
variable "volume_backup_policy_schedules_retention_seconds" {
    type              = string
    default           = "1209600" #2 weeks in seconds
}

variable "schedules" {
  description = "Map of schedules (define as 'name' = ['backup_type', 'period', 'retention_seconds', 'day_of_week', 'hour_of_day', 'offset_type', 'time_zone'])"
  type        = map(list(any))
  default     = {
        schedule1 = ["FULL","ONE_WEEK","1209600","SUNDAY",0,"STRUCTURED","UTC"] #1209600 = 2 weeks
        schedule2 = ["INCREMENTAL","ONE_DAY","604800","",0,"","UTC"] #604800 = 1 week
  }
}