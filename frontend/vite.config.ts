import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// base is "/devstral-lab/" for production builds (GitHub Pages project site)
// and "/" in dev so the local proxy keeps working.
export default defineConfig(({ command }) => ({
  base: command === "build" ? "/devstral-lab/" : "/",
  plugins: [react()],
  server: {
    host: "127.0.0.1",
    port: 5175,
    strictPort: false,
    proxy: { "/api": "http://127.0.0.1:8788" },
  },
}));
