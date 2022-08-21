

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_20326449585527495860449834516309156618926102419378288491298949181828016993584656862954444967831146003129901901260711160962257629153967749207483354176669953919176796444741299039580320192654577727539125926584106755062587030254295822172393751897133892256648145970874774478251106012708960409317407807274235035861825570371547345619809460241972892415625991277152538920538638723170027607448813701474316231219613823052506743322991703390348178943440496425043154916198801542108528371572880571017853741192010420339790617581929743285308913733291755212589081288918825499760442382541178095301824844511414477229250027024972458842487 = Integer(20326449585527495860449834516309156618926102419378288491298949181828016993584656862954444967831146003129901901260711160962257629153967749207483354176669953919176796444741299039580320192654577727539125926584106755062587030254295822172393751897133892256648145970874774478251106012708960409317407807274235035861825570371547345619809460241972892415625991277152538920538638723170027607448813701474316231219613823052506743322991703390348178943440496425043154916198801542108528371572880571017853741192010420339790617581929743285308913733291755212589081288918825499760442382541178095301824844511414477229250027024972458842487); _sage_const_17058507585412040045298406489145987136726884330845064983490422386641362731763575374465739739918144979059081889485438057079864626405054183714749985596978580186902978805822976838984965323538825959258842321470554534281199713042887758854055408707365037277139862922869059040165866385585231637419868300705068359594037032594130001480668295660927886398733147207693938855904000371127922317183503023137047962118035239917772185719061158191054429319408347508765722481250290113651673276369477912877833118725607201757440380675514080972193541070288682769405088323579315853193723544668668542471143665039007236036976946388940919745152 = Integer(17058507585412040045298406489145987136726884330845064983490422386641362731763575374465739739918144979059081889485438057079864626405054183714749985596978580186902978805822976838984965323538825959258842321470554534281199713042887758854055408707365037277139862922869059040165866385585231637419868300705068359594037032594130001480668295660927886398733147207693938855904000371127922317183503023137047962118035239917772185719061158191054429319408347508765722481250290113651673276369477912877833118725607201757440380675514080972193541070288682769405088323579315853193723544668668542471143665039007236036976946388940919745152); _sage_const_3 = Integer(3); _sage_const_256 = Integer(256); _sage_const_72 = Integer(72); _sage_const_0p05 = RealNumber('0.05'); _sage_const_0 = Integer(0)
from Crypto.Util.number import bytes_to_long, long_to_bytes

n = _sage_const_20326449585527495860449834516309156618926102419378288491298949181828016993584656862954444967831146003129901901260711160962257629153967749207483354176669953919176796444741299039580320192654577727539125926584106755062587030254295822172393751897133892256648145970874774478251106012708960409317407807274235035861825570371547345619809460241972892415625991277152538920538638723170027607448813701474316231219613823052506743322991703390348178943440496425043154916198801542108528371572880571017853741192010420339790617581929743285308913733291755212589081288918825499760442382541178095301824844511414477229250027024972458842487 
c = _sage_const_17058507585412040045298406489145987136726884330845064983490422386641362731763575374465739739918144979059081889485438057079864626405054183714749985596978580186902978805822976838984965323538825959258842321470554534281199713042887758854055408707365037277139862922869059040165866385585231637419868300705068359594037032594130001480668295660927886398733147207693938855904000371127922317183503023137047962118035239917772185719061158191054429319408347508765722481250290113651673276369477912877833118725607201757440380675514080972193541070288682769405088323579315853193723544668668542471143665039007236036976946388940919745152 

e = _sage_const_3 

R = Zmod(n)['m']; (m,) = R._first_ngens(1)

message = "Dear Sir/Madam,\n\n" + "I am writing this email to let you know about our new CTF.\n" + "The CTF is hosted at https://welcomectf.nusgreyhats.org/ \n" + "We have a rsa encryption challenge here. Do you want to try and solve it?\n\n" 
f = (bytes_to_long(message.encode()) * _sage_const_256 **_sage_const_72  + m)**e - c

print(long_to_bytes(int(f.small_roots(X=_sage_const_256 **_sage_const_72 , epsilon=_sage_const_0p05 )[_sage_const_0 ])))
