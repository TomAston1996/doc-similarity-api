-- Create the document table
CREATE TABLE document (
  id SERIAL PRIMARY KEY,  -- Use SERIAL for auto-incrementing
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Insert some test data
INSERT INTO document (title, content)
VALUES 
  ('Test Title', 'Some Text'),
  ('Another Test Title', 'Some other text');