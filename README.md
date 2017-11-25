## APIs
### Acconts
- `/api/acconts/signin/` POST
  - username
  - password
- `/api/accounts/logout/` GET
- `/api/accounts/` GET
  - username
  - tags
  - modes
  - location_count
  ```
  {
    "上海科技大学": 23,
    "金科路": 13,
    "人民广场": 8
  }
  ```

### Mode
- `/api/mode/` POST
  - name
  - duration
  - begin_time
  - end_time
  - come_over_locations
  ```
  {
      "name": "上学",
      "extra_fields": {
        "duration": 30,
        "begin_time": 0,
        "end_time": 0,
        "come_over_locations": [
          "金科路",
          "上海科技大学"
        ]
      }
  }
  ```

### Tag
- `/api/tag/` GET
- `/api/tag/add/` POST
  - title

