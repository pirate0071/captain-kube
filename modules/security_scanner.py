from kubernetes import client
from rich.console import Console
from rich.table import Table

console = Console()

def scan_k8s_security():
    rbac_api = client.RbacAuthorizationV1Api()
    roles = rbac_api.list_role_for_all_namespaces().items

    table = Table(title="RBAC Security Risks")
    table.add_column("Namespace", style="bold")
    table.add_column("Role Name", style="bold cyan")
    table.add_column("Risk Level", style="bold red")

    for role in roles:
        for rule in role.rules:
            if "*" in rule.resources and "*" in rule.verbs:
                table.add_row(role.metadata.namespace, role.metadata.name, "High (Full Access)")

    console.print(table)