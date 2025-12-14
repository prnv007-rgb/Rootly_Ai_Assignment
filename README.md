# Rootly_Ai_Assignment
# NLP → DSL → Strategy Execution Prototype

> A demonstration of natural language processing, domain-specific language design, and automated code execution for trading rule evaluation.

## Overview

This project implements an end-to-end pipeline that transforms **natural language trading rules** into **executable Python code** through a custom Domain-Specific Language (DSL). The system demonstrates language design, parsing, AST construction, and programmatic execution—focusing on the technical architecture rather than production trading.

### Pipeline Architecture

```
Natural Language Input
        ↓
Structured Rule Extraction
        ↓
DSL Generation
        ↓
AST Construction
        ↓
Code Generation
        ↓
Backtest Execution
```

## Key Features

- **Natural Language Processing**: Converts plain English rules into structured format
- **Custom DSL**: Domain-specific language for expressing trading logic
- **Grammar-Based Parsing**: Uses Lark parser for robust syntax analysis
- **AST Generation**: Builds abstract syntax trees for code representation
- **Dynamic Code Generation**: Produces executable Python from AST
- **Technical Indicators**: Supports SMA and RSI calculations
- **Backtest Engine**: Simulates strategy execution on time-series data

## Project Structure

```
├── demo.py              # End-to-end demonstration
├── nl_parser.py         # Natural language → structured rules
├── dsl_parser.py        # DSL grammar and AST builder
├── ast_nodes.py         # AST node definitions
├── codegen.py           # AST → Python code generator
├── indicators.py        # Technical indicator implementations
├── backtest.py          # Strategy backtest simulator
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd <repo-name>

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the end-to-end demonstration:

```bash
python demo.py
```

### Example

**Input (Natural Language):**
```
Buy when the close price is above the 20-day moving average 
and volume is above 1 million. Exit when RSI is below 30.
```

**Generated DSL:**
```
ENTRY:
  close > sma(close, 20) AND volume > 1000000

EXIT:
  rsi(close, 14) < 30
```

**Output:**
```
Backtest Results:
Entry: 2023-02-25 | Exit: 2023-02-26 | PnL: -0.84
Total Trades: 1
```

## DSL Specification

### Syntax

The DSL supports two main blocks: `ENTRY` and `EXIT`, each containing conditional logic.

**Supported Operations:**
- **Comparisons**: `>`, `<`, `>=`, `<=`, `==`
- **Logical Operators**: `AND`, `OR`
- **Indicators**: 
  - `sma(series, period)` - Simple Moving Average
  - `rsi(series, period)` - Relative Strength Index
- **Data Fields**: `open`, `high`, `low`, `close`, `volume`

### Example DSL

```
ENTRY:
  close > sma(close, 50) AND volume > sma(volume, 20)

EXIT:
  close < sma(close, 20) OR rsi(close, 14) > 70
```

## Technical Implementation

### 1. Natural Language Parser
Extracts structured information from plain English using pattern matching and NLP techniques.

### 2. DSL Parser
Uses Lark grammar to parse DSL text into an Abstract Syntax Tree (AST).

### 3. Code Generator
Traverses the AST to generate executable Python functions for strategy logic.

### 4. Backtest Engine
Simulates strategy execution on synthetic OHLCV data with position tracking and PnL calculation.

## Data

The project uses **synthetically generated OHLCV data** to maintain self-containment:
- Price follows a random walk model
- Volume is randomly generated
- Seeded for reproducibility
- No external data dependencies

## Limitations & Scope

This is an **educational prototype** demonstrating language design and execution concepts:

- Natural language parsing supports limited predefined patterns
- DSL grammar is intentionally minimal for clarity
- Backtest logic is simplified (single position, no fees/slippage)
- No optimization or production-grade error handling
- Synthetic data only—not suitable for real trading decisions

## Project Goals

This project demonstrates:

✓ End-to-end language processing pipeline  
✓ Custom DSL design and implementation  
✓ AST-based program transformation  
✓ Clean, modular software architecture  
✓ Automated code generation techniques  

## Requirements

- Python 3.8+
- pandas
- numpy
- lark-parser

See `requirements.txt` for complete dependency list.

## License

This project is intended for educational and demonstration purposes.

---

**Status**:  Complete and ready for evaluation
