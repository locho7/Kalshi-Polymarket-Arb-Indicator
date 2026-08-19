# Kalshi/Polymarket Arbitrage Scanner
This is a full stack web application that tracks price differences between manually paired Kalshi and Polymarket markets.

This project is designed as a indicator, it does not connect to any trading accounts or execute any orders.


## Overview
Kalshi and Polymarket are exchanges where users can trade yes/no contracts on real world events. Contracts are priced between $0.01 to $0.99 based on the probability of that specific event happening. In binary markets, a correct contract settles at $1.00, while an incorrect contract settles at $0.00. Price discreptencies between Yes/No contracts between Kalshi and Polymarket can be traded to yield small profits, which this app helps to find.

This project was built to practice full-stack development. It features a React frontend, FastAPI backend, and PostgreSQL database to store matching markets between Kalshi/Polymarket


## Features
- Fetches live market data from Kalshi/Polymarket
- Stores manually matched market pairs in PostgreSQL
- Builds opportunity objects from matched market pairs
- Displays price differences in a React dashboard
- Includes automatic 30s refreshes
- Includes manual refreshing with 5s cooldown
- Uses backend caching to reduce repeated API calls
- Includes loading, empty, and error states


## Tech Stack
### Frontend
- React
- Typescript
- Tailwind CSS
- Vite

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- python-dotenv
- requests


## Getting Started
Prerequisites:
Install Node.js, Python, PostgreSQL


Backend Setup:
1. CD into your backend folder, then create and activate a virtual environment by typing: 
```bash
python -m venv .venv
```

2. In your Windows Powershell type: .\.venv\Scripts\Activate.ps1

3. Install backend dependencies by typing: 
```bash
pip install fastapi uvicorn requests sqlalchemy psycopg2-binary python-dotenv
```

4. Create and .env file inside your backend folder. This is where you will store your Postgres database url. In that file, type in: 
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

5. Run the backend: 
```bash
python -m uvicorn app.main:app --reload.
``` 
The backend will run at http://127.0.0.1:8000.

6. FastAPI docs are available at http://127.0.0.1:8000/docs. Use this to easily get/post/delete marketpairs or to get available opportunities.

Frontend Setup:
1. CD into your frontend folder and run: npm install

2. Then run: npm run dev

3. The frontend will run at: http://localhost:5173


## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/get-opportunities` | Returns current cross-market pricing opportunities |
| GET | `/get-marketpairs` | Returns stored Kalshi/Polymarket market pairs |
| POST | `/marketpair` | Adds a new market pair to the database |
| DELETE | `/marketpair` | Deletes a market pair by Kalshi market ticker and Polymarket ID |


## How it works
1. Market pairs are manually found and stored in PostgreSQL

2. The backend reads through all the pairs in the database, finding unique Kalshi events / Polymarket slugs.

3. The backend fetches matching market data for these events/slugs from Kalshi/Polymarket.

4. Event/slug market data is cached briefly to avoid unnecessary API calls when later fetching individual market data.

5. The app compares YES/NO prices, calculates price differences, and stores these opportunities as an object.

6. The frontend displays these pricing gaps and gross edge.


## Opportunity Calculation
The app compares two possible market positions:
1. Kalshi YES + Polymarket NO
2. Kalshi NO + Polymarket YES

The gross edge, before fees, slippage, and liquidity constraints, is calculated as:
gross edge = 1.00 - (lowest combined contract cost)

For example, if Kalshi and Polymarket had (YES, NO) spreads of (0.21, 0.79) for Kalshi and (0.25, 0.75) for Polymarket,
then the greatest gross edge would be 1.00 - (Kalshi NO + Polymarket YES).

Please note that this is a gross estimate, and does not fully account for fees, slippage, or liquidity.


## What I learned
This is my very first full-stack app. Through the process of creating this project, I learned to:

- Build a frontend with React/Typescript

- Style components using Tailwind CSS

- Create a FastAPI backend

- Connect FastAPI to PostgreSQL using SQLAlchemy

- Fetch data from external APIs

- Managing loading/error states

- Using Git/Github to streamline development

For someone who learned to code relatively late, this project was overall a great learning experience.


## Future Improvements
- Frontend tool for adding/deleting market pairs

- Improve opportunity filtering and sorting

- Estimated fee calculator

- Add liquidity/orderbook checks

- AI-assisted market-pair matching 

- Deploy the app


## Disclaimer
This project is first and foremost a learning experience. It is not an automated trader, it does not place trades, and should not be used as financial advice. Display opportunities may not account for slippage, fees, or liquidity.
