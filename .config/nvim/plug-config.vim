" Airline
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1

set termguicolors     " enable true colors support
let ayucolor="mirage"   " for dark version of theme
colorscheme ayu
let g:airline_theme = 'ayu'

" File explorer
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | exe 'cd '.argv()[0] | endif

" Indent line
let g:indentLine_setColors = 239
let g:indentLine_char = '¦'