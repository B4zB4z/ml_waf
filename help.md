# ML-Based Web Application Firewall (WAF)

## Quick Start – First-Time Use

This file explains the **minimum steps** required to run the project for the first time.

---

## 1. Requirements

- Python **3.9+**
- `pip`
- Terminal / PowerShell

---

## 2. Create and Activate Virtual Environment

From the project root:

```bash
python -m venv venv
```

Activate it:

**Windows:**

```powershell
venv\Scripts\Activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Train the Model

Run this **once**:

```bash
python -m model.train_model
```

This will create a trained model file.

---

## 5. Run the WAF

```bash
python waf/app.py
```

The WAF will start on:

```
http://127.0.0.1:8080
```

---

## 6. Test (Optional)



From your terminal use these commands:



Legitimate request:

```bash
curl "http://localhost:8080/?id=123"
```

Malicious request:

```bash
curl "http://localhost:8080/?id=1 OR 1=1"
```

---

##
