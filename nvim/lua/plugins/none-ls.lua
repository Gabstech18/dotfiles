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
				--Configuration for linting and formating ruby
				null_ls.builtins.diagnostics.rubocop,
				null_ls.builtins.formatting.rubocop,
				--configuration for linting and formating python
				null_ls.builtins.diagnostics.pylint,
				null_ls.builtins.formatting.pyink,
				--null_ls.builtins.formatting.black,
				--null_ls.builtins.formatting.isort,

				--configuration for linting and formating js
				null_ls.builtins.formatting.prettier,
			},
		})
		vim.keymap.set("n", "<leader>gf", vim.lsp.buf.format, {})
	end,
}
