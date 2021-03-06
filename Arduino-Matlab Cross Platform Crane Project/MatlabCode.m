clear;
delete(instrfind);
pause(0.1);
ev3 = legoev3('usb')
motora = motor(ev3, 'A')
motorb = motor(ev3, 'B')
motorc = motor(ev3, 'C')
motord = motor(ev3, 'D');
resetRotation(motora)
resetRotation(motorb)
resetRotation(motorc)
resetRotation(motord)
motora.Speed = 0
motorb.Speed = 0
motorc.Speed = 0
motord.Speed = 0
start(motora)
start(motorb)
start(motorc)
start(motord)
mycolorsensor = colorSensor(ev3);
s = serial("COM6");
set(s,'BaudRate',9600,'DataBits', 8, 'Parity', 'none','StopBits', 1, 'FlowControl', 'none','Terminator','CR/LF');
fopen(s);
while true
    out = fscanf(s)
    processedOut = str2num(out)
    red = processedOut(1,1)
    green = processedOut(1,2)
    blue = processedOut(1,3)
    RG = red./green
    GB = green./blue
    
    if RG>3 && GB < 1.3
        color = "red"
    elseif RG<3 && GB >1.3
        color = "orange"
    elseif RG <1.5 && GB < 1.3
        color = "blue"
    else
        color = "none"
    end
    
    
    
    if color == "red"
        color2 = readColor(mycolorsensor);
        if color2=="red"
            color = "red"
        else
            movemotor(motord,-55,-10);
            color2 = readColor(mycolorsensor);
            if color2 == "red"
                color = "orange"
            else
                color = "blue"
            end
            movemotor(motord,55,10);
        end
    
    elseif color == "orange"
        color2 = readColor(mycolorsensor);
        if color2 ~="red" && color2 ~= "blue"
            color = "red"
        else
            movemotor(motord,-55,-10);
            color2 = readColor(mycolorsensor);
            if color2 ~= "red" && color2 ~= "blue"
                color = "orange"
            else
                color = "blue"
            end
            movemotor(motord,55,10);
        end
    
    elseif color == "blue"
        color2 = readColor(mycolorsensor);
        if color2=="blue"
            color = "red"
        else
            movemotor(motord,-55,-10);
            color2 = readColor(mycolorsensor);
            if color2 == "blue"
                color = "orange"
            else
                color = "blue"
            end
            movemotor(motord,55,10);
        end
    end
    
    
    
    
    if color == "red"
        motorc.Speed = -90
        pause(2)
        motorc.Speed = 0
        movemotor(motorb, 750, 50)
        movemotor(motora, 80, 50)
        movemotor(motorb, -650, -50)
        motorc.Speed = 70
        pause(2)
        motorc.Speed = 0
        movemotor(motorb, 650, 50)
        movemotor(motora,-80,-50)
        movemotor(motorb, -750, -50)
    elseif color == "orange"
        motorc.Speed = -90
        pause(2)
        motorc.Speed = 0
        movemotor(motorb, 750, 50)
        movemotor(motora, 135, 50)
        movemotor(motorb, -650, -50)
        motorc.Speed = 70
        pause(2)
        motorc.Speed = 0
        movemotor(motorb, 650, 50)
        movemotor(motora,-135,-50)
        movemotor(motorb, -750, -50)
    elseif color == "blue"
        motorc.Speed = -90
        pause(2)
        motorc.Speed = 0
        movemotor(motorb, 740, 50)
        movemotor(motora, 180, 50)
        movemotor(motorb, -650, -50)
        motorc.Speed = 70
        pause(2)
        motorc.Speed = 0
        movemotor(motorb, 650, 50)
        movemotor(motora,-180,-50)
        movemotor(motorb, -750, -50)
     end
end
fclose(s);
delete(s)

function movemotor(motor, rotate, speed)
resetRotation(motor)
motor.Speed = speed
while abs(readRotation(motor)) < abs(rotate)
    pause(0.01);
    readRotation(motor)
end
motor.Speed = 0;
%stop(motor);
end
