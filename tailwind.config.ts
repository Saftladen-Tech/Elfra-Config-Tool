module.exports = {
    content: [
        "./app/templates/**/*.html",
        "./app/static/js/**/*.js"
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#1D4ED8', // blue-700
                    light: '#3B82F6', // blue-500
                    dark: '#1E40AF' // blue-800
                },
            },
            fontFamily: {
                sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'sans-serif', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'],
            },
            plugins: [],
        },
    },
}