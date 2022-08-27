#!/usr/bin/env python3

import stscan_routines as ss

rend1 = ss.StripScanner()

rend1.angSet( 45 * 3.14159 / 180 )
rend1.dump()

rend1.step()
rend1.dump()

