# Bell 206 Cyclic/Collective controls, rigging and swash-plate

Photo of model

Link to model file

Demo video

## Cyclic? Collective? How helicopters maneuver.
  
For a good introduction to how helicopters fly and the function of the
swashplate modeled here, I suggest [this video][heli-fly]. 

[heli-fly]: https://www.youtube.com/watch?v=2tdnqZgKa0E

In short, each blade of a helicopter rotor acts like a wing, generating lift as
it sweeps through the air, pulling up the aircraft.

By changing the pitch of all blades by the same amount we can increase or
decrease vertical thrust, moving the helicopter up or down. This is called the
**collective**.

By setting the pitch of each blade differently we can change the direction of
the thrust, moving the helicopter horizontally. This is called the **cyclic**

There are two interesting problems here: 
1. How to adjust the pitch of the blades as they rotate through a full cycle,
   since the pitch of each blade under cyclic input has to depend on where it is
   in its rotation.
2. How to convert mechanical inputs of the cyclic and collective from the
   stationary cabin, where the pilot sits, to the rotating blades.

These problems are solved by the **swashplate**.

## Swashplate

- Diagram of swashplate from Bell 206 manual

- Corresponding part of model

## Rigging

While researching this topic I became fascinated not only by swashplate, but by
the mechanisms that convert a pilot's cyclic and collective inputs to swashplate
angles (the **rigging**), so I modeled that too.

- Overview diagram from manual

### Note:
The Bell 206 has a servo section between the mixing lever and the swashplate
that I did not model. The servo section does not add anything educationally and
increases clutter. In this respect the model is closer to the [Robinson
R22](r22). I did not find detailed enough diagrams for the R22 as I did for the
Bell, so I modeled the Bell.

[r22]: https://en.wikipedia.org/wiki/Robinson_R22


### Cyclic control

- Diagram of cyclic control from Bell 206 manual

- Corresponding part of model

As an aside, I was confused by linkage 10 in the diagram for a while, [until a
nice person on aviation stack exchange helped me out][aviation-stack-1]. 

[aviation-stack-1]:
    https://aviation.stackexchange.com/questions/91631/how-does-this-bell-206-cyclic-control-linkage-work

### Collective control

- Diagram of cyclic control from Bell 206 manual

- Corresponding part of model

### Mixing lever/bell crank

- Diagram of mixing lever from Bell 206 manual

- Video

The design of the part is pretty deliberate, and it took me a lot of
experimentation to replicate the functionality.

- Corresponding part of model



## Post-script: Helicopters in the computer age

There are current attempts to replace the mechanical swashplate with servo
motors on each blade that would electronically adjust the pitch of the blades.
This would reduce mechanical complexity (and insert new points of failure, IMO)
but I'm guessing this can make the helicopter lighter and perhaps more agile?

## Other LEGO helicopter models with cyclic/collcetive

The aim of my model is educational: clearly expose all the linkages and levers
so that the principle of operation can be studied. The other models listed here
aim at creating a playable helicopter model with functioning controls, so the
mechanisms are completely or partially obscured.

- [Lama Helicopter](https://www.youtube.com/watch?v=8U2VM3m6Ypc). It has working
  collective, cyclic and tail rotor controls beautifully compressed to scale,
  and it's been motorized. Some of the build is not reqular LEGO. There is a
  wire connector for the cyclic and a modified piece in the rotor. The mechanism
  is hard to see.
- [Pattspatt's
  model](https://rebrickable.com/mocs/MOC-87154/Pattspatt/helicopter-42110-c-model/#details).
  This is an impressive helicopter built as an alternate build for the Land
  Rover set. It has the clearest diagrams for a LEGO helicopter control model I
  have seen.
- [Ivan_M's AH-77
  model](https://rebrickable.com/mocs/MOC-21317/Ivan_M/ah-77-hunter-helicopter/#details)
- [A wonderful KA-32 model from
  sheepo.es](https://www.sheepo.es/2014/10/kamov-ka-32-coaxial-helicopter.html#more).
  This is a coaxial helicopter, two rotors on top of each other, and the model
  shows how a swashplate works in this case, which is excellent. Again, the
  mechanism is hard to see.
- [cyclic/collective rigging
  diagram](https://www.eurobricks.com/forum/index.php?/forums/topic/156205-moc-calypso-hughes-269b300-helicopter/&do=findComment&comment=2888754)
- Nice discussions
  [1](https://www.eurobricks.com/forum/index.php?/forums/topic/156205-moc-calypso-hughes-269b300-helicopter/)
  and
  [2](https://www.eurobricks.com/forum/index.php?/forums/topic/60459-effes-moc-corner/&page=24)
  on mixing levers on EuroBricks.


## References
- [Bell 206 maintenance
  manual](https://pscorp.ph/wp-content/uploads/2019/06/206-MO-S04-Flight-Controls.pdf)
- [Bell 206 mixing lever video](https://www.youtube.com/watch?v=cVNBC9EDOcU)
- [Robinson R22
  manual](https://robinsonheli.com/wp-content/uploads/2020/11/r22_mm_8.pdf)
