<html>
<body>

<form action="form.php" method="post">
Användarnamn: <input type="text" name="Användarnamn"> <br>
Lösenord: <input type="text" name="Lösenord"> <br>
<input type="submit">
</form>

$match = array("fredrikpahlen"=>"apelsin1");

echo $match[fredrikpahlen];
