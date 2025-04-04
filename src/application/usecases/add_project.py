from src.application.interfaces.credentials import Credentials
from src.application.usecases.abs import AbstractUseCase
from src.domain.entities.project import Project
from src.domain.exceptions.base import ConflictException


class CreateProjectUseCase(AbstractUseCase):
    async def __call__(
        self,
        project: Project,
        *,
        credentials: Credentials | None = None,
    ) -> Project:
        async with self.uow as uow:
            try:
                p = await uow.projects.create_project(project)
            except ConflictException:
                raise ConflictException(f"Project conflict: {project.title}")
            await uow.commit()
            return p
