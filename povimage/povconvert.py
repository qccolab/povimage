#!/usr/bin/env python
from PIL import Image
import math

class POVConvert(object):
    def __init__(self, source, innerRadius=0.2):
        self.source = Image.open(source)
        self.innerRadius = innerRadius

    def polarToCartesian(self, srcsize, pos):
        (x,y) = pos
        (w,h) = srcsize

        angle = -(y / 180.0 * math.pi * 2) - math.pi
        radius = x / 32.0 * (1.0 - self.innerRadius) + self.innerRadius

        sample_x = math.sin(angle) * radius
        sample_y = math.cos(angle) * radius

        return (
            round(sample_x * (w * 0.5) + (w * 0.5)),
            round(sample_y * (h * 0.5) + (h * 0.5))
                )

    def convert(self):
        self.destination = Image.new('RGB', (32, 180))
        (sx, sy) = self.source.size

        for dx in xrange(32):
            for dy in xrange(180):
                sample_pos = self.polarToCartesian((sx, sy), (dx, dy))
                pixel = self.source.getpixel(sample_pos)
                self.destination.putpixel((dx, dy), pixel)

        #self.destination = self.destination.quantize(colors=16) #, palette=self.PALETTE)

    def save(self, fp):
        self.destination.save(fp)


