#!/bin/bash

# Clear the build directory to avoid conflicts
rm -rf build/html

# Get all version directories inside source/versions/
VERSIONS=$(ls -d source/versions/*/ | xargs -n 1 basename)

# Build each version
for VERSION in $VERSIONS; do
  echo "Building documentation for version: $VERSION"
  export CURRENT_VERSION=$VERSION
  make html
  mv build/html "build/${VERSION}"
done

# Create a redirect from the main index.html to the latest version
LATEST_VERSION=$(echo "$VERSIONS" | sort -r | head -n 1)
echo "Creating main index.html with a redirect to the latest version: $LATEST_VERSION"
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
