clear,clc 
% точки данных
t=[-1 0 1];
z=t.*t+1-acos(t);
x = [-1 0.4 1 ] ;
y = [-1.142 -0.570 2];
xx = linspace(-1,1,10); % массив точек х
x0 = [-0.5 0.5 1]; % узловые точки между каждыми двумя узлами
y0 = ones(size(x0));
[yy] = newton(x, y, xx);
[y0] = newton(x, y, x0);% функция в некоторой точке и полином
y0
plot(x,y,'o',xx,yy,':r',x0,y0,'*b',t,z), grid on
legend('Данные','Интерполяция','Точка', 'location', 'northwest')