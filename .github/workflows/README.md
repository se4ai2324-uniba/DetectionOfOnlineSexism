# GitHub Actions Documentation

## Introduction
GitHub Actions is a feature provided by GitHub that enables the automation of software workflows directly within the GitHub environment.
It can be used to build, test and deploy applications directly from the GitHub repository, reducing the need for external continuous integration services.

It relies on YAML configuration files that define the entire workflow. These files are placed in the `.github/workflows` directory of the repository.
A workflow consists of a series of jobs and steps, where each job represents a separate unit of work while the steps are individual tasks within a job.

We developed GitHub Actions for integrating key tools and frameworks into our project:
-   **FastAPI** for automating the building of our API [fastapi_check.yml](./fastapi_check.yaml)
-   **Pydantic** for data validation, ensuring that incoming data adheres to defined models [pydantic_check.yml](./pydantic_check.yaml)
-   **Pytest** for automated testing, allowing us to maintain code quality and catch potential issues early in the development process [pytest_check.yml](./pytest_check.yaml)
-   **Pylint**, employed to enforce coding standards and improve code readability [pylint_check.yml](./pylint_check.yaml)
-   **Alibi-detect** for providing drift detection capabilities [alibi-detect_check.yml](./alibi-detect_check.yaml)

With these GitHub Actions in place, our development process is streamlined and we can confidently deliver robust and well-tested functionalities.