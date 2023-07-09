# Start from the official Ruby image
FROM ruby:3.2.2

# Install dependencies
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

# Set the working directory inside the Docker container
WORKDIR /myapp

# Copy the Gemfile and Gemfile.lock into the working directory
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock

# Install gems
RUN bundle install --without development test

# Copy the rest of the application into the working directory
COPY . /myapp

# Precompile Rails assets
RUN RAILS_ENV=production bundle exec rake assets:precompile

# Expose port 3000 to the Docker host, so we can access our application
EXPOSE 3000

# The command to start our application
CMD ["rails", "server", "-e", "production", "-b", "0.0.0.0"]
