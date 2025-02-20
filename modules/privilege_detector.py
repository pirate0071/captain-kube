from kubernetes import client
from rich.console import Console
from rich.table import Table

console = Console()

def check_pod_privileges():
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces().items

    table = Table(title="Pods with Privilege Escalation Risks")
    table.add_column("Namespace", style="bold")
    table.add_column("Pod Name", style="bold cyan")
    table.add_column("Security Risk", style="bold red")

    for pod in pods:
        for container in pod.spec.containers:
            if container.security_context:
                if getattr(container.security_context, "privileged", False):
                    table.add_row(pod.metadata.namespace, pod.metadata.name, "Privileged: True")
                if getattr(container.security_context, "allowPrivilegeEscalation", False):
                    table.add_row(pod.metadata.namespace, pod.metadata.name, "allowPrivilegeEscalation: True")

    console.print(table)