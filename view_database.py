#!/usr/bin/env python
import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\n" + "="*60)
print("DATABASE STRUCTURE & CONTENTS")
print("="*60)

for table in tables:
    table_name = table[0]
    print(f"\n📋 TABLE: {table_name}")
    print("-" * 60)
    
    # Get column info
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    print("Columns:")
    for col in columns:
        print(f"  • {col[1]} ({col[2]})")
    
    # Get row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cursor.fetchone()[0]
    print(f"\nTotal Rows: {count}")
    
    # Show sample data if exists
    if count > 0:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        rows = cursor.fetchall()
        if rows:
            print(f"\nSample Data (showing up to 5 rows):")
            for i, row in enumerate(rows, 1):
                print(f"  Row {i}: {row}")

print("\n" + "="*60 + "\n")
conn.close()
