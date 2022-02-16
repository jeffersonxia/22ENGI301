# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Introduction
--------------------------------------------------------------------------
License:   
Copyright 2021 Jefferson Xia

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program to introduce myself

--------------------------------------------------------------------------
"""
import time
from bbpystepper import Stepper

# ------------------------------------------------------------------------
# Splitflap Module Initialization
# ------------------------------------------------------------------------

mod1 = Stepper(pins=["P2_18", "P2_20", "P2_22", "P2_24"])
mod2 = Stepper(pins=["P2_2", "P2_4", "P2_6", "P2_8"])

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    mod1.rotate(-90)            
    mod2.rotate(-105)
    time.sleep(2)
    mod1.rotate(-9)            
    mod2.rotate(-54)
    time.sleep(2)
    mod1.rotate(-18)            
    mod2.rotate(-126)
    time.sleep(2)
    mod1.rotate(-243)            
    mod2.rotate(-81)
    