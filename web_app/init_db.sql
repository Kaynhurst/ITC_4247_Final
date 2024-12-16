/*-- Create Tasks table if it doesn't already exist
CREATE TABLE IF NOT EXISTS rest_api_tasks (
    id BIGINT PRIMARY KEY,
    task CHARACTER VARYING(180) NOT NULL,
    description CHARACTER VARYING(400),
    timestamp TIMESTAMP WITH TIME ZONE,
    completed BOOLEAN,
    updated TIMESTAMP WITH TIME ZONE,
    user_id INTEGER
);
*/
-- Insert task data into the table
INSERT INTO rest_api_tasks (id, task, description, timestamp, completed, updated, user_id)
VALUES 
    (1, 'Make soup', 'Gather the ingridients', '2024-12-15 20:13:20.566959+00', FALSE, '2024-12-15 20:13:20.566978+00', 1),
    (2, 'Get the dog', 'Animal shelter near the store.', '2024-12-15 20:13:33.205051+00', FALSE, '2024-12-15 20:13:33.205082+00', 1),
    (3, 'New Simple Task', 'Be productive', '2024-12-15 20:30:56.693376+00', TRUE, '2024-12-15 20:30:56.6934+00', 1),
    (4, 'Finish the Project', 'Do everything', '2024-12-15 20:37:17.940634+00', FALSE, '2024-12-15 20:37:17.940653+00', 1),
    (5, 'Touch grass', 'You know what to do.', '2024-12-15 20:15:03.86957+00', FALSE, '2024-12-15 20:15:03.869768+00', 1)
ON CONFLICT (id) DO NOTHING;




/*-- Create table for auth_user if it doesn't already exist
CREATE TABLE IF NOT EXISTS auth_user (
    
    id INTEGER PRIMARY KEY,
    password CHARACTER VARYING(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL,
    username CHARACTER VARYING(150) NOT NULL,
    first_name CHARACTER VARYING(150),
    last_name CHARACTER VARYING(150),
    email CHARACTER VARYING(254),
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL
);
*/
-- Insert data into the auth_user table
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES
    (1, 'pbkdf2_sha256$600000$jSucj5SwVk5J298bMax6d5T8W/J7NVwjzHNBU0gyuVOXrMAP6GXq0b6zY6D6l...', '2024-12-15 13:08:58.789014+00', TRUE, 'admin', '', '', 'admin@admin.edu', TRUE, TRUE, '2024-12-15 20:00:04.464980+00')
ON CONFLICT (id) DO NOTHING;
