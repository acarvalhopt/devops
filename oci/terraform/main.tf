module "custom-backup-retention-01" {
  source = "./modules/volume-backup-policy"
  compartment_id = var.compartment_ocid
  display_name = "CUSTOM-BACKUP-RETENTION-01"
  freeform_tags = local.freeform_tags
  schedules = {
    schedule1 = ["FULL","ONE_WEEK","1209600","SUNDAY",0,"STRUCTURED","UTC"] #1209600 = 2 weeks
    schedule2 = ["INCREMENTAL","ONE_DAY","604800","",0,"STRUCTURED","UTC"] #604800 = 1 week
  }
}