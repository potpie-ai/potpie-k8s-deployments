path "secret/data/mcore/*" {
  capabilities = ["read"]
}


path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "secret1/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "secret2/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "pgbouncer/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "neo4j/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
