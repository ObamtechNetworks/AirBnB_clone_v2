#!/usr/bin/env bash
# a bash script that sets up web servers for deplyment of web_static

# install nginx if not already installed
sudo apt install -y nginx

# function to handle directory creation
create_directory() {
        local directory="$1"

        # check if the directory already exists
        if [ ! -d "$directory" ]; then
                echo "Creating $directory directory..."
                sudo mkdir "$directory"
        else
                echo "$directory directory already exists."
        fi
}

# create a folders /data/, /web_static/, etc  if it doens't already exist
# folderst to create, store them in variables
data_folder="/data"
web_static_folder="$data_folder/web_static"
release_folder="$web_static_folder/releases"
shared_folder="$web_static_folder/shared"
test_folder="$release_folder/test"

# folder symbolic links
web_static_current="$web_static_folder/current"

# call function on these directories above for creation
# for /data/
create_directory "$data_folder"

# for /data/web_static/
create_directory "$web_static_folder"

# for /data/web_static/release_folder/
create_directory "$release_folder"

# for /data/web_static/shared/
create_directory "$shared_folder"

# for /data/web_static/releases/test/
create_directory "$test_folder"

# for /data/web_static/current
# create_directory "$web_static_current"

# create file if not already exist
fake_html="$test_folder/index.html"

if [ ! -e "$fake_html" ]; then
        echo "Creating fake html file $fake_html..."
        sudo touch "$fake_html"
        # add simple content
        echo -e "<h1>HELLO SOMEBODY!</h1>" | sudo tee "$test_folder/index.html"
else
        echo "$fake_html already exists."
fi

# create symbolic links
# check if symbolic link already exists
if [ -L "$web_static_current" ]; then
        echo "Removing existing symb link: $web_static_current"
        sudo rm -rf "$web_static_current"
else
        # create a new symb link
        sudo ln -s "$test_folder" "$web_static_current"
fi

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.

sudo chown -R ubuntu:ubuntu "$data_folder"

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/^}$/i \\n    location \/hbnb_static {\n        alias \/data\/web_static\/current;\n        index index.html;\n    }' /etc/nginx/sites-available/default

# restart server
sudo service nginx restart
