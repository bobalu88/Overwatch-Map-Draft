const webpack = require('webpack');
const config = {
    entry:  __dirname + '/src/index.js',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
        publicPath: '/public/'
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.jsx?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        }
      ]
    },
};
module.exports = config;