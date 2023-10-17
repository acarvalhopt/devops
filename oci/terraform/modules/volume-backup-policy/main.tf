resource "oci_core_volume_backup_policy" "volume_backup_policy" {
    #Required
    compartment_id = var.compartment_id

    #Optional
    # destination_region = var.volume_backup_policy_destination_region
    display_name = var.display_name
    freeform_tags  = var.freeform_tags

    dynamic "schedules" {
        for_each = [ 
        for key, value in var.schedules: {
            backup_type              = value[0]
            period                   = value[1]
            retention_seconds        = value[2]
            #Optional            
            day_of_week              = value[3]
            hour_of_day              = value[4]            
            offset_type              = value[5]
            time_zone                = value[6]            
            # day_of_month             = value[3]
            # offset_seconds           = value[6]
            # month                    = value[9]
        }        
        ]
        content {
            backup_type = schedules.value.backup_type
            period = schedules.value.period
            retention_seconds = schedules.value.retention_seconds
            #Optional            
            day_of_week = schedules.value.day_of_week
            hour_of_day = schedules.value.hour_of_day                     
            offset_type = schedules.value.offset_type
            time_zone = schedules.value.time_zone
            # day_of_month = schedules.value.day_of_month
            # offset_seconds = schedules.value.offset_seconds
            # month = schedules.value.month
        }
    }
}