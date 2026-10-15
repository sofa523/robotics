## Обычный запуск при `hz = 10 Гц`
```bash
root@eb0ad288836d:/work/robotics# ros2 topic hz /turtle1/cmd_vel
average rate: 10.002
        min: 0.099s max: 0.101s std dev: 0.00037s window: 11
average rate: 10.001
        min: 0.099s max: 0.101s std dev: 0.00031s window: 21
average rate: 10.001
        min: 0.099s max: 0.101s std dev: 0.00035s window: 32
average rate: 9.998
        min: 0.099s max: 0.101s std dev: 0.00040s window: 42
average rate: 10.000
        min: 0.099s max: 0.101s std dev: 0.00041s window: 53
```

## Попытка установить большое значение или ноль
Вывод
```bash
root@eb0ad288836d:/work/robotics# ros2 param set /patrol publish_hz 234.
Setting parameter failed: Invalid 'publish_rate': 234.0. Must be [1., 30.]
root@eb0ad288836d:/work/robotics#  ros2 param set /patrol publish_hz 0.0
Setting parameter failed: Invalid 'publish_rate': 0.0. Must be [1., 30.]
root@eb0ad288836d:/work/robotics#  ros2 topic hz /turtle1/cmd_vel
average rate: 9.995
        min: 0.099s max: 0.101s std dev: 0.00053s window: 9
average rate: 10.000
        min: 0.099s max: 0.101s std dev: 0.00047s window: 19
average rate: 10.000
        min: 0.099s max: 0.101s std dev: 0.00040s window: 29
```

## Установка `hz = 17 Гц`
```bash
root@eb0ad288836d:/work/robotics#  ros2 param set /patrol publish_hz 17.0
Set parameter successful
```
Проверка установки
```bash
average rate: 16.999
        min: 0.058s max: 0.059s std dev: 0.00021s window: 19
average rate: 17.001
        min: 0.058s max: 0.059s std dev: 0.00027s window: 37
average rate: 17.001
        min: 0.058s max: 0.059s std dev: 0.00028s window: 55
average rate: 17.001
        min: 0.058s max: 0.060s std dev: 0.00033s window: 73
average rate: 16.998
        min: 0.058s max: 0.060s std dev: 0.00034s window: 91
```


## Работа с action и service

### Отправка цели
Действие поворта на заданный theta (в радианах):
```bash
ros2 action send_goal /turtle1/rotate_absolute turtlesim_msgs/action/RotateAbsolute '{theta: 2.0}' --feedback
```

Сервис для отчистки пути черепахи
```ros2 service call /clear std_srvs/srv/Empty '{}'```