<?php

$target_dir = "uploads/"; 
$allowed_extensions = array("jpg", "jpeg", "png", "gif"); 
$max_file_size = 500000; 

if (isset($_FILES["image"]) && !empty($_FILES["image"]["tmp_name"])) {

   
    $imageFileType = strtolower(pathinfo($_FILES["image"]["name"], PATHINFO_EXTENSION));

    if (!in_array($imageFileType, $allowed_extensions)) {
        echo "Error: Only JPG, JPEG, PNG & GIF files are allowed.";
        exit; 
    }

    
    if ($_FILES["image"]["size"] > $max_file_size) {
        echo "Error: File size exceeds limit (" . $max_file_size . " bytes).";
        exit; 
    }

  
    $target_file = $target_dir . md5(uniqid()) . "." . $imageFileType;

    
    if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
        echo "The file " . htmlspecialchars(basename($_FILES["image"]["name"])) . " has been uploaded successfully.";
    } else {
        echo "Error: An error occurred while uploading the file.";
    }
} else {
    echo "No image selected for upload.";
}

?>
