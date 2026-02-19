#!/bin/bash

# manage.sh - Manage isolated conda environments and services for Awabot Demo
# This script creates conda environments (if needed) and runs the services on assigned ports.

set -e

# Configuration
CONDA_BASE=$(conda info --base)
source "$CONDA_BASE/etc/profile.d/conda.sh"

# Port Mapping
VOXTRAL_PORT=8082
QWEN_ASR_PORT=8083
QWEN_TTS_PORT=8084

# Service Setup Function
setup_and_run() {
    local service_name=$1
    local env_name=$2
    local dir_name=$3
    local port=$4

    echo "--------------------------------------------------"
    echo "Setting up service: $service_name"
    echo "--------------------------------------------------"

    # Create conda environment if it doesn't exist
    if ! conda env list | grep -q "$env_name"; then
        echo "Creating conda environment: $env_name..."
        conda create -y -n "$env_name" python=3.10
    fi

    conda activate "$env_name"

    # Install dependencies
    echo "Installing/Updating dependencies for $service_name..."
    cd "$dir_name"
    pip install -r requirements.txt
    
    # Run service in background
    echo "Launching $service_name on port $port..."
    # Using nohup to keep it running, logging to service.log
    nohup uvicorn server:app --host 0.0.0.0 --port "$port" > service.log 2>&1 &
    echo "$service_name launched (PID: $!). Check service.log for output."
    
    cd ..
}

# Main Execution
cd "$(dirname "$0")"

# Kill existing services if they are running on these ports
echo "Cleaning up existing services on ports $VOXTRAL_PORT, $QWEN_ASR_PORT, $QWEN_TTS_PORT..."
for port in $VOXTRAL_PORT $QWEN_ASR_PORT $QWEN_TTS_PORT; do
    pid=$(lsof -t -i:"$port" || true)
    if [ -n "$pid" ]; then
        echo "Killing process $pid on port $port"
        kill -9 "$pid"
    fi
done

# Setup each service
setup_and_run "Voxtral ASR" "awabot-voxtral" "voxtral-asr" "$VOXTRAL_PORT"
setup_and_run "Qwen ASR" "awabot-qwen-asr" "qwen-asr" "$QWEN_ASR_PORT"
setup_and_run "Qwen TTS" "awabot-qwen-tts" "qwen-tts" "$QWEN_TTS_PORT"

echo "--------------------------------------------------"
echo "All services launched."
echo "Voxtral ASR: http://localhost:$VOXTRAL_PORT"
echo "Qwen ASR:    http://localhost:$QWEN_ASR_PORT"
echo "Qwen TTS:    http://localhost:$QWEN_TTS_PORT"
echo "--------------------------------------------------"
