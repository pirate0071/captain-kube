from kubernetes import client
from rich.console import Console
from rich.table import Table

console = Console()

def detect_unused_resources():
    v1 = client.CoreV1Api()
    
    pvcs = v1.list_persistent_volume_claim_for_all_namespaces().items
    used_pvcs = {pvc.spec.volume_name for pvc in v1.list_persistent_volume_for_all_namespaces().items}
    unused_pvcs = [pvc.metadata.name for pvc in pvcs if pvc.spec.volume_name not in used_pvcs]

    table = Table(title="Unused Kubernetes Resources")
    table.add_column("Resource Type", style="bold")
    table.add_column("Name", style="bold cyan")

    for pvc in unused_pvcs:
        table.add_row("Unused PVC", pvc)

    console.print(table)