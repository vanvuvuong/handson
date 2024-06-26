## Generate environment-based configuration file

```
generate "backend_buildspec_image" {
  path              = "modules/example/config/test.yml"
  if_exists         = "overwrite"
  contents          = base64decode(filebase64("test.yml"))
  disable_signature = true
}
```
