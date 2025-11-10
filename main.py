import os
import argparse
from urllib.parse import urlparse


def url_path(value):
    if os.path.exists(value):
        return value

    try:
        result = urlparse(value)
        #Проверяем, что есть схема и домен для полных URL
        if result.scheme and result.netloc:
            return value
        #Относительные URL типа "github.com/user/repo"
        elif not result.scheme and ('.' in value or '/' in value):
            return value
        else:
            raise ValueError("Некорректный URL")
    except Exception:
        raise argparse.ArgumentTypeError(
            f"'{value}' не является допустимым URL, путем к файлу или относительным URL"
        )
def valid_mode(value):
    allow_modes = {'clone','delete','download'}
    if value not in allow_modes:
        raise argparse.ArgumentTypeError(
            f"Некорректный режим : '{value}'. Допустимые режимы: {', '.join(allow_modes)}"
        )
    return value

def main():
    parser = argparse.ArgumentParser(
        description="Минимальная CLI утилита для конфигурации анализа пакетов."
    )

    parser.add_argument(
        "--package-name",
        required=True,
        help="Имя пакета.",
    )
    parser.add_argument(
        "--repo-url",
        required=True,
        type=url_path,
        help="Ссылка.",
    )
    parser.add_argument(
        "--mode",
        required=True,
        type=valid_mode,
        help="Режимы работы с репозиторием: clone, local, or download.",
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Версия пакета",
    )

    print("Configuration:")
    print(f"package-name={parser.parse_args().package_name}")
    print(f"repo-url={parser.parse_args().repo_url}")
    print(f"mode={parser.parse_args().mode}")
    print(f"version={parser.parse_args().version}")

main()