Stargate Dialing Program
========================

Simulates the Stargate SGC dialing program.

Building and Running
====================

You will need a C compiler and the Allegro 5 library.

On Mac OS X, I built using clang (Xcode command line tools). Allegro was installed with homebrew.

Ubuntu works with gcc and allegro installed by apt-get.

    git clone https://github.com/dgroddick/sgc-dialing-program.git stargate
    cd stargate
    make
    ./stargate
