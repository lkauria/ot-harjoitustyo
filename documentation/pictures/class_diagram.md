## Class diagram

Class User and Transaction

```mermaid
 classDiagram
      Transaction "*" --> "1" User
      class User{
          username
          password
      }
      class Transaction{
          user_id
          subject
          amount
      }
```