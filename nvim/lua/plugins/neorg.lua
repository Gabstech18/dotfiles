return {
  "nvim-neorg/neorg",
  built = ":Neorg sync-parsers",
  config = function()
    require("neorg").setup({
      load = {
        ["core.defaults"] = {},
        ["core.concealer"] = {
          config = {
            folds = true,
            icon_preset = "varied",
          },
        },
        ["core.summary"] = {},
      },
      vim.cmd("set conceallevel=3"),
    })
  end,
}
