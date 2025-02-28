# IAT 460 A3: ClearLED Installation
Olivia Steed
301421820

## Conceptual Approach

For my ClearLED installation, I am leveraging the layered nature of the clear screens to show the layered process of GAN image generation. While we were learning about Autolume, I found it fascinating how GANs generate images in layers, starting with very low resolution pixel matrices, and doubling in size until the output appears as a high resolution image. Once this output is produced, you don’t see the layers that gave rise to it. I want to demystify the process of GAN image generation by showing this process on the clear screens simultaneously, so one can see the full GAN image generation process.

I used the face generation model, since faces are highly recognizable, and this dataset was the most unsettling yet captivating to me. In addition to showing how GANs generate imagery, the installation can also be interpreted as a representation of personality and ‘self,’ with similar layers of early development and core values making the ever-changing outside selves we try on and present to the world. I used colours referencing glitch or no signal screens to reference the disconnect that can happen between the inner core of a person and their outer presentation. The intended user experience is to both walk around the screens to view the different layers, and to view them in a row to see the progress layers and the end result at once, mirroring the process of individuation and self development, and that there is always more than meets the eye under the surface of external presentation.

## Computational Methods

I used Autolume to generate a series of faces in a one minute loop so that I could show the layers of GAN image generation and evoke exploration of personality with human imagery. When exploring the pretrained Autolume models, I found the faces the most interesting because faces are so familiar, and the generated imagery appeared believable, even when I knew they didn’t exist. This mirrors the point that the outside persona people present can be false.

I recorded each layer of output over the looped minute. To map the video output to the screen dimensions, I put the videos in Premiere and resized them. Then I flattened the pixels of each video into black and white using a Python script that extracts the minimum and maximum pixel value, and creates a threshold in between them so that the lighter half are mapped to white, and darker half mapped to black. I then arranged the clips in sequence in Premiere, and remapped the white pixels to colours that change as the video plays. I also used a Python script to generate sounds mapped to the average colours in each video and overlaid these during the final video to mirror the overlapped imagery.

The key difficulty was recording and mapping the clips to black and white. When I used the inbuilt Autolume screen recording it stopped recording when I tried to reveal the lower layers, so I had to use Windows screen record as a workaround. Then, because of the very low contrast in the lower layers, my attempts to turn the video to black and white resulted in only white pixels, so I had to create the threshold dynamically from each video instead of use the standard threshold of 128.

