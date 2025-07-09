# Shadow filler
A tool to fill content for the shadow project

## Installation 
```bash
conda create -p ./venv python=3.13 pip
conda activate ./venv
pip install -r requiremnts.txt
python -m camoufox fetch
```
#### Removal
```bash
python -m camoufox remove
```

[!NOTE]  
> On a fresh installation of Linux, you may also need the following Firefox
dependencies:
```bash
sudo apt install -y libgtk-3-0 libx11-xcb1 libasound2 # debian based
sudo pacman -S gtk3 libx11 libxcb cairo libasound alsa-lib # arch distos
```


## Usage
```
python main.py
```