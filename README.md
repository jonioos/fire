# FIRE Engine
A fancy parse engine for JML (Jonio Markup Language) files

<h2>What's FIRE?</h2>
<p>Fire it's a parser engine which will read JML files</p>

<h2>What's JML (Jonio Markup Language)?</h2>
<p>JML is a new stunning markup language easier to understand and faster to read and write</p>

<h2>Ok, but what can I do?</h2>
<p>The syntax is very simple. You can write the key inside square brackets and the value. For now it supports up to 5 type of objects: Strings, Int, Boolean, Tuple and Lists. The fire engine will read the file and return the objects.</p>

<h2>What's the syntax?</h2>
<p>To write a simple string you have to write the follow code, the name inside square brackets can be everything you want:</br>
</br>
  <code>[MY_NAME]"Bob"</code></br></br>
  Or if you want to save a Int you have to write the follow code:</br></br>
  <code>[KEYINT]0</code></br></br>
  If you want to make a list (Lists are typed, which means you cant put inside the same list strings or boolean together):</br>
  </br>
  <code>[LISTSAMPLE]"Alice"|"Bob"</code></br></br>
  And if you want to make a tuple you have to write the follow code:</br></br>
  <code>[TUPLESAMPLE]"Alice"/0/True/</code></br></br>
  (Yes, boolean values need the capital letter)</br>
</p>
<h2> GROUPS! </h2>
<p> Yeah! You can actually make groups! To make groups you have to use the round brackets
</br>
```
  (ADDRESS_GROUP)
  [NAME]"Alice". 
  [SURNAME]"Bob". 
  [ADDRESS]"123 Evergreen Terrace". 
  [HOBBIES]"Guitar"|"Photography". 
  (ENDGROUP). 
  (ADDRESS_GROUP)  
  [NAME]"Alice"  
  [SURNAME]"Bob"  
  [ADDRESS]"123 Evergreen Terrace"  
  [HOBBIES]"Guitar"|"Photography"  
  (ENDGROUP)
  ```
** Remember, the tag (ENDGROUP) is important! </p>

 ```
