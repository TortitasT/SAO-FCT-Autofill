# SAO-FCT-Autofill

Crawler that automates the process of writing the FCT SAO diary so you don't have to ;)

## Usage

- Install dependencies:  
  `pip3 install pyautogui pyperclip python-dotenv requests`

- Clone repo:  
  `git clone https://github.com/TortitasT/SAO-FCT-Autofill`

- Set your randomized responses in descriptions.txt spaced by newlines.

- Rename .env.example to .env and fill in the variables with the parameters from the url of the pdf and the session cookie value.
![Captura de pantalla 2022-05-22 214506](https://user-images.githubusercontent.com/76071376/169713109-9308ae2e-a3ed-4c24-b5fd-7412160f0152.png)
![Captura de pantalla 2022-05-22 214333](https://user-images.githubusercontent.com/76071376/169713118-fc72b17d-9996-4657-a9f8-77a4edf052c1.png)

- Run:  
  `python3 main.py`

- Open Firefox and navigate to first week of FCT SAO page.
