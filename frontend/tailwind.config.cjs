module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
      },
      gridTemplateColumns: {
        '70/30': '70% 28%',
      },
      colors: {
        primary: '#343959',
        secondary: {
          default: '#0B7781',
          light: '#119DAA',
          dark: '#0f799b',
        },
        accent: '#f59e0b',
        modal: '#272B4A',
        background: '#181A2A',
        sideground: '#292834',
        brand: {
          light: '#3b82f6',
          DEFAULT: '#1d4ed8',
          dark: '#1e3a8a',
        },
      },
    },
  },
  plugins: [],
};