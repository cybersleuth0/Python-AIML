from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(
    title="swiggy order service",
    description=(
        "Internal api for managing orders"
        "handle creation tracking of delivery systems"
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    # fastapi converts this dictionary to JSON automatically
    return {"message": "Welcome to the Swiggy Order Service", "status": "healthy"}


@app.get("/about")
def read_about():
    """About endpoint - Information about the Swiggy Order Service"""
    return {
        "service": "Swiggy Order Service",
        "description": "Internal API for managing orders, handling creation and tracking of delivery systems.",
        "version": "1.0.0"
    }


@app.get("/orders")
def list_order():
    """List Recent orders"""
    return {
        "orders": [
            {"id": 1, "item": "Buttern chicken", "status": "delivered", },
            {"id": 1, "item": "Masala Dosa", "status": "delivered", },
            {"id": 1, "item": "Paneer tikka", "status": "delivered", }
        ]
    }


@app.get("/orders/status")
def list_order():
    """order status"""
    return {
        "total_orders": 3,
        "delivered": 3,
        "pending": 0,
        "top_city": "Bangalore"
    }
