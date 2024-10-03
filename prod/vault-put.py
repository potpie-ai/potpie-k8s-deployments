import os
import json
from hvac import Client
from hvac.exceptions import InvalidPath

# Initialize the Vault client
vault_url = "http://127.0.0.1:8200/"
vault_token = input("Enter your Vault token: ")

client = Client(url=vault_url, token=vault_token)

# Define the mount point and path for your Vault secrets
kv_mount_point = "potpie"
secret_path = f"secret"

# Load secrets from the JSON file
json_file_path = "secrets.json"
data = {}

# Read data from the JSON file
try:
    with open(json_file_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: The file {json_file_path} was not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: The file {json_file_path} contains invalid JSON.")
    exit(1)

# Ensure the KV engine is mounted at the desired path
try:
    # Attempt to read from the secret path to verify it's accessible
    client.secrets.kv.v2.read_secret_version(path="secrets", mount_point=kv_mount_point)
except InvalidPath:
    # If the path doesn't exist, enable the KV engine at the mount point
    client.sys.enable_secrets_engine(
        backend_type='kv',
        path=kv_mount_point,
        options={'version': '2'}
    )
    print(f"KV engine mounted at {kv_mount_point}")

# Create or update the secret in Vault
client.secrets.kv.v2.create_or_update_secret(path=secret_path, secret=data, mount_point=kv_mount_point)

print(f"Secrets from {json_file_path} have been written to {vault_url} at path {secret_path}")
