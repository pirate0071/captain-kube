# Captain Kube - Kubernetes Admin Toolkit

![Captain Kube](https://img.shields.io/badge/Kubernetes-Admin%20Toolkit-blue)
![Build Status](https://github.com/pirate0071/captain-kube/actions/workflows/pipeline.yml/badge.svg)
![License](https://img.shields.io/github/license/pirate0071/captain-kube)

## Overview
**Captain Kube** is a powerful Kubernetes CLI tool for security, validation, and optimization. It helps you:
- **Find unused resources**
- **Validate Helm charts**
- **Detect pod privilege escalation risks**
- **Scan for Kubernetes security vulnerabilities**

## Installation

### Install via `pip`
```sh
pip install captain_kube
```

### Install as a Standalone Binary
```sh
pyinstaller --onefile --name captain-kube captain_kube.py
./dist/captain-kube --help
```


## Usage
```sh
captain-kube --help
```

### Find Unused Resources
```sh
captain-kube find-unused-resources
```

### Validate Helm Chart
```sh
captain-kube validate-helm-chart ./mychart
```

### Detect Pod Privilege Escalations
```sh
captain-kube detect-pod-privileges
```

### Scan for Kubernetes Security Risks
```sh
captain-kube scan-security
```

## Contributing
We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support the Project
If you find **Captain Kube** useful, please **star the repo** and share it with others!
