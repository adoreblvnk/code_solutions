from git import Repo
import os


class CustomError(Exception):
    """base class for custom exceptions"""
    pass


class ExcessFilesError(CustomError):
    """raised when too many files are untracked"""
    pass


class NoFilesError(CustomError):
    """raised when no files are untracked"""
    pass


class InvalidTitleError(CustomError):
    """raised when title (first line) is invalid"""
    pass


def validate_untracked_files() -> None:
    if len(repo.untracked_files) > 1:
        raise ExcessFilesError("Too many untracked files")
    if len(repo.untracked_files) == 0:
        raise NoFilesError("No files to commit")


def get_commit_message(file_to_add: str) -> str:
    with open(file_to_add, 'r') as f:
        title = f.readlines()[0]
        if not title.startswith("# "):
            raise InvalidTitleError("Title must start with '# '")
        title = title[2:-1].lower()
    return title


def make_commit(message: str, lang: str = "py") -> None:
    repo.index.commit(f"feat({lang}): {message}")


def git_push() -> None:
    repo.remote(name="origin").push()


if __name__ == "__main__":
    repo = Repo()

    # add
    validate_untracked_files()
    file_to_add = repo.untracked_files[0]
    repo.index.add(file_to_add)

    # commit
    message = get_commit_message(file_to_add)
    make_commit(message)

    # push
    try:
        git_push()
    except Exception as e:
        print(e)
