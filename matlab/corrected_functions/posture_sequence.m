%let's find the posture sequence:

postures = load('postures_90-centers_20-files_5000-framesPerFile.mat');

postures = postures.postures;

%let's use load the angle array:
[N,M] = size(R);

posture_seq = zeros(1,M);

for i=1:M
    x = [];
    for k=1:90
        cost = R(:,i)-Q(:,k);
        abs_cost = dot(cost,cost);
        x(k) = abs_cost;
    [x1,x2] = min(x);
    posture_seq(i) = x2;
    end
end
