import type { Config } from 'tailwindcss'
import typography from '@tailwindcss/typography'

export default {
    content: [],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            },
            colors: {
                awabot: {
                    orange: '#FF7E22',
                    yellow: '#FAC130',
                },
            },
        },
    },
    plugins: [typography],
} satisfies Config
