vim.cmd("set expandtab")
vim.cmd("set tabstop=2")
vim.cmd("set softtabstop=2")
vim.cmd("set shiftwidth=2")

vim.cmd("set nu")
vim.cmd("set relativenumber")
vim.g.mapleader = " "

--MOVE LINES WITH ALT WITHIN TEXT
--VISUAL
vim.keymap.set("v", "<C-j>", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "<C-k>", ":m '<-2<CR>gv=gv")
--NORMAL
vim.keymap.set("n", "<C-j>", ":m .+1<CR<==<ENTER>==")
vim.keymap.set("n", "<C-k>", ":m .-2<CR<==<ENTER>==")
--INSERT
vim.keymap.set("i", "<C-j>", "<Esc>:m .+1<CR>==gi")
vim.keymap.set("i", "<C-k>", "<Esc>:m .-2<CR>==gi")

--configuracion de algunos movimientos
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

vim.opt.hlsearch = false
vim.opt.incsearch = true
vim.opt.scrolloff = 8

--configuracion de agregado de comentarios
vim.keymap.set("n", "<leader>ac", "<Cmd>set formatoptions=croql<CR>")
vim.keymap.set("n", "<leader>dc", "<Cmd>set formatoptions=<CR>")

-- agregando clipboard ctrl c y ctrl p
vim.keymap.set("v", "<C-c>", '"+y')
vim.keymap.set("v", "<C-p>", '"+p')
vim.keymap.set("n", "<C-p>", '"+p')

--Agregar salto de lina hacia abajo
vim.keymap.set("n", "G", "Gzz")

--Identacion sin formater
vim.keymap.set("n", "<leader>gg", "ggVG==")

