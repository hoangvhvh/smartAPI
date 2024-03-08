<?php

$target_dir = "uploads/"; 


function is_image($filename) {
    $allowed_extensions = array("jpg", "jpeg", "png", "gif");
    $ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
    return in_array($ext, $allowed_extensions);
}


$files = scandir($target_dir);


$images = array_filter($files, function($file) use ($target_dir) {
    return is_image($target_dir . $file);
});


$html = "";
foreach ($images as $image) {
    $html .= "<img src='" . $target_dir . $image . "' alt='" . $image . "'>";
}

echo $html;

?>
