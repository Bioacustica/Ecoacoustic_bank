module.exports = {
  webpackDevServer: (config) => {
    config.watchOptions = {
      ignored: /node_modules/,
      aggregateTimeout: 300,
    };
    config.hot = true; // Habilitar HMR
    return config;
  },
  style: {
    postcss: {
      plugins: [require("tailwindcss"), require("autoprefixer")],
    },
  },
};
