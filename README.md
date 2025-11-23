# Transferring Parametric Equations to TI-84 Plus CE

The main idea is to be able to take any reference picture, pass it through [Maltaisn/svg-equations](https://github.com/maltaisn/svg-equations) to get the parametric equations that would form the picture, then use this code to translate the parametric equations into code that is readable by the TI Connect CE app, so that the picture may be graphed on the TI-84 Graphing Calculator.

With some creativity, you can go from an image like this:<br/>
<img width="428" height="350" alt="HCJC_Nguyen Vu Kien Raymond" src="https://github.com/user-attachments/assets/ec9e4944-8512-411f-a24a-697148c6d8ec" />

To this on a Ti-84 calculator:<br/>
<img width="428" height="322" alt="HCJC_Nguyen Vu Kien Raymond" src="https://github.com/user-attachments/assets/e4fc5bf3-5501-4d86-a417-e538d673ba97" />


## Instructions

Git clone this repository and place your parametric-equations.txt in the same folder.  

Edit the second line in the main.py file:

` with open ('your_file.txt','r') as f1: `

Running the main.py file will produce a result.txt. The contents of which can be copy and pasted into the TI Connect CE app.

## Challenges

The syntax used in the TI Connect CE app is incredible.

```
"4671(1-T)^3+13959T(1-T)^2+13836T^2(1-T)+4580T^3"→X₁ 
"­10075(1-T)^3-30201T(1-T)^2-30132T^2(1-T)-10025T^3"→Y₁ 
```

In the above, the first line has no negative sign in front of the 4671, while the 10075 in the second line actually has a negative sign in front of it. Although the sign is shown within the TI Connect app, most text editors would not be able to properly display the negative sign, which can result in some confusion.
