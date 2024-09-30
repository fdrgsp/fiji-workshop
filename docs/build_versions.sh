#!/bin/bash

# Automatically detect all versions in the docs/source/versions/ directory
VERSIONS=($(ls -d docs/source/versions/* | xargs -n 1 basename | sort -r))

# Build each version
for version in "${VERSIONS[@]}"; do
  echo "Building documentation for version: $version"
  (cd docs/source/versions/$version && make html)
done

# Path to the build directory
BUILD_DIR="docs/build"

# Get the latest version (first item in the array)
LATEST_VERSION=${VERSIONS[0]}

# Create the index.html file with a redirect to the latest version
INDEX_FILE="${BUILD_DIR}/index.html"

echo "Generating index.html to redirect to the latest version: $LATEST_VERSION"

cat <<EOL > $INDEX_FILE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="0; url=/versions/$LATEST_VERSION/html/index.html">
    <title>Redirecting...</title>
</head>
<body>
    <p>If you are not redirected, <a href="/versions/$LATEST_VERSION/html/index.html">click here</a>.</p>
</body>
</html>
EOL

echo "index.html generated with redirect to /versions/$LATEST_VERSION/html/index.html"

# Optionally print a success message
echo "Build complete! Latest version: $LATEST_VERSION"
