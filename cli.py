#!/usr/bin/env python3

import stscan_routines as ss

ss.init()

ss.angSet( 45 * 3.14159 / 180 )
ss.dump()

ss.step()
ss.dump()

