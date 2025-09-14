# /// script
# requires-python = ">=3.12"
# dependencies = ["prime>=0.3.26"]
# ///

from prime_cli.api.client import APIClient
from prime_cli.api.sandbox import SandboxClient


def main() -> None:
    client = SandboxClient(APIClient())
    sandbox_ids = [
        sandbox.id
        for sandbox in client.list(per_page=100, exclude_terminated=True).sandboxes
        if sandbox.user_id == "cmakj7hyo002rz091pdjngniy"
    ]
    print(f"Deleting {len(sandbox_ids)} sandboxes")
    client.bulk_delete(sandbox_ids)
    print(f"Success!")


if __name__ == "__main__":
    main()
