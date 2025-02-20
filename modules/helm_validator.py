import subprocess
from rich.console import Console

console = Console()

def validate_helm(chart_path):
    result = subprocess.run(["helm", "lint", chart_path], capture_output=True, text=True)
    if result.returncode == 0:
        console.print("[green]Helm chart validation passed![/green]")
    else:
        console.print("[red]Helm chart validation failed![/red]\n", result.stdout)