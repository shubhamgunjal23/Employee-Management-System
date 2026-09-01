from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Employee Management System")

def conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST","db"),
        dbname=os.getenv("DB_NAME","appdb"),
        user=os.getenv("DB_USER","appuser"),
        password=os.getenv("DB_PASSWORD","apppass"),
        port=int(os.getenv("DB_PORT","5432"))
    )

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/items")
def list_items():
    with conn() as c:
        with c.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM items ORDER BY id DESC")
            return cur.fetchall()

class Item(BaseModel):
    name: str
    description: str = ""

@app.post("/items")
def create_item(item: Item):
    with conn() as c:
        with c.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO items(name,description) VALUES(%s,%s) RETURNING *",
                (item.name,item.description))
            return cur.fetchone()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    with conn() as c:
        with c.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM items WHERE id=%s",(item_id,))
            row=cur.fetchone()
            if not row: raise HTTPException(404,"Item not found")
            return row
