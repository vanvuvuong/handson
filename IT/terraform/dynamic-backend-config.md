# Dynamic Config Backend for Terraform IaC

## Terraform-native way

Declare empty backend config on `terraform` block
```
terraform {
  required_version = "~> 1.0"
  required_providers {
    aws = {
        version = "~> 5.26.0"
    }
  }
  backend "s3" {
    # configuration at dynamic.tfbackend.hcl
  }
}
```

And then run `terraform init` with this backend file
```
terraform init -backend-config dynamic.tfbackend.hcl
```

## Terragrunt way

```
remote_state {
  backend = "s3"
  config = {
    bucket         = "terraform-backend-statefiles"
    key            = "${path_relative_to_include()}/terraform.tfstate"
    region         = "ap-northeast-1"
    encrypt        = true
    dynamodb_table = "${path_relative_to_include()}-terraform-lock-table"
    profile        = "example"
  }
  generate = {
    path      = "backend.tf"
    if_exists = "overwrite_terragrunt"
  }
}
```