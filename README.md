# Subtitles-Shifter
Small program that will help synchronizing subtitles with your movie.

# Command line options
`python subtitles_shifter.py --help`

```Subtitles Shifter
This is a small program that I wrote to help myself 
with the synchronization of subtitles in movies.

Check readme.md for example usage.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Path to the file with original subtitles.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to the file where shifted subtitles will be
                        saved.
  -m MODE, --mode MODE  Shift subtitles forward or backward. Usage: --mode
                        forward/backward |Default: forward
  -t TIME, --time TIME  Amount of time in seconds to shift the subtitles |
                        Usage: --time 5.4
  -r RANGE [RANGE ...], --range RANGE [RANGE ...]
                        The range you want the subtitles to be shifted (only
                        two first numbers will be used) | Usage: --range 50
                        125
```
# Example use
`python subtitles_shifter.py -i django.srt -o django.srt -m forward -t 5.6 -r 1 250`

```
|''''''''''''''''''''''''''''''''''''''''|
| Starting subtitles shifter aplication. |
|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,| 


|''''''''''''''''''''''''''''''''''''''''''''
| Selected file:  django.srt           
| Subtitles will be shifted by 5.6 seconds   
| Selected mode: forward                     
| Selected range: [1, 250]                     
|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


|''''''''''''''''''''''''''''''''''''''''''''
|Shifted from:                               
| 00:00:50,845 --> 00:00:55,093              
|To:                                         
| 00:00:56,445 --> 00:01:00,693              
|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


|''''''''''''''''''''''''''''''''''''''''''''
|Shifted subtitles were saved to:  django.srt   
|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```
# Additional notes
Be sure to backup your original subtitles file.  
If you want to modify your file in place, go ahead and use the same file for input and output argument.  
To get the best out of this, check the timestamp of the first subtitle in your source file and try to match it with the time it appears in the movie.  
Repeat until you are satisfied with the result.
