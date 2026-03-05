# FastAPI Coffee Shop Lessons

This guide helps you learn the project step-by-step, from beginner to practical understanding.

---

## Lesson 1: Understand the big picture

This project has **3 layers**:

1. **Frontend (HTML + JS)**
   - Customer page: `backend/templates/customer.html`
   - Kitchen page: `backend/templates/kitchen.html`
2. **Backend API (FastAPI)**
   - Main app and endpoints: `backend/app/main.py`
3. **Database (SQLite via SQLModel)**
   - Models: `backend/app/models.py`
   - DB engine + table creation: `backend/app/db.py`

### Goal
- Customer sends order -> API saves order -> Kitchen updates status.

---

## Lesson 2: Run the app locally

```bash
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/` (Customer)
- `http://127.0.0.1:8000/kitchen` (Kitchen)
- `http://127.0.0.1:8000/docs` (API docs)

### What to observe
- Startup creates DB tables automatically.
- Inventory is seeded with default stock.

---

## Lesson 3: Read the backend flow in `main.py`

Follow this order:

1. `startup()`
   - Creates tables.
   - Seeds inventory with stock 10 for each menu item.
2. `GET /`
   - Serves customer page.
3. `GET /kitchen`
   - Serves kitchen page.
4. `GET /api/menu`
   - Returns hardcoded menu items.
5. `POST /api/orders`
   - Validates item and qty.
   - Checks stock.
   - Decreases stock.
   - Saves new order.
6. `PATCH /api/orders/{id}/status`
   - Kitchen updates order status.

### Why this is useful
You can see a real product behavior: **validation + state changes + role-based pages**.

---

## Lesson 4: Understand data models

In `backend/app/models.py`:

- `OrderStatus` = enum (`RECEIVED`, `PREPARING`, `READY`, `CANCELLED`)
- `Order` = DB table for orders
- `Inventory` = DB table for stock
- `OrderCreate`, `OrderRead`, `OrderStatusUpdate` = request/response schemas

### Key concept
- Same project uses one model set for both DB and API schema, which is common in small FastAPI projects.

---

## Lesson 5: Trace one complete user journey

### Customer side
1. Open `/`
2. Fill name, drink, qty, note
3. Click **Place order**
4. Browser sends `POST /api/orders`

### Backend side
1. Validate request
2. Check inventory
3. Insert order in DB
4. Return JSON response

### Kitchen side
1. Open `/kitchen`
2. See order list
3. Click status button (`PREPARING` / `READY`)
4. Browser sends `PATCH /api/orders/{id}/status`

---

## Lesson 6: Learn API quickly with curl

### Get menu
```bash
curl http://127.0.0.1:8000/api/menu
```

### Create order
```bash
curl -X POST http://127.0.0.1:8000/api/orders \
  -H "Content-Type: application/json" \
  -d '{"customer_name":"Nina","item_id":1,"qty":1,"note":"hot"}'
```

### Update status
```bash
curl -X PATCH http://127.0.0.1:8000/api/orders/1/status \
  -H "Content-Type: application/json" \
  -d '{"status":"READY"}'
```

### Check inventory
```bash
curl http://127.0.0.1:8000/api/inventory
```

---

## Lesson 7: Suggested practice tasks

1. Add a new menu item and seed inventory.
2. Show item name in order response (not only item_id).
3. Add endpoint to restock inventory.
4. Add simple authentication for kitchen page.
5. Write tests for create-order and update-status endpoints.

---

## Lesson 8: Common beginner issues

1. **"Module not found"**
   - Ensure virtual environment is activated.
2. **"Address already in use"**
   - Another app uses port 8000.
3. **Order not created**
   - Check stock and qty > 0.
4. **Data resets in cloud**
   - SQLite can be ephemeral on some hosting providers.

---

## Lesson 9: Where to go next

- Replace SQLite with PostgreSQL.
- Split routes into `routers/` modules.
- Add unit/integration tests.
- Deploy with Docker.

If you want, I can create a **Lesson 10 (testing)** with ready-to-run `pytest` examples for this exact project.
