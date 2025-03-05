from django.shortcuts import render
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def memorygallery(request):
        image_data = [
        ("/static/images/imagesForMemoryHome/Firstone.jpg", "This song signifies the new that we looking ahead when we just arrived at the spsu for the first time. I dont know what is cse but i am doing it. I only knew names of these 3 people whom i dont really know","/static/audio/give_me_some_sunshine-trimmed.mp3"),
        ("/static/images/imagesForMemoryHome/Second.jpg", "Badne do yaari ka circle jaara happy happy sa har pal jara, new friendship new word. I still remember teeno ne is baat pe meeting ki thi ki mujhe wiered na lage isliye sab dhyan rakhe", "/static/audio/ye_no_oneYaari_trimmed.mp3"),
        ("/static/images/imagesForMemoryHome/third.jpg", "Yaado ke purane album me, i still hold of these photos. These were good times i always missed. But its okay now. Sunset is beatiful isnt it?","/static/audio/woh_din_bhi_kya_din_the_trimmed.mp3"),
        ("/static/images/imagesForMemoryHome/fourth.jpg", "I dont think you people will understand this song 😂. It feels like we are gang of four members at that time. Who seek to fight except me offcourse.", "/static/audio/tora_friendship_trimmed.mp3"), 
        ("/static/images/imagesForMemoryHome/fifth.jpg", "Well well well dimonds are tough. so strong, like i give a shit about it. I know my friends will be corepati so i will take loan from them and buy a lot of dimonds 🤑","/static/audio/yaro_mere_waste_trimmed.mp3"),
        ("/static/images/imagesForMemoryHome/eight.jpg", "Something about the night something very special. Is din se mitra ka karja dena hai sala khatam hi nhi ho rha hai", "/static/audio/disco_for_suit_trimmed.mp3"),
        ("/static/images/imagesForMemoryHome/sixth.jpg", "I dont find any photos of group with anjali it takes me enternity to find these two images. Is time pe anjali thodi kaam khatarnak thi. Or atleast mujhe esa lagta tha.", "/static/audio/abhi_to_party_suru_hui_trimmed.mp3"),
        ("/static/images/imagesForMemoryHome/seventh.jpg", "Raat ko hoga hangama jab chamke ka chanda mama, I still remebered we danced for long time and mitra chale guye the upar (for unkown reason)","/static/audio/pajama_party_trimmed.mp3"),
        
        ("/static/images/imagesForMemoryHome/lastONe.jpg", "Well guess this one is the last dont know if we ever cross path in life but i think its a good experiance. Sometimes you hate life, but after sometime you realise it good, and everything happens for a reason. Well its in black(No need to remind me that its gray) and white (Because i hold you people in my black and white life)", "/static/audio/its_been_a_long_day.mp3"),

        
        # Add all 8 images with their descriptions
        ]
        return render(request, "memoryHome.html", {"image_data": image_data})



@login_required
def gallery(request):
    image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
    image_list = [f"/media/gallery/{img}" for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'webp'))]

    
    
    # Paginate images (12 per page)
    paginator = Paginator(image_list, 12)
    page_number = request.GET.get('page', 1)  # Get page number from URL
    page_obj = paginator.get_page(page_number)  # Get images for that page

    return render(request, 'gallery.html', {'page_obj': page_obj})


