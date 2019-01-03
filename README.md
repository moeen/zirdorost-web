## Installation

For install and run zirdorost-web, run the commands below:

```bash
git clone https://gitlab.com/zirdorost/zirdorost-web/
cd zirodorost-web
git clone https://gitlab.com/zirdorost/zirdorost-library/
mv zirodorost-library/zirodorost_library.py .
rm -rf zirodorost-library
virtualenv -p python2 --no-site-packages --distribute .env
source .env/bin/activate
pip install Flask
python main.py
```

## License

This project is under [AGPL3](https://gitlab.com/zirdorost/zirdorost-web/blob/master/LICENSE)
