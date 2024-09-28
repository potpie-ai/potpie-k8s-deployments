# Enable secrets engine
path "sys/mounts/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# List enabled secrets engine
path "sys/mounts" {
  capabilities = ["read", "list"]
}

# Work with secrets
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
