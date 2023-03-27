program factorial;

function factorial(n: int): longint;
begin
    if n = 0 then
        factorial := 1
    else
        factorial := n * factorial(n-1);
end;

var
    n = interger;

begin
    for n := 0 to 16 do
        writeln(n, '! = ', factorial(n));
end.