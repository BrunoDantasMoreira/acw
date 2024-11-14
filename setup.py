import pathlib 

import setuptools

setuptools.setup(
        name="automatically_change_wallpaper",
        version="0.1",
        description= "A simple Python CLI tool for generating wallpapers from video frames and updating your wallpaper with a new frame each time you run it.",
        long_description=pathlib.Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        author="Bruno Dantas Moreira",
        author_email="brunodmoreira73@gmail.com",
        project_urls={
            "Source": "https://github.com/BrunoDantasMoreira/automatically-change-wallpaper"
            },
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"console_scripts": ["acw = automatically_change_wallpaper:main"]}

        )
