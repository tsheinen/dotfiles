# random jump
#
# jump to a random function in the current binaryview

import random
randomIndex = random.randint(0, len(bv.functions)-1)
destination = bv.functions[randomIndex].start
log_info("Jumping to: 0x%x" % destination)
here = destination