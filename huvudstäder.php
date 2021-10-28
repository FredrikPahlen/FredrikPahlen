<?php
$huvudstader = array("Sverige"=>"Stockholm", "Finland"=>"Helsingfors", "Norge"=>"Oslo", "Danmark"=>"Köpenhamn", "Island"=>"Reykjavik", "Estland"=>"Tallinn", "Lettland"=>"Riga", "Litauen"=>"Vilnius");

foreach($huvudstader as $key => $value){
  echo "$key" . "s huvudstad heter " . "$value";
  <br>;

}
