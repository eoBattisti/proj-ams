#!/usr/bin/env bash

echo "Installing poetry..."
pip install poetry

echo "Installing project dependencies..."
poetry install
