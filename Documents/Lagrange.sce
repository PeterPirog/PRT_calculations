
function y = lagrange_interp(x,data)
    
    for i = 1:length(x)
        y(i) = P(x(i),data);
    end
endfunction    
    function y = P(x,data)

    n = size(data,1);

    xi = data(:,1);
    yi = data(:,2);

    L = cprod_e(xi,x) ./ cprod_i(xi); 
    y = yi' * L;
endfunction    
    function y = cprod_e(x,a)
    
    n = length(x);
    y(1) = prod(a-x(2:$));
    for i = 2:n-1
        y(i) = prod(a-x(1:i-1))*prod(a-x(i+1:$));
    end
    y(n) = prod(a-x(1:$-1));
    
endfunction
function y=cprod_i(x)
    
    n = length(x);
    y(1) = prod(x(1)-x(2:$));
    for i = 2:n-1
        y(i) = prod(x(i)-x(1:i-1))*prod(x(i)-x(i+1:$));
    end
    y(n) = prod(x(n)-x(1:$-1));
    
endfunction

