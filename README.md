# DavaX_Python
# 🔢 Math Microservice API – FastAPI + SQLite

A simple and modular microservice that performs mathematical operations like:

-  Power (`x^y`)
-  Factorial (`n!`)
-  Fibonacci (`F(n)`)

Each operation has its own **POST endpoint** and **GET history endpoint**.  
Results are **saved in SQLite** and **logged to file**.

>  **API protected by API key**  
> Include header: `x-api-key: math123secret`

---

## 🚀 How to Run

### 1. Clone & install dependencies

```bash
git clone https://github.com/IoanaZin/DavaX_Python_homework.git
cd DavaX_Python_homework
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
