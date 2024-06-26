# Hands-on notable guide

## Condition resource

```
resource "null_resource" "test" {
  count = true ? 1: 0
}
```

```
resource "time_rotating" "mysql" {
  count = var.enable_mysql ? 1 : 0

  rotation_months = 3
}
resource "random_password" "mysql" {
  count = var.enable_mysql ? 1 : 0

  length      = 16
  min_upper   = 2
  min_numeric = 2
  min_special = 1
  keepers = {
    time = time_rotating.mysql[0].id
  }
}
```

## Get index from map & concat string

```
variable "public_subnets" {
  type = map(any)
  default = {
    "key": "value"
  }
}

data "aws_availability_zones" "azs" {
  state = "available"
}

resource "aws_subnet" "public_subnets" {
  for_each                        = var.public_subnets

  vpc_id                          = aws_vpc.vpc.id
  cidr_block                      = each.value
  availability_zone               = data.aws_availability_zones.azs.names[index(keys(var.public_subnets), each.key)]
  map_public_ip_on_launch         = var.map_public_ip_on_launch
  assign_ipv6_address_on_creation = var.enable_ipv6
  tags = {
    "Name" = format("%s-%s", each.key, data.aws_availability_zones.azs.names[index(keys(var.public_subnets), each.key)])
  }
}
```

## Multiple target regex function (BASH/SHELL function)

```
get_target() {
    # $1: pattern of target resource you want to filter(based on your terraform files), e.g: aws_subnet
    # $2: prefix that you want to add to -target, e.g: module.test.
    # result: -target module.test.aws_subnet.subnet_name
    if [ $# -ne 2 ]; then
        printf "Please run this function like this example\n- general: \t\t\t get_target \"pattern\" \"prefix\"\n- 1 pattern resource:\t\t get_target \"aws_s3\" \"module.frontend.\"\n- multiple pattern resource:\t get_target \"aws_s3,aws_subnet,aws_route\" \"module.frontend.\" "
        return 1
    fi
    array_pattern=($(echo "$1" | tr ',' '\n'))
    prefix=$2
    output_pattern=""
    apply_targets=""
    for pattern in "${array_pattern[@]}"; do
        output_pattern="^resource.*$pattern|$output_pattern"
    done
    output_pattern=${output_pattern%?}
    echo $output_pattern
    for target in $(grep -hRE "$output_pattern" | sed -e 's/resource "//g' | sed 's/" {//g' | sed 's/" "/./g'); do apply_targets="$apply_targets -target $prefix$target"; done
    echo $apply_targets
}
```

Usage:

```
terraform apply $(get_target "aws_subnet,aws_vpc" "module.network.")
```

## Terracost with terraform (BASH/SHELL function)

### Terracost with `terraform plan output` file - no argument needed

```
function tfpcost() {
    # use terraform plan output file file to estimate infrastructure cost
    # $1: terraform.tfstate
    state_file=${1}
    if ! [ -x "$(command -v jq)" ]; then
        echo "jq package not found. Please install 'jq'"
        exit 1
    fi

    if ! [ -e "${HOME}/terraform.jq" ]; then
        wget https://raw.githubusercontent.com/antonbabenko/terraform-cost-estimation/master/terraform.jq -O ~/terraform.jq
    fi
    terraform plan -out=/tmp/plan.tfplan >/dev/null && terraform show -json /tmp/plan.tfplan | jq -cf ~/terraform.jq | curl -s -X POST -H "Content-Type: application/json" -d @- https://cost.modules.tf/
    rm /tmp/plan.tfplan
}
```

### Terracost with `terraform.tfstate` file (BASH/SHELL function)

```
function terracost() {
    # use terraform.tfstate file to estimate infrastructure cost
    # $1: terraform.tfstate
    state_file=${1}
    if ! [ -x "$(command -v jq)" ]; then
        echo "jq package not found. Please install 'jq'"
        exit 1
    fi

    if ! [ -e "${HOME}/terraform.jq" ]; then
        wget https://raw.githubusercontent.com/antonbabenko/terraform-cost-estimation/master/terraform.jq -O ~/terraform.jq
    fi
    jq <"${state_file}" -cf "${HOME}/terraform.jq" | curl -s -X POST -H "Content-Type: application/json" -d @- https://cost.modules.tf/
}
```
