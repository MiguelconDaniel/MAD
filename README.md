# MAD SET UP

[1] First clone repository into a folder called mad

    git clone https://github.com/MiguelconDaniel/MAD.git mad


[2] Next create a python virtual environment 

    virtualenv mad

[3] Activate the python environment just created

    source mad/bin/activate
    cd mad

   You are ready to work

[4] Install required packages

    pip install -r requirements.txt

   Ready to run!


[5] Generation of some test data

    Create some time signals with/without noise to test our denoising

    python mad_signal.py --hz 30 --time 100.0 --signal 1 --out test1.data
    python mad_signal.py --hz 30 --time 100.0 --signal 1 --out test1_5.data   --decibel 5.0
    python mad_signal.py --hz 30 --time 100.0 --signal 1 --out test1_7.data   --decibel 7.0
    python mad_signal.py --hz 30 --time 100.0 --signal 1 --out test1_10.data  --decibel 10.0
    python mad_signal.py --hz 30 --time 100.0 --signal 1 --out test1_15.data  --decibel 15.0
    

    python mad_signal.py --hz 30 --time 100.0 --signal 2 --out test2.data
    python mad_signal.py --hz 30 --time 100.0 --signal 2 --out test2_5.data   --decibel 5.0
    python mad_signal.py --hz 30 --time 100.0 --signal 2 --out test2_7.data   --decibel 7.0
    python mad_signal.py --hz 30 --time 100.0 --signal 2 --out test2_10.data  --decibel 10.0
    python mad_signal.py --hz 30 --time 100.0 --signal 2 --out test2_15.data  --decibel 15.0


    Optionally also add the --display flag to visualize the signals during generation


[5] Display data

    You can display the data in a single file or compare the data of two files as such


    python mad_display.py --input test1_7.data
    python mad_display.py --input test1_7.data test1.data
    


