# libraries
import os
import glob

# placeholder
html_files = []

# get html files
files = glob.glob('docs/*')
for f in files:
    if os.path.basename(f).endswith('.html'):
        html_files.append(f)

# only keep chapters
html_files.remove('docs/index.html')
html_files.sort()

# set counter
cnt = 0

# loop html files: fix headers, fix individual TOC entries
for htmlf in html_files:

    # initialise template
    with open(htmlf) as file:
      html_content = file.read()

    # update headers
    html_content = html_content.replace('<span class="header-section-number">1', \
                                        '<span class="header-section-number">' + str(0 + cnt))
    
    # update counter
    cnt += 1
    
    # update TOC chapter 1
    html_content = html_content.replace('<span class="menu-text">Data Preparation</span>', \
                                        '<span class="menu-text">1 Data Preparation</span>')
    # update TOC chapter 2
    html_content = html_content.replace('<span class="menu-text">Data Mapping</span>', \
                                        '<span class="menu-text">2 Data Mapping</span>')
    # update TOC chapter 3
    html_content = html_content.replace('<span class="menu-text">Worksheet</span>', \
                                        '<span class="menu-text">3 Worksheet</span>')
    
    with open(htmlf, 'w') as file:
        file.write(html_content)
