<?php

require_once "./bootstrap.php";

$newProductName = $argv[1];

$product = new Product();
$product->setName($newProductName);

$entityManager->persist($product);
$entityManager->flush();

echo sprintf("Created product with id %d", $product->getId());
