#Get the data from instance
data "oci_core_instance" "instance" {
    instance_id = oci_core_instance.INSTANCE-01.id
}

#Find the policy
data "oci_core_volume_backup_policies" "volume_backup_policy" {
    compartment_id = var.compartment_ocid
    filter {
        name = "display_name"
        values = ["CUSTOM-BACKUP-RETENTION-01"]
    }
}

output "policy_id" {
  value = data.oci_core_volume_backup_policies.volume_backup_policy.volume_backup_policies[0].id
}

# #Assign the policy to the instance.
# resource "oci_core_volume_backup_policy_assignment" "volume_backup_policy_assignment" {
#     asset_id = data.oci_core_instance.instance.boot_volume_id
#     policy_id = data.oci_core_volume_backup_policies.volume_backup_policy.volume_backup_policies[0].id
# }
