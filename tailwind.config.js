module.exports = {
  purge: {
    enabled: true,
    content: [
      '../**/templates/*.html',
      '../**/templates/**/*.html'
    ]

  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      'blue1': '#023e8a',
      'blue2': '#0057c4',
      'grey1': '#3B3B3B',
      'grey2': '#272727',
      'red1': '#ff3347'
      
    },
  },
  variants: {
    extend: {

    },
  },
  plugins: [],
}
