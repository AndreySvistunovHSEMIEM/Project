# Project

## Установка

Клонировать репозиторий:

```bash
git clone git@github.com:AndreySvistunovHSEMIEM/Project.git
cd Project
```

Модули уже включены в репозиторий через git subtree — ничего дополнительного делать не нужно.

## Обновление modules

Подтянуть последнюю версию модулей:

```bash
git subtree pull --prefix=libs/modules git@github.com:AndreySvistunovHSEMIEM/module.git main --squash
```
