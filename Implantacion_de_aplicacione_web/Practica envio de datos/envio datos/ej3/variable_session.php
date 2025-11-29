<?php
$carpetaImagenes = "imagenes";

// Verificar que la carpeta existe
if (!is_dir($carpetaImagenes)) {
    die("Error: El directorio 'imagenes' no existe.");
}

// Leer archivos
$archivos = scandir($carpetaImagenes);

// Extensiones permitidas
$extensionesPermitidas = ["jpg", "jpeg", "png", "gif", "webp"];
?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Listado de imágenes</title>
</head>
<body>

<h2>Listado de imágenes del directorio "<?= $carpetaImagenes ?>"</h2>

<ul>
<?php
foreach ($archivos as $archivo) {

    $ruta = $carpetaImagenes . "/" . $archivo;
    $extension = strtolower(pathinfo($archivo, PATHINFO_EXTENSION));

    // Mostrar solo archivos válidos de imagen
    if (is_file($ruta) && in_array($extension, $extensionesPermitidas)) {

        echo "<li>";
        echo "<a href='$ruta' target='_blank'>";
        echo "<img src='$ruta'>";
        echo $archivo;
        echo "</a>";
        echo "</li>";
    }
}
?>
</ul>

</body>
</html>