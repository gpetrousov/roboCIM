Authors
--------------

| Ioannis Petrousov |  | Efstathios Lymperidis |
|:-:|:-:|:-:|
|| Department of Informatics <br /> and Telecommunications Engineering <br /> University of Western Macedonia <br /> Kozani, 50100, Greece  |   |
|  petrousov@gmail.com   |   | e.l.d@live.com  |


About
=====
This project was developed as a semester assignment for the robotics class and received the highest grade among others.

# roboCIM chessplayer #

## Description ##
<p>

The roboCIM chess player is a system that allows you to play chess or solve chess puzzles, such as the 8 queen puzzle, with the robotic arm Lab-Volt Servo Robot System Model 5250,
using our custom made platform.
The system consists of 3 parts: the user interface (PC), the arduino and the arm.
The platform connects the user interface (chessboard) with an arduino via a serial bus and the arduino with the arm via digital pins and TTL I/Os.
The UI communicates with the arm by sending binary signals, which correspond to actions listed bellow.
In turn, the arduino receives the signals and activates digital pins which corresponding to them and are connected with the arm's TTL I/Os.
A1, A2,...,H7 and H8 correspond to squares on the chessboard.

<p/>

| Signal  | Action  |
| ------- |:---------:|
| 0000000 | open grip |
| 1111111 | close grip|
| 0000001 | A1        |
| 0000010 | A2|
| 0000011 | A3|
| 0000100 | A4|
| 0000101 | A5|
| 0000110 | A6|
| 0000111 | A7|
| 0001000 | A8|
| 0001001 | B1|
| 0001010 | B2|
| 0001011 | B3|
| 0001100 | B4|
| 0001101 | B4|
| 0001110 | B5|
| 0001111 | B6|
| 0010000 | B7|
| 0010001 | B8|
| 0010010 | C1|
| 0010011 | C2|
| 0010100 | C3|
| 0010101 | C4|
| 0010110 | C5|
| 0010111 | C6|
| 0011000 | C7|
| 0011001 | C8|
| 0011010 | D1|
| 0011011 | D2|
| 0011100 | D3|
| 0011101 | D4|
| 0011111 | D5|
| 0100000 | D6|
| 0100001 | D7|
| 0100010 | D8|
| 0100011 | E1|
| 0100100 | E2|
| 0100101 | E3|
| 0100110 | E4|
| 0100111 | E5|
| 0101000 | E6|
| 0101001 | E7|
| 0101010 | E8|
| 0101011 | F1|
| 0101100 | F2|
| 0101101 | F3|
| 0101110 | F4|
| 0101111 | F5|
| 0110000 | F6|
| 0110001 | F7|
| 0110010 | F8|
| 0110011 | G1|
| 0110100 | G2|
| 0110101 | G3|
| 0110110 | G4|
| 0110111 | G5|
| 0111000 | G6|
| 0111001 | G7|
| 0111010 | G8|
| 0111011 | H1|
| 0111100 | H2|
| 0111101 | H3|
| 0111111 | H4|
| 1000000 | H5|
| 1000001 | H6|
| 1000010 | H7|
| 1000011 | H8|
<br />


