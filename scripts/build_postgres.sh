podman pull postgres

podman run \
    --name pythentic-postgres \
    -e POSTGRES_PASSWORD=root \
    -p 5432:5432 \
    -d postgres