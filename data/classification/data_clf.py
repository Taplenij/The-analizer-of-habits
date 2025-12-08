entertainment_apps = [
    "TikTok", "YouTube", "Netflix", "Instagram", "Snapchat", "Spotify", "Twitch", "Disney+",
    "HBO Max", "Roblox", "Fortnite", "Steam", "Discord", "Pinterest", "SoundCloud", "Reddit",
    "Prime Video", "Apple Music", "Audible", "Shazam", "VK", "Likee", "Telegram", "WeChat",
    "LINE", "Clubhouse", "Tumblr", "iQIYI", "Bilibili", "Crunchyroll", "IMDB", "Vimeo",
    "MX Player", "Hotstar", "Yandex Music", "Last.fm", "Deezer", "Pandora", "Tidal", "9GAG",
    "Goodreads", "Stadia", "Epic Games Store", "Apple TV+", "Resso", "Napster", "Zedge",
    "Pocket Casts", "Overcast"
]

education_apps = [
    "Duolingo", "Khan Academy", "Coursera", "edX", "Udemy", "Quizlet", "Google Classroom",
    "Photomath", "Wolfram Alpha", "Brainly", "Udacity", "Brilliant", "Babbel", "Rosetta Stone",
    "SoloLearn", "Skillshare", "LinkedIn Learning", "Codecademy", "Lumosity", "Memrise",
    "Mimo", "Microsoft Math Solver", "Kahoot", "StudySmarter", "Busuu", "TED", "EWA",
    "Unacademy", "Byju’s", "Alison", "Chegg", "MasterClass", "OpenLearn", "Treehouse",
    "Replit", "Geogebra", "Canva for Education", "Preply", "LingQ", "FluentU", "Mathway",
    "LeetCode", "SoloLearn Pro", "Khan Kids", "LearnPython", "Coursera Plus", "Codewars",
    "Hackerrank", "Brighterly", "Codecademy Go", "Brilliant Kids"
]

system_apps = [
    "Google Chrome", "Gmail", "Google Maps", "Google Drive", "Microsoft Teams", "Dropbox",
    "OneDrive", "Windows Defender", "CCleaner", "Total Commander", "FileZilla", "WinRAR",
    "7-Zip", "Ubuntu", "macOS Finder", "Task Manager", "iCloud", "Firefox", "Safari",
    "Edge", "Brave", "Opera", "NordVPN", "ExpressVPN", "LastPass", "Bitwarden", "Notepad++",
    "Visual Studio Code", "Sublime Text", "Atom", "PyCharm", "IntelliJ IDEA", "System Monitor",
    "Alfred", "Launchy", "CleanMyMac", "Malwarebytes", "Avast", "AVG", "Norton", "McAfee",
    "Kaspersky", "VirtualBox", "VMware", "Docker", "GitHub Desktop", "GitLab Runner",
    "Windows Terminal", "PowerToys", "Monitorian", "Process Explorer", "Recuva"
]

work_apps = [
    "Slack", "Zoom", "Microsoft Office", "Trello", "Asana", "Notion", "ClickUp", "Monday.com",
    "Google Docs", "Google Sheets", "Google Slides", "Evernote", "Jira", "Confluence",
    "Basecamp", "Airtable", "Miro", "Figma", "Canva", "Adobe Photoshop", "Illustrator",
    "Lightroom", "Premiere Pro", "After Effects", "DaVinci Resolve", "WPS Office", "LibreOffice",
    "OnlyOffice", "Zoho Projects", "Smartsheet", "HubSpot", "Salesforce", "PipeDrive", "Bitrix24",
    "Toggl Track", "RescueTime", "Harvest", "Clockify", "Slack Huddle", "Zoom Rooms",
    "Google Meet", "Webex", "BlueJeans", "Dropbox Paper", "Microsoft Planner", "Google Keep",
    "Obsidian", "Roam Research", "Everhour", "Todoist", "Basecamp 3"
]

other_apps = [
    "Uber", "Bolt", "Lyft", "BlaBlaCar", "Google Pay", "Apple Pay", "PayPal", "Venmo",
    "Cash App", "Yandex Go", "Delivery Club", "DoorDash", "Glovo", "Uber Eats", "Wolt",
    "AliExpress", "Amazon Shopping", "Ozon", "Wildberries", "eBay", "Shein", "Booking.com",
    "Airbnb", "TripAdvisor", "Expedia", "Google Earth", "Weather.com", "AccuWeather",
    "Yahoo Mail", "ProtonMail", "Signal", "Viber", "Messenger", "WhatsApp", "Telegram X",
    "Truecaller", "MyFitnessPal", "Strava", "Fitbit", "Nike Run Club", "Adidas Running",
    "Samsung Health", "Headspace", "Calm", "Flo", "Period Tracker", "Sleep Cycle",
    "Google Calendar", "Outlook Calendar", "Forest", "Daylio"
]

games_apps = [
    "Minecraft", "Among Us", "Clash of Clans", "Clash Royale", "PUBG Mobile", "Call of Duty Mobile",
    "Genshin Impact", "Brawl Stars", "Free Fire", "League of Legends",
    "Valorant", "Counter-Strike 2", "Dota 2", "Overwatch 2", "Rocket League", "The Sims 4",
    "GTA V", "Cyberpunk 2077", "Elden Ring", "Baldur’s Gate 3", "Honkai Star Rail",
    "Candy Crush Saga", "Subway Surfers", "Temple Run", "Angry Birds", "Plants vs Zombies",
    "Stumble Guys", "Mobile Legends", "Arena of Valor", "Pokemon Go", "Tetris", "Wordle",
    "2048", "Crossy Road", "Asphalt 9", "Real Racing 3", "Hill Climb Racing", "Mini Metro",
    "Monument Valley", "Geometry Dash", "SimCity", "Fall Guys", "Destiny 2", "Roblox Studio",
    "The Witcher 3", "Red Dead Redemption 2", "Skyrim", "Valorant Mobile", "World of Tanks"
]

categories = ['Games', 'Entertainments', 'Education', 'Work', 'System', 'Other']

dict_apps = {k: v for k, v in zip(categories, [games_apps, entertainment_apps,
                                               education_apps,work_apps,
                                               system_apps, other_apps])}
addit_data = {'Baldur’s Gate 3': 'A story-driven RPG set in the Dungeons & Dragons universe, featuring branching narratives, tactical combat, and deep role-playing. Players explore detailed environments, interact with companions, and make impactful choices that shape the world.',
'Stumble Guys': 'A colorful multiplayer party game where up to 32 players race through chaotic obstacle courses. Fast rounds, silly physics, and fun cosmetics make it popular among casual mobile gamers.',
'Valorant Mobile': 'The mobile adaptation of Riot’s tactical 5v5 shooter, combining precise gunplay with strategic agent abilities. Optimized controls and streamlined maps recreate the competitive feel of the PC version.',
'SoloLearn': 'A beginner-friendly coding platform with lessons, quizzes, and hands-on practice in languages like Python and JavaScript. Community features and gamification help learners stay motivated.',
'StudySmarter': 'A study platform offering flashcards, notes, and personalized study plans. Spaced repetition, progress analytics, and shared learning materials help students prepare for exams effectively.',
'Byju’s': 'An educational app with video lessons, quizzes, and adaptive learning paths for school subjects. Visual explanations and personalized assessments support deep understanding for learners of all ages.',
'Canva for Education': 'A design tool for teachers and students to create presentations, posters, and worksheets. Classroom templates and collaboration features support creative assignments and group projects.',
'LingQ': 'A language-learning app focused on immersion through reading and listening. Users import content, save vocabulary, and learn naturally through meaningful exposure.',
'FluentU': 'A language-learning app using real-world videos with interactive subtitles and personalized quizzes. It teaches vocabulary in context and tracks learner progress.',
'Mathway': 'A math-solving app providing step-by-step explanations for algebra, calculus, and more. Users enter problems via text or camera to receive structured solutions.',
'SoloLearn Pro': 'The premium version of SoloLearn offering advanced coding exercises, deeper insights, and unlimited learning tools for motivated learners.',
'Khan Kids': 'An educational app for children featuring interactive lessons in math, literacy, and social-emotional learning through stories, videos, and games.',
'LearnPython': 'A beginner-focused Python learning app with clear lessons, quizzes, and hands-on programming exercises that cover variables, loops, functions, and more.',
'Coursera Plus': 'A subscription that provides unlimited access to thousands of courses and professional certificates from leading universities and companies.',
'Hackerrank': 'A coding challenge platform offering algorithm problems, interview prep, and domain-specific tasks. Leaderboards and contests help developers grow their skills.',
'Brighterly': 'A children’s math-learning platform offering personalized one-on-one tutoring, interactive exercises, and visual explanations to build confidence and mastery.',
'Codecademy Go': 'A mobile companion to Codecademy that delivers quick quizzes and micro-lessons to reinforce programming concepts on the go.',
'Brilliant Kids': 'A STEM-focused learning app with puzzles and interactive challenges that teach math, logic, and scientific thinking through play.',
'PipeDrive': 'A sales CRM designed to track leads, manage pipelines, automate tasks, and provide insights through intuitive visual dashboards.',
'Bitrix24': 'A collaboration suite offering CRM, project management, chat, cloud storage, and workflow automation in a unified workspace.',
'RescueTime': 'A productivity tool that automatically tracks digital activity, categorizes usage, and provides insights to help improve focus and work habits.',
'Clockify': 'A time-tracking app for individuals and teams with timers, project tracking, reports, and scheduling, widely used by freelancers and remote workers.',
'Slack Huddle': 'An informal audio meeting feature inside Slack that enables quick real-time conversations, screen sharing, and lightweight collaboration.',
'Zoom Rooms': 'A room-based conferencing system integrating displays, cameras, and audio devices for seamless hybrid meetings in professional environments.',
'Roam Research': 'A note-taking tool based on networked thought, using bidirectional links to connect ideas and support deep research and knowledge organization.',
'Todoist': 'A task management app with priorities, labels, reminders, recurring tasks, and collaboration features for organizing personal and work responsibilities.',
'Basecamp 3': 'A project-management platform combining messaging, to-dos, file sharing, and scheduling to keep team communication organized and efficient.',
'macOS Finder': 'The default macOS file manager used to browse, organize, and manage documents, drives, and cloud files with tagging, previews, and search.',
'GitLab Runner': 'A lightweight tool that executes CI/CD jobs for GitLab pipelines, supporting Docker, virtual machines, and local environments for automated builds.',
'Monitorian': 'A simple Windows utility for adjusting brightness across multiple monitors, offering quick access and hardware-level control.',
'Yandex Go': 'A multi-service app combining taxi rides, food delivery, car-sharing, and courier tools, streamlining everyday urban mobility.',
'Delivery Club': 'A food delivery platform offering restaurant menus, grocery options, real-time tracking, ratings, and easy digital payments.',
'Nike Run Club': 'A running app with GPS tracking, guided runs, training plans, and community challenges to help runners improve performance.',
'Adidas Running': 'A fitness tracking app for running and walking, offering GPS metrics, challenges, training plans, and wearable integrations.',
'Period Tracker': 'An app for tracking menstrual cycles, symptoms, moods, and ovulation with predictions, reminders, and personalized health insights.',
'Twitch': 'A live-streaming platform primarily for gamers, creators, and online communities to broadcast and watch real-time content.',
'Shazam': 'An audio recognition app that identifies songs, lyrics, and artists by listening to short audio snippets.',
'VK': 'A social networking platform popular in Eastern Europe, offering messaging, media sharing, communities, and music streaming.',
'Clubhouse': 'A social audio app where users join live voice chat rooms to discuss topics, host panels, and listen to conversations.',
'Tidal': 'A music streaming service known for high-fidelity audio quality and exclusive content from artists.',
'Stadia': 'Google’s cloud gaming service that allowed users to stream and play video games without dedicated hardware (now discontinued).',
'Brilliant': 'An interactive learning platform focused on math, science, and computer science through problem-solving and engaging courses.',
'TED': 'An app offering access to TED Talks—short, influential presentations on ideas in technology, education, design, and more.',
'EWA': 'A language-learning app that uses short lessons, books, movies, and AI tools to help users study English and other languages.',
'Alison': 'An online learning platform providing free courses and certificates in a wide range of professional fields.',
'Slack': 'A team communication platform enabling organized messaging, channels, file sharing, and integrations for workplace collaboration.',
'Zoom': 'A video conferencing app used for meetings, webinars, and online communication with screen-sharing and collaboration tools.',
'Notion': 'An all-in-one workspace app combining notes, databases, tasks, and wiki features for personal and team productivity.',
'Miro': 'A collaborative online whiteboard tool used for brainstorming, diagramming, workshops, and remote teamwork.',
'Edge': 'Microsoft’s web browser focused on speed, security, and productivity features like collections and vertical tabs.',
'Brave': 'A privacy-focused web browser that blocks trackers and ads while offering optional crypto-based rewards.',
'Alfred': 'A productivity app for macOS that enhances search, shortcuts, and automation for faster workflows.',
'Norton': 'A cybersecurity suite providing antivirus protection, VPN, device security, and identity-theft safeguards.',
'Bolt': 'A ride-hailing and mobility app offering transportation, scooters, car rentals, and food delivery services.',
'Headspace': 'A meditation and mindfulness app offering guided sessions, sleep sounds, and mental-well-being exercises.',
'Calm': 'A relaxation and sleep app featuring meditations, breathing exercises, music, and soothing bedtime stories.',
'Flo': 'A women’s health app for period tracking, ovulation prediction, health insights, and cycle-based guidance.'}