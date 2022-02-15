<?php

require_once './vendor/autoload.php';
require "./user.php";
session_start();
$loader = new Twig_Loader_Filesystem('./views');
$twig = new Twig_Environment($loader, []);

$submitButtonHTML = '<input type="submit" value="Log In" />';
$loginHeaderText = "Log In";
$isAdminLogin = $_GET['admin'] === 'true' ? true : false;
$totalSiteLogins = isset($_SESSION["totalSiteLogins"]) ? $_SESSION["totalSiteLogins"] : '0.00';
$error = null;

if (isset($_POST['username']) && isset($_POST['password'])) {
    $user = findUserByUsernameAndPassword($_POST['username'], $_POST['password'], $users);

    if ($user !== null) {
        $isValidSession = $user->getIsAdmin() === $isAdminLogin;

        if ($isValidSession) {
            if (isset($_SESSION["totalSiteLogins"])) {
                $totalSiteLogins = $_SESSION["totalSiteLogins"];
            }
            $totalSiteLogins++;
            $_SESSION["totalSiteLogins"] = $totalSiteLogins;
        }
    }
    $error = "User not found";
}

function findUserByUsernameAndPassword(string $username, string $password, $users)
{
    foreach ($users as $user) {
        if ($username === $user->getUsername() && $password === $user->getPassword()) {
            return $user;
        }
    }
    return null;
}

echo $twig->render('index.twig', compact(
    "submitButtonHTML",
    "loginHeaderText",
    "isAdminLogin",
    "totalSiteLogins",
    "error"
));
