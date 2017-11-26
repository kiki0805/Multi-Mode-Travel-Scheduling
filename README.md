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
- `/api/mode` GET
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


### Scheme
- `/scheme/` GET
  - origin
  - destination
  - mode_id
  - duration
  - begin_time
  - end_time
  - come_over_locations

## Instruction
- Install dependencies both for backend or frontend.(in `requirements.txt` and `package.json`)
- Backend startup: In `route_scheme` folder, run `sudo python manage.py runserver 0.0.0.0:8000`.
- Frontend startup: In `scheme-frontend` folder, run `sudo npm run start`.
- Collaborative filtering: In `collaborative filtering`, run `sudo python3 generate_route.py`.
