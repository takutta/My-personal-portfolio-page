/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    './templates/**/*.html',
    './projektit/**/*.html'
  ],
  theme: {
    fontFamily: {
      teksti: ["Alata", "cursive"],
      otsikko: ["Amethysta", "cursive"]
    },
    },
  plugins: [
    require('daisyui' ),
    require('@tailwindcss/typography')
  ],
  daisyui: {
    themes: [
      {
        dracula: {
          ...require("daisyui/src/colors/themes")["[data-theme=dracula]"],
          primary: "#D4441E",
          secondary: "#BFC906",
          accent: "#FBBA07"
        },
      },
    ],
  },
}
