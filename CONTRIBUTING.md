# Contributing to Captain Kube

Thank you for your interest in contributing to **Captain Kube**! We welcome all contributions, whether it's fixing a bug, improving documentation, or adding new features. Follow this guide to get started.

---

## Getting Started

1. **Fork the Repository**: Click the "Fork" button at the top-right of this page to create your own copy of the repo.
2. **Clone Your Fork**:
   ```sh
   git clone https://github.com/pirate0071/captain-kube.git
   cd captain-kube
   ```
3. **Set Up the Upstream Remote**:
   ```sh
   git remote add upstream https://github.com/pirate0071/captain-kube.git
   ```
4. **Create a New Branch**:
   ```sh
   git checkout -b feature-branch-name
   ```

---

## How to Contribute

### 1️⃣ Code Contributions
- Ensure your code follows **PEP 8** coding standards.
- Write **unit tests** for new features or bug fixes.
- Run tests before submitting:
  ```sh
  pytest
  ```
- Format your code using **Black**:
  ```sh
  black .
  ```

### Reporting Issues
- Check **existing issues** before opening a new one.
- Provide detailed **steps to reproduce the issue**.
- Include relevant **logs and error messages**.

### Improving Documentation
- If you spot an error or missing information, feel free to update the **README.md** or any related docs.
- Documentation updates should be submitted as pull requests.

---

## Submitting a Pull Request (PR)

1. **Commit Your Changes**:
   ```sh
   git add .
   git commit -m "Add feature/fix description"
   ```
2. **Push to Your Fork**:
   ```sh
   git push origin feature-branch-name
   ```
3. **Open a Pull Request**:
   - Navigate to the original repository.
   - Click on "New Pull Request".
   - Select your branch and submit the PR.
   - Add a **clear description** of what the PR does.

---

## Community & Support
- Join our **Discussions** to ask questions or propose ideas.
- Follow best practices for **security** when submitting code.

---

## License
By contributing, you agree that your contributions will be licensed under the **MIT License**.

Thank you for making **Captain Kube** better!
