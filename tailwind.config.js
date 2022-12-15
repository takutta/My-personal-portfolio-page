/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  corePlugins: {
    fontSize: false,
    // ...
},
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