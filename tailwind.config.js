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
    extend: {},
  },
  plugins: [require("tailwindcss-fluid-type"), require("daisyui")],
}