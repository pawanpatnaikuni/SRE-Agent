# SRE-Agent

Simple AI Agent that automatically restarts Windows services based on New Relic alerts.

## Project Structure

```
SRE-Agent/
│
├── app.py
├── config.py
├── webhook.py
├── restart_service.py
├── verify_service.py
├── logger.py
├── requirements.txt
└── README.md
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app:app --reload
```

The API starts at:

```
http://127.0.0.1:8000
```

## Health Check

```
GET /
```

Response:

```json
{
  "status": "running",
  "application": "SRE-Agent"
}
```

## Webhook Endpoint

```
POST /webhook
```

Example Request:

```json
{
  "service_name": "Spooler"
}
```

Example Success Response:

```json
{
  "success": true,
  "message": "Spooler restarted successfully"
}
```

## Log File

Logs are written to:

```
agent.log
```