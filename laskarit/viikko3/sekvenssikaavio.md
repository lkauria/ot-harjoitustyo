## Sekvenssikaavio

```mermaid
sequenceDiagram
    main->>machine1: Machine()
    machine1->>fueltank1: FuelTank()
    machine1->>fueltank1: fill(40)
    machine1->>engine1: Engine(fueltank1)
    machine1->>main: drive()

```