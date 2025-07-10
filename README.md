# Shadow filler
A tool to fill content for the shadow project

## Installation 
```bash
git clone
git submodule init 
git submodule update --recursive --remote

conda create -p ./venv python=3.13 pip
conda activate ./venv

pip install -r requiremnts.txt
python -m camoufox fetch
```

> [!NOTE]  
> On a fresh installation of Linux, you may also need the following Firefox
dependencies:
```bash
sudo apt install -y libgtk-3-0 libx11-xcb1 libasound2 # debian based
sudo pacman -S gtk3 libx11 libxcb cairo libasound alsa-lib # arch distos
```

#### Environment Variables
set all variables mentioned in the .default.env in the local environemt.
Making a .env with the same info will also suffice.

#### Removal
```bash
python -m camoufox remove
```


## Usage
```
python main.py
```