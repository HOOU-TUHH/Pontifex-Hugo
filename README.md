 [![](https://collaborating.tuhh.de/e-10/hoou/pontifex-hugo/-/jobs/artifacts/dev/raw/nodes.svg?job=dynamic_badge)]()
 [![](https://collaborating.tuhh.de/e-10/hoou/pontifex-hugo/-/jobs/artifacts/dev/raw/edges.svg?job=dynamic_badge)]()
 [![](https://collaborating.tuhh.de/e-10/hoou/pontifex-hugo/-/jobs/artifacts/dev/raw/podcasts.svg?job=dynamic_badge)]()

# Pontifex

This repo contains the essential Python and Bash scripts to build the pontifex project
It also provides all teaching and learning material used in the instance running on the domain [pntfx.com](https://pntfx.com) licensed under ....

# Terms of Use

> How is the content of Pontifex licensed?

# Getting Started

> If you want to kickstart your own project with Pontifex and HUGO

## Kickstart your own application on GitHub

* **Import project**: visit https://github.com/new/import and paste the URL `https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo.git`
* **Enable GitHub Actions**: visit the [repository settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) to manage the repository actions and check the boxes next to *Allow all actions  and reusable workflows* and *Read and write permissions*
* **Triggering the GitHub Action**: every change in your repository files should trigger the action `github-pages`. Visit your repository environments list to find out about the deployment status of your project.
* Once the GitHub-Action has finished, visit the page `https://your-github-username.github.io/pontifex/` to explore your Pontifex application.

For details on the implementation, checkout the GitHub workflow in the file `.github/workflows/gh-pages.yml`

## Modifying the content

### Graph Database

All connections are stored in the [JSON](https://en.wikipedia.org/wiki/JSON) file `nodes/graph.json`.
This file encodes all nodes and directed edges. Furthermore, the file contains and links the relevant metadata.
On the top-level it is a list containing the dictionaries `nodes` and `edges`.
In the following, we explain how the entries of the dictionaries are constructed.

#### Nodes

Example entry:
```json
    "305": {
      "id": "305",
      "label": "Epsilon-Delta\nDefinition",
      "meta": "RA28",
      "content": "A different notion of continuity using open intervals. If the input to a continuous function varies less than delta, then the output values should vary less than epsilon.",
      "notes": "305-snippet.html",
      "video": "https://www.youtube-nocookie.com/embed/4xhyqdjmxHU?start=11",
      "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=Library/Berkeley/StewCalcET7e/2.4/2-4-03.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
      "podcast": "<iframe src=\"https://anchor.fm/profmoppi/embed/episodes/Continuity-Part-1-with-Fabian-Gabel-e1kvb1u\" height=\"102px\" width=\"100%\" frameborder=\"0\" scrolling=\"no\"></iframe><p>Courtesy of Marcus Waurick. <i>Well-defined & Wonderful podcast</i>, <a href=\"https://www.marcus-waurick.de/teaching\">marcus-waurick.de</a>.</p>"
    },
```

This entry describes the concept node `305` for the concept "Epsilon-Delta Definition"

* `id` should be a unique three-digit number. The first digit specifies the chapter (0-9). The second and third digits run from `00` to `99`. The `id` identifies the node and is also used for defining the edges.
* `label` is the text used as title of the node. It will show as the title of the corresponding webpage and as label of the node in the graph
* `meta` contains further information for the content. In the above example, it specifies the name of the video; no routine processes this text, so one can use the entry to store further info.
* `content` explains the topic; this text shows on the top of each webpage below the title
* `notes` name of the html file containing the lecture notes.
* `video` link to the YouTube video that should be embedded. Currently we use the `youtube` [shortcode](https://gohugo.io/content-management/shortcodes/) such that only the information `/embed/` will be further processed.
* `webwork` link to webwork exercise or other webpage that will be embedded via an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe).
* `podcast` plain html-`<iframe>` code to go in the *Podcast* section.
#### Edges

Example entry:
```json
    "005-300": {
      "source": "005",
      "target": "300",
      "label": "Boundedness of a function can be expressed in terms of the image or range."
    },
```

This entry describes the directed edge going from node `005` to node `300`.

* `source` is the `id` of the outgoing node.
* `target` is the `id` of the incoming node.
* `label` contains information on why this connection is needed. The content of `label` is displayed when one clicks on the `label` in the graph view. 

### Node Content

During the creation of the website, each node automatically gets it's own standardized [Markdown](https://www.markdownguide.org/) page `xxx.md`.
The template for this page can be found in the file `nodes/dummy_for_hugo.md`.
This file encodes the overall structure of the content page for a node. A change in the template will affect all node pages simultaneously once the webpage has been rebuilt.
The template uses certain marker-words that are replaced with specific counterparts during the build process. In particular, the information from the `JSON` database will be filled in.
In the following, we describe which data needs to be provided in order to start building the webpage.

#### TeX Snippets

Each node provides a section called "Notes". 
For your nodes to show up here, an `HTML`-file needs to be provided and will be included automatically by the build-process. 
The name of this `HTML` is stored in the attribute `notes` in each entry of the `JSON` database.
It should reside in the folder `nodes/xxx/xxx-node.html` where  `xxx` stands for the specific node.

The current version of Pontifex assumes that you provide a file `nodes/xxx/xxx.tex` for each node, i.e., a `TeX`-file containing the content for each notes-section.
This file will be parsed to `HTML` using `pandoc` during the creation process.
User-specific macros are stored centrally in the file `nodes/packages.tex`. 
We suggest to refrain from using user-specific macros as `pandoc` may be struggling to resolve the macros.
You may find [de-macro](https://ctan.org/pkg/de-macro) helpful for automatized resolution of TeX-macros.
For details on the preprocessing of TeX Snippets, refer to the developer documentation below.

#### YouTube Videos

YouTube Videos are included via the `youtube` [shortcode](https://gohugo.io/content-management/shortcodes/). 
Here the URL specified in the `video` attribute of the `JSON` database is used, starting from `/embed/...`.
See [here](https://support.google.com/youtube/answer/171780?hl=en) for more information on embedding YouTube videos.

#### Podcast Episodes

This section is optional and will only be processed when the `podcast` attribute in the `JSON` database is nonempty. 
En empty entry looks like
```JSON
      "podcast": ""
```

If "podcast" is nonempty, the full html-content will by copied to the corresponding section in the template.
The original version of pontifex uses either `<iframe>` code provided by the podcast hosters, e.g. [AnchorFM](https://anchor.fm/), 
```html
      "podcast": "<iframe src=\"https://anchor.fm/profmoppi/embed/episodes/Rearrangement-of-Series-with-Fabian-Gabel-e1iq2sr/a-a7vb2vp\" height=\"102px\" width=\"100%\" frameborder=\"0\" scrolling=\"no\"></iframe><p>Courtesy of Marcus Waurick. <i>Well-defined & Wonderful podcast</i>, <a href=\"https://www.marcus-waurick.de/teaching\">marcus-waurick.de</a>.</p>"
```
or provides short snippets to include content that has been copied to the server.
```html
      "podcast": "<audio controls src=\"/e-10/pontifex/podcast/imvt.mp3\">Your browser does not support the <code>audio</code> element.</audio>"},
```

#### Discussion Forum

The current version of pontifex uses a discussion tab on each webpage.
Each discussion features a GitHub-Like discussion thread provided by [Vssue](https://vssue.js.org/).
In order to enable Vssues on your own instance of Pontifex, follow the following steps
* In case you are not hosting your repo on GitHub, create a public repo on GitHub repository and generate the `clientID` and `clientSecret` yourself to make it work. Refer to https://vssue.js.org/guide/github.html for how to do that.
* Modify the following portion of your `layouts/partial/footer/script-footer.html` by changing all of the exemplary values to the ones of your repo.

```javascript
// here set the options for your OAuth App
options: {
  owner: 'owner',
  repo: 'repo-name',
  clientId: 'generate-one-on-github',
  clientSecret: 'generate-one-on-github', // only required for some of the platforms
  labels: ['Comment'],
  prefix: '[Pontifex Website] ',
},
```

* Log in to comment.

#### WeBWorK or other Electronic Exercises

The bottom of each page includes an electronic [WeBWorK](https://github.com/openwebwork/) exercise in the form of an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe).
```json
"webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=Library/Berkeley/StewCalcET7e/2.4/2-4-03.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
```
will render the exercise once the webpage has been loaded.

Details on the WeBWorK course creation can be found [here](https://michaelgage.blogspot.com/2015/06/whether-writing-full-text-book-or-just.html).

# Developer Info

## Python Preprocessing

`*.py` files in `bin`-folder:

| Preprocessor | Description |
| - | - |
| `build_json.py` | Build `JSON` file for each node containing only neighbors of distance 1 |
| `build_md.py` | Build `MD` file for each node substituting placeholders by node-specific values |

## Build Process

In order to build the HUGO project, the Bash-script `/bin/build_pontifex.sh` needs to be executed. 
The build process consists of 3 parts: 
1) Preprocessing using the Python scripts and [`pandoc`](https://pandoc.org/)
2) Copying the files to their location to be picked up by HUGO
3) Running HUGO to create the static webpage. The resulting files are then located in the folder `public`.

## Cytoscape.js

We rely on [Cytoscape.js](https://js.cytoscape.org/) in order to visualize the graph.

Colors and functionality of the graph are encoded in the files
`static/js/vendor/{pontifex-graph,pontifex-overview}.js`

Each page using a Cytoscape.js graph needs to include a specific `header1.html` page. See the shortcode below.

## Pandoc

Translation of `TeX` to `HTML` with MathJax support is achieved with [`pandoc`](https://pandoc.org/).
If building the Pontifex project locally without the use of the provided Docker container make sure to have a `pandoc` version >= 2.18.

## Node

The HUGO project is built using [Node.js](https://nodejs.org/en/).
If building the Pontifex project locally without the use of the provided Docker container make sure to have a `node` version >= 18.5.

## Dummies and Shortcodes

`nodes/dummy_for_hugo.md` specifies the overall structure of each page.
We use special shortcodes for including WeBWorK exercises and Tabs, see `layouts/shortcodes/` for details.

### `header1`

This  is needed for the Cytoscape.js objects to function properly. 
The syntax is `{{< header1 "index">}}` where `index` specifies the id of the node and will be used in order to load the node-specific `JSON`-file.

### `header2`

Same as `header1` but this is used only on for the overview page and not in `dummy_for_hugo.md`

## Branding 

All files that apply some sort of branding reside in the **private** repository

https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-brand

Content is copied to their respective locations in the `.gitlab-ci.yml`-stage: `brand`.

As `pontifex-brand` is private, the repo `pontifex-hugo` needs to have an *access token* in the pipeline variables in order to clone `pontifex-brand`. The presently used token was generated within `pontifex-brand`/Settings/Access Tokens with `read repository` scope and added to `pontifex-hugo` as the pipeline variable `PROJECT_TOKEN`.

## Development environment using Docker

Download or clone `pontifex-hugo` first:

```bash
git clone git@collaborating.tuhh.de:e-10/hoou/pontifex-hugo.git
```

# Building the Docker image locally and building the HUGO project

Download or clone `pontifex-hugo`
```bash
git clone git@collaborating.tuhh.de:e-10/hoou/pontifex-hugo.git
```

Within `pontifex-hugo` run 
```bash
docker build . -t pontifex-hugo
```

Now, run 
```bash
docker run -it --rm -v `pwd`:/app -w /app pontifex-hugo ./bin/build_pontifex.sh
```
to build the project.

This process should also be carried out every time, an update of `pontifex-hugo/{bin/,Dockerfile}` is carried out.

# Building the HUGO project with an external Docker image

Within a git-clone of [`pontifex-hugo`](https://collaborating.tuhh.de/e-10/hoou/pontifex-hugo), run
```bash
docker run -it --rm -v `pwd`:/app -w /app collaborating.tuhh.de:5005/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo:latest ./bin/build_pontifex.sh
```
This will use the root image from the [Container Registry](https://collaborating.tuhh.de/e-10/hoou/pontifex-hugo/container_registry/).

You may need to
```
docker login collaborating.tuhh.de:5005
```
and authenticate first. Note that, the first time you `docker run` the above command, it may take longer as the image needs to be downloaded first.

# Contributors

Here could be a list of people who have contributed to the project.

---
This is the original documentation for the HUGO theme used by Pontifex.


# HUGO Doks 


<p align="center">
  <a href="https://getdoks.org/">
    <img alt="Doks" src="https://doks.netlify.app/doks.svg" width="60">
  </a>
</p>

<h1 align="center">
  Doks
</h1>

<h3 align="center">
  Modern Documentation Theme
</h3>

<p align="center">
  Doks is a Hugo theme for building secure, fast, and SEO-ready documentation websites, which you can easily update and customize.
</p>

<p align="center">
  <a href="https://github.com/h-enk/doks/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/h-enk/doks?style=flat-square" alt="GitHub">
  </a>
  <a href="https://github.com/h-enk/doks/releases">
    <img src="https://img.shields.io/github/v/release/h-enk/doks?include_prereleases&style=flat-square"alt="GitHub release (latest SemVer including pre-releases)">
  </a>
  <a href="https://www.npmjs.com/package/@hyas/doks">
    <img src="https://img.shields.io/npm/v/@hyas/doks?style=flat-square" alt="npm (scoped)">
  </a>
  <a href="https://github.com/h-enk/doks/actions?query=workflow%3A%22Hyas+CI%22">
    <img src="https://img.shields.io/github/workflow/status/h-enk/doks/Hyas%20CI/master?style=flat-square" alt="GitHub Workflow Status (branch)">
  </a>
  <a href="https://app.netlify.com/sites/doks/deploys">
    <img src="https://img.shields.io/netlify/8a1009d5-88ac-413e-96ef-3f928674a083?style=flat-square" alt="Netlify">
  </a>
</p>

![Doks — Modern Documentation Theme](https://raw.githubusercontent.com/h-enk/doks/master/images/tn.png)

## Demo

- [doks.netlify.app](https://doks.netlify.app/)

## Why Doks?

Nine main reasons why you should use Doks:

1. __Security aware__. Get B+ scores on [Mozilla Observatory](https://observatory.mozilla.org/analyze/doks.netlify.app) out of the box. Easily change the default Security Headers to suit your needs.

2. __Fast by default__. Get 104 scores on [Google Lighthouse](https://googlechrome.github.io/lighthouse/viewer/?gist=7731347bb8ce999eff7428a8e763b637) by default. Doks removes unused css, prefetches links, and lazy loads images.

3. __SEO-ready__. Use sensible defaults for structured data, open graph, and Twitter cards. Or easily change the SEO settings to your liking.

4. __Development tools__. Code with confidence. Check styles, scripts, and markdown for errors and fix automatically or manually.

5. __Bootstrap framework__. Build robust, flexible, and intuitive websites with Bootstrap 5. Easily customize your Doks site with the source Sass files.

6. __Netlify-ready__. Deploy to Netlify with sensible defaults. Easily use Netlify Functions, Netlify Redirects, and Netlify Headers.

7. __Full text search__. Search your Doks site with FlexSearch. Easily customize index settings and search options to your liking.

8. __Page layouts__. Build pages with a landing page, blog, or documentation layout. Add custom sections and components to suit your needs.

9. __Dark mode__. Switch to a low-light UI with the click of a button. Change colors with variables to match your branding.

### Other features

- __Multilingual and i18n__ support
- __Versioning__ documentation support
- __KaTeX__ math typesetting
- __Mermaid__ diagrams and visualization
- __highlight.js__ syntax highlighting

## Requirements

- [Git](https://git-scm.com/) — latest source release
- [Node.js](https://nodejs.org/) — latest LTS version or newer

<details>
<summary>Why Node.js?</summary>

Doks uses npm (included with Node.js) to centralize dependency management, making it [easy to update](https://getdoks.org/docs/help/how-to-update/) resources, build tooling, plugins, and build scripts.

</details>

## Get started

Start a new Doks project in three steps:

### 1. Create a new site

Doks is available as a child theme and a starter theme.

#### Child theme

- Intended for novice to intermediate users
- Intended for minor customizations
- [Easily update npm packages](https://getdoks.org/docs/help/how-to-update/) — __including__ [Doks](https://www.npmjs.com/package/@hyas/doks)

```bash
git clone https://github.com/h-enk/doks-child-theme.git my-doks-site && cd my-doks-site
```

#### Starter theme

- Intended for intermediate to advanced users
- Intended for major customizations
- [Easily update npm packages](https://getdoks.org/docs/help/how-to-update/)

```bash
git clone https://github.com/h-enk/doks.git my-doks-site && cd my-doks-site
```

<details>
<summary>Help me choose</summary>

Not sure which one is for you? Pick the child theme.

</details>

### 2. Install dependencies

```bash
npm install
```

### 3. Start development server

```bash
npm run start
```

## Other commands

Doks comes with [commands](https://getdoks.org/docs/prologue/commands/) for common tasks.

## Documentation

- [Netlify](https://docs.netlify.com/)
- [Hugo](https://gohugo.io/documentation/)
- [Doks](https://getdoks.org/)

## Communities

- [Netlify Community](https://community.netlify.com/)
- [Hugo Forums](https://discourse.gohugo.io/)
- [Doks Discussions](https://github.com/h-enk/doks/discussions)

## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.

[![OC sponsor 0](https://opencollective.com/doks/tiers/sponsor/0/avatar.svg)](https://opencollective.com/doks/tiers/sponsor/0/website)
[![OC sponsor 1](https://opencollective.com/doks/tiers/sponsor/1/avatar.svg)](https://opencollective.com/doks/tiers/sponsor/1/website)

## Backers

Support this project by becoming a backer. Your avatar will show up here.

[![Backers](https://opencollective.com/doks/tiers/backer.svg)](https://opencollective.com/doks)
