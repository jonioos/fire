# fire
A fancy parse engine for JML (Jonio Markup Language) files

<h2>What's FIRE?</h2>
<p>Fire it's a parser engine which will read JML files</p>

<h2>What's JML (Jonio Markup Language)?</h2>
<p>JML is a new stunning markup language easier to understand and faster to read and write</p>

<h2>Ok, but what can I do?</h2>
<p>The syntax is very simple. You can write the key inside square brackets and the value. For now it supports up to 5 type of objects: Strings, Int, Boolean, Tuple and Lists. The fire engine will read the file and return the objects.</p>

<h2>What's the syntax?</h2>
<p>To write a simple string you have to write the follow code, the name inside square brackets can be everything you want:</br></br>
  <code>[KEYNAME]"String"</code></br></br>
  Or if you want to save a Int you have to write the follow code:</br></br>
  <code>[KEYINT]0</code></br>
  If you want to make a list (Lists are typed, which means you cant put inside the same list strings or boolean together):</br></br>
  <code>[LISTSAMPLE]"First Element"|"Second Element"</code></br>
  And if you want to make a tuple you have to write the follow code:</br></br>
  <code>[TUPLESAMPLE]"string"/0/True/</code></br>
  (Yes, boolean values need the capital letter)</br>
</p>
