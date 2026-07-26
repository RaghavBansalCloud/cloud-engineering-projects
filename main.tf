terraform {
  required_version = ">= 1.0.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4.0"
    }
  }
}

provider "local" {}

# Define a simple resource managed by Terraform
resource "local_file" "infra_status" {
  filename = "infrastructure_output.txt"
  content  = "Infrastructure successfully provisioned via Terraform on GitHub Actions!"
}

output "file_status" {
  value = "The infrastructure file was created at ${local_file.infra_status.filename}"
}
