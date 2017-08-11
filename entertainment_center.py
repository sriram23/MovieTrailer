import fresh_tomatoes
import media

#Creating instance for Vanamagan
vanamagan = media.Movie("Vanamagan", 
                        "The story of Nature's own son born and broughtup in Jungle",
                        "https://wallpapers.filmibeat.com/ph-1024x768/2017/04/vanamagan_149318336830.jpg",
                        "https://www.youtube.com/watch?v=G9fWmZtVhzo")

#Creating instance for Singham 3
s3 = media.Movie("Singham - 3",
                 "The story sequel of Universal COP, Durai Singham",
                 "http://media2.intoday.in/indiatoday/images/stories/singam-story_647_092616022640.jpg",
                 "https://www.youtube.com/watch?v=L5YMrYNSxiE")

#Creating instance for Irumugan
iru = media.Movie("IruMugan",
                  "Irumugan is a science fiction story based on a smuggler Love and NIA agent",
                  "http://www.ssmusic.tv/wp-content/uploads/2016/08/maxresdefault.jpg",
                  "https://www.youtube.com/watch?v=L_0jexAQsB0")

#Creating instance for Yennai Arindhal
yennai = media.Movie("Yennai Arindhal",
                     "Yennai Arindhal is a cop film by Thala Ajith Kumar",
                     "https://c.saavncdn.com/651/Yennai-Arindhaal-Tamil-2015-500x500.jpg",
                     "https://www.youtube.com/watch?v=B7c87SWQg-Y")

#Creating instance for Nanban
nanban = media.Movie("Nanban",
                     "Nanban is a film starring Vijay,Srikanth and Jeeva, which tells about true friendship",
                     "http://3.bp.blogspot.com/-uVRBlkDwDP4/TxEBtHhDtuI/AAAAAAAAAu4/uy5Qn_P_G2U/s1600/nanban-hd-wallpapers-02.jpg",
                     "https://www.youtube.com/watch?v=372OS5dbxUI&t=13s")

#Creating instance for MS Dhoni - The Untold Story
dhoni = media.Movie("MS DHONI, The Untold Story",
                    "The untold story is the biography film of Indian cricket star MS Dhoni",
                    "http://images.indianexpress.com/2016/08/ms-dhoni-the-untold-story-759.jpg",
                    "https://www.youtube.com/watch?v=6L6XqWoS8tw")

#Putting those objects in a list
movies = [yennai, nanban, s3, vanamagan, iru, dhoni]

#Calling open_movies_page() function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
