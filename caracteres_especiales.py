"""
    CARACTERES ESPECIALES Y SU SIGNIFICADO

    [] : Un set de caracteres ,ejmp [a-z] de la a la z
    \ : Una secuencia especial o caractes especial, ejmp \d el car debe ser entero
    . : Cualquier char menos nueva linea ejmp M.xi
    ^ : El string debe empezar con el siguiente patron ejmp ^Buenos dias
    $ : El string debe terminar con el patron ejmp adios$
    * : cero o mas ocurrencias del patron
    + : Al menos una ocurrencia del patron, Magic kode+ , debe haber al menos una ocurrencia
    ? : Cero o una ocurrencia del patron, Maxi? cero o una vez debe estar Maxi
    {} : Numero especifico de ocurrencias, Maxi{4} , debe estar exacto 4 veces
    | : OR ,papel|tijera , buscamos papel o tijesras
    () : Agrupamos RE,aplicamos un operador a un grupo, (abc|dfg){2} buscamos abc 2 veces o dgf 2 veces

    Combinaciones Especiales

    \A , al principio , \AMagickode debe empezar con magickode
    \b , al principio o la final, \bMaxi Maxi\b
    \B , en algun sitio pero no al principio o al final, \bMaxi Maxi\b
    \d, match cuando el string contiene digitos
    \D, cuanto NO contiene digitos
    \s, match cuando contiene espacio blanco
    \S, match cuando NO contiene espacio blanco
    \w, match any character a-Z 0-9 _
    \W, math cuando NO hay un caracer
    \Z, match si esta en el fial del string

    Sets

    [jeh] match donde se encuentra cualquiea j, e ,h
    [a-x] match cualquier char entre la a y x minusculas
    [^zxc] match en cualquier MENOS z, x, c
    [0123] match 0,1,2,3
    [0-9] match entre 0 y 9
    [0-9][0-9] match cualquier numero de dos digitos desde 00 al 99
    [a-zA-Z] match cualquier letra may o min.


"""