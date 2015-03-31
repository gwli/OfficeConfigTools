


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>vim-ipython/ipy.vim at master · ivanov/vim-ipython · GitHub</title>
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

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="CB123204:79EB:A98BEC:551A6D7A" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged Out">
    <meta class="js-ga-set" name="dimension2" content="Header v3">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="7uq9E+XIzOBOP4ARZzPxR1Org81HveyAB0jdG+/SpQWBS26/uVO9i1cNgyO3evUyqPKY1QWmXjKS2JYZf7GYTQ==" name="csrf-token" />

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
      <a class="btn" href="/login?return_to=%2Fivanov%2Fvim-ipython%2Fblob%2Fmaster%2Fftplugin%2Fpython%2Fipy.vim" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
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
          

<a href="/ivanov/vim-ipython/blob/a47d92b371588a81f8501c66604d79e2827c60a8/ftplugin/python/ipy.vim" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:7ff0bb65439e0e623a86e1ded50a36f7 -->

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
               href="/ivanov/vim-ipython/blob/kernel-interupt/ftplugin/python/ipy.vim"
               data-name="kernel-interupt"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="kernel-interupt">
                kernel-interupt
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/ivanov/vim-ipython/blob/master/ftplugin/python/ipy.vim"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ivanov/vim-ipython/blob/notebook-io/ftplugin/python/ipy.vim"
               data-name="notebook-io"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="notebook-io">
                notebook-io
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/ivanov/vim-ipython/blob/vader/ftplugin/python/ipy.vim"
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
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ivanov/vim-ipython" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">vim-ipython</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ivanov/vim-ipython/tree/master/ftplugin" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">ftplugin</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ivanov/vim-ipython/tree/master/ftplugin/python" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">python</span></a></span><span class="separator">/</span><strong class="final-path">ipy.vim</strong>
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
          <strong>11</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="ivanov" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=ivanov"><img alt="@ivanov" class="avatar" data-user="118211" height="20" src="https://avatars2.githubusercontent.com/u/118211?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="idbrii" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=idbrii"><img alt="@idbrii" class="avatar" data-user="43559" height="20" src="https://avatars3.githubusercontent.com/u/43559?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="pag" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=pag"><img alt="@pag" class="avatar" data-user="20008" height="20" src="https://avatars3.githubusercontent.com/u/20008?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="minrk" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=minrk"><img alt="@minrk" class="avatar" data-user="151929" height="20" src="https://avatars2.githubusercontent.com/u/151929?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="nonameentername" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=nonameentername"><img alt="@nonameentername" class="avatar" data-user="425111" height="20" src="https://avatars0.githubusercontent.com/u/425111?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="pielgrzym" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=pielgrzym"><img alt="@pielgrzym" class="avatar" data-user="124301" height="20" src="https://avatars1.githubusercontent.com/u/124301?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="enzbang" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=enzbang"><img alt="@enzbang" class="avatar" data-user="36661" height="20" src="https://avatars1.githubusercontent.com/u/36661?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="luispedro" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=luispedro"><img alt="@luispedro" class="avatar" data-user="79334" height="20" src="https://avatars1.githubusercontent.com/u/79334?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="koepsell" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=koepsell"><img alt="@koepsell" class="avatar" data-user="139912" height="20" src="https://avatars3.githubusercontent.com/u/139912?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="dstahlke" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=dstahlke"><img alt="@dstahlke" class="avatar" data-user="313200" height="20" src="https://avatars2.githubusercontent.com/u/313200?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="zeekay" href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim?author=zeekay"><img alt="@zeekay" class="avatar" data-user="285707" height="20" src="https://avatars2.githubusercontent.com/u/285707?v=3&amp;s=40" width="20" /> </a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@ivanov" data-user="118211" height="24" src="https://avatars0.githubusercontent.com/u/118211?v=3&amp;s=48" width="24" />
            <a href="/ivanov">ivanov</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@idbrii" data-user="43559" height="24" src="https://avatars1.githubusercontent.com/u/43559?v=3&amp;s=48" width="24" />
            <a href="/idbrii">idbrii</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@pag" data-user="20008" height="24" src="https://avatars1.githubusercontent.com/u/20008?v=3&amp;s=48" width="24" />
            <a href="/pag">pag</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@minrk" data-user="151929" height="24" src="https://avatars0.githubusercontent.com/u/151929?v=3&amp;s=48" width="24" />
            <a href="/minrk">minrk</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@nonameentername" data-user="425111" height="24" src="https://avatars2.githubusercontent.com/u/425111?v=3&amp;s=48" width="24" />
            <a href="/nonameentername">nonameentername</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@pielgrzym" data-user="124301" height="24" src="https://avatars3.githubusercontent.com/u/124301?v=3&amp;s=48" width="24" />
            <a href="/pielgrzym">pielgrzym</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@enzbang" data-user="36661" height="24" src="https://avatars3.githubusercontent.com/u/36661?v=3&amp;s=48" width="24" />
            <a href="/enzbang">enzbang</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@luispedro" data-user="79334" height="24" src="https://avatars3.githubusercontent.com/u/79334?v=3&amp;s=48" width="24" />
            <a href="/luispedro">luispedro</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@koepsell" data-user="139912" height="24" src="https://avatars1.githubusercontent.com/u/139912?v=3&amp;s=48" width="24" />
            <a href="/koepsell">koepsell</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@dstahlke" data-user="313200" height="24" src="https://avatars0.githubusercontent.com/u/313200?v=3&amp;s=48" width="24" />
            <a href="/dstahlke">dstahlke</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@zeekay" data-user="285707" height="24" src="https://avatars0.githubusercontent.com/u/285707?v=3&amp;s=48" width="24" />
            <a href="/zeekay">zeekay</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/ivanov/vim-ipython/raw/master/ftplugin/python/ipy.vim" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/ivanov/vim-ipython/blame/master/ftplugin/python/ipy.vim" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/ivanov/vim-ipython/commits/master/ftplugin/python/ipy.vim" class="btn btn-sm " rel="nofollow">History</a>
      </div>


          <button type="button" class="octicon-btn disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
            <span class="octicon octicon-pencil"></span>
          </button>

        <button type="button" class="octicon-btn octicon-btn-danger disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </button>
    </div>

    <div class="file-info">
        208 lines (191 sloc)
        <span class="file-info-divider"></span>
      9.071 kb
    </div>
  </div>
  
  <div class="blob-wrapper data type-viml">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c">&quot; Vim integration with IPython 0.11+</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-c">&quot; A two-way integration between Vim and IPython.</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-c">&quot; Using this plugin, you can send lines or whole files for IPython to execute,</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line"><span class="pl-c">&quot; and also get back object introspection and word completions in Vim, like</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line"><span class="pl-c">&quot; what you get with: object?&lt;enter&gt; object.&lt;tab&gt; in IPython</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-c">&quot; -----------------</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line"><span class="pl-c">&quot; Quickstart Guide:</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line"><span class="pl-c">&quot; -----------------</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line"><span class="pl-c">&quot; Start `ipython qtconsole`, `ipython console`, or  `ipython notebook` and</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line"><span class="pl-c">&quot; open a notebook using you web browser.  Source this file, which provides new</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line"><span class="pl-c">&quot; IPython command</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line"><span class="pl-c">&quot;   :source ipy.vim</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line"><span class="pl-c">&quot;   :IPython</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line"><span class="pl-c">&quot; written by Paul Ivanov (http://pirsquared.org)</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line"><span class="pl-k">if</span> !<span class="pl-c1">has</span>(<span class="pl-s">&#39;python&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line"><span class="pl-c">    &quot; exit if python is not available.</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line"><span class="pl-c">    &quot; XXX: raise an error message here</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line">    finish</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line"><span class="pl-k">endif</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line"><span class="pl-c">&quot; Allow custom mappings.</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line"><span class="pl-k">if</span> !<span class="pl-c1">exists</span>(<span class="pl-s">&#39;g:ipy_perform_mappings&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">    <span class="pl-c1">let</span> <span class="pl-smi">g:ipy_perform_mappings</span> = <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line"><span class="pl-k">endif</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line"><span class="pl-c">&quot; Register IPython completefunc</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line"><span class="pl-c">&quot; &#39;global&#39;   -- for all of vim (default).</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line"><span class="pl-c">&quot; &#39;local&#39;    -- only for the current buffer.</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line"><span class="pl-c">&quot; otherwise  -- don&#39;t register it at all.</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line"><span class="pl-c">&quot; you can later set it using &#39;:set completefunc=CompleteIPython&#39;, which will</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line"><span class="pl-c">&quot; correspond to the &#39;global&#39; behavior, or with &#39;:setl ...&#39; to get the &#39;local&#39;</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line"><span class="pl-c">&quot; behavior</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line"><span class="pl-k">if</span> !<span class="pl-c1">exists</span>(<span class="pl-s">&#39;g:ipy_completefunc&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">    <span class="pl-c1">let</span> <span class="pl-smi">g:ipy_completefunc</span> = <span class="pl-s">&#39;global&#39;</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line"><span class="pl-k">endif</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">python &lt;&lt; EOF</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">import vim</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">import sys</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">vim_ipython_path = vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&quot;expand(&#39;&lt;sfile&gt;:h&#39;)&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">sys<span class="pl-k">.</span>path<span class="pl-k">.</span><span class="pl-c1">append</span>(vim_ipython_path)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">from vim_ipython import <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">EOF</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line"><span class="pl-k">fun</span>! <span class="pl-c1">&lt;SID&gt;</span><span class="pl-c1">toggle_send_on_save</span>()</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">exists</span>(<span class="pl-s">&quot;s:ssos&quot;</span>) <span class="pl-k">&amp;&amp;</span> <span class="pl-smi">s:ssos</span> <span class="pl-k">==</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">        <span class="pl-c1">let</span> <span class="pl-smi">s:ssos</span> = <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">        <span class="pl-c1">au</span> BufWritePost <span class="pl-k">*.</span>py :py <span class="pl-c1">run_this_file</span>()</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">        <span class="pl-c1">echo</span> <span class="pl-s">&quot;Autosend On&quot;</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">    <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">        <span class="pl-c1">let</span> <span class="pl-smi">s:ssos</span> = <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">        <span class="pl-c1">au</span>! BufWritePost <span class="pl-k">*.</span>py</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">        <span class="pl-c1">echo</span> <span class="pl-s">&quot;Autosend Off&quot;</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">    <span class="pl-k">endif</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line"><span class="pl-k">endfun</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line"><span class="pl-c">&quot; Update the vim-ipython shell when the cursor is not moving.</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line"><span class="pl-c">&quot; You can change how quickly this happens after you stop moving the cursor by</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line"><span class="pl-c">&quot; setting &#39;updatetime&#39; (in milliseconds). For example, to have this event</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line"><span class="pl-c">&quot; trigger after 1 second:</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line"><span class="pl-c">&quot;       :set updatetime 1000</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line"><span class="pl-c">&quot; NOTE: This will only be triggered once, after the first &#39;updatetime&#39;</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line"><span class="pl-c">&quot; milliseconds, *not* every &#39;updatetime&#39; milliseconds. see :help CursorHold</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line"><span class="pl-c">&quot; for more info.</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line"><span class="pl-c">&quot;</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line"><span class="pl-c">&quot; TODO: Make this easily configurable on the fly, so that an introspection</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line"><span class="pl-c">&quot; buffer we may have opened up doesn&#39;t get closed just because of an idle</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line"><span class="pl-c">&quot; event (i.e. user pressed \d and then left the buffer that popped up, but</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line"><span class="pl-c">&quot; expects it to stay there).</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line"><span class="pl-c1">au</span> CursorHold <span class="pl-k">*.*</span>,vim-ipython :python <span class="pl-k">if</span> <span class="pl-c1">update_subchannel_msgs</span>(): <span class="pl-c1">echo</span>(<span class="pl-s">&quot;vim-ipython shell updated (on idle)&quot;</span>,<span class="pl-s">&#39;Operator&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line"><span class="pl-c">&quot; XXX: broken - cursor hold update for insert mode moves the cursor one</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line"><span class="pl-c">&quot; character to the left of the last character (update_subchannel_msgs must be</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line"><span class="pl-c">&quot; doing this)</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line"><span class="pl-c">&quot;au CursorHoldI *.* :python if update_subchannel_msgs(): echo(&quot;vim-ipython shell updated (on idle)&quot;,&#39;Operator&#39;)</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line"><span class="pl-c">&quot; Same as above, but on regaining window focus (mostly for GUIs)</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line"><span class="pl-c1">au</span> FocusGained <span class="pl-k">*.*</span>,vim-ipython :python <span class="pl-k">if</span> <span class="pl-c1">update_subchannel_msgs</span>(): <span class="pl-c1">echo</span>(<span class="pl-s">&quot;vim-ipython shell updated (on input focus)&quot;</span>,<span class="pl-s">&#39;Operator&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line"><span class="pl-c">&quot; Update vim-ipython buffer when we move the cursor there. A message is only</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line"><span class="pl-c">&quot; displayed if vim-ipython buffer has been updated.</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line"><span class="pl-c1">au</span> BufEnter vim-ipython :python <span class="pl-k">if</span> <span class="pl-c1">update_subchannel_msgs</span>(): <span class="pl-c1">echo</span>(<span class="pl-s">&quot;vim-ipython shell updated (on buffer enter)&quot;</span>,<span class="pl-s">&#39;Operator&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line"><span class="pl-c">&quot; Setup plugin mappings for the most common ways to interact with ipython.</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunFile)            :python <span class="pl-c1">run_this_file</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLine)            :python <span class="pl-c1">run_this_line</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLines)           :python <span class="pl-c1">run_these_lines</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-OpenPyDoc)          :python <span class="pl-c1">get_doc_buffer</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-UpdateShell)        :python <span class="pl-k">if</span> <span class="pl-c1">update_subchannel_msgs</span>(force=True): <span class="pl-c1">echo</span>(<span class="pl-s">&quot;vim-ipython shell updated&quot;</span>,<span class="pl-s">&#39;Operator&#39;</span>)<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-ToggleReselect)     :python <span class="pl-c1">toggle_reselect</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line"><span class="pl-c">&quot;noremap  &lt;Plug&gt;(IPython-StartDebugging)     :python send(&#39;%pdb&#39;)&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line"><span class="pl-c">&quot;noremap  &lt;Plug&gt;(IPython-BreakpointSet)      :python set_breakpoint()&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line"><span class="pl-c">&quot;noremap  &lt;Plug&gt;(IPython-BreakpointClear)    :python clear_breakpoint()&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line"><span class="pl-c">&quot;noremap  &lt;Plug&gt;(IPython-DebugThisFile)      :python run_this_file_pdb()&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line"><span class="pl-c">&quot;noremap  &lt;Plug&gt;(IPython-BreakpointClearAll) :python clear_all_breaks()&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-ToggleSendOnSave)   :call <span class="pl-c1">&lt;SID&gt;</span><span class="pl-c1">toggle_send_on_save</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-PlotClearCurrent)   :python <span class="pl-c1">run_command</span>(<span class="pl-s">&quot;plt.clf()&quot;</span>)<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-PlotCloseAll)       :python <span class="pl-c1">run_command</span>(<span class="pl-s">&quot;plt.close(&#39;all&#39;)&quot;</span>)<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line"><span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLineAsTopLevel)  :python <span class="pl-c1">dedent_run_this_line</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line"><span class="pl-c1">xnoremap</span> <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLinesAsTopLevel) :python <span class="pl-c1">dedent_run_these_lines</span>()<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line"><span class="pl-k">if</span> <span class="pl-smi">g:ipy_perform_mappings</span> <span class="pl-k">!=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;F5&gt;</span>           <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunFile)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;S-F5&gt;</span>         <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLine)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;F9&gt;</span>           <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLines)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;LocalLeader&gt;</span>d <span class="pl-c1">&lt;Plug&gt;</span>(IPython-OpenPyDoc)</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;LocalLeader&gt;</span>s <span class="pl-c1">&lt;Plug&gt;</span>(IPython-UpdateShell)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;S-F9&gt;</span>         <span class="pl-c1">&lt;Plug&gt;</span>(IPython-ToggleReselect)</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;C-F6&gt;         &lt;Plug&gt;(IPython-StartDebugging)</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;F6&gt;           &lt;Plug&gt;(IPython-BreakpointSet)</span></td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;S-F6&gt;         &lt;Plug&gt;(IPython-BreakpointClear)</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;F7&gt;           &lt;Plug&gt;(IPython-DebugThisFile)</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;S-F7&gt;         &lt;Plug&gt;(IPython-BreakpointClearAll)</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">    <span class="pl-c1">imap</span> <span class="pl-c1">&lt;buffer&gt;</span>          <span class="pl-c1">&lt;C-F5&gt;</span>         <span class="pl-c1">&lt;C-o&gt;&lt;Plug&gt;</span>(IPython-RunFile)</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line">    <span class="pl-c1">imap</span> <span class="pl-c1">&lt;buffer&gt;</span>          <span class="pl-c1">&lt;S-F5&gt;</span>         <span class="pl-c1">&lt;C-o&gt;&lt;Plug&gt;</span>(IPython-RunLines)</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">    <span class="pl-c1">imap</span> <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;F5&gt;</span>           <span class="pl-c1">&lt;C-o&gt;&lt;Plug&gt;</span>(IPython-RunFile)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span>          <span class="pl-c1">&lt;C-F5&gt;</span>         <span class="pl-c1">&lt;Plug&gt;</span>(IPython-ToggleSendOnSave)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line"><span class="pl-c">    &quot;&quot; Example of how to quickly clear the current plot with a keystroke</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;F12&gt;          &lt;Plug&gt;(IPython-PlotClearCurrent)</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line"><span class="pl-c">    &quot;&quot; Example of how to quickly close all figures with a keystroke</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line"><span class="pl-c">    &quot;map  &lt;buffer&gt; &lt;silent&gt; &lt;F11&gt;          &lt;Plug&gt;(IPython-PlotCloseAll)</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line"><span class="pl-c">    &quot;pi custom</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;C-Return&gt;</span>     <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunFile)</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;C-s&gt;</span>          <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLine)</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">    <span class="pl-c1">imap</span> <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;C-s&gt;</span>          <span class="pl-c1">&lt;C-o&gt;&lt;Plug&gt;</span>(IPython-RunLine)</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">    <span class="pl-c1">map</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;M-s&gt;</span>          <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLineAsTopLevel)</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">    <span class="pl-c1">xmap</span> <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;C-S&gt;</span>          <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLines)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">    <span class="pl-c1">xmap</span> <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;M-s&gt;</span>          <span class="pl-c1">&lt;Plug&gt;</span>(IPython-RunLinesAsTopLevel)</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">    <span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;M-c&gt;</span>      I#<span class="pl-c1">&lt;ESC&gt;</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">    <span class="pl-c1">xnoremap</span> <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;M-c&gt;</span>      I#<span class="pl-c1">&lt;ESC&gt;</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">    <span class="pl-c1">noremap</span>  <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;M-C&gt;</span>      :s<span class="pl-sr">/^\([ \t]*\)#/</span><span class="pl-k">\</span><span class="pl-c1">1</span>/<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">    <span class="pl-c1">xnoremap</span> <span class="pl-c1">&lt;buffer&gt;</span> <span class="pl-c1">&lt;silent&gt;</span> <span class="pl-c1">&lt;M-C&gt;</span>      :s<span class="pl-sr">/^\([ \t]*\)#/</span><span class="pl-k">\</span><span class="pl-c1">1</span>/<span class="pl-c1">&lt;CR&gt;</span></td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line"><span class="pl-k">endif</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line"><span class="pl-c1">command</span>! <span class="pl-c1">-nargs=</span><span class="pl-k">*</span> IPython :py <span class="pl-c1">km_from_string</span>(<span class="pl-s">&quot;&lt;args&gt;&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line"><span class="pl-c1">command</span>! <span class="pl-c1">-nargs=</span><span class="pl-c1">0</span> IPythonClipboard :py <span class="pl-c1">km_from_string</span>(vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&#39;@+&#39;</span>))</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line"><span class="pl-c1">command</span>! <span class="pl-c1">-nargs=</span><span class="pl-c1">0</span> IPythonXSelection :py <span class="pl-c1">km_from_string</span>(vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&#39;@*&#39;</span>))</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code js-file-line"><span class="pl-c1">command</span>! <span class="pl-c1">-nargs=</span><span class="pl-k">*</span> IPythonNew :py <span class="pl-c1">new_ipy</span>(<span class="pl-s">&quot;&lt;args&gt;&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code js-file-line"><span class="pl-c1">command</span>! <span class="pl-c1">-nargs=</span><span class="pl-k">*</span> IPythonInterrupt :py <span class="pl-c1">interrupt_kernel_hack</span>(<span class="pl-s">&quot;&lt;args&gt;&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code js-file-line"><span class="pl-c1">command</span>! <span class="pl-c1">-nargs=</span><span class="pl-c1">0</span> IPythonTerminate :py <span class="pl-c1">terminate_kernel_hack</span>()</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code js-file-line"><span class="pl-k">function</span>! <span class="pl-en">IPythonBalloonExpr</span>()</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code js-file-line">python &lt;&lt; endpython</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code js-file-line">word = vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&#39;v:beval_text&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code js-file-line">reply = <span class="pl-c1">get_doc</span>(word)</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code js-file-line">vim<span class="pl-k">.</span><span class="pl-c1">command</span>(<span class="pl-s">&quot;let l:doc = %s&quot;</span><span class="pl-k">%</span> reply)</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code js-file-line">endpython</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code js-file-line"><span class="pl-k">return</span> <span class="pl-smi">l:doc</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code js-file-line"><span class="pl-k">endfunction</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code js-file-line"><span class="pl-k">fun</span>! <span class="pl-c1">CompleteIPython</span>(findstart, base)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code js-file-line">      <span class="pl-k">if</span> <span class="pl-smi">a:findstart</span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code js-file-line"><span class="pl-c">        &quot; locate the start of the word</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code js-file-line">        <span class="pl-c1">let</span> line = <span class="pl-c1">getline</span>(<span class="pl-s">&#39;.&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code js-file-line">        <span class="pl-c1">let</span> start = <span class="pl-c1">col</span>(<span class="pl-s">&#39;.&#39;</span>) - <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code js-file-line">        <span class="pl-k">while</span> start &gt; <span class="pl-c1">0</span> <span class="pl-k">&amp;&amp;</span> line[start<span class="pl-c1">-1</span>] <span class="pl-k">=~</span> <span class="pl-s">&#39;\k\|\.&#39;</span> <span class="pl-c">&quot;keyword</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code js-file-line">          <span class="pl-c1">let</span> start -= <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code js-file-line">        <span class="pl-k">endwhile</span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code js-file-line">        <span class="pl-c1">echo</span> start</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code js-file-line">        python &lt;&lt; endpython</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code js-file-line">current_line = vim<span class="pl-k">.</span>current<span class="pl-k">.</span>line</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code js-file-line">endpython</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code js-file-line">        <span class="pl-k">return</span> start</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code js-file-line">      <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code js-file-line"><span class="pl-c">        &quot; find months matching with &quot;a:base&quot;</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code js-file-line">        <span class="pl-c1">let</span> res = []</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code js-file-line">        python &lt;&lt; endpython</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code js-file-line">base = vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&quot;a:base&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code js-file-line">findstart = vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&quot;a:findstart&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code js-file-line">matches = <span class="pl-c1">ipy_complete</span>(base, current_line, vim<span class="pl-k">.</span><span class="pl-c1">eval</span>(<span class="pl-s">&quot;col(&#39;.&#39;)&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code js-file-line"># we need to be careful with unicode, because we can have unicode</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code js-file-line"># completions <span class="pl-k">for</span> filenames (<span class="pl-k">for</span> the <span class="pl-k">%</span>run magic, <span class="pl-k">for</span> example)<span class="pl-k">.</span> So the next</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code js-file-line"># line will fail on those:</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code js-file-line">#completions= [<span class="pl-c1">str</span>(u) <span class="pl-k">for</span> u <span class="pl-k">in</span> matches]</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code js-file-line"># because <span class="pl-c1">str</span>() won&#39;t work <span class="pl-k">for</span> non-ascii characters</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code js-file-line"># and we also have problems with unicode <span class="pl-k">in</span> vim, hence the followin<span class="pl-smi">g:</span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code js-file-line">completions = [s<span class="pl-k">.</span><span class="pl-c1">encode</span>(vim_encoding) <span class="pl-k">for</span> s <span class="pl-k">in</span> matches]</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code js-file-line">## Additionally, we have no good way of communicating lists to vim, so we have</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code js-file-line">## to turn <span class="pl-k">in</span> into one long string, which can be problematic <span class="pl-k">if</span> e<span class="pl-k">.</span>g<span class="pl-k">.</span> the</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code js-file-line">## completions contain quotes<span class="pl-k">.</span> The next line will not work <span class="pl-k">if</span> some filenames</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code js-file-line">## contain quotes - but <span class="pl-k">if</span> that<span class="pl-s">&#39;s the case, the user&#39;</span>s just asking <span class="pl-k">for</span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code js-file-line">## it, right?</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code js-file-line">#completions = <span class="pl-s">&#39;[&quot;&#39;</span>+ <span class="pl-s">&#39;&quot;, &quot;&#39;</span><span class="pl-k">.</span><span class="pl-c1">join</span>(completions)+<span class="pl-s">&#39;&quot;]&#39;</span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code js-file-line">#vim<span class="pl-k">.</span><span class="pl-c1">command</span>(<span class="pl-s">&quot;let completions = %s&quot;</span> <span class="pl-k">%</span> completions)</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code js-file-line">## An alternative <span class="pl-k">for</span> the above, which will insert matches one at a time, so</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code js-file-line">## <span class="pl-k">if</span> there<span class="pl-s">&#39;s a problem with turning a match into a string, it&#39;</span>ll just not</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code js-file-line">## include the problematic match, instead of not including anything<span class="pl-k">.</span> There&#39;s a</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code js-file-line">## bit more indirection here, but I think it&#39;s worth it</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code js-file-line"><span class="pl-k">for</span> c <span class="pl-k">in</span> completion<span class="pl-smi">s:</span></td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code js-file-line">    vim<span class="pl-k">.</span><span class="pl-c1">command</span>(<span class="pl-s">&#39;call add(res,&quot;&#39;</span>+c+<span class="pl-s">&#39;&quot;)&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code js-file-line">endpython</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code js-file-line"><span class="pl-c">        &quot;call extend(res,completions) </span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code js-file-line">        <span class="pl-k">return</span> res</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code js-file-line">      <span class="pl-k">endif</span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code js-file-line">    <span class="pl-k">endfun</span></td>
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
      <li>&copy; 2015 <span title="0.03767s from github-fe129-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
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

