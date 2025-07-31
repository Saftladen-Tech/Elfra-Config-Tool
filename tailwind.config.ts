module.exports = {
    content: [
        "./app/templates/**/*.html",
        "./app/static/js/**/*.js"
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    primary: "#669c35",
                    secondary: "#aaaaaa",
                    accent: "#fde1af",
                    dark: "#0e0e11",
                    bright: "#ffffff",
                    success: "#00DC82",
                    warn: "#fcc800",
                    error: "#ff6467",
                    black: "#171717",
                },
            },
            fontFamily: {
                sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'sans-serif', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'],
            },
            plugins: [],
        },
    },
}