# Starship Marketplace Backend

## Quick start

This test works with either [Docker](https://docs.docker.com/compose/install/#install-compose) or
[Vagrant](https://www.vagrantup.com/downloads.html). But docker were not tested by me. Seems like here
is some bugs, maybe with docker too. Vagrant also had some problems, as of latest vagrant + vitrualbox 
provider versions. It's fixed and works well for me.

```shell
$ vagrant up
$ vagrant ssh
$ runserver         - new shortcut
```
The DRF swagger must be available on http://localhost:8008/api/v1/docs/

## Tasks

- [+] We need to be able to import all existing
      [Starships](https://swapi.co/documentation#starships) to the provided Starship
      Model
- [+] A potential buyer can browse all Starships
- [+] A potential buyer can browse all the listings for a given `starship_class`
- [+] A potential buyer can sort listings by price or time of listing
- [+] To list a Starship as for sale, the user should supply the Starship name and
      list price
- [+] A seller can deactivate and reactivate their listing

## P.S.

Django 1.11? Really? Let's use django-south migrations =) 
