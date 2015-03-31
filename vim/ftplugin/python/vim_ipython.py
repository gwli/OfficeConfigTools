


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>vim-ipython/vim_ipython.py at master · ivanov/vim-ipython · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="ivanov/vim-ipython" name="twitter:title" /><meta content="vim-ipython - A two-way integration between Vim and IPython 0.11+" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/118211?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/118211?v=3&amp;s=400" property="og:image" /><meta content="ivanov/vim-ipython" property="og:title" /><meta content="https://github.com/ivanov/vim-ipython" property="og:url" /><meta content="vim-ipython - A two-way integration between Vim and IPython 0.11+" property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="CB123204:63F9:7EE5A9:551A6D94" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged Out">
    <meta class="js-ga-set" name="dimension2" content="Header v3">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="Z+ntrzE3cfD6lIW1sC/FmCuZlia+DSlYzdWKcGW7zAq470D9RIYVBl8Id8dkAjn+0BqEhuJsnkkt7pZ1H/+RwQ==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-391b32dc1132ef0837cee6b206cad9c2726c7f495e5047901a7afa551e81d695.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-14b629a12b237ffde72fb70f31de6a515754f0f686189a072cc00e54ee202fd1.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="0cdf73d6f5d84ba34af332a36c975c0a">

      
  <meta name="description" content="vim-ipython - A two-way integration between Vim and IPython 0.11+">
  <meta name="go-import" content="github.com/ivanov/vim-ipython git https://github.com/ivanov/vim-ipython.git">

  <meta content="118211" name="octolytics-dimension-user_id" /><meta content="ivanov" name="octolytics-dimension-user_login" /><meta content="2122256" name="octolytics-dimension-repository_id" /><meta content="ivanov/vim-ipython" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="2122256" name="octolytics-dimension-repository_network_root_id" /><meta content="ivanov/vim-ipython" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/ivanov/vim-ipython/commits/master.atom" rel="alternate" title="Recent Commits to vim-ipython:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        
        <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions" role="navigation">
        <a class="btn btn-primary" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      <a class="btn" href="/login?return_to=%2Fivanov%2Fvim-ipython%2Fblob%2Fmaster%2Fftplugin%2Fpython%2Fvim_ipython.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search repo-scope js-site-search" role="search">
      <form accept-charset="UTF-8" action="/ivanov/vim-ipython/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/ivanov/vim-ipython/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
    </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/features" data-ga-click="(Logged out) Header, go to features, text:features">Features</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://enterprise.github.com/" data-ga-click="(Logged out) Header, go to enterprise, text:enterprise">Enterprise</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="(Logged out) Header, go to blog, text:blog">Blog</a>
          </li>
      </ul>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2Fivanov%2Fvim-ipython"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <span class="octicon octicon-eye"></span>
    Watch
  </a>
  <a class="social-count" href="/ivanov/vim-ipython/watchers">
    48
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fivanov%2Fvim-ipython"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/ivanov/vim-ipython/stargazers">
      595
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fivanov%2Fvim-ipython"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/ivanov/vim-ipython/network" class="social-count">
        79
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/ivanov" class="url fn" itemprop="url" rel="author"><span itemprop="title">ivanov</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/ivanov/vim-ipython" class="js-current-repository" data-pjax="#js-repo-pjax-container">vim-ipython</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/ivanov/vim-ipython/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/ivanov/vim-ipython" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /ivanov/vim-ipython">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/ivanov/vim-ipython/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /ivanov/vim-ipython/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/ivanov/vim-ipython/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /ivanov/vim-ipython/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/ivanov/vim-ipython/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /ivanov/vim-ipython/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/ivanov/vim-ipython/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /ivanov/vim-ipython/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/ivanov/vim-ipython.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/ivanov/vim-ipython" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a> or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/ivanov/vim-ipython/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of ivanov/vim-ipython as a zip file"
                   title="Download the contents of ivanov/vim-ipython as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/ivanov/vim-ipython/blob/a47d92b371588a81f8501c66604d79e2827c60a8/ftplugin/python/vim_ipython.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:e84c5b4361bd419191e30cc1dfc5157a -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ivanov/vim-ipython/blob/kernel-interupt/ftplugin/python/vim_ipython.py"
               data-name="kernel-interupt"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="kernel-interupt">
                kernel-interupt
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/ivanov/vim-ipython/blob/master/ftplugin/python/vim_ipython.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ivanov/vim-ipython/blob/notebook-io/ftplugin/python/vim_ipython.py"
               data-name="notebook-io"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="notebook-io">
                notebook-io
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ivanov/vim-ipython/blob/vader/ftplugin/python/vim_ipython.py"
               data-name="vader"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="vader">
                vader
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/ivanov/vim-ipython/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ivanov/vim-ipython" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">vim-ipython</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ivanov/vim-ipython/tree/master/ftplugin" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">ftplugin</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ivanov/vim-ipython/tree/master/ftplugin/python" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">python</span></a></span><span class="separator">/</span><strong class="final-path">vim_ipython.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@ivanov" class="avatar" data-user="118211" height="24" src="https://avatars0.githubusercontent.com/u/118211?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/ivanov" rel="author">ivanov</a></span>
        <time datetime="2014-07-17T23:17:51Z" is="relative-time">Jul 17, 2014</time>
        <div class="commit-title">
            <a href="/ivanov/vim-ipython/commit/cf545308c9a6e13a4889d12020e12285fae6cea4" class="message" data-pjax="true" title="use KernelManager for starting a new kernel">use KernelManager for starting a new kernel</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>2</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="ivanov" href="/ivanov/vim-ipython/commits/master/ftplugin/python/vim_ipython.py?author=ivanov"><img alt="@ivanov" class="avatar" data-user="118211" height="20" src="https://avatars2.githubusercontent.com/u/118211?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="luispedro" href="/ivanov/vim-ipython/commits/master/ftplugin/python/vim_ipython.py?author=luispedro"><img alt="@luispedro" class="avatar" data-user="79334" height="20" src="https://avatars1.githubusercontent.com/u/79334?v=3&amp;s=40" width="20" /> </a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@ivanov" data-user="118211" height="24" src="https://avatars0.githubusercontent.com/u/118211?v=3&amp;s=48" width="24" />
            <a href="/ivanov">ivanov</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@luispedro" data-user="79334" height="24" src="https://avatars3.githubusercontent.com/u/79334?v=3&amp;s=48" width="24" />
            <a href="/luispedro">luispedro</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/ivanov/vim-ipython/raw/master/ftplugin/python/vim_ipython.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/ivanov/vim-ipython/blame/master/ftplugin/python/vim_ipython.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/ivanov/vim-ipython/commits/master/ftplugin/python/vim_ipython.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>


          <button type="button" class="octicon-btn disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
            <span class="octicon octicon-pencil"></span>
          </button>

        <button type="button" class="octicon-btn octicon-btn-danger disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </button>
    </div>

    <div class="file-info">
        646 lines (584 sloc)
        <span class="file-info-divider"></span>
      24.692 kb
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line">reselect <span class="pl-k">=</span> <span class="pl-c1">False</span>            <span class="pl-c"># reselect lines after sending from Visual mode</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line">show_execution_count <span class="pl-k">=</span> <span class="pl-c1">True</span> <span class="pl-c"># wait to get numbers for In[43]: feedback?</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line">monitor_subchannel <span class="pl-k">=</span> <span class="pl-c1">True</span>   <span class="pl-c"># update vim-ipython &#39;shell&#39; on every send?</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line">run_flags<span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-i<span class="pl-pds">&quot;</span></span>             <span class="pl-c"># flags to for IPython&#39;s run magic when using &lt;F5&gt;</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line">current_line <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">    <span class="pl-k">from</span> queue <span class="pl-k">import</span> Empty <span class="pl-c"># python3 convention</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">    <span class="pl-k">from</span> Queue <span class="pl-k">import</span> Empty</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">    <span class="pl-k">import</span> vim</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">    <span class="pl-k">class</span> <span class="pl-en">NoOp</span>(<span class="pl-e"><span class="pl-c1">object</span></span>):</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">        <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__getattribute__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">key</span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">            <span class="pl-k">return</span> <span class="pl-k">lambda</span> *<span class="pl-smi">args</span>: <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">    vim <span class="pl-k">=</span> NoOp()</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>uh oh, not running inside vim<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line"><span class="pl-c"># get around unicode problems when interfacing with vim</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line">vim_encoding<span class="pl-k">=</span>vim.eval(<span class="pl-s"><span class="pl-pds">&#39;</span>&amp;encoding<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">    sys.stdout.flush</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line"><span class="pl-k">except</span> <span class="pl-c1">AttributeError</span>:</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">    <span class="pl-c"># IPython complains if stderr and stdout don&#39;t have flush</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">    <span class="pl-c"># this is fixed in newer version of Vim</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">    <span class="pl-k">class</span> <span class="pl-en">WithFlush</span>(<span class="pl-e"><span class="pl-c1">object</span></span>):</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line">        <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>,<span class="pl-smi">noflush</span>):</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">            <span class="pl-v">self</span>.write<span class="pl-k">=</span>noflush.write</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">            <span class="pl-v">self</span>.writelines<span class="pl-k">=</span>noflush.writelines</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">        <span class="pl-k">def</span> <span class="pl-en">flush</span>(<span class="pl-smi">self</span>):<span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">    sys.stdout <span class="pl-k">=</span> WithFlush(sys.stdout)</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">    sys.stderr <span class="pl-k">=</span> WithFlush(sys.stderr)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">vim_variable</span>(<span class="pl-smi">name</span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">    exists <span class="pl-k">=</span> <span class="pl-c1">int</span>(vim.eval(<span class="pl-s"><span class="pl-pds">&quot;</span>exists(&#39;<span class="pl-c1">%s</span>&#39;)<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> name))</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">    <span class="pl-k">return</span> vim.eval(name) <span class="pl-k">if</span> exists <span class="pl-k">else</span> default</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line"> </td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">vim_regex_escape</span>(<span class="pl-smi">x</span>):</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">    <span class="pl-k">for</span> old, new <span class="pl-k">in</span> ((<span class="pl-s"><span class="pl-pds">&quot;</span>[<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>[<span class="pl-pds">&quot;</span></span>), (<span class="pl-s"><span class="pl-pds">&quot;</span>]<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>]<span class="pl-pds">&quot;</span></span>), (<span class="pl-s"><span class="pl-pds">&quot;</span>:<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>:<span class="pl-pds">&quot;</span></span>), (<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>\.<span class="pl-pds">&quot;</span></span>), (<span class="pl-s"><span class="pl-pds">&quot;</span>*<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span>*<span class="pl-pds">&quot;</span></span>)):</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">        x <span class="pl-k">=</span> x.replace(old, new)</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">    <span class="pl-k">return</span> x</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line"><span class="pl-c"># status buffer settings</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">status_prompt_in <span class="pl-k">=</span> vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_in<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>In [<span class="pl-c1">%(line)d</span>]: <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">status_prompt_out <span class="pl-k">=</span> vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_out<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Out[<span class="pl-c1">%(line)d</span>]: <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">status_prompt_colors <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>in_ctermfg<span class="pl-pds">&#39;</span></span>: vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_in_console_color<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Green<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>in_guifg<span class="pl-pds">&#39;</span></span>: vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_in_gui_color<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Green<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>out_ctermfg<span class="pl-pds">&#39;</span></span>: vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_out_console_color<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Red<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>out_guifg<span class="pl-pds">&#39;</span></span>: vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_out_gui_color<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Red<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>out2_ctermfg<span class="pl-pds">&#39;</span></span>: vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_out2_console_color<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Gray<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>out2_guifg<span class="pl-pds">&#39;</span></span>: vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_out2_gui_color<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Gray<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">}</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">status_blank_lines <span class="pl-k">=</span> <span class="pl-c1">int</span>(vim_variable(<span class="pl-s"><span class="pl-pds">&#39;</span>g:ipy_status_blank_lines<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">ip <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>127.0.0.1<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line"><span class="pl-c"># this allows us to load vim_ipython multiple times</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">    km</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">    kc</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">    pid</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line"><span class="pl-k">except</span> <span class="pl-c1">NameError</span>:</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">    km <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">    kc <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line">    pid <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">_install_instructions <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>You *must* install IPython into the Python that</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line"><span class="pl-s">your vim is linked against. If you are seeing this message, this usually means</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line"><span class="pl-s">either (1) installing IPython using the system Python that vim is using, or</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line"><span class="pl-s">(2) recompiling Vim against the Python where you already have IPython</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line"><span class="pl-s">installed. This is only a requirement to allow Vim to speak with an IPython</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line"><span class="pl-s">instance using IPython&#39;s own machinery. It does *not* mean that the IPython</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line"><span class="pl-s">instance with which you communicate via vim-ipython needs to be running the</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line"><span class="pl-s">same version of Python.</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">new_ipy</span>(<span class="pl-smi">s</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Create a new IPython kernel (optionally with extra arguments)</span></td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line"><span class="pl-s">    XXX: Allow passing of profile information here</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line"><span class="pl-s">    Examples</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line"><span class="pl-s">    --------</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line"><span class="pl-s">        new_ipy()</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line">    <span class="pl-k">from</span> IPython.kernel <span class="pl-k">import</span> KernelManager</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line">    km <span class="pl-k">=</span> KernelManager()</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line">    km.start_kernel()</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line">    <span class="pl-k">return</span> km_from_string(km.connection_file)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">km_from_string</span>(<span class="pl-smi">s</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>create kernel manager from IPKernelApp string</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line"><span class="pl-s">    such as &#39;--shell=47378 --iopub=39859 --stdin=36778 --hb=52668&#39; for IPython 0.11</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line"><span class="pl-s">    or just &#39;kernel-12345.json&#39; for IPython 0.12</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line">        <span class="pl-k">import</span> IPython</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line">        <span class="pl-k">raise</span> <span class="pl-c1">ImportError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Could not find IPython. <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> _install_instructions)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line">    <span class="pl-k">from</span> IPython.config.loader <span class="pl-k">import</span> KeyValueConfigLoader</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line">        <span class="pl-k">from</span> IPython.kernel <span class="pl-k">import</span> (</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line">            KernelManager,</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">            find_connection_file,</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">        <span class="pl-c">#  IPython &lt; 1.0</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">        <span class="pl-k">from</span> IPython.zmq.blockingkernelmanager <span class="pl-k">import</span> BlockingKernelManager <span class="pl-k">as</span> KernelManager</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line">        <span class="pl-k">from</span> IPython.zmq.kernelapp <span class="pl-k">import</span> kernel_aliases</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line">            <span class="pl-k">from</span> IPython.lib.kernel <span class="pl-k">import</span> find_connection_file</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line">            <span class="pl-c"># &lt; 0.12, no find_connection_file</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">    <span class="pl-k">global</span> km, kc, send</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line">    s <span class="pl-k">=</span> s.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>--existing<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>connection_file<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> KernelManager.class_trait_names():</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line">        <span class="pl-c"># 0.12 uses files instead of a collection of ports</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line">        <span class="pl-c"># include default IPython search path</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">        <span class="pl-c"># filefind also allows for absolute paths, in which case the search</span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line">        <span class="pl-c"># is ignored</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line">            <span class="pl-c"># XXX: the following approach will be brittle, depending on what</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">            <span class="pl-c"># connection strings will end up looking like in the future, and</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">            <span class="pl-c"># whether or not they are allowed to have spaces. I&#39;ll have to sync</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">            <span class="pl-c"># up with the IPython team to address these issues -pi</span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>--profile<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">                k,p <span class="pl-k">=</span> s.split(<span class="pl-s"><span class="pl-pds">&#39;</span>--profile<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">                k <span class="pl-k">=</span> k.lstrip().rstrip() <span class="pl-c"># kernel part of the string</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">                p <span class="pl-k">=</span> p.lstrip().rstrip() <span class="pl-c"># profile part of the string</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">                fullpath <span class="pl-k">=</span> find_connection_file(k,p)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line">                fullpath <span class="pl-k">=</span> find_connection_file(s.lstrip().rstrip())</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">IOError</span> <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>:IPython <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> failed<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Info<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>^-- failed &#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>&#39; not found<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Error<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code js-file-line">        km <span class="pl-k">=</span> KernelManager(<span class="pl-smi">connection_file</span> <span class="pl-k">=</span> fullpath)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code js-file-line">        km.load_connection_file()</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code js-file-line">        <span class="pl-k">if</span> s <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>:IPython 0.11 requires the full connection string<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code js-file-line">        loader <span class="pl-k">=</span> KeyValueConfigLoader(s.split(), <span class="pl-smi">aliases</span><span class="pl-k">=</span>kernel_aliases)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code js-file-line">        cfg <span class="pl-k">=</span> loader.load_config()[<span class="pl-s"><span class="pl-pds">&#39;</span>KernelApp<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code js-file-line">            km <span class="pl-k">=</span> KernelManager(</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code js-file-line">                <span class="pl-smi">shell_address</span><span class="pl-k">=</span>(ip, cfg[<span class="pl-s"><span class="pl-pds">&#39;</span>shell_port<span class="pl-pds">&#39;</span></span>]),</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code js-file-line">                <span class="pl-smi">sub_address</span><span class="pl-k">=</span>(ip, cfg[<span class="pl-s"><span class="pl-pds">&#39;</span>iopub_port<span class="pl-pds">&#39;</span></span>]),</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code js-file-line">                <span class="pl-smi">stdin_address</span><span class="pl-k">=</span>(ip, cfg[<span class="pl-s"><span class="pl-pds">&#39;</span>stdin_port<span class="pl-pds">&#39;</span></span>]),</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code js-file-line">                <span class="pl-smi">hb_address</span><span class="pl-k">=</span>(ip, cfg[<span class="pl-s"><span class="pl-pds">&#39;</span>hb_port<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">KeyError</span> <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>:IPython <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span>s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> failed<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Info<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>^-- failed --<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>e.message.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>_port<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span> not specified<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Error<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code js-file-line">        kc <span class="pl-k">=</span> km.client()</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">AttributeError</span>:</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code js-file-line">        <span class="pl-c"># 0.13</span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code js-file-line">        kc <span class="pl-k">=</span> km</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code js-file-line">    kc.start_channels()</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code js-file-line">    send <span class="pl-k">=</span> kc.shell_channel.execute</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code js-file-line">    <span class="pl-c">#XXX: backwards compatibility for IPython &lt; 0.13</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code js-file-line">    <span class="pl-k">import</span> inspect</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code js-file-line">    sc <span class="pl-k">=</span> kc.shell_channel</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code js-file-line">    num_oinfo_args <span class="pl-k">=</span> <span class="pl-c1">len</span>(inspect.getargspec(sc.object_info).args)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code js-file-line">    <span class="pl-k">if</span> num_oinfo_args <span class="pl-k">==</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code js-file-line">        <span class="pl-c"># patch the object_info method which used to only take one argument</span></td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code js-file-line">        klass <span class="pl-k">=</span> sc.<span class="pl-c1">__class__</span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code js-file-line">        klass._oinfo_orig <span class="pl-k">=</span> klass.object_info</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code js-file-line">        klass.object_info <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">s</span>,<span class="pl-smi">x</span>,<span class="pl-smi">y</span>: s._oinfo_orig(x)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code js-file-line">    <span class="pl-c">#XXX: backwards compatibility for IPython &lt; 1.0</span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(kc, <span class="pl-s"><span class="pl-pds">&#39;</span>iopub_channel<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code js-file-line">        kc.iopub_channel <span class="pl-k">=</span> kc.sub_channel</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code js-file-line">    <span class="pl-c"># now that we&#39;re connect to an ipython kernel, activate completion</span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code js-file-line">    <span class="pl-c"># machinery, but do so only for the local buffer if the user added the</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code js-file-line">    <span class="pl-c"># following line the vimrc:</span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code js-file-line">    <span class="pl-c">#   let g:ipy_completefunc = &#39;local&#39;</span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code js-file-line"><span class="pl-s">        if g:ipy_completefunc == &#39;global&#39;</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code js-file-line"><span class="pl-s">            set completefunc=CompleteIPython</span></td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code js-file-line"><span class="pl-s">        elseif g:ipy_completefunc == &#39;local&#39;</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code js-file-line"><span class="pl-s">            setl completefunc=CompleteIPython</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code js-file-line"><span class="pl-s">        endif</span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code js-file-line">    <span class="pl-c"># also activate GUI doc balloons if in gvim</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code js-file-line"><span class="pl-s">        if has(&#39;balloon_eval&#39;)</span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code js-file-line"><span class="pl-s">            set bexpr=IPythonBalloonExpr()</span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code js-file-line"><span class="pl-s">        endif</span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code js-file-line">    set_pid()</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code js-file-line">    <span class="pl-k">return</span> km</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">echo</span>(<span class="pl-smi">arg</span>,<span class="pl-smi">style</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Question<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>echohl <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> style)</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>echom <span class="pl-cce">\&quot;</span><span class="pl-c1">%s</span><span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> arg.replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\&quot;</span><span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span><span class="pl-cce">\&quot;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>echohl None<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code js-file-line">    <span class="pl-k">except</span> vim.error:</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code js-file-line">        <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>-- <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> arg)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">disconnect</span>():</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>disconnect kernel manager<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code js-file-line">    <span class="pl-c"># XXX: make a prompt here if this km owns the kernel</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code js-file-line">    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_doc</span>(<span class="pl-smi">word</span>, <span class="pl-smi">level</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code js-file-line">    <span class="pl-k">if</span> kc <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code js-file-line">        <span class="pl-k">return</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Not connected to IPython, cannot query: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> word]</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> kc.shell_channel.object_info(word, level)</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code js-file-line">    doc <span class="pl-k">=</span> get_doc_msg(msg_id)</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code js-file-line">    <span class="pl-c"># get around unicode problems when interfacing with vim</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code js-file-line">    <span class="pl-k">return</span> [d.encode(vim_encoding) <span class="pl-k">for</span> d <span class="pl-k">in</span> doc]</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code js-file-line"><span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code js-file-line"><span class="pl-c"># from http://serverfault.com/questions/71285/in-centos-4-4-how-can-i-strip-escape-sequences-from-a-text-file</span></td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code js-file-line">strip <span class="pl-k">=</span> re.compile(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\x1B</span>\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">strip_color_escapes</span>(<span class="pl-smi">s</span>):</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code js-file-line">    <span class="pl-k">return</span> strip.sub(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,s)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_doc_msg</span>(<span class="pl-smi">msg_id</span>):</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code js-file-line">    n <span class="pl-k">=</span> <span class="pl-c1">13</span> <span class="pl-c"># longest field name (empirically)</span></td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code js-file-line">    b<span class="pl-k">=</span>[]</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code js-file-line">        content <span class="pl-k">=</span> get_child_msg(msg_id)[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code js-file-line">    <span class="pl-k">except</span> Empty:</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code js-file-line">        <span class="pl-c"># timeout occurred</span></td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code js-file-line">        <span class="pl-k">return</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>no reply from IPython kernel<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> content[<span class="pl-s"><span class="pl-pds">&#39;</span>found<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code js-file-line">        <span class="pl-k">return</span> b</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code js-file-line">    <span class="pl-k">for</span> field <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>type_name<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>base_class<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>string_form<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>namespace<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>file<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>length<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>definition<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>source<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>docstring<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code js-file-line">        c <span class="pl-k">=</span> content.get(field,<span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code js-file-line">        <span class="pl-k">if</span> c:</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code js-file-line">            <span class="pl-k">if</span> field <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>definition<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code js-file-line">                c <span class="pl-k">=</span> strip_color_escapes(c).rstrip()</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code js-file-line">            s <span class="pl-k">=</span> field.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>).title()<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>:<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code js-file-line">            s <span class="pl-k">=</span> s.ljust(n)</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code js-file-line">            <span class="pl-k">if</span> c.find(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)<span class="pl-k">==</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code js-file-line">                b.append(s<span class="pl-k">+</span>c)</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code js-file-line">                b.append(s)</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code js-file-line">                b.extend(c.splitlines())</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code js-file-line">    <span class="pl-k">return</span> b</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_doc_buffer</span>(<span class="pl-smi">level</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code js-file-line">    <span class="pl-c"># empty string in case vim.eval return None</span></td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>let isk_save = &amp;isk<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># save iskeyword list</span></td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>let &amp;isk = &#39;@,48-57,_,192-255,.&#39;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code js-file-line">    word <span class="pl-k">=</span> vim.eval(<span class="pl-s"><span class="pl-pds">&#39;</span>expand(&quot;&lt;cword&gt;&quot;)<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>let &amp;isk = isk_save<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># restore iskeyword list</span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code js-file-line">    doc <span class="pl-k">=</span> get_doc(word, level)</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(doc) <span class="pl-k">==</span><span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code js-file-line">        echo(<span class="pl-c1">repr</span>(word)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span> not found<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Error<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code js-file-line">        <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code js-file-line">    <span class="pl-c"># documentation buffer name is same as the query made to ipython</span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>new <span class="pl-pds">&#39;</span></span><span class="pl-k">+</span>word)</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>setlocal modifiable noro<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code js-file-line">    <span class="pl-c"># doc window quick quit keys: &#39;q&#39; and &#39;escape&#39;</span></td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>nnoremap &lt;buffer&gt; q :q&lt;CR&gt;<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code js-file-line">    <span class="pl-c"># Known issue: to enable the use of arrow keys inside the terminal when</span></td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code js-file-line">    <span class="pl-c"># viewing the documentation, comment out the next line</span></td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>nnoremap &lt;buffer&gt; &lt;Esc&gt; :q&lt;CR&gt;<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code js-file-line">    <span class="pl-c"># and uncomment this line (which will work if you have a timoutlen set)</span></td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&#39;nnoremap &lt;buffer&gt; &lt;Esc&gt;&lt;Esc&gt; :q&lt;CR&gt;&#39;)</span></td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code js-file-line">    b <span class="pl-k">=</span> vim.current.buffer</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code js-file-line">    b[:] <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code js-file-line">    b[:] <span class="pl-k">=</span> doc</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>setlocal nomodified bufhidden=wipe<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&#39;setlocal previewwindow nomodifiable nomodified ro&#39;)</span></td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&#39;set previewheight=%d&#39;%len(b))# go to previous window</span></td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>resize <span class="pl-c1">%d</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-c1">len</span>(b))</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&#39;pcl&#39;)</span></td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&#39;pedit doc&#39;)</span></td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&#39;normal! &#39;) # go to previous window</span></td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code js-file-line">    <span class="pl-k">if</span> level <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code js-file-line">        <span class="pl-c"># use the ReST formatting that ships with stock vim</span></td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>setlocal syntax=rst<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code js-file-line">        <span class="pl-c"># use Python syntax highlighting</span></td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>setlocal syntax=python<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">ipy_complete</span>(<span class="pl-smi">base</span>, <span class="pl-smi">current_line</span>, <span class="pl-smi">pos</span>):</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> kc.shell_channel.complete(base, current_line, pos)</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code js-file-line">        m <span class="pl-k">=</span> get_child_msg(msg_id)</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code js-file-line">        matches <span class="pl-k">=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>matches<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code js-file-line">        matches.insert(<span class="pl-c1">0</span>,base) <span class="pl-c"># the &quot;no completion&quot; version</span></td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code js-file-line">        <span class="pl-c"># we need to be careful with unicode, because we can have unicode</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code js-file-line">        <span class="pl-c"># completions for filenames (for the %run magic, for example). So the next</span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code js-file-line">        <span class="pl-c"># line will fail on those:</span></td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code js-file-line">        <span class="pl-c">#completions= [str(u) for u in matches]</span></td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code js-file-line">        <span class="pl-c"># because str() won&#39;t work for non-ascii characters</span></td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code js-file-line">        <span class="pl-c"># and we also have problems with unicode in vim, hence the following:</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code js-file-line">        <span class="pl-k">return</span> matches</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code js-file-line">    <span class="pl-k">except</span> Empty:</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code js-file-line">        echo(<span class="pl-s"><span class="pl-pds">&quot;</span>no reply from IPython kernel<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code js-file-line">        <span class="pl-k">return</span> [<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">vim_ipython_is_open</span>():</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code js-file-line"><span class="pl-s">    Helper function to let us know if the vim-ipython shell is currently</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code js-file-line"><span class="pl-s">    visible</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code js-file-line">    <span class="pl-k">for</span> w <span class="pl-k">in</span> vim.windows:</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code js-file-line">        <span class="pl-k">if</span> w.buffer.name <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">and</span> w.buffer.name.endswith(<span class="pl-s"><span class="pl-pds">&quot;</span>vim-ipython<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">update_subchannel_msgs</span>(<span class="pl-smi">debug</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">force</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code js-file-line"><span class="pl-s">    Grab any pending messages and place them inside the vim-ipython shell.</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code js-file-line"><span class="pl-s">    This function will do nothing if the vim-ipython shell is not visible,</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code js-file-line"><span class="pl-s">    unless force=True argument is passed.</span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code js-file-line">    <span class="pl-k">if</span> kc <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">or</span> (<span class="pl-k">not</span> vim_ipython_is_open() <span class="pl-k">and</span> <span class="pl-k">not</span> force):</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code js-file-line">    msgs <span class="pl-k">=</span> kc.iopub_channel.get_msgs()</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code js-file-line">    b <span class="pl-k">=</span> vim.current.buffer</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code js-file-line">    startedin_vimipython <span class="pl-k">=</span> vim.eval(<span class="pl-s"><span class="pl-pds">&#39;</span>@%<span class="pl-pds">&#39;</span></span>)<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>vim-ipython<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> startedin_vimipython:</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code js-file-line">        <span class="pl-c"># switch to preview window</span></td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code js-file-line">        vim.command(</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>try<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>|silent! wincmd P<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>|catch /^Vim\%((<span class="pl-cce">\a</span>\+)\)\=:E441/<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>|silent pedit +set\ ma vim-ipython<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>|silent! wincmd P<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>|endtry<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code js-file-line">        <span class="pl-c"># if the current window is called &#39;vim-ipython&#39;</span></td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code js-file-line">        <span class="pl-k">if</span> vim.eval(<span class="pl-s"><span class="pl-pds">&#39;</span>@%<span class="pl-pds">&#39;</span></span>)<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>vim-ipython<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code js-file-line">            <span class="pl-c"># set the preview window height to the current height</span></td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>set pvh=<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> vim.eval(<span class="pl-s"><span class="pl-pds">&#39;</span>winheight(0)<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code js-file-line">            <span class="pl-c"># close preview window, it was something other than &#39;vim-ipython&#39;</span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>pcl<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>silent pedit +set\ ma vim-ipython<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>wincmd P<span class="pl-pds">&quot;</span></span>) <span class="pl-c">#switch to preview window</span></td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code js-file-line">            <span class="pl-c"># subchannel window quick quit key &#39;q&#39;</span></td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>nnoremap &lt;buffer&gt; q :q&lt;CR&gt;<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>set bufhidden=hide buftype=nofile ft=python<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>setlocal nobuflisted<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># don&#39;t come up in buffer lists</span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>setlocal nonumber<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># no line numbers, we have in/out nums</span></td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>setlocal noswapfile<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># no swap file (so no complaints cross-instance)</span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code js-file-line">            <span class="pl-c"># make shift-enter and control-enter in insert mode behave same as in ipython notebook</span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code js-file-line">            <span class="pl-c"># shift-enter send the current line, control-enter send the line</span></td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code js-file-line">            <span class="pl-c"># but keeps it around for further editing.</span></td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>inoremap &lt;buffer&gt; &lt;s-Enter&gt; &lt;esc&gt;dd:python run_command(&#39;&#39;&#39;&lt;C-r&gt;<span class="pl-cce">\&quot;</span>&#39;&#39;&#39;)&lt;CR&gt;i<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code js-file-line">            <span class="pl-c"># pkddA: paste, go up one line which is blank after run_command,</span></td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code js-file-line">            <span class="pl-c"># delete it, and then back to insert mode</span></td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>inoremap &lt;buffer&gt; &lt;c-Enter&gt; &lt;esc&gt;dd:python run_command(&#39;&#39;&#39;&lt;C-r&gt;<span class="pl-cce">\&quot;</span>&#39;&#39;&#39;)&lt;CR&gt;pkddA<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code js-file-line">            <span class="pl-c"># ctrl-C gets sent to the IPython process as a signal on POSIX</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code js-file-line">            vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>noremap &lt;buffer&gt;  :IPythonInterrupt&lt;cr&gt;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code js-file-line">    <span class="pl-c">#syntax highlighting for python prompt</span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code js-file-line">    <span class="pl-c"># QtConsole In[] is blue, but I prefer the oldschool green</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code js-file-line">    <span class="pl-c"># since it makes the vim-ipython &#39;shell&#39; look like the holidays!</span></td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code js-file-line">    colors <span class="pl-k">=</span> status_prompt_colors</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>hi IPyPromptIn ctermfg=<span class="pl-c1">%s</span> guifg=<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (colors[<span class="pl-s"><span class="pl-pds">&#39;</span>in_ctermfg<span class="pl-pds">&#39;</span></span>], colors[<span class="pl-s"><span class="pl-pds">&#39;</span>in_guifg<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>hi IPyPromptOut ctermfg=<span class="pl-c1">%s</span> guifg=<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (colors[<span class="pl-s"><span class="pl-pds">&#39;</span>out_ctermfg<span class="pl-pds">&#39;</span></span>], colors[<span class="pl-s"><span class="pl-pds">&#39;</span>out_guifg<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>hi IPyPromptOut2 ctermfg=<span class="pl-c1">%s</span> guifg=<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (colors[<span class="pl-s"><span class="pl-pds">&#39;</span>out2_ctermfg<span class="pl-pds">&#39;</span></span>], colors[<span class="pl-s"><span class="pl-pds">&#39;</span>out2_guifg<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code js-file-line">    in_expression <span class="pl-k">=</span> vim_regex_escape(status_prompt_in <span class="pl-k">%</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>line<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">999</span>}).replace(<span class="pl-s"><span class="pl-pds">&#39;</span>999<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>[ 0-9]*<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>syn match IPyPromptIn /^<span class="pl-c1">%s</span>/<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> in_expression)</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code js-file-line">    out_expression <span class="pl-k">=</span> vim_regex_escape(status_prompt_out <span class="pl-k">%</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>line<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">999</span>}).replace(<span class="pl-s"><span class="pl-pds">&#39;</span>999<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>[ 0-9]*<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>syn match IPyPromptOut /^<span class="pl-c1">%s</span>/<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> out_expression)</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>syn match IPyPromptOut2 /^<span class="pl-cce">\\</span>.<span class="pl-cce">\\</span>.<span class="pl-cce">\\</span>.* /<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code js-file-line">    b <span class="pl-k">=</span> vim.current.buffer</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code js-file-line">    update_occured <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code js-file-line">    <span class="pl-k">for</span> m <span class="pl-k">in</span> msgs:</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code js-file-line">        s <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>msg_type<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>header<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code js-file-line">            <span class="pl-c"># debug information</span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code js-file-line">            <span class="pl-c">#echo(&#39;skipping a message on sub_channel&#39;,&#39;WarningMsg&#39;)</span></td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code js-file-line">            <span class="pl-c">#echo(str(m))</span></td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code js-file-line">            <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code js-file-line">        header <span class="pl-k">=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>header<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>msg_type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code js-file-line">        <span class="pl-k">if</span> header <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code js-file-line">            <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code js-file-line">        <span class="pl-k">elif</span> header <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>stream<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code js-file-line">            <span class="pl-c"># TODO: alllow for distinguishing between stdout and stderr (using</span></td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code js-file-line">            <span class="pl-c"># custom syntax markers in the vim-ipython buffer perhaps), or by</span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code js-file-line">            <span class="pl-c"># also echoing the message to the status bar</span></td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code js-file-line">            s <span class="pl-k">=</span> strip_color_escapes(m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code js-file-line">        <span class="pl-k">elif</span> header <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>pyout<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code js-file-line">            s <span class="pl-k">=</span> status_prompt_out <span class="pl-k">%</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>line<span class="pl-pds">&#39;</span></span>: m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>execution_count<span class="pl-pds">&#39;</span></span>]}</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code js-file-line">            s <span class="pl-k">+=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>text/plain<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code js-file-line">        <span class="pl-k">elif</span> header <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>display_data<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code js-file-line">            <span class="pl-c"># TODO: handle other display data types (HMTL? images?)</span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code js-file-line">            s <span class="pl-k">+=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>text/plain<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code js-file-line">        <span class="pl-k">elif</span> header <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>pyin<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code js-file-line">            <span class="pl-c"># TODO: the next line allows us to resend a line to ipython if</span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code js-file-line">            <span class="pl-c"># %doctest_mode is on. In the future, IPython will send the</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code js-file-line">            <span class="pl-c"># execution_count on subchannel, so this will need to be updated</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code js-file-line">            <span class="pl-c"># once that happens</span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code js-file-line">            line_number <span class="pl-k">=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>].get(<span class="pl-s"><span class="pl-pds">&#39;</span>execution_count<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code js-file-line">            prompt <span class="pl-k">=</span> status_prompt_in <span class="pl-k">%</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>line<span class="pl-pds">&#39;</span></span>: line_number}</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code js-file-line">            s <span class="pl-k">=</span> prompt</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code js-file-line">            <span class="pl-c"># add a continuation line (with trailing spaces if the prompt has them)</span></td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code js-file-line">            dots <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span> <span class="pl-k">*</span> <span class="pl-c1">len</span>(prompt.rstrip())</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code js-file-line">            dots <span class="pl-k">+=</span> prompt[<span class="pl-c1">len</span>(prompt.rstrip()):]</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code js-file-line">            s <span class="pl-k">+=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>code<span class="pl-pds">&#39;</span></span>].rstrip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> dots)</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code js-file-line">        <span class="pl-k">elif</span> header <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>pyerr<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code js-file-line">            c <span class="pl-k">=</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code js-file-line">            s <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.join(<span class="pl-c1">map</span>(strip_color_escapes,c[<span class="pl-s"><span class="pl-pds">&#39;</span>traceback<span class="pl-pds">&#39;</span></span>]))</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code js-file-line">            s <span class="pl-k">+=</span> c[<span class="pl-s"><span class="pl-pds">&#39;</span>ename<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>:<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> c[<span class="pl-s"><span class="pl-pds">&#39;</span>evalue<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code js-file-line">        <span class="pl-k">if</span> s.find(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">==</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code js-file-line">            <span class="pl-c"># somewhat ugly unicode workaround from </span></td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code js-file-line">            <span class="pl-c"># http://vim.1045645.n5.nabble.com/Limitations-of-vim-python-interface-with-respect-to-character-encodings-td1223881.html</span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">unicode</span>):</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code js-file-line">                s<span class="pl-k">=</span>s.encode(vim_encoding)</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code js-file-line">            b.append(s)</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code js-file-line">                b.append(s.splitlines())</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code js-file-line">                b.append([l.encode(vim_encoding) <span class="pl-k">for</span> l <span class="pl-k">in</span> s.splitlines()])</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code js-file-line">        update_occured <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code js-file-line">    <span class="pl-c"># make a newline so we can just start typing there</span></td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code js-file-line">    <span class="pl-k">if</span> status_blank_lines:</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code js-file-line">        <span class="pl-k">if</span> b[<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code js-file-line">            b.append([<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code js-file-line">    <span class="pl-k">if</span> update_occured <span class="pl-k">or</span> force:</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>normal! G<span class="pl-pds">&#39;</span></span>) <span class="pl-c"># go to the end of the file</span></td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> startedin_vimipython:</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>normal! p<span class="pl-pds">&#39;</span></span>) <span class="pl-c"># go back to where you were</span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code js-file-line">    <span class="pl-k">return</span> update_occured</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_child_msg</span>(<span class="pl-smi">msg_id</span>):</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code js-file-line">    <span class="pl-c"># XXX: message handling should be split into its own process in the future</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code js-file-line">    <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code js-file-line">        <span class="pl-c"># get_msg will raise with Empty exception if no messages arrive in 1 second</span></td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code js-file-line">        m <span class="pl-k">=</span> kc.shell_channel.get_msg(<span class="pl-smi">timeout</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code js-file-line">        <span class="pl-k">if</span> m[<span class="pl-s"><span class="pl-pds">&#39;</span>parent_header<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>msg_id<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> msg_id:</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code js-file-line">            <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code js-file-line">            <span class="pl-c">#got a message, but not the one we were looking for</span></td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&#39;</span>skipping a message on shell_channel<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>WarningMsg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code js-file-line">    <span class="pl-k">return</span> m</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code js-file-line">            </td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">print_prompt</span>(<span class="pl-smi">prompt</span>,<span class="pl-smi">msg_id</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Print In[] or In[42] style messages<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code js-file-line">    <span class="pl-k">global</span> show_execution_count</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code js-file-line">    <span class="pl-k">if</span> show_execution_count <span class="pl-k">and</span> msg_id:</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code js-file-line">        <span class="pl-c"># wait to get message back from kernel</span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code js-file-line">            child <span class="pl-k">=</span> get_child_msg(msg_id)</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code js-file-line">            count <span class="pl-k">=</span> child[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>execution_count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>In[<span class="pl-c1">%d</span>]: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(count,prompt))</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code js-file-line">        <span class="pl-k">except</span> Empty:</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>In[]: <span class="pl-c1">%s</span> (no reply from IPython kernel)<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> prompt)</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code js-file-line">        echo(<span class="pl-s"><span class="pl-pds">&quot;</span>In[]: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> prompt)</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">with_subchannel</span>(<span class="pl-smi">f</span>,*<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>conditionally monitor subchannel<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code js-file-line">    <span class="pl-k">def</span> <span class="pl-en">f_with_update</span>(*<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code js-file-line">            f(<span class="pl-k">*</span>args)</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code js-file-line">            <span class="pl-k">if</span> monitor_subchannel:</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code js-file-line">                update_subchannel_msgs(<span class="pl-smi">force</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">AttributeError</span>: <span class="pl-c">#if kc is None</span></td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>not connected to IPython<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Error<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code js-file-line">    <span class="pl-k">return</span> f_with_update</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code js-file-line"><span class="pl-en">@with_subchannel</span></td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">run_this_file</span>():</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> send(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%%</span>run <span class="pl-c1">%s</span> <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (run_flags, <span class="pl-c1">repr</span>(vim.current.buffer.name),))</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code js-file-line">    print_prompt(<span class="pl-s"><span class="pl-pds">&quot;</span>In[]: <span class="pl-c1">%%</span>run <span class="pl-c1">%s</span> <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (run_flags, <span class="pl-c1">repr</span>(vim.current.buffer.name)),msg_id)</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code js-file-line"><span class="pl-en">@with_subchannel</span></td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">run_this_line</span>(<span class="pl-smi">dedent</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code js-file-line">    line <span class="pl-k">=</span> vim.current.line</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code js-file-line">    <span class="pl-k">if</span> dedent:</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code js-file-line">        line <span class="pl-k">=</span> line.lstrip()</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code js-file-line">    <span class="pl-k">if</span> line.rstrip().endswith(<span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code js-file-line">        <span class="pl-c"># intercept question mark queries -- move to the word just before the</span></td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code js-file-line">        <span class="pl-c"># question mark and call the get_doc_buffer on it</span></td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code js-file-line">        w <span class="pl-k">=</span> vim.current.window</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code js-file-line">        original_pos <span class="pl-k">=</span>  w.cursor</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code js-file-line">        new_pos <span class="pl-k">=</span> (original_pos[<span class="pl-c1">0</span>], vim.current.line.index(<span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span>)<span class="pl-k">-</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code js-file-line">        w.cursor <span class="pl-k">=</span> new_pos</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code js-file-line">        <span class="pl-k">if</span> line.rstrip().endswith(<span class="pl-s"><span class="pl-pds">&#39;</span>??<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code js-file-line">            <span class="pl-c"># double question mark should display source</span></td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code js-file-line">            <span class="pl-c"># XXX: it&#39;s not clear what level=2 is for, level=1 is sufficient</span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code js-file-line">            <span class="pl-c"># to get the code -- follow up with IPython team on this</span></td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code js-file-line">            get_doc_buffer(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code js-file-line">            get_doc_buffer()</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code js-file-line">        <span class="pl-c"># leave insert mode, so we&#39;re in command mode</span></td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&#39;</span>stopi<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code js-file-line">        w.cursor <span class="pl-k">=</span> original_pos</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code js-file-line">        <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> send(line)</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code js-file-line">    print_prompt(line, msg_id)</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code js-file-line"><span class="pl-en">@with_subchannel</span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">run_command</span>(<span class="pl-smi">cmd</span>):</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> send(cmd)</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code js-file-line">    print_prompt(cmd, msg_id)</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code js-file-line"><span class="pl-en">@with_subchannel</span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">run_these_lines</span>(<span class="pl-smi">dedent</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code js-file-line">    r <span class="pl-k">=</span> vim.current.range</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code js-file-line">    <span class="pl-k">if</span> dedent:</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code js-file-line">        lines <span class="pl-k">=</span> <span class="pl-c1">list</span>(vim.current.buffer[r.start:r.end<span class="pl-k">+</span><span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code js-file-line">        nonempty_lines <span class="pl-k">=</span> [x <span class="pl-k">for</span> x <span class="pl-k">in</span> lines <span class="pl-k">if</span> x.strip()]</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> nonempty_lines:</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code js-file-line">        first_nonempty <span class="pl-k">=</span> nonempty_lines[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code js-file-line">        leading <span class="pl-k">=</span> <span class="pl-c1">len</span>(first_nonempty) <span class="pl-k">-</span> <span class="pl-c1">len</span>(first_nonempty.lstrip())</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code js-file-line">        lines <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.join(x[leading:] <span class="pl-k">for</span> x <span class="pl-k">in</span> lines)</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code js-file-line">        lines <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.join(vim.current.buffer[r.start:r.end<span class="pl-k">+</span><span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> send(lines)</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code js-file-line">    <span class="pl-c">#alternative way of doing this in more recent versions of ipython</span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code js-file-line">    <span class="pl-c">#but %paste only works on the local machine</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code js-file-line">    <span class="pl-c">#vim.command(&quot;\&quot;*yy&quot;)</span></td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code js-file-line">    <span class="pl-c">#send(&quot;&#39;%paste&#39;)&quot;)</span></td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code js-file-line">    <span class="pl-c">#reselect the previously highlighted block</span></td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code js-file-line">    vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>normal! gv<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> reselect:</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code js-file-line">        vim.command(<span class="pl-s"><span class="pl-pds">&quot;</span>normal! <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code js-file-line">    <span class="pl-c">#vim lines start with 1</span></td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code js-file-line">    <span class="pl-c">#print(&quot;lines %d-%d sent to ipython&quot;% (r.start+1,r.end+1))</span></td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code js-file-line">    prompt <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>lines <span class="pl-c1">%d</span>-<span class="pl-c1">%d</span> <span class="pl-pds">&quot;</span></span><span class="pl-k">%</span> (r.start<span class="pl-k">+</span><span class="pl-c1">1</span>,r.end<span class="pl-k">+</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code js-file-line">    print_prompt(prompt,msg_id)</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">set_pid</span>():</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code js-file-line"><span class="pl-s">    Explicitly ask the ipython kernel for its pid</span></td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code js-file-line">    <span class="pl-k">global</span> pid</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code js-file-line">    lines <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join([<span class="pl-s"><span class="pl-pds">&#39;</span>import os<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>_pid = os.getpid()<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code js-file-line">    msg_id <span class="pl-k">=</span> send(lines, <span class="pl-smi">silent</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">user_variables</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>_pid<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code js-file-line">    <span class="pl-c"># wait to get message back from kernel</span></td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code js-file-line">        child <span class="pl-k">=</span> get_child_msg(msg_id)</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code js-file-line">    <span class="pl-k">except</span> Empty:</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code js-file-line">        echo(<span class="pl-s"><span class="pl-pds">&quot;</span>no reply from IPython kernel<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code js-file-line">        <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code js-file-line">        pid <span class="pl-k">=</span> <span class="pl-c1">int</span>(child[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>user_variables<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>_pid<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">TypeError</span>: <span class="pl-c"># change in IPython 1.0.dev moved this out</span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code js-file-line">        pid <span class="pl-k">=</span> <span class="pl-c1">int</span>(child[<span class="pl-s"><span class="pl-pds">&#39;</span>content<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>user_variables<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>_pid<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>][<span class="pl-s"><span class="pl-pds">&#39;</span>text/plain<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>: <span class="pl-c"># change in IPython 1.0.dev moved this out</span></td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code js-file-line">        echo(<span class="pl-s"><span class="pl-pds">&quot;</span>Could not get PID information, kernel not running Python?<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code js-file-line">    <span class="pl-k">return</span> pid</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">terminate_kernel_hack</span>():</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;</span>Send SIGTERM to our the IPython kernel<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code js-file-line">    <span class="pl-k">import</span> signal</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code js-file-line">    interrupt_kernel_hack(signal.SIGTERM)</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">interrupt_kernel_hack</span>(<span class="pl-smi">signal_to_send</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code js-file-line"><span class="pl-s">    Sends the interrupt signal to the remote kernel.  This side steps the</span></td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code js-file-line"><span class="pl-s">    (non-functional) ipython interrupt mechanisms.</span></td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code js-file-line"><span class="pl-s">    Only works on posix.</span></td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code js-file-line">    <span class="pl-k">global</span> pid</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code js-file-line">    <span class="pl-k">import</span> signal</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code js-file-line">    <span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code js-file-line">    <span class="pl-k">if</span> pid <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code js-file-line">        <span class="pl-c"># Avoid errors if we couldn&#39;t get pid originally,</span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code js-file-line">        <span class="pl-c"># by trying to obtain it now</span></td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code js-file-line">        pid <span class="pl-k">=</span> set_pid()</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code js-file-line">        <span class="pl-k">if</span> pid <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code js-file-line">            echo(<span class="pl-s"><span class="pl-pds">&quot;</span>cannot get kernel PID, Ctrl-C will not be supported<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> signal_to_send:</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code js-file-line">        signal_to_send <span class="pl-k">=</span> signal.SIGINT</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code js-file-line">    echo(<span class="pl-s"><span class="pl-pds">&quot;</span>KeyboardInterrupt (sent to ipython: pid <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%i</span> with signal <span class="pl-c1">%s</span>)<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (pid, signal_to_send),<span class="pl-s"><span class="pl-pds">&quot;</span>Operator<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code js-file-line">        os.kill(pid, <span class="pl-c1">int</span>(signal_to_send))</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">OSError</span>:</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code js-file-line">        echo(<span class="pl-s"><span class="pl-pds">&quot;</span>unable to kill pid <span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> pid)</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code js-file-line">        pid <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">dedent_run_this_line</span>():</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code js-file-line">    run_this_line(<span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">dedent_run_these_lines</span>():</td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code js-file-line">    run_these_lines(<span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code js-file-line"><span class="pl-c">#def set_this_line():</span></td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code js-file-line"><span class="pl-c">#    # not sure if there&#39;s a way to do this, since we have multiple clients</span></td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code js-file-line"><span class="pl-c">#    send(&quot;get_ipython().shell.set_next_input(\&#39;%s\&#39;)&quot; % vim.current.line.replace(&quot;\&#39;&quot;,&quot;\\\&#39;&quot;))</span></td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code js-file-line"><span class="pl-c">#    #print(&quot;line \&#39;%s\&#39; set at ipython prompt&quot;% vim.current.line)</span></td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code js-file-line"><span class="pl-c">#    echo(&quot;line \&#39;%s\&#39; set at ipython prompt&quot;% vim.current.line,&#39;Statement&#39;)</span></td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">toggle_reselect</span>():</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code js-file-line">    <span class="pl-k">global</span> reselect</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code js-file-line">    reselect<span class="pl-k">=</span><span class="pl-k">not</span> reselect</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>F9 will<span class="pl-c1">%s</span>reselect lines after sending to ipython<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code js-file-line">            (reselect <span class="pl-k">and</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&quot;</span> not <span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code js-file-line"><span class="pl-c">#def set_breakpoint():</span></td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code js-file-line"><span class="pl-c">#    send(&quot;__IP.InteractiveTB.pdb.set_break(&#39;%s&#39;,%d)&quot; % (vim.current.buffer.name,</span></td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code js-file-line"><span class="pl-c">#                                                        vim.current.window.cursor[0]))</span></td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code js-file-line"><span class="pl-c">#    print(&quot;set breakpoint in %s:%d&quot;% (vim.current.buffer.name, </span></td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code js-file-line"><span class="pl-c">#                                      vim.current.window.cursor[0]))</span></td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code js-file-line"><span class="pl-c">#    </span></td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code js-file-line"><span class="pl-c">#def clear_breakpoint():</span></td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code js-file-line"><span class="pl-c">#    send(&quot;__IP.InteractiveTB.pdb.clear_break(&#39;%s&#39;,%d)&quot; % (vim.current.buffer.name,</span></td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code js-file-line"><span class="pl-c">#                                                          vim.current.window.cursor[0]))</span></td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code js-file-line"><span class="pl-c">#    print(&quot;clearing breakpoint in %s:%d&quot; % (vim.current.buffer.name,</span></td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code js-file-line"><span class="pl-c">#                                            vim.current.window.cursor[0]))</span></td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code js-file-line"><span class="pl-c">#def clear_all_breakpoints():</span></td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code js-file-line"><span class="pl-c">#    send(&quot;__IP.InteractiveTB.pdb.clear_all_breaks()&quot;);</span></td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code js-file-line"><span class="pl-c">#    print(&quot;clearing all breakpoints&quot;)</span></td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code js-file-line"><span class="pl-c">#def run_this_file_pdb():</span></td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code js-file-line"><span class="pl-c">#    send(&#39; __IP.InteractiveTB.pdb.run(\&#39;execfile(&quot;%s&quot;)\&#39;)&#39; % (vim.current.buffer.name,))</span></td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code js-file-line"><span class="pl-c">#    #send(&#39;run -d %s&#39; % (vim.current.buffer.name,))</span></td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code js-file-line"><span class="pl-c">#    echo(&quot;In[]: run -d %s (using pdb)&quot; % vim.current.buffer.name)</span></td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code js-file-line">
</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.03522s from github-fe128-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-d22b59d0085e83b7549ba4341ec9e68f80c2f29c8e49213ee182003dc8d568c6.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-2c46bf7af744168851951e2fa4f404675a09c3d3f5b8ec92e4d28c3238de7936.js"></script>
      
      

  </body>
</html>

