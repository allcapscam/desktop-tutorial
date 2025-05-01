
Navigate to your project directory
cd ~/projects/movielens-twotower-pytorch

Optional: deactivate existing env
deactivate

Create a new virtual environment
python3 -m venv .venv

Activate the environment (Mac/Linux)
source .venv/bin/activate

 (Windows)
 .venv\Scripts\activate

 Upgrade pip and install dependencies
pip install --upgrade pip
pip install torch torchmetrics pandas scikit-learn jupyter tqdm