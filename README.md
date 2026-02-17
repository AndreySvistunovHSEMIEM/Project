# Project

## Установка

Клонировать репозиторий вместе с submodules:

```bash
git clone --recurse-submodules git@github.com:AndreySvistunovHSEMIEM/Project.git
cd Project
```

Если репозиторий уже клонирован без `--recurse-submodules`:

```bash
git submodule init
git submodule update
```

## Обновление modules

Подтянуть последнюю версию submodule:

```bash
git submodule update --remote libs/modules
git add libs/modules
git commit -m "chore: update modules submodule"
git push
```
