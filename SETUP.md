# Pokémon Card Scanner - Setup Guide

This guide provides detailed instructions for setting up the development environment for the Pokémon Card Scanner application.

## System Requirements

### macOS
- macOS 10.15 or later
- Homebrew package manager
- Xcode Command Line Tools
- Python 3.8 or later
- Node.js 16 or later
- MySQL 8.0 or later

### Windows
- Windows 10 or later
- Python 3.8 or later
- Node.js 16 or later
- MySQL 8.0 or later
- Visual Studio Build Tools

### Linux (Ubuntu/Debian)
- Ubuntu 20.04 or later
- Python 3.8 or later
- Node.js 16 or later
- MySQL 8.0 or later
- Build essentials

## System Dependencies

### macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install system dependencies
brew install mysql-client
brew install rust
brew install node
brew install python

# Set up MySQL client environment variables
echo 'export LDFLAGS="-L/opt/homebrew/opt/mysql-client/lib"' >> ~/.zshrc
echo 'export CPPFLAGS="-I/opt/homebrew/opt/mysql-client/include"' >> ~/.zshrc
echo 'export PKG_CONFIG_PATH="/opt/homebrew/opt/mysql-client/lib/pkgconfig"' >> ~/.zshrc
source ~/.zshrc
```

### Windows
```bash
# Install Chocolatey if not already installed
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install system dependencies
choco install python
choco install nodejs
choco install mysql
choco install rust
```

### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y nodejs npm
sudo apt install -y mysql-server
sudo apt install -y build-essential
sudo apt install -y pkg-config
sudo apt install -y libmysqlclient-dev

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

## Backend Setup

1. Create and activate virtual environment:
```bash
cd backend
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
.\venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database:
```bash
# Start MySQL service
# On macOS
brew services start mysql

# On Windows
net start mysql

# On Linux
sudo service mysql start

# Create database
mysql -u root -p
CREATE DATABASE pokemon_cards;
exit;
```

## Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm start
```

## Development Tools

### Recommended IDE Extensions
- Python
  - Pylance
  - Python Test Explorer
  - SQLTools
- JavaScript/React
  - ESLint
  - Prettier
  - React Native Tools

### Database Management
- MySQL Workbench (recommended)
- DBeaver
- TablePlus

## Troubleshooting

### Common Issues

1. MySQL Client Installation Issues
   - Ensure MySQL client libraries are properly installed
   - Verify environment variables are set correctly
   - Check system PATH includes MySQL binaries

2. Python Package Installation Issues
   - Ensure Rust is installed and in PATH
   - Verify Python virtual environment is activated
   - Check system dependencies are installed

3. Node.js Issues
   - Clear npm cache: `npm cache clean --force`
   - Delete node_modules: `rm -rf node_modules`
   - Reinstall dependencies: `npm install`

### Getting Help

If you encounter issues not covered in this guide:
1. Check the project's GitHub Issues
2. Consult the documentation of individual packages
3. Search for similar issues on Stack Overflow

## Production Deployment

For production deployment, additional steps are required:
1. Set up a production database
2. Configure environment variables
3. Set up SSL certificates
4. Configure reverse proxy (e.g., Nginx)
5. Set up monitoring and logging

Refer to the `DEPLOYMENT.md` file for detailed production setup instructions. 