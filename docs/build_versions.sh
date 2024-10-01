#!/bin/bash

# Automatically detect all versions in the docs/source/versions/ directory
VERSIONS=($(ls -d docs/source/versions/* | xargs -n 1 basename | sort -r))

# Build each version
for version in "${VERSIONS[@]}"; do
  echo "Building documentation for version: $version"
  
  # Set the CURRENT_VERSION environment variable for this version
  export CURRENT_VERSION=$version
  
  # Run sphinx-build with the root conf.py, specifying the source and build directories
  sphinx-build -b html "docs/source/versions/$version" "docs/build/versions/$version" -c "docs/source"

done

# Path to the build directory
BUILD_DIR="docs/build"

# Get the latest version (first item in the array)
LATEST_VERSION=${VERSIONS[0]}

# Automatically detect the repository name from the Git configuration
# Try to extract from GitHub if available, otherwise fallback to the Git remote URL
if [ -n "$GITHUB_REPOSITORY" ]; then
  REPO_NAME=$(echo $GITHUB_REPOSITORY | cut -d'/' -f2)
else
  # Extract from the git remote URL (for local usage)
  REPO_NAME=$(git config --get remote.origin.url | sed 's/.*\/\([^\/]*\)\.git/\1/')
fi

# Create the index.html file with a redirect to the latest version
INDEX_FILE="${BUILD_DIR}/index.html"

echo "Generating index.html to redirect to the latest version: $LATEST_VERSION"

cat <<EOL > $INDEX_FILE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="refresh" content="0; url=https://hms-iac.github.io/$REPO_NAME/versions/$LATEST_VERSION/index.html">
    <title>Documentation Redirect</title>
</head>
<body>
    <p>If you are not redirected automatically, follow this <a href="https://hms-iac.github.io/$REPO_NAME/versions/$LATEST_VERSION/index.html">link to the latest version</a>.</p>
</body>
</html>
EOL

echo "index.html generated with redirect to https://hms-iac.github.io/$REPO_NAME/versions/$LATEST_VERSION/index.html"

# Optionally print a success message
echo "Build complete! Latest version: $LATEST_VERSION"
