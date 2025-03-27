from src.application.interfaces.uow.projects import AbstractProjectsUnitOfWork
from src.domain.entities.project import Project
from src.domain.exceptions.base import ConflictException


class AddNewProjectUseCase:
    def __init__(self, project_uow: AbstractProjectsUnitOfWork):
        self.project_uow = project_uow

    async def __call__(self, project: Project) -> Project:
        async with self.project_uow as uow:
            try:
                p = await uow.projects.create_project(project)
            except ConflictException:
                raise ConflictException(f"Project conflict: {project.title}")
            await uow.commit()
        return p  # type: ignore
