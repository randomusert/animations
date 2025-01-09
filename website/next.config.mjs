/** @type {import('next').NextConfig} */

const config = {
    webpack(config, { isServer }) {
      // Custom Webpack rule for video files
      config.module.rules.push({
        test: /\.(mp4|webm|ogg)$/i,
        use: {
          loader: "file-loader", // Ensure file-loader is installed
          options: {
            publicPath: "/_next/static/media/",
            outputPath: "static/media/",
            name: "[name].[hash].[ext]",
          },
        },
      });
  
      return config;
    },
  };
  
export default config;
  