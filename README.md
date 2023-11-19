<a name="readme-top"></a>

[![Contributors][contributors-shield]](https://github.com/gelndjj/Emaner/graphs/contributors)
[![Forks][forks-shield]](https://github.com/gelndjj/Emaner/forks)
[![Stargazers][stars-shield]](https://github.com/gelndjj/Emaner/stargazers)
[![Issues][issues-shield]](https://github.com/gelndjj/Emaner/issues)
[![MIT License][license-shield]](https://github.com/gelndjj/Emaner/blob/main/LICENSE)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jonathanduthil/)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gelndjj/"Emaner">
    <img src="https://github.com/gelndjj/Emaner/blob/main/resources/image.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Emaner</h3>

  <p align="center">
    Batch rename your files as per your will.
    <br />
    <a href="https://github.com/gelndjj/Emaner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/gelndjj/Emaner/issues">Report Bug</a>
    ·
    <a href="https://github.com/gelndjj/Emaner/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/gelndjj/Emaner/blob/main/resources/main_windows.png" alt="Logo" width="628" height="293">
</br>
</br>
Emaner is a dynamic and user-friendly file renaming application designed to facilitate quick and efficient organization of your digital files. Developed in Python and utilizing the tkinter framework for its graphical user interface, Emaner stands out for its intuitive design and versatile functionality.</br>
</br>
</br>
Key Features:

1. Customizable File Renaming: Allows users to rename files in bulk according to specific patterns or criteria.
2. Regular Expression Support: Advanced users can utilize regular expressions for complex renaming patterns, making it ideal for large datasets.
3. User-Friendly Interface: Designed with a clean and easy-to-navigate GUI, ensuring accessibility for users of all skill levels.
4. Extension-Specific Renaming: Users can target specific file extensions, providing greater control over the renaming process.
5. Preview Capability: Before finalizing changes, users can preview the new file names, ensuring accuracy and satisfaction with the results.
6. Platform Independence: Being a Python-based application, it can be run on any platform that supports Python and tkinter.
</br>
</br>
Emaner is particularly suited for professionals who manage large collections of files, such as photographers, digital librarians, and data analysts, as well as for personal use in organizing documents, images, and multimedia files.
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

<a href="https://www.python.org">
<img src="https://github.com/gelndjj/Emaner/blob/main/resources/py_icon.png" alt="Icon" width="32" height="32">
</a>
&nbsp;
<a href="https://customtkinter.tomschimansky.com">
<img src="https://github.com/gelndjj/Emaner/blob/main/resources/ctk_icon.png" alt="Icon" width="32" height="32">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
</br>

|      	Feature	      |                            	Description	                            |
|:-------------------:|:-------------------------------------------------------------------:|
|    Select Folder    |            Display files present in the selected folder             |
| Include Subfolders  |              Display files present in every subfolders              |
| Regular Expression  | Activate the RE naming - The Replace field will accept RE sequences |
|          ?          | Display the most used RE sequences in a separate window as example  |
| Preserve Extension  |              Prevent the extensions file to be changed              |
|    Rename Files     |                        Execute the renaming                         |
|   "Combobox"        |       Sort out files by extensions (down right of the window)       |

1. Starting the Application: Simply run the emaner.py script in a Python environment where tkinter is installed.
2. Selecting Files: Use the 'Select Folder' button to choose the directory containing the files you wish to rename.
3. Setting Renaming Criteria:
4. Basic Renaming: Enter the desired new name for the files.
5. Using Regular Expressions: For advanced renaming, activate the regular expression option and enter the appropriate pattern.
6. Choosing File Extensions: If you want to rename files of a specific type, select the desired extension from the dropdown menu.
7. Preview Renames: Before applying changes, you can preview the new file names to ensure they match your expectations.
8. Applying Changes: Once satisfied with the preview, click on 'Rename Files' to apply the changes.
</br>
Note: Emaner also supports subfolder inclusion and preservation of file extensions during renaming, providing additional flexibility. Detailed instructions and tips for using regular expressions are provided within the application for users unfamiliar with this powerful tool.
</br>

<!-- GETTING STARTED -->
## Standalone APP

Install pyintaller
```
pip install pyinstaller
```
Generate the standalone app
```
pyinstaller --onefile your_script_name.py
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[LinkedIn](https://www.linkedin.com/in/jonathanduthil/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
