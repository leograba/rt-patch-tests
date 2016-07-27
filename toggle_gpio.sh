#!/bin/sh

case "$1" in
   start)
        echo "Toggle-gpio from userspace, via /sys/class/gpio - starting"

                #start the process
                /home/root/gpio-squarewave-release &
                stress -c 2 -i 2 &

                #get process PID so the priority can be changed
                i=2
                until [ $(ps -eLfc | grep gpio-squarewave | grep -v grep | cut -d " " -f $i) != " " ]; do
                        let i+=1
                done
                echo "Process PID:"
                pid_blink=$(ps -eLfc | grep gpio-squarewave | grep -v grep | cut -d " " -f $i)
                echo $pid_blink

                if [ "$2" = "rt" ]
                then
                        echo "priority set to RT"
                        chrt -r -p 99 $pid_blink
                fi
        ;;
   stop)
        echo "Toggle-gpio from userspace, via /sys/class/gpio - stopping"
                killall gpio-squarewave-release
                killall stress
           ;;
        *)
        echo "Usage: $0 start|stop [rt]"
          exit 1
          ;;
esac
