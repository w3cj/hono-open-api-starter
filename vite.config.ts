import path from 'node:path'
import { defineConfig } from 'vite'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
	plugins: [tsconfigPaths()],
	build: {
		lib: {
			entry: path.resolve(__dirname, 'src/index.ts'),
			formats: ['es'],
			fileName: 'index',
		},
		rollupOptions: {
			external: [
				// Node.js built-ins
				/^node:.*/,
				// All dependencies from package.json
				'@hono/node-server',
				'@hono/zod-openapi',
				'@scalar/hono-api-reference',
				'dotenv',
				'dotenv-expand',
				'drizzle-orm',
				'hono',
				'hono-pino',
				'pino',
				'pino-pretty',
				'postgres',
				'stoker',
				'zod',
			],
		},
		outDir: 'dist',
		target: 'node22',
		ssr: true,
		sourcemap: true,
	},
	resolve: {
		alias: {
			'~': path.resolve(__dirname, './src'),
		},
	},
})
