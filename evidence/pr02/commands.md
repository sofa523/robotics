# PR02

## Команды:
* `2>&1`
Пример: `ros2 pkg prefix turtlesim > /tmp/prefix.txt 2>&1`
Назначение:
`> file 2>&1` — записать stdout в файл и направить туда же stderr; прежнее содержимое файла заменяется.

`>> file 2>&1` — записать stdout в файл и направить туда же stderr; новое содержимое дописывается в конец файла.

* `tee`
Пример: ros2 pkg prefix turtlesim | tee /tmp/prefix.txt`
Назначение: 
`| tee file` — вывести stdout на терминал и одновременно записать его в файл; прежнее содержимое файла заменяется.
`| tee -a file` — вывести stdout на терминал и одновременно дописать его в файл.

* `ros2 pkg prefix turtlesim`
Мой вывод: `/opt/ros/jazzy`
Назначение: вывести путь установки (префикс) пакета turtlesim в текущем окружении ROS 2.

* Отличие `>` от `|`
`>` - перенапрвляет результат вывода в файл
`|` - передает вывод предыдущей команды в следующую

* Отличие `source` от запуска новой программы
`source` - выполняет команды из файла в текущем shell; переменные окружения, PATH и функции сохраняются в текущей сессии.
Запуск новой программы - открывает новую сессию, изменения (переменные, cd) исчезают после завершения и на текущий shell не влияют. 

## Launch-файл

Запуск: ` ros2 launch turtle_bringup sim.launch.py `
Проверка графа: `ros2 node list --no-daemon --spin-time 2` - вывод: `turtlesim`

Вывод: Launch-файл — это удобный способ описать набор фоновых процессов, которые запускаются параллельно, и каждый такой процесс может быть отдельной нодой.

## Движение
`ros2 topic type /turtle1/pose` - позиция черепашки

`ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist \ '{linear: {x: 1.0}, angular: {z: 0.5}}' ` - один раз отправить черепашке команду движения: вперёд со скоростью 1.0 и поворот со скоростью 0.5.

Позиция до поворота:
```
x: 5.544444561004639
y: 5.544444561004639
theta: 0.0
linear_velocity: 0.0
angular_velocity: 0.0
```

Позиция после поворота:
```
x: 6.4386515617370605
y: 5.759484767913818
theta: 0.46399998664855957
linear_velocity: 0.0
angular_velocity: 0.0
```

## Ошибка в имени и исправление

```
ros2 topic pub --rate 1 --wait-matching-subscriptions 0 \
  /cmd_vel geometry_msgs/msg/Twist \
  '{linear: {x: 1.0}, angular: {z: 0.5}}'
```

Вывод:
```
root@eb0ad288836d:/work/robotics# ros2 topic info /cmd_vel --verbose
Type: geometry_msgs/msg/Twist

Publisher count: 1

Node name: _ros2cli_112471
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: PUBLISHER
GID: 01.0f.eb.7d.57.b7.a9.85.00.00.00.00.00.00.07.03
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite

Subscription count: 0

root@eb0ad288836d:/work/robotics# ros2 topic info /turtle1/cmd_vel --verbose
Type: geometry_msgs/msg/Twist

Publisher count: 0

Subscription count: 1

Node name: turtlesim
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: SUBSCRIPTION
GID: 01.0f.eb.7d.7a.ae.6d.c9.00.00.00.00.00.00.1d.04
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite
```

Исправляем:
```
ros2 topic pub --rate 1 --wait-matching-subscriptions 0 \
  /turtle1/cmd_vel geometry_msgs/msg/Twist \
  '{linear: {x: 1.0}, angular: {z: 0.5}}'
```

Вывод:
```
ros2 topic info /turtle1/cmd_vel --verbose
Type: geometry_msgs/msg/Twist

Publisher count: 1

Node name: _ros2cli_114851
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: PUBLISHER
GID: 01.0f.eb.7d.a3.c0.30.c1.00.00.00.00.00.00.07.03
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite

Subscription count: 1

Node name: turtlesim
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: SUBSCRIPTION
GID: 01.0f.eb.7d.7a.ae.6d.c9.00.00.00.00.00.00.1d.04
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite
```