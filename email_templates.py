import random

messages = [
"""
Wishing you a birthday filled with joy,
love and countless beautiful moments.
Have a truly wonderful day!
""",

"""
May your birthday bring new hopes,
new achievements and endless happiness.
Enjoy every moment!
""",

"""
Happy Birthday!
May your life be filled with love,
peace and all the success you deserve.
""",

"""
Another year older,
another year wiser.
Wishing you endless happiness and success!
""",

"""
May every candle on your cake
light up another beautiful memory.
Happy Birthday!
""",

"""
Wishing you a day full of laughter,
surprises and cherished moments.
Happy Birthday!
""",

"""
May today be the beginning
of another incredible chapter in your life.
Happy Birthday!
""",

"""
Celebrate today with a smile,
a grateful heart and lots of cake.
Happy Birthday!
""",

"""
Hope your special day
is filled with love,
laughter and wonderful surprises.
""",

"""
Sending you warm wishes
for a birthday filled with happiness
and a year filled with blessings.
""",

"""
May your birthday be as bright
as your smile
and as wonderful as your heart.
""",

"""
Here's to celebrating you today!
Wishing you health,
joy and endless success.
""",

"""
Happy Birthday!
May every dream you have
find its way to reality.
""",

"""
May happiness surround you today
and remain with you
throughout the coming year.
""",

"""
Wishing you love,
good fortune and unforgettable memories
on your special day.
""",

"""
May your birthday
be filled with magical moments
and beautiful surprises.
""",

"""
Enjoy every smile,
every hug and every slice of cake.
Happy Birthday!
""",

"""
Hope today brings you
everything your heart desires.
Have an amazing birthday!
""",

"""
Life is meant to be celebrated.
Have a fantastic birthday
and a wonderful year ahead!
""",

"""
May your birthday
be filled with sunshine,
laughter and endless joy.
""",

"""
Here's wishing you
countless reasons to smile
throughout the year.
Happy Birthday!
""",

"""
Celebrate your day
with happiness in your heart
and dreams in your eyes.
""",

"""
Happy Birthday!
May your journey ahead
be filled with exciting adventures.
""",

"""
May every moment today
be as special
as you are to everyone around you.
""",

"""
Wishing you
beautiful memories today
and endless happiness tomorrow.
""",

"""
Happy Birthday!
May life reward you
with love, peace and prosperity.
""",

"""
Hope your birthday
is overflowing with joy,
love and sweet surprises.
""",

"""
May every sunrise
bring new opportunities
and every sunset bring peace.
Happy Birthday!
""",

"""
Sending heartfelt wishes
for a birthday full of smiles
and unforgettable moments.
""",

"""
Happy Birthday!
May you continue
to inspire everyone around you.
""",

"""
May today
bring happiness to your heart
and success to your journey.
""",

"""
Wishing you endless laughter,
wonderful friendships
and dreams that come true.
Happy Birthday!
""",

"""
Another birthday,
another opportunity
to create beautiful memories.
Enjoy your day!
""",

"""
May your life
always be filled with positivity,
kindness and happiness.
Happy Birthday!
""",

"""
Wishing you strength,
good health and boundless happiness.
Have a fantastic birthday!
""",

"""
Happy Birthday!
May this year
be your best one yet.
""",

"""
May all the love
you share with others
return to you today.
Happy Birthday!
""",

"""
Hope every wish you make today
brings you one step closer
to your dreams.
""",

"""
Celebrate your birthday
with happiness today
and hope for tomorrow.
""",

"""
May your heart
always remain young
and your smile never fade.
Happy Birthday!
""",

"""
Wishing you
an unforgettable birthday
filled with joy and celebration.
""",

"""
Happy Birthday!
May success,
love and happiness always find you.
""",

"""
May your special day
be filled with warmth,
kindness and laughter.
""",

"""
Here's to another year
of making beautiful memories.
Happy Birthday!
""",

"""
May your birthday
be the start
of a year full of achievements.
""",

"""
Wishing you peace,
prosperity and happiness
today and always.
Happy Birthday!
""",

"""
Birthdays are not about growing older,
they are reminders that time is trusting you
with another chapter to write.
Happy Birthday!
""",

"""
A beautiful life is not measured by years,
but by the lives you touch
and the memories you leave behind.
Happy Birthday!
""",

"""
Every birthday is a quiet reminder
that life is finite,
and that makes every moment priceless.
Happy Birthday!
""",

"""
May this year give you
more reasons to grow
than reasons to regret.
Happy Birthday!
""",

"""
The greatest gift of another year
is not age,
but perspective.
Happy Birthday!
""",

"""
Time changes everyone,
but wisdom belongs only
to those who learn from it.
Happy Birthday!
""",

"""
May your journey
always be richer in experiences
than in possessions.
Happy Birthday!
""",

"""
A birthday is life whispering,
'There is still more for you
to become.'
Happy Birthday!
""",

"""
The candles on your cake
do not count your years,
they illuminate your journey.
Happy Birthday!
""",

"""
May your heart remain curious,
your mind remain humble
and your soul remain fearless.
Happy Birthday!
""",

"""
Growing older is inevitable,
growing wiser is a choice.
May you choose wisely.
Happy Birthday!
""",

"""
The finest victories in life
are the ones
you achieve over yourself.
Happy Birthday!
""",

"""
Every year teaches a lesson,
every lesson shapes a life.
May yours always be meaningful.
Happy Birthday!
""",

"""
Life rarely gives certainty,
but it always offers possibility.
May you embrace both.
Happy Birthday!
""",

"""
Success is temporary,
character is timeless.
May this year strengthen both.
Happy Birthday!
""",

"""
May you never lose
the courage to begin again,
no matter how many birthdays pass.
""",

"""
Another year has passed,
yet your greatest masterpiece
is still the person you are becoming.
Happy Birthday!
""",

"""
Do not count the candles,
count the moments
that made your soul feel alive.
Happy Birthday!
""",

"""
The most meaningful journeys
are not across places,
but within ourselves.
Happy Birthday!
""",

"""
May your dreams
always be bigger than your fears
and your gratitude greater than both.
Happy Birthday!
""",

"""
Every sunrise is a gift,
every birthday is proof
that hope has not given up on you.
""",

"""
Life is less about finding yourself
and more about creating someone
worth remembering.
Happy Birthday!
""",

"""
A meaningful life
is built one ordinary day
at a time.
Happy Birthday!
""",

"""
The strongest people
are not those who never fall,
but those who always rise.
Happy Birthday!
""",

"""
May this birthday
bring you fewer distractions
and more purpose.
""",

"""
A year well lived
is worth more
than a decade merely survived.
Happy Birthday!
""",

"""
Happiness is not a destination,
it is the way
you choose to travel.
Happy Birthday!
""",

"""
Your greatest competition
has always been
the person you were yesterday.
Happy Birthday!
""",

"""
Some people grow older,
others grow deeper.
May you always choose depth.
Happy Birthday!
""",

"""
Life rewards
those who remain patient
while pursuing their purpose.
Happy Birthday!
""",

"""
Every birthday is evidence
that the universe
still believes in your story.
""",

"""
May your legacy
be measured not by wealth,
but by kindness.
Happy Birthday!
""",

"""
Do not fear the passing years;
fear only the days
that pass without meaning.
Happy Birthday!
""",

"""
The richest people
are those whose hearts
remain grateful despite everything.
Happy Birthday!
""",

"""
Wisdom begins
where the need to impress
comes to an end.
Happy Birthday!
""",

"""
The most beautiful version of life
is written with courage,
not comfort.
Happy Birthday!
""",

"""
May every scar
become a story,
and every story become strength.
Happy Birthday!
""",

"""
Life owes us nothing,
yet every birthday
arrives like an unexpected gift.
Cherish it.
""",

"""
The older we become,
the less we need perfection
and the more we appreciate peace.
Happy Birthday!
""",

"""
May your success
never be louder
than your humility.
Happy Birthday!
""",

"""
A fulfilled life
is not one without storms,
but one that keeps sailing.
Happy Birthday!
""",

"""
Every birthday
is another opportunity
to become the person
your younger self admired.
""",

"""
Some years add age,
the best ones add wisdom.
May this be one of them.
Happy Birthday!
""",

"""
The purpose of life
is not merely to exist,
but to leave light behind.
Happy Birthday!
""",

"""
May you always
find beauty in simplicity
and strength in silence.
Happy Birthday!
""",

"""
The world remembers achievements,
but hearts remember kindness.
May you be remembered well.
Happy Birthday!
""",

"""
Time never waits,
yet it always leaves enough room
for those willing to begin again.
Happy Birthday!
""",

"""
A birthday is not the end
of another year,
but the beginning of another chance.
""",

"""
Live in such a way
that your presence
becomes someone's favorite memory.
Happy Birthday!
""",

"""
The greatest celebration
is not adding another year,
but becoming someone
worthy of the years you've lived.
Happy Birthday!
""",

"""
Hope your birthday
brings endless reasons
to celebrate life.
""",

"""
May every passing year
make your life
even more meaningful.
Happy Birthday!
""",

"""
Sending smiles,
warm wishes and positive vibes
on your birthday.
""",

"""
Happy Birthday!
May your future
be brighter than ever before.
""",

"""
May your day
be as sweet as cake,
as bright as sunshine
and as joyful as laughter.
""",

"""
Wishing you
love that never fades,
dreams that never stop
and happiness that never ends.
Happy Birthday!
""",

"""
Have a birthday
filled with family,
friends and beautiful memories
to treasure forever.
""",

"""
May today
be full of blessings,
gratitude and joyful moments.
Happy Birthday!
""",

"""
Happy Birthday!
May every new day
bring fresh hope and success.
""",

"""
Wishing you courage
to chase your dreams
and happiness to enjoy the journey.
""",

"""
May your life
continue to bloom
with happiness and success.
Happy Birthday!
""",

"""
Hope your birthday
is filled with everything
that makes you smile.
""",

"""
May this birthday
bring you closer
to all your goals and dreams.
""",

"""
Happy Birthday!
May your heart
always find reasons to celebrate.
""",

"""
Wishing you
countless blessings,
beautiful moments
and endless happiness.
""",

"""
May laughter fill your day,
love fill your heart
and success fill your life.
Happy Birthday!
""",

"""
Another year,
another blessing,
another reason to celebrate.
Happy Birthday!
""",

"""
May every birthday
remind you
how truly special you are.
""",

"""
Hope your special day
is surrounded by love,
laughter and lasting memories.
Happy Birthday!
""",

"""
Wishing you
joy today,
success tomorrow
and happiness forever.
Happy Birthday!
""",

"""
May this birthday
open the door
to exciting new opportunities.
""",

"""
Happy Birthday!
Stay happy,
stay healthy
and keep shining.
""",

"""
May every dream
you hold close to your heart
come true this year.
Happy Birthday!
""",

"""
Wishing you
beautiful beginnings,
wonderful experiences
and endless joy.
Happy Birthday!
""",

"""
Celebrate yourself today,
because you deserve
all the happiness in the world.
Happy Birthday!
"""

]

