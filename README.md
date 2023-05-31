 [![](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo/-/jobs/artifacts/dev/raw/nodes.svg?job=dynamic_badge)]()
 [![](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo/-/jobs/artifacts/dev/raw/edges.svg?job=dynamic_badge)]()
 [![](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo/-/jobs/artifacts/dev/raw/podcasts.svg?job=dynamic_badge)]()

# Pontifex = pntfx

This repo contains the essential Python and Bash scripts to build the Pontifex project.
It also provides all teaching and learning material used in the instance running on the domain [pntfx.com](https://pntfx.com) licensed under [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/).

# Terms of Use

The software pntfx is licensed under MIT.

If you use pntfx for visualization of your network, please add the following text to your application:

> The data for the interactive network on this webpage was generated with pntfx Copyright Fabian Gabel and Julian Großmann. pntfx is licensed under the MIT license. Visualization of the network uses the open-source graph theory library Cytoscape.js licensed under the MIT license.


# Getting Started

> If you want to kick-start your own project with Pontifex and HUGO

## Kick-start your own application on GitHub

* **Import project**: visit https://github.com/new/import and paste the URL `https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo.git`
* Choose a *Repository Name*, e.g. `my-pntfx-project` and set the privacy/visibility settings to `public`
* **Enable GitHub Actions**: visit the [repository settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) to manage the repository actions (*Code and automatization/Actions/General* and check the boxes next to 
  * *Allow all actions and reusable workflows* and 
  * *Read and write permissions*.
* **Trigger the GitHub Action**: every change in your repository files should trigger the action `github-pages`. Visit your repository environments list to find out about the deployment status of your project. Make a small change to one of the files in order to start the GitHub action.
* In *Settings/Code and automatization* go to *Pages* , select *Deploy from a branch*, and the branch `gh-pages` with `/root` and save
* Once the GitHub-Action has finished, visit the page `https://your-github-username.github.io/pontifex/` to explore your Pontifex application.

For details on the implementation, checkout the GitHub workflow in the file `.github/workflows/gh-pages.yml`. See also the [Doks documentation](https://getdoks.org/docs/how-to/hosting/deployment/).

## Modifying the content

### Graph database

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
      "exercise": "quiz.html",
      "podcast": "Click <a href=\"https://anchor.fm/profmoppi/Setsepisodes/--Relations--and-Mappings-e193jss/a-a6knu04\" target=\"_blank\">here</a> or on the thumbnail to open up a podcast episode in a separate tab!<a href=\"https://anchor.fm/profmoppi/episodes/Sets--Relations--and-Mappings-e193jss/a-a6knu04\" target=\"_blank\"><img src=\"./well-defined-and-wonderful.jpg\"></a><p>Courtesy of Marcus Waurick. <i>Well-defined & Wonderful podcast</i>, <a href=\"https://www.marcus-waurick.de/teaching\" target=\"_blank\">marcus-waurick.de</a>.</p>"
    }
```

This entry describes the concept node `305` for the concept "Epsilon-Delta Definition"

* `id` should be a unique three-digit number. The first digit specifies the chapter (0-9). The second and third digits run from `00` to `99`. The `id` identifies the node and is also used for defining the edges.
* `label` is the text used as title of the node. It will show as the title of the corresponding webpage and as label of the node in the graph
* `meta` contains further information for the content. In the above example, it specifies the name of the video; no routine processes this text, so one can use the entry to store further info.
* `content` explains the topic; this text shows on the top of each webpage below the title
* `notes` name of the html file containing the lecture notes.
* `video` ID (+ optional timestamp) of the YouTube video that should be linked. Can be used to either embed the video via an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) or for an external link (currently implemented).
* `webwork` link to [WeBWorK](https://github.com/openWeBWorK) exercise or other webpage that will be embedded via an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe). 
* `exercise` html file (with javascript) for a quiz about the video (can be used additionally to WeBWorK or as a substitution). It will also be embedded via an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe). 
* `podcast` plain html code to go in the *Podcast* section.
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

### Node content

During the creation of the website, each node automatically gets it's own standardized [Markdown](https://www.markdownguide.org/) page `xxx.md`.
The template for this page can be found in the file `nodes/dummy_for_hugo.md`.
This file encodes the overall structure of the content page for a node. A change in the template will affect all node pages simultaneously once the webpage has been rebuilt.
The template uses certain marker-words that are replaced with specific counterparts during the build process. In particular, the information from the `JSON` database will be filled in.
In the following, we describe which data needs to be provided in order to start building the webpage.

#### TeX snippets

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

##### Including Images

We recommend using vector graphics like `.svg`. If your code contains TiKz, we recommend to use the `standalone` package in order to create an `.svg`-file.

In order to include the image `image.svg` in the node `107`, inside the file `107/107.tex` use the code
```latex
\includegraphics{./image.svg}
```
and place `image.svg` also in the `107` folder.

###### Using HUGO Shortcodes

HUGO Shortcodes work inside `.tex` files due to the `sed`-postprocessing
```bash
sed -i -e 's/{{&lt; baseurl &gt;}}/{{< baseurl >}}/g' $i/$i-snippet.html
```
inside `build_pontifex.sh`.

#### YouTube videos

##### Thumbnails and External Links

In order to cope with internet privacy requirements, the current version of Pontifex does not embed YouTube Videos but external links. This is realized the file `nodes/dummy_for_hugo.md` via the snippet
```html
Click [here](https://youtu.be/###YTURLEND###) or on the thumbnail below to open up the YouTube video in a separate tab!
<a href="https://youtu.be/###YTURLEND###" target="_blank">
  <img src="./###YTID###.jpg">
</a>
```
In order to keep using this snippet for other YouTube videos, the corresponding thumbnail needs to be saved in the folder `nodes/xxx`, where `xxx` corresponds to the node id.
The thumbnail name should be `ytid.jpg`, where `ytid` is the YouTube-Id of the corresponding video, e.g., the video `https://youtu.be/iA-Dtf7529M` has the id `iA-Dtf7529M`.
In order to appropriately download and save the thumbnails, you may use the script `bin/get_thumbnails.py`.

##### YouTube shortcode

Alternatively, you can include YouTube Videos via the `youtube` [shortcode](https://gohugo.io/content-management/shortcodes/). 
Here the URL specified in the `video` attribute of the `JSON` database is used, starting from `/embed/...`.
See [here](https://support.google.com/youtube/answer/171780?hl=en) for more information on embedding YouTube videos.
In order to use the `youtube` shortcode, in the file `nodes/dummy_for_hugo.md`, you need to substitute the paragraph
```html
###VIDEO###
```
by
```
{{< tab tabName="Video">}}
{{< youtube "###YTURLEND###">}}
{{< /tab >}}
```

#### Podcast episodes

This section is optional and will only be processed when the `podcast` attribute in the `JSON` database is nonempty. 
En empty entry looks like
```JSON
      "podcast": ""
```

If "podcast" is nonempty, the full `HTML`-content will by copied to the corresponding section in the template.
The original version of Pontifex uses either `<iframe>` code provided by the podcast hosters, e.g. [AnchorFM](https://anchor.fm/), 
```html
      "podcast": "<iframe src=\"https://anchor.fm/profmoppi/embed/episodes/Rearrangement-of-Series-with-Fabian-Gabel-e1iq2sr/a-a7vb2vp\" height=\"102px\" width=\"100%\" frameborder=\"0\" scrolling=\"no\"></iframe><p>Courtesy of Marcus Waurick. <i>Well-defined & Wonderful podcast</i>, <a href=\"https://www.marcus-waurick.de/teaching\">marcus-waurick.de</a>.</p>"
```
or provides short snippets to include content that has been copied to the server.
```html
      "podcast": "<audio controls src=\"/e-10/pontifex/podcast/imvt.mp3\">Your browser does not support the <code>audio</code> element.</audio>"},
```

#### Discussion forum

The current version of Pontifex uses a discussion tab on each webpage.
Each discussion features a GitHub-Like discussion thread provided by [Vssue](https://vssue.js.org/).
In order to enable Vssue on your own instance of Pontifex, follow the following steps
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

#### WeBWorK or other electronic exercises

The bottom of each page includes an electronic [WeBWorK](https://github.com/openwebwork/) exercise in the form of an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe).
```json
"webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=Library/Berkeley/StewCalcET7e/2.4/2-4-03.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
```
will render the exercise once the webpage has been loaded.

Details on the WeBWorK course creation can be found [here](https://michaelgage.blogspot.com/2015/06/whether-writing-full-text-book-or-just.html).

The problemSeed is randomized via JavaScript+RegEx and will change everytime the page is reloaded, see `/layouts/shortcodes/webwork.html` for details.

##### Pontifex-Coloring in WeBWorK Buttons

To this end use the CSS-theme `nodes/math4-pontifex-coloring.css` and include it in your WeBWorK-Service.

## Adding Branding to your pntfx Project

In order to add a university or institute logo, just overwrite the files

`/static/images/university-logo.svg` and `/static/images/institute-logo.svg`

or use a separate repository for branding your project as described in the developer info below.

# Developer info

## Python preprocessing

`*.py` files in `bin`-folder:

| Preprocessor | Description |
| - | - |
| `build_json.py` | Build `JSON` file for each node containing only neighbors of distance 1 |
| `build_md.py` | Build `MD` file for each node substituting placeholders by node-specific values |

## Build process

In order to build the HUGO project, the Bash-script `/bin/build_pontifex.sh` needs to be executed. 
The build process consists of 3 parts: 
1) Preprocessing using the Python scripts and [`pandoc`](https://pandoc.org/).
2) Copying the files to their location to be picked up by HUGO.
3) Running HUGO to create the static webpage. The resulting files are then located in the folder `public`.

## Cytoscape.js

We rely on [Cytoscape.js](https://js.cytoscape.org/) in order to visualize the graph.

Colors and functionality of the graph are encoded in the files
`static/js/vendor/pontifex-graph.js`

Each page using a Cytoscape.js graph needs to include a specific `header1.html` page. See the shortcode below.

## Pandoc

Translation of `TeX` to `HTML` with MathJax support is achieved with [`pandoc`](https://pandoc.org/).
If building the Pontifex project locally without the use of the provided Docker container make sure to have a `pandoc` version >= 2.18.

## Node

The HUGO project is built using [Node.js](https://nodejs.org/en/).
If building the Pontifex project locally without the use of the provided Docker container make sure to have a `node` version >= 18.5.

## Dummies, templates, and shortcodes

`nodes/dummy_for_hugo.md` specifies the overall structure of each page.
We use special shortcodes for including WeBWorK exercises and Tabs, see `layouts/shortcodes/` for details.

### `header1`

This  is needed for the Cytoscape.js objects to function properly. 
The syntax is `{{< header1 "index">}}` where `index` specifies the id of the node and will be used in order to load the node-specific `JSON`-file.

### `header2`

Same as `header1` but this is used only on for the overview page and not in `dummy_for_hugo.md`

### `plausible`

In order to enable [plausible.io](https://plausible.io/), every page that needs web analytics should include `layouts/partials/header/plausible.html` via
```html
{{ partial "header/plausible.html" }}
```
The unbranded version of Pontifex uses an empty file. In order to use your plausible data, change the file content to
```html
<script defer data-domain="your-domain.com" src="https://plausible.io/js/plausible.js"></script>
```
see, the [Plausible Documentation](https://plausible.io/docs/) for details on registration and implementation on your webpage.

## Branding 

All files that apply some sort of branding reside in the **private** repository

https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-brand

Content is copied to their respective locations in the `.gitlab-ci.yml`-stage: `brand`.

As `pontifex-brand` is private, the repo `pontifex-hugo` needs to have an *access token* in the pipeline variables in order to clone `pontifex-brand`. The presently used token was generated within `pontifex-brand`/Settings/Access Tokens with `read repository` scope and added to `pontifex-hugo` as the pipeline variable `PROJECT_TOKEN`.

## Development environment using Docker

Download or clone `pontifex-hugo` first
```bash
git clone git@collaborating.tuhh.de:hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo.git
```
Follow the instructions on https://docs.docker.com/get-docker/ to install Docker on your machine.
Note that the process below for building the Pontifex project needs to be repeated each time you modify the source files of your webpage.

### Building the Docker image locally and building the HUGO project

Within a git-clone of [`pontifex-hugo`](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo) run 
```bash
docker build . -t pontifex-hugo
```
This process should also be carried out every time, an update of `pontifex-hugo/Dockerfile` is carried out.

Now, run 
```bash
docker run -it --rm -v `pwd`:/app -w /app pontifex-hugo ./bin/build_pontifex.sh
```
to build the project.

### Building the HUGO project with an external Docker image

Within a git-clone of [`pontifex-hugo`](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo), run
```bash
docker run -it --rm -v `pwd`:/app -w /app collaborating.tuhh.de:5005/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo:latest ./bin/build_pontifex.sh
```

This will use the root image from the [Container Registry](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo/container_registry/).

You may need to
```
docker login collaborating.tuhh.de:5005
```
and authenticate first. Note that, the first time you `docker run` the above command, it may take longer as the image needs to be downloaded first.

### Starting a web server

If your build process was successful, you find all files to be hosted in the folder `public`.
Within your `pontifex-hugo` folder, you may start up a web server via
```
docker run -it --rm --name apache-server -p 8080:80 -v `pwd`/public:/usr/local/apache2/htdocs/ httpd:2.4-alpine
```
and open up http://localhost:8080/ in order to view the Pontifex webpage on your machine.

## Further configuration

### Darkmode

HUGO-Doks comes with a darkmode capability that has been disabled in order to prevent the usage of local storage on the client side. In order to activate the darkmode adapt the file `config/_default/params.toml` to read
```toml
darkMode = true
```

### Push Mirroring to GitHub

The protected branches `master` and `dev` are [push mirrored](https://docs.gitlab.com/ee/user/project/repository/mirror/push.html) to the GitHub repository: https://github.com/HOOU-TUHH/Pontifex-Hugo.

To this end, this repo uses password authentication with a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub using the *repo* and *workflow* scope.


# Contributors

In alphabetical order.

* [Axel Dürkop](https://collaborating.tuhh.de/hoou-an-der-tuhh-projekte/pontifex/pontifex-hugo/-/commits/dev?author=Axel%20D%C3%BCrkop) (C2A Overlay, Embedding of Vssues)
* Katja Eberhage (Landing Page Design)
* Fabian Gabel
* Julian Großmann

---
[Here](https://github.com/h-enk/doks) is the original documentation for the HUGO theme used by pntfx.
