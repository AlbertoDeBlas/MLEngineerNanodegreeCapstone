#!/bin/bash
sudo -u ec2-user -i <<'EOF'
source activate pytorch_p36
pip install -U numpy
pip install -U joblib
pip install -U scipy
pip install -U scikit-learn
source deactivate
EOF
