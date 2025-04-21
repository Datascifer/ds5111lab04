echo "Updating package lists..."
sudo apt update

echo "Installing make..."
sudo apt install -y make

echo "Installing Python 3.12 venv..."
sudo apt install -y python3.12-venv

echo "Installing tree..."
sudo apt install -y tree

echo "All base packages installed!"
