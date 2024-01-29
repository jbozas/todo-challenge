<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">TO-DO API</h3>

  <p align="center">
    Create a Task list, interact with them
    <a href="https://github.com/jbozas/todo-challenge"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jbozas/todo-challenge">Report Bug</a>
    <a href="https://github.com/jbozas/todo-challenge">Request Feature</a>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



### Built With

[![Django][Django-url]][Django-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

With this API you can:

  - Handle User:
    - Create a user
    - Login
    - Get user token
    - Refresh user's token
  - Handle Task:
    - Create a Task
    - Retrieve a single task
    - Mark a task as completed
    - Delete a Task
    - Update a Task
    - Retrieve a Task List and filter it. 


### Installation

1. Build the image.
   ```
   docker build -t baseapi .
   ```
2. Run it.
   ```
   docker run -p 8000:8000 baseapi
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jbozas/todo-challenge.svg?style=for-the-badge
[contributors-url]: https://github.com/jbozas/todo-challenge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jbozas/todo-challenge.svg?style=for-the-badge
[forks-url]: https://github.com/jbozas/todo-challenge/network/members
[stars-shield]: https://img.shields.io/github/stars/jbozas/todo-challenge.svg?style=for-the-badge
[stars-url]: https://github.com/jbozas/todo-challenge/stargazers
[issues-shield]: https://img.shields.io/github/issues/jbozas/todo-challenge.svg?style=for-the-badge
[issues-url]: https://github.com/jbozas/todo-challenge/issues
[license-shield]: https://img.shields.io/github/license/jbozas/todo-challenge.svg?style=for-the-badge
[license-url]: https://github.com/jbozas/todo-challenge/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jbozas
[product-screenshot]: images/screenshot.png
[Django-url]: https://img.shields.io/badge/django-%252300ADD8.svg?style=for-the-badge&logo=django&logoColor=white
