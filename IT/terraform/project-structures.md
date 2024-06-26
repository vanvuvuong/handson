# Terraform Project Structure

Generally, there are 2 ways to structure a terraform project:

- Flat structure
- Module structure

| Structure | Pros                                                                      | Cons                                                                                                   |
| --------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Flat      | - Fast, simple & easy to create<br>- Testable through `terratest` modules | - Duplicated codes, hard to maintain for big & complex infrastructure                                  |
| Module    | - Reusable, easy to maintain                                              | - Hard to test through `terratest` module<br>- Take long time to design modules & write reusable codes |

## Flat structure:

All terraform declaration code sit on the same folder & treat all resource as the same level, like this:

```
flat_structure
├── 0.provider.tf
├── 1.vpc.tf
├── 2.compute.tf
├── 3.rds.tf
├── 4.variables.tf
└── 5.output.tf
```

## Module structure

All terraform declaration code will be devide into hierarchy modules & all resource reference will be link through a `main.tf` outside the modules

```
module_structure
├── main.tf
├── modules
│   ├── backend
│   │   ├── 0-provider.tf
│   │   ├── 1-vpc.tf
│   │   ├── 2-ecs.tf
│   │   ├── 3-ecr.tf
│   │   ├── 4-variables.tf
│   │   ├── 5-main.tf
│   │   ├── 6-output.tf
│   └── frontend
│       ├── 0-provider.tf
│       ├── 1-policy.tf
│       ├── 2-main.tf
│       └── 3-variables.tf
├── provider.tf
└── variables.tf
```
