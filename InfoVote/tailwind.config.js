/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    './**/templates/**/*.html'  // for apps' templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}