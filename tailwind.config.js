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
    require('tailwindcss-fluid-type'),
    require('@tailwindcss/typography')
  ]
}
