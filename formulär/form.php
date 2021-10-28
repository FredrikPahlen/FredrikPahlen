<html>
<body>

<?php

$txt = $_POST["Användarnamn"];
$lösenord = $_POST["Lösenord"];
if ($txt=="fredrikpahlen" and $lösenord=="apelsin1")
    echo "Grattis, rätt inloggningsuppgifter!";
//om både användarnamn och lösenord är rätt
if ($txt=="fredrikpahlen" and $lösenord!="apelsin1")
    echo "Användarnamnet är rätt, men pröva ett annat lösenord";
//om endast användarnamnet är korrekt

if ($txt!="fredrikpahlen" and $lösenord=="apelsin1")
   echo "Rätt lösenord, men användarnamnet är tyvärr fel";
//om endast lösenordet är korrekt

if ($txt!="fredrikpahlen" and $lösenord !="apelsin1")
   echo "Fel inloggningsuppgifter";
//om både användarnamn och lösenord fel

?>

</body>
</html>
