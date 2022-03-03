# Credit-Card-Validation
Validate the Credit numbers based on the following conditions: 
<p>
Begins with 4,5, or 6 </p>
<p>Contain exactly 16 digits</p>
<p>Contains only numbers ( 0 to 9 )</p>
<p>For every 4 digits a hyphen (-) may be included (not mandatory)</p>
<p>No other special character permitted</p>
<p>Must not have 4 or more consecutive same digits</p>
<pre>
Input                  Output:
4253625879615786        Valid
4424424424442444        Valid
5122-2368-7954-3214     Valid
42536258796157867       Invalid
4424444424442444        Invalid
5122-2368-7954 - 3214   Invalid
44244x4424442444        Invalid
0525362587961578        Invalid
61234-567-8912-3456     Invalid
</pre>
