<?php

class User
{
    private string $username;
    private string $password;
    private bool $isAdmin;

    public function __construct(string $username, string $password, ?bool $isAdmin = false)
    {
        $this->username = $username;
        $this->password = $password;
        $this->isAdmin = $isAdmin;
    }

    public function getUsername()
    {
        return $this->username;
    }

    public function getPassword()
    {
        return $this->password;
    }

    public function getIsAdmin()
    {
        return $this->isAdmin;
    }
}

$users = [
    new User("admin", "secure", true),
    new User("john_doe", "secure", false),
];