_available = messages.copy()
random.shuffle(_available)

def random_message():
    global _available

    if not _available:
        _available = messages.copy()
        random.shuffle(_available)

    return _available.pop()

birthday_songs = [

    (
        "Happy Birthday To You 🎉",
        "https://www.youtube.com/watch?v=R0be6mdFTgU"
    ),

    (
        "Happy Birthday Song (Classic)",
        "https://www.youtube.com/watch?v=kgorGhLmeA0"
    ),

    (
        "Pharrell Williams - Happy",
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    ),

    (
        "Justin Timberlake - CAN'T STOP THE FEELING!",
        "https://www.youtube.com/watch?v=ru0K8uYEZWw"
    ),

    (
        "Kool & The Gang - Celebration",
        "https://www.youtube.com/watch?v=3GwjfUFyY6M"
    ),

    (
        "Katy Perry - Birthday",
        "https://www.youtube.com/watch?v=jqYxyd1iSNk"
    ),

    (
        "Stevie Wonder - Happy Birthday",
        "https://www.youtube.com/watch?v=inS9gAgSENE"
    ),

    (
        "Maroon 5 - Sugar",
        "https://www.youtube.com/watch?v=09R8_2nJtjg"
    ),

    (
        "Coldplay - A Sky Full of Stars",
        "https://www.youtube.com/watch?v=VPRjCeoBqrI"
    ),

    (
        "OneRepublic - I Lived",
        "https://www.youtube.com/watch?v=z0rxydSolwU"
    ),

    (
        "Imagine Dragons - On Top Of The World",
        "https://www.youtube.com/watch?v=w5tWYmIOWGk"
    ),

    (
        "American Authors - Best Day Of My Life",
        "https://www.youtube.com/watch?v=Y66j_BUCBMY"
    ),

    (
        "Walk Off The Earth - Fire In My Soul",
        "https://www.youtube.com/watch?v=F9kXstb9FF4"
    ),

    (
        "Instrumental Birthday Music",
        "https://www.youtube.com/results?search_query=happy+birthday+instrumental+piano"
    ),

    (
        "Relaxing Piano Birthday Music",
        "https://www.youtube.com/results?search_query=happy+birthday+piano"
    ),

]

def random_song():
    return random.choice(birthday_songs)