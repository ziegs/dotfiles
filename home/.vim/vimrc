"
" Vim Config
" Matthew Ziegelbaum
"

" Preconfig for Vundle
set nocompatible               " be iMproved

let mapleader = ","
let maplocalleader = "\\"

filetype off                   " required!

set rtp+=~/.vim/bundle/Vundle.vim/
call vundle#begin()

" let Vundle manage Vundle
Plugin 'gmarik/Vundle.vim'

"Navigation
Plugin 'ZoomWin'
Plugin 'kien/ctrlp.vim'
Plugin 'JazzCore/ctrlp-cmatcher'
Plugin 'Lokaltog/vim-easymotion'

" UI
Plugin 'bling/vim-airline'
Plugin 'scrooloose/nerdtree'
Plugin 'Rykka/colorv.vim'
Plugin 'nanotech/jellybeans.vim'
Plugin 'tomtom/quickfixsigns_vim'
Plugin 'croaker/mustang-vim'
Plugin 'tomasr/molokai'
Plugin 'altercation/vim-colors-solarized'
Plugin 'ervandew/supertab'
Plugin 'edkolev/tmuxline.vim'
Plugin 'christoomey/vim-tmux-navigator'

" Commands
Plugin 'scrooloose/nerdcommenter'
Plugin 'tpope/vim-surround'
Plugin 'tpope/vim-speeddating'
Plugin 'tpope/vim-fugitive'
Plugin 'godlygeek/tabular'
Plugin 'gmarik/sudo-gui.vim'
Plugin 'milkypostman/vim-togglelist'
Plugin 'mutewinter/swap-parameters'
Plugin 'keepcase.vim'
Plugin 'scratch.vim'
Plugin 'mattn/zencoding-vim'
Plugin 'mutewinter/GIFL'
Plugin 'sjbach/lusty'
Plugin 'YankRing.vim'
Plugin 'benmills/vimux'
Plugin 'mileszs/ack.vim'

" JS
Plugin 'pangloss/vim-javascript'
Plugin 'jelera/vim-javascript-syntax'
Plugin 'othree/javascript-libraries-syntax.vim'
Plugin 'Raimondi/delimitMate'
Plugin 'leshill/vim-json'
Plugin 'itspriddle/vim-jquery'
Plugin 'marijnh/tern_for_vim'

" Random languages
Plugin 'Blackrush/vim-gocode'
Plugin 'ChrisYip/Better-CSS-Syntax-for-Vim'
Plugin 'acustodioo/vim-tmux'
Plugin 'hallison/vim-markdown'
Plugin 'scrooloose/syntastic'
Plugin 'tfnico/vim-gradle'
Plugin 'Valloric/YouCompleteMe'
Plugin 'mattn/emmet-vim'
Plugin 'ingydotnet/yaml-vim'

call vundle#end()

filetype plugin indent on

syntax on
silent! source ~/.vimrc-pre

if has('gui_running')
  set guioptions=aegirLt
endif

if has('gui_macvim')
  if has("gui_running")
    set guioptions=egmrt
  endif
  set macmeta
endif

colorscheme solarized
set background=light
if has('gui_running')
else
endif

set backup
set backupdir=~/.vim/backup//
set directory=~/.vim/tmp//
set undodir=~/.vim/tmp/undo//
set noswapfile

set ruler
set nu
set nowrap
set laststatus=2
set cmdheight=2
set encoding=utf-8
if exists("+colorcolumn")
  set colorcolumn=+1
endif

syntax on
set autoread
set wildmenu
set hidden
set history=768
set cf
set autowrite
au FocusLost * :wa

set tabstop=2
set backspace=2
set shiftwidth=2
set cindent
set autoindent
set smarttab
set expandtab

nnoremap / /\v
vnoremap / /\v
set ignorecase
set smartcase
set incsearch
set hlsearch
set gdefault
set wildignore+=*.o,*.obj,*.exe,*.so,*.dll,*.pyc,.svn,.hg,.bzr,.git,
  \.sass-cache,*.class,*.scssc,*.cssc,sprockets%*,*.lessc
set sidescrolloff=2
set numberwidth=4
nnoremap <leader><space> :noh<cr>
nnoremap <tab> %
vnoremap <tab> %

set showmatch
set matchtime=2

set equalalways
set splitbelow splitright
:noremap ,v <C-w>v<C-w>l
:noremap ,h <C-w>s<C-w>j

set cursorline
set relativenumber
set undofile

set list

" Reset the listchars
set listchars=""
" a tab should display as "  ", trailing whitespace as "."
set listchars=tab:▸\·,eol:¬,trail:\·,extends:»,precedes:«
highlight NonText ctermfg=DarkGrey
highlight SpecialKey ctermbg=0 ctermfg=DarkRed
" Demo: tab & trailing spaces should be red	text    

set noerrorbells
set novisualbell
set t_vb=

" set mousehide
set mouse=a

set complete=.,w,b,u,U

command! W w
command! Q q

" ---------------
" Window movement
" ---------------
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" ---------------
" Turn off the arrows
" ---------------
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>
" Move by visual line, not file line
nnoremap j gj
nnoremap k gk



nmap <C-d> <C-b>
if has("gui_macvim")
  nmap <D-f> <C-f>
  nmap <D-d> <C-b>
else
  nmap <M-f> <C-f>
  nmap <M-d> <C-b>
endif

nmap gy :%y+<cr> " Yank entire buffer


" ---------------
" NERDTree
" ---------------
nnoremap <leader>nn :NERDTreeToggle<CR>
nnoremap <leader>nf :NERDTreeFind<CR>
let NERDTreeShowBookmarks=1
let NERDTreeChDirMode=2 " Change the NERDTree directory to the root node
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType")
  \&& b:NERDTreeType == "primary") | q | endif

"----------------
" YankRing
" ---------------
nnoremap <silent> <F3> :YRShow<cr>
inoremap <silent> <F3> <ESC>:YRShow<cr>
let g:yankring_replace_n_pkey = '<M-p>'
let g:yankring_replace_n_nkey = '<M-n>'

" ---------------
" Session
" ---------------
let g:session_autosave=0
let g:session_autoload=0
nnoremap <leader>os :OpenSession<CR>

" ---------------
" SpeedDating
" ---------------
let g:speeddating_no_mappings=1 " Remove default mappings (C-a etc.)
nmap <silent><leader>dm <Plug>SpeedDatingDown
nmap <silent><leader>dp <Plug>SpeedDatingUp
nmap <silent><leader>dn <Plug>SpeedDatingNowUTC

" ---------------
" Tabular
" ---------------
nmap <Leader>t= :Tabularize /=<CR>
vmap <Leader>t= :Tabularize /=<CR>
nmap <Leader>t: :Tabularize /:\zs<CR>
vmap <Leader>t: :Tabularize /:\zs<CR>
nmap <Leader>t, :Tabularize /,\zs<CR>
vmap <Leader>t, :Tabularize /,\zs<CR>
nmap <Leader>t> :Tabularize /=>\zs<CR>
vmap <Leader>t> :Tabularize /=>\zs<CR>
nmap <Leader>t- :Tabularize /-<CR>
vmap <Leader>t- :Tabularize /-<CR>
nmap <Leader>t" :Tabularize /"<CR>
vmap <Leader>t" :Tabularize /"<CR>

" ---------------
" Fugitive
" ---------------
nmap <Leader>gc :Gcommit -v<CR>
nmap <Leader>gw :Gwrite<CR>
nmap <Leader>gs :Gstatus<CR>
nmap <Leader>gp :Git push<CR>
 " Mnemonic, gu = Git Update
nmap <Leader>gu :Git pull<CR>
nmap <Leader>gd :Gdiff<CR>
" Exit a diff by closing the diff window
nmap <Leader>gx :wincmd h<CR>:q<CR>

" ---------------
" Zoomwin
" ---------------
" Zoom Window to Full Size
nmap <silent> <leader>wo :ZoomWin<CR>

" ---------------
" ctrlp.vim
" ---------------

" Ensure max height isn't too large.
let g:ctrlp_max_height = 10
let g:ctrl_cmd = 'CtrlPMixed'
let g:ctrlp_match_func = {'match' : 'matcher#cmatch' }
let g:ctrlp_working_path_mode = 'ra'

" ---------------
" Vundle
" ---------------
nmap <Leader>bi :BundleInstall<CR>
nmap <Leader>bu :BundleInstall!<CR> " Because this also updates
nmap <Leader>bc :BundleClean<CR>

" ---------------
" Strip Trailing White Space
" ---------------
" From http://vimbits.com/bits/377
" Preserves/Saves the state, executes a command, and returns to the saved state
function! Preserve(command)
  " Preparation: save last search, and cursor position.
  let _s=@/
  let l = line(".")
  let c = col(".")
  " Do the business:
  execute a:command
  " Clean up: restore previous search history, and cursor position
  let @/=_s
  call cursor(l, c)
endfunction
"strip all trailing white space
command! StripTrailingWhiteSpace :call Preserve("%s/\\s\\+$//e")<CR>

imap jj <Esc>
imap uu _
imap hh =>
imap aa @

map <S-Enter> O<ESC>
map <Enter> o<ESC>
imap <C-c> <CR><Esc>O

" Key mappings " {{{
nnoremap <silent> <LocalLeader>rs :source ~/.vimrc<CR>
nnoremap <silent> <LocalLeader>rt :tabnew ~/.vim/vimrc<CR>
nnoremap <silent> <LocalLeader>re :e ~/.vim/vimrc<CR>
nnoremap <silent> <LocalLeader>rd :e ~/.vim/ <CR>

vmap so !sort<CR>
nmap <silent> <leader>w :w<CR>
nmap <silent> <leader>x :bd<CR>

nmap <silent> <Space> <PageDown>
nmap <silent> <M-Space> <PageUp>

nnoremap <leader>a :Ack

noremap  <F2> :NERDTreeToggle<cr>
inoremap <F2> <esc>:NERDTreeToggle<cr>

let g:airline_powerline_fonts = 1
let g:tmuxline_preset = 'crosshair'

"au FileType javascript call JavaScriptFold()

" Post-config
silent! source ~/.vimrc-post

