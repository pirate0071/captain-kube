import click
from kubernetes import client, config
import subprocess
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel

console = Console()

def print_header():
    header_text = Text("🚀 Captain Kube - Kubernetes Admin Toolkit 🚀", style="bold cyan")
    sub_text = Text("\nA powerful and easy-to-use CLI tool for Kubernetes security, validation, and optimization.", style="italic white")
    
    commands_text = Text("\nCommands:\n", style="bold yellow")
    commands_text.append("  - find-unused-resources     : Detects and lists unused Kubernetes resources.\n", style="bold white")
    commands_text.append("  - validate-helm-chart       : Validates Helm charts for misconfigurations.\n", style="bold white")
    commands_text.append("  - detect-pod-privileges     : Detects Kubernetes pods with privilege escalation risks.\n", style="bold white")
    commands_text.append("  - scan-security             : Scans Kubernetes clusters for security vulnerabilities.\n", style="bold white")
    
    console.print(Panel(
        f"\n{header_text}\n{sub_text}\n{commands_text}\n", 
        border_style="bright_blue", 
        expand=True,
        padding=(1, 4)  # Adds space around text
    ))

# Load Kubernetes Configuration
def load_k8s_config():
    try:
        config.load_kube_config()
    except:
        config.load_incluster_config()

@click.group()
def cli():
    """
    Captain Kube - Kubernetes Admin Toolkit
    
    A powerful CLI tool for managing Kubernetes security, auditing Helm charts,
    detecting privilege escalations, and finding unused resources.
    
    Author:
    Montassar SMIDA (smida.montasser@gmail.com)
    """
    print_header()
    load_k8s_config()

@cli.command()
def find_unused_resources():
    """Find and list unused Kubernetes resources."""
    from modules.find_unused_resources import detect_unused_resources
    detect_unused_resources()

@cli.command()
@click.argument('chart_path')
def validate_helm_chart(chart_path):
    """Validate Helm chart for misconfigurations."""
    from modules.helm_validator import validate_helm
    validate_helm(chart_path)

@cli.command()
def detect_pod_privileges():
    """Detect Kubernetes pods with privilege escalation risks."""
    from modules.privilege_detector import check_pod_privileges
    check_pod_privileges()

@cli.command()
def scan_security():
    """Scan Kubernetes cluster for security vulnerabilities."""
    from modules.security_scanner import scan_k8s_security
    scan_k8s_security()

if __name__ == "__main__":
    cli()