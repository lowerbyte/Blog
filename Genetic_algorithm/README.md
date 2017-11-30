Genetic Algorithm

Hello!  
Inspired by this:  
https://github.com/gynvael/stream/tree/master/028-monaliza-genetycznie

I trought I would to the same but in Python and with triangles, but not with Mona Lisa. I would rather go with _The Lady with an Ermine gray_ And I have to be honest. The biggest problem was to render the triangle!  
But I found this article:  
http://www.sunshine2k.de/coding/java/TriangleRasterization/TriangleRasterization.html

And I want to thank to aal who have contributed to this, because it is awesome! It help me to write this and it works like a charm. Like very, very slow charm, but hey!  
Whatever works! ; )

Here you've got some examples how it all worked (only 1000 generation, because my laptop couldn't do more):

For 100 generation we can see there is some shape of our art:

![Screen one.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/100pokolen_triangle.png)

So it could only be better (300, 700 and 1000 generations)!

![Screen two.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/300pokolen_triangle.png)![Screen three.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/700pokolen_triangle.png)![Screen four.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/1000pokolen_triangle.png)

Ok it looks really nice, but I wasn't pleased enough so I change the alghoritm to estimate by rectangles and the results are as follows (100, 300, 700 and 1000 generations):

![Screen five.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/100pokolen.png)![Screen six.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/300pokolen.png)![Screen seven.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/700pokolen.png)![Screen eight.](https://github.com/lowerbyte/Blog/blob/master/Genetic_algorithm/images/1000pokolen.png)

The results are similar and it looks very promissing. Feel free to change the code and draw what ever you want with your genetic alghoritm!  
Take care!
