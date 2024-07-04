return {
	"nvimtools/none-ls.nvim",
	dependencies = {
		"nvimtools/none-ls-extras.nvim",
	},
	config = function()
		local null_ls = require("null-ls")

		null_ls.setup({
			sources = {
				null_ls.builtins.formatting.stylua,
				--configuration for linting and formating python
				null_ls.builtins.diagnostics.pylint,
				null_ls.builtins.formatting.pyink,

				--configuration for linting and formating js
				null_ls.builtins.formatting.prettier,

				--configuration for linting and formating cpp
        null_ls.builtins.formatting.clang_format

        --Formater for django
        ,null_ls.builtins.formatting.djlint
			},
		})
		vim.keymap.set("n", "<leader>gf", vim.lsp.buf.format, {})
	end,
}
