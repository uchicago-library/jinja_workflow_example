import random

from .lorem import posts


pseudo_db = {
    "people": [
        {
            "name": "Michael",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/d/dc/MichaelScott.png"
        },
        {
            "name": "Jim",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Jim-halpert.jpg/220px-Jim-halpert.jpg"
        },
        {
            "name": "Pam",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Pam_Beesley.jpg/220px-Pam_Beesley.jpg"
        },
        {
            "name": "Dwight",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Dwight_Schrute.jpg/220px-Dwight_Schrute.jpg"
        },
        {
            "name": "Ryan",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/Ryan_Howard_%28The_Office%29.jpg/235px-Ryan_Howard_%28The_Office%29.jpg"
        },
        {
            "name": "Andy",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Andy_Bernard_photoshot.jpg/250px-Andy_Bernard_photoshot.jpg"
        },
        {
            "name": "Stanley",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Stanley_Hudson.jpg/245px-Stanley_Hudson.jpg"
        },
        {
            "name": "Kevin",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Office-1200-baumgartner1.jpg/260px-Office-1200-baumgartner1.jpg"
        },
        {
            "name": "Meredith",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Meredith_Palmer.jpg/255px-Meredith_Palmer.jpg"
        },
        {
            "name": "Angela",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/Angela_Martin.jpg/230px-Angela_Martin.jpg"
        },
        {
            "name": "Oscar",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Oscar_Martinez_of_The_Office.jpg/250px-Oscar_Martinez_of_The_Office.jpg"
        },
        {
            "name": "Phyllis",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/f/ff/Phyllis_Lapin-Vance.jpg/220px-Phyllis_Lapin-Vance.jpg"
        },
        {
            "name": "Kelly",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Kelly_Kapoor.jpg/240px-Kelly_Kapoor.jpg"
        },
        {
            "name": "Toby",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Toby_Flenderson_promo_picture.jpg/235px-Toby_Flenderson_promo_picture.jpg"
        },
        {
            "name": "Creed",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/CreedBratton%28TheOffice%29.jpg/220px-CreedBratton%28TheOffice%29.jpg"
        },
        {
            "name": "Darryl",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/6/65/DarrylPhilbin.jpg"
        },
        {
            "name": "Erin",
            "profile_picture": "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Erin_Hannon.jpg/250px-Erin_Hannon.jpg"
        }
    ]
}

for i,x in enumerate(pseudo_db['people']):
    x['id'] = i

for x in pseudo_db['people']:
    x['friends'] = []
    for y in pseudo_db['people']:
        if x == y:
            continue
        if random.randrange(0, 2) == 1:
            x['friends'].append(y['id'])

    x['posts'] = [posts[random.randrange(0, len(posts))]
                  for _ in range(random.randrange(0, 22))]
