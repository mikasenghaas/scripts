# /// script
# requires-python = ">=3.12"
# dependencies = ["prime>=0.3.23"]
# ///

from prime_cli.api.client import APIClient
from prime_cli.api.sandbox import SandboxClient


def main() -> None:
    client = SandboxClient(APIClient())
    for sandbox in client.list().sandboxes:
        if sandbox.user_id == "cmakj7hyo002rz091pdjngniy" and sandbox.status == "RUNNING":
            print(f"Deleting sandbox {sandbox.id}")
            client.delete(sandbox.id)


if __name__ == "__main__":
    main()

