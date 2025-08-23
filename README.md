# Elfra-Config-Tool

The Elfra Config Tool is a modern Flask web application with a Tailwind CSS frontend. The web interface provides an intuitive form-based configuration experience for generating TypeScript configuration files for ELFRA.

## How to Install and Use:

To install and use our service, we use docker to containerize it.

### Method 1: Build it for later re-use of the Image

To Build the current Version use the command:

> `docker compose build`

This builds the container under the name "Elfra" with the current version as "tag".

To run the container now use this command:

> `docker compose up`
> \*This will start the latest Version used in docker compose

Now you can stop/end the container by using

> `docker compose stop`
> _Keeps files and mounted volumes_

#### OR

> `docker compose down`
> !! If you use "down" the container will also get removed !!

---

### Method 2: Build and start it

To Build the current Version use the command:

> `docker compose up --build`

This builds the container under the name "Elfra" with the current version as "tag" and also starts it.

Now you can stop/end the container by using

> `docker compose stop`
> _Keeps files and mounted volumes_

#### OR

> `docker compose down`
> !! If you use "down" the container will also get removed !!
