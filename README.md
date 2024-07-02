
Welcome to this incredibly versatile and potentially under-engineered project. If you've ever wanted to tweak, twist, or tinker with something until it either becomes something magnificent or breaks spectacularly, you're in the right place!

## Credits and Acknowledgments

Special thanks to:

- **[Tufte CSS](https://github.com/edwardtufte/tufte-css)**: For the elegant and practical CSS inspired by Edward Tufte’s principles of information design. The aesthetic of this project owes much to these styles.
- **[Hugo](https://gohugo.io/)**: As the powerful and flexible static site generator that brings this project to life, Hugo's speed and efficiency are indispensable.
- **[Hugo Bearblog](https://themes.gohugo.io/themes/hugo-bearblog/)**: For inspiration in minimalist design and functionality, which has greatly influenced the development of this project.
- [jqMath](https://mathscribe.com/author/jqmath.html): For Math support.
- **ChatGPT 4, Claude 3.5 Sonnet**
- As of now, please use external tools like Graphviz or D2lang for generating diagrams and embed as a image file. Hugo has no inbuilt support for diagram libs such as Mermaid. Of course, you can download any min.js and link it to the header html.

Each of these projects represents significant efforts by their contributors and maintainers. Feel free to explore the linked resources to learn more about these projects and perhaps incorporate some of their ideas into your own work.


## Usage

### Installation and Updates: Quick Start

1. **Download the Theme**:
   - Navigate to the [theme repository](https://github.com/shashankpritam/hugo-tufte/tree/main).
   - Click on the `Code` button and select "Download ZIP".
   - Extract the ZIP file and place the folder in the `themes` directory of your Hugo site.

2. **Configure Your Site**:
   - Open your `hugo.toml` file and ensure it is configured to use the theme. Here’s a basic example of what the configuration might look like:

   ```toml
   baseURL = 'https://yourdomain.com'
   languageCode = 'en-us'
   title = 'My Blog'
   theme = 'hugo-tufte'
   ```

   - Replace the `baseURL`, `title`, and other settings as necessary to match your site’s details.

### Keeping Your Theme Updated

If you want to keep your theme up to date with the latest changes, consider using a Git submodule. This allows you to easily update the theme by pulling in the latest changes from the source repository.

- **Add the Theme as a Submodule**:

  ```bash
  git submodule add https://github.com/shashankpritam/hugo-tufte.git themes/hugo-tufte
  git submodule update --init --recursive
  ```

- **Update the Theme**:

  When updates are made to the original theme, you can update your theme submodule using:

  ```bash
  git submodule update --remote --merge
  ```

This method ensures that your theme stays up-to-date with any improvements or bug fixes made to the source theme.

### Features:

- **Math Support**: Includes built-in support for rendering mathematical expressions thanks to jqMath.
- **Diagram Support via Mermaid**: Just add the necessary Mermaid JS link in `custom_head.html` to enable beautiful diagram visualizations.
- **Extended Shortcodes**: Utilize shortcodes for side lists, side tables, side images, side citations, and even side dishes (metaphorically speaking).

---

Feel free to use, modify, and run this project wherever and however you see fit. Whether you're powering a small blog or launching it on a toaster to run Doom, the sky's the limit (though not legally binding). No credit is required, wanted, or cared about—live your best anonymous life!

**Note**: Yes, there are redundancies, and I'll attempt to address these. Feel free to submit a PR if you have improvements or fixes to suggest.

Here’s how the ideal `hugo.toml` should look to work seamlessly with this theme:

```toml
baseURL = 'https://yourprecious.site'
languageCode = 'en-us'
title = 'Fanstastic Title'
theme = 'hugo-tufte'

[markup]
  [markup.highlight]
    codeFences = true          # Enables or disables code fencing
    guessSyntax = false        # Disables automatic guessing of the code syntax
    hl_Lines = ""              # No specific lines are highlighted
    lineNoStart = 1            # Starting line number for code blocks
    lineNos = true             # Enable line numbers to be shown next to the code blocks
    lineNumbersInTable = false # Disable line numbers within tables to reduce clutter
    noClasses = true           # Enables classes for styling with CSS
    style = "rose-pine"        # Sets the syntax highlight style
    tabWidth = 4               # Sets the width of tabs in spaces

[menu]
  [[menu.main]]
    name = "Blog"
    url = "/blog/"
    weight = 2
  [[menu.main]]
    name = "Current"
    url = "/current/"
    weight = 3
```


## License

This project is released under the MIT License, which means you can do pretty much anything you want with it, except claim you wrote it yourself. Here’s the gist of it:

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Finally

If you find this project helpful, a nod, wink, or tip of the hat is appreciated but not required. If it breaks, remember – it’s not a bug, it’s a feature!


