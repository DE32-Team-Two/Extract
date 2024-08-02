import pandas as pd
from nine_to_twelve.api.ninetotwelve import ice_breaking, req, gen_url

def test_ice_breaking():

    print(ice_breaking())
    
    assert ice_breaking() == """
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...........................................................
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...,.....................................................
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.,....................................................
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,..................................................
        --,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.,..............................................,
        ----,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,....................................,,,.,,,,
        -----,,-,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,.,,,....,.,.,,,.,.,,....,..,..,,,,,,,,,,,
        -----------,-,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        -------------,--,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        -------------------,-,-,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        -------------------,,-------,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ----------------------------------------,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,-
        -~-----------------------------,----------,------,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,---------~-
        ,-~---------------------------------------------,-----,,,,------------------~~:;!*******!!**!*******
        ,-~~~~~~~~~--------------------------------~::;!*****!!!!!!!!!*****=======**=****!***************$**
        ,,-~~:~~~~~~::;;!!!*!!!!!!!!!!!!**========**=********=***********!!!!!!!!!!***!*****!!!**********=*!
        ,,--=#$$$====================*!!;!!******************=**!**!!!!!!!!!!!!!!!!*!!!!!***************!!*!
        ,,,-=$========****************!!!!!!*!***************=*******!!!!!!;;;;;;!!*!!!!!!!!*!!!!!*!!!!!!**!
        ,,,-=$*==***=**************!!*;;;;!!!*****************!!!!!!!!!!!!;;:~~::;!;*!!!!!!!!!!!!!!!!!!!!!*!
        ,,,-=$**===*=*************!!;!:--~:;!!!**!!***!***!!!!!!!!!!!!!!!;;:,..-:;!;=!!!!!!!!!!!!!!;;!!!!!*;
        ,,,-=$***=********!!******!!;;-. ,~;!!!!!!!**!!*!!!!!!:;!!!!!!!;;;:-   .~:;;*!!!!!!!!!!!;;-  :;;;;=;
        ,,,~==****=*****!;::~!==*!!!;~.   -:;!!!!!!!!!!!!!!;:: -:;;;;;;;::~-   ,~:;;!!;;;;;;;;;;;;~-~::::::;
        ,,,;=!******!!!*****!;!*=*!;;-.   -:;;;!!!!!!!!!!;;:~:,,~::;:::::~~-,.,-~::;;!;;;;;;;;;;;::::::;;;~!
        ,,,!=:*!!!;;*=*!!!!***!!**!;:;,. .-:::;;;;;!;;;;;;::~!;-:::;::::::::~~~~::;;:!;;;;;;;;;;;:::::::;::!
        ,,,!=:!!!;!===*=====!=**!*;;:;~,,-~::;;;;!;!;;;;;;:::*;~:::::::~~~:~~~~~~~::::::::~~~~::::::::::::::
        .,,!=:!!!*==$$$$===***!*!!*;;:~~~~:::;;;;;;;;;::::~~:=:~~~~~~--,-~~~.        :        ,::::::~~~::.:
        ..,!=!!!!=$==$$$=$==*=!*!!!=;;;:~~~::;;;;;;;~........-,         ,~~.        .;..,,,,,-::::::~. .:;:!
        ..,!=!!!*$$$$$$$$$$=$==*!!*=!!;::~--:;;;;;;:,        ,-,..,.,,,. ,~~~~~~:::::=::~,~:::::::::::-::;::
        ..,!=!!!=$$$#$$$$=$====!!!*!*!!!~-,,-:;;;;;;:~~~~~~-~;:~~~~~~~~, -~:::::::::~*;;!!*!!;;!!!!;;!!***;;
        ...!*!;!$$$#$$#$$$$====!!!*==***;,,.-:;;;;;;;;::~~~~~:!;;;;;;;;:~~:;!*===*;;:!:~----;*===*!*;,,.,.  
        ..,!!;;!#$##$$$$=$$$==$;!;!!=*=*=!***;;;;;;!=$#$==*;:-*~-------,,,,,,,,,,,,--~!--,,*=*!===***!,....,
        ...!;!!*$$##==$**=====$:;;;*$====;;;;;;:::~~--,,,,,,..*,,,,,,,,.            .-;-,,;#=*~~:!*===!,,,,,
        ..,*=*!!$$#*:*;!!!;!***~:;;*=$=$=~~~~~~~----,.        ;      ,,  .......,,,,,-;---##*-....,:==$;,,,.
        ..,!;~~~=$$;-~~;!;!!;!;~~~:*;=$$*~~~~~~~----,....,,,,,;,,,,,,,,,,,,,,,,,,,,,--;-,-#=~,...   .*#=,   
        ..,!;~~~;==-,,,-:~*;;:~,-~:~~!==;~~~~~~~~-----,,,,,,,,;-,,,,,,,,,,,,....,,,---!~,!#;-,.....-, =#=,,,
        ..,*;~~:~;*--,,.,-~-,-,.,~$=!~!*~~~~~~~~------,,,,,,,,~:--,,,        .,,-,----*~,$@;-~:,.,,. .~##*.,
        ..,!;----;;-,,...,,,,,. .,--,,:*:!***;;~~---,      ...~:,,--,,,,,,,,--------- -, =@:~-,~..;~. .=@$,.
        ...!;--,~~:--,......,..  .,.. ~***!**=#!~~~~---,-,,---:;,----.    . .---------;:-#@:~:~,.....  !##~.
        ...!;----~~--,,... .,,.    .  ~$==$==*#$!~~~-,,.,,.,..;~,~,.,,----------------~!~$#:,,.,. .... :$#*.
        ...!;--,-----,,.. .,,,.      .:$$$===!*@*;~~~---------!:~----------------------!~$#;-,,~-,.....:$#$-
        ..,*:---,----,,....--~~-,.   .*$$==*;,,=$*~~~-~-------!~------,-,,,------,,-,,,;~$##~-,,~,  ...:=$$:
        ..~*~--------,,,...,:~~-,   ..$::~--, .:$*~~----------;:-,,,,,,,,,,,,,,,,,,-,,,;~=#@:--,---~...!*$#*
        ..:*-----~---,,,....,,,.    .-:-~~-.   ,$$!-----,,,,,,:;,,,,,,,,,,,,,,,,,,,-,,-!;=#@*---~-....-#$$$*
        ..!*-----~----,,,,,,,..   ...;-:-.-,.,-,-#*-------,-,,~!,,,,,,,,,,,--,,,,,,-,,-!;=@#@!--,,. .-~#$===
        ..**-----~~----,,-:~~~,-.....:,.~;-~-~,,-@;~-----------!-,,,,,,,,;$#$!,-~~~~~--;!=##@@=~,,,,-,,=$=**
        ..**~----~~~~----,--~:::~-..~-,,..,:-::--$~~~---------~*~--,,-~;=##$=$*~~:;*=*;!!=#@#@#:~---,.,*=##$
        ..!=~----~:::~~--,,--,,.,,,,~-,,~.- ,.. !=~;!**!;;;;:::!=#$*;;;;###$$$!-,,-----~*=#@#@@=~--,,,:!===*
        ..!=~:$#~~:;;::~----~~~-,,,:~---,-;,....-;;:~:::::~~--~=~---::::;;:$;$!,,,--,,--*$##@@@@~-,,,-:!$===
        !=$$##=:~~:;;;:~~-,,,,,,,,~=:--,~,.,,,,.,-~~~~~~~---~::*:--,~:::::,-,=*-,,,-,---*=$#@@@@;---,--!$$==
        $$$###;:~~~:;!;:~-,.,...,~*$;~-,---,,...,::~~~~~--~~:::**---~:::;:,,,,   ,,-----!$###@@@;~-----$$$==
        $$####::~~~~;;!;:-,,...,~!*$*:~,,,.....,;;;:~~~:::::::;!$---~:::::~~,.   .,-----;$#@@@@#!~--,,-#$$$$
        $$$###!:~--~~::;;;~----;;;*$$!:~,,,..,,:;;::~-.::::::;!!*:--::::~;!;,     .-----;=-##@###---,,*#$$$$
        $$$$##$~~---~::::::::-!;;;*=#=;:~-,,,,:::;.~:-.::::::::!*:~::::::~::.      ,----:#:$#####=--,-##$$$$
        $$$####~~----~::~~~~-~;;;*!$$#!:~~~-; ~:::,--,-:~~::!!~*;:~::::::-:~.       ,--~:$######@@#$=###$$$$
        $$$$###=-~---~::~~~--=!;;*!$=$*:~--;!*.:::-.~.,- ~:;!*:*;;:~.::::,~-.        --~:$$##@##@@######$$$$
        $$$$####!~~---~::~~-;$=!!*!*$$=---;;!*-:~;~ ,. . ,:;!;**!;;;~:;;!;**~---~~~~~~:::::;;~#@#@@@####$$$$
        $$$#$####;~~~~~~~--~#$==$$!*$==:-~=:!:::~;:. ..  -;!!:;!*;;;;!*!!!!!!!!!;;!!!!!!!!!!!;*#@@@@####$$$$
        $$$$$$####~~~:::~~~*$$$$#$*!=$!!:=!;*;;::::..-,..,;!*~:*!;;;:!-~-~!!!!!!!!!!!!!!!!!;;;;########$==$=
        =$$$$$#$##$~~:~~~~~$$=$=##=$=**!=;;;!*!!~~:.-~,  ,;!:~:;!;:;-;----!!!!!!!!!!!!!!!!;;;;;#$#####$$$==$
        ===$$$$#####:~~~~-*$$$$$##======*=;;!=;!~.~, .-- .!*;;:;;:!;,~!-,,~!!!!!!!!!!!!!!!!;;;;:$#####$$$$=#
        ===$$$$######*~-,,=$$$=$##$====*==!;*=;!:-:~,-~. ,!*!:.,~*;:--:!!!!!!!!!!!!!!!!!!;;;;;;;=####$=$$$*!
        ==$$$$$#####@##$=*=$$$=$#@$=====*=!!**!!!;~---:. -***...,,.....!!!!!!!!!!!!!!!!!!!!;;;;;;###$$$$$$;!
        =$=$$$###########$$$$$=$##$=$===$=**=**!;;~---!. ,~-!,,.,......:!!!!!!!!!!!!!!!!!!!;;;;;;$##@@@####@
        $$==$$$#######$$$$$$$$=$##$$$$=$==**=!*!*!---~;. ..,--..,...   .;!!!!!!!!!!!!!!!!!!!!;;;;!~,$#######
        $$$$$$##########$$$$$$$$##$$$$$$=$==*=**;:-,-,. .,,::~~~-=,-~~:-~;;;!!!!!!!!!*!!!!!!!;;;;:-~=$#$#$$#
        $=$$$$#########$$$$$$$$$##$$$$$$$$==*$==:~-,,,:;;;;-:~!!!!##=#!:.;;;!!!!******!!!!!!!!;;;;-,===$$=$#
    """
    assert True

def test_data_check():
    df = req()

    print(df)

    assert len(df) > 1

def gen_url():
    print(gen_url())