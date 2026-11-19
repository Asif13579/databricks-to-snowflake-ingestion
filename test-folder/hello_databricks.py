# Databricks notebook source

print("Hello from Databricks!")

# Create sample data
data = [
    (1, "John"),
    (2, "David"),
    (3, "Smith")
]

df = spark.createDataFrame(
    data,
    ["id", "name"]
)

display(df)