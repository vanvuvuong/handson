# Passing parameter in Terraform

## By default value
When you define a parameter, you can set it value through parameter definition
```
variable "region" {
  type    = string
  default = "ap-northeast-1"
}
```

## By `[any-name].tfvars`
Create a file like this above format, for example: `dev.tfvars` (in the same folder level that run terraform code) and passing variable value in this file

```
region = "ap-northeast-1"
```

When you create `[any-name].tfvars` not in the same folder level as the terrafrom main code, please pass this file path to the terraform argument to apply change
```
terraform apply -var-file ./path-to-file/dev.tfvars
```

## By command-line
Passing variable value during apply change to infrastructure with terraform

```
terraform apply -var 'region=ap-northeast-1'
```
