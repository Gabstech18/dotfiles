return {
  "JosefLitos/colorizer.nvim",
  config = function()
    require("colorizer").setup({
      filetypes = { "*" },
    })
  end,
}
