# NewRobotics Documentation

## Mecanumdrive (manual)

```python
rotate(x, y, rotation_angle=math.pi / 4):
```

- `x`: float or integer
- `y`: float or integer
- `rotation_angle`: float angle in radians

```python
parse(axis, velo, units=RPM):
```

- `axis`: motor group datatype to set velocity to
- `velo`: velocity (signed)
- `units`: RPM or PERCENT (default is RPM)

```python
drive_mapping()
```

- Maps left joystick and triggers to omnidirectional movement and turning respectively

## Autonomous Drive

