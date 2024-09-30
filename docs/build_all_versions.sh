#!/bin/bash

# Ensure the build directory exists
mkdir -p build

# Clear the build directory to avoid conflicts
rm -rf build/html

# Get all version directories inside docs/versions/
VERSIONS=$(ls -d docs/versions/*/ | xargs -n 1 basename)

# Build each version
for VERSION in $VERSIONS; do
  echo "Building documentation for version: $VERSION"
  
  # Check if Makefile exists inside the source folder
  if [ ! -f "docs/versions/$VERSION/source/Makefile" ]; then
    echo "No Makefile found for version: $VERSION, skipping..."
    continue
  fi
  
  # Create the build directory for this version
  mkdir -p "build/${VERSION}"

  # Run the make command within the version's source directory
  (cd "docs/versions/$VERSION/source" && make html)

  # Check if the HTML was built
  if [ ! -d "docs/versions/$VERSION/source/_build/html" ]; then
    echo "HTML build failed for version: $VERSION"
    continue
  fi
  
  # Move the built HTML files to the main build directory
  mv "docs/versions/$VERSION/source/_build/html" "build/${VERSION}"
done

# Create a redirect from the main index.html to the latest version
LATEST_VERSION=$(echo "$VERSIONS" | sort -r | head -n 1)
echo "Creating main index.html with a redirect to the latest version: $LATEST_VERSION"

# Ensure build directory exists before writing the index.html
mkdir -p build

cat <<EOF > build/index.html
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url=./$LATEST_VERSION/index.html">
    <title>Redirecting to the latest version</title>
  </head>
  <body>
    <p>If you are not redirected automatically, follow this <a href="./$LATEST_VERSION/index.html">link to the latest version</a>.</p>
  </body>
</html>
EOF

echo "All versions have been built, and main index.html redirects to $LATEST_VERSION"
