import type { Config } from 'tailwindcss'
import typography from '@tailwindcss/typography'

export default {
    content: [
        './app/**/*.{vue,js,ts,jsx,tsx}',
        './components/**/*.{vue,js,ts}',
        './layouts/**/*.vue',
        './pages/**/*.vue',
        './plugins/**/*.{js,ts}',
        './nuxt.config.{js,ts}'
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            },
            colors: {
                awabot: {
                    orange: '#ff7e22',
                    yellow: '#fac130',
                    carbon: '#111111',
                    chalk: '#F5F6F7',
                },
            },
        },
    },
    plugins: [typography],
} satisfies Config
