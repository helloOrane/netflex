/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
    colors: {
      "amber-400": "#fbbf24",
      "amber-600": "#d97706",
    },
  },
  plugins: [require("flowbite/plugin")],
};
