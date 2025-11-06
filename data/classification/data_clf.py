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
    "Genshin Impact", "Apex Legends Mobile", "Brawl Stars", "Free Fire", "League of Legends",
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