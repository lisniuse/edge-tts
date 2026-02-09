#!/bin/bash
# Install required Python dependencies for Edge TTS

echo "Installing edge-tts package..."
pip install edge-tts

echo ""
echo "✓ Dependencies installed successfully!"
echo ""
echo "You can now use the TTS synthesizer:"
echo "  python scripts/edge_tts_synthesizer.py --help"
