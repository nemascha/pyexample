# coding=utf-8

from googlemaps import directions


direction = directions('texarkana', 'atlanta')

for step in direction['Directions']['Routes'][0]['Steps']:
    print(step['descriptionHtml'])

