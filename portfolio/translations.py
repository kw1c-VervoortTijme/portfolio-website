# portfolio/translations.py

# Dictionary of translations for each language
TRANSLATIONS = {
'en': {
        # Navigation & Common Elements
        'portfolio_website': 'Portfolio Website',
        'home': 'Home',
        'internship_1': 'Internship 1',
        'internship_2': 'Internship 2',
        'portfolio': 'Portfolio',
        'admin_panel': 'Admin Panel',
        'login': 'Login',
        'register': 'Register',
        'logout': 'Logout',
        'close': 'Close',
        'profile_picture': 'Profile Picture',
        'toggle_navigation': 'Toggle navigation',
        'copyright': 'Tijme Vervoort.',
        'language': 'Language',
        
        # Page Titles
        'home_title': 'Home - Portfolio Website',
        'login_title': 'Login - Portfolio Website',
        'register_title': 'Register - Portfolio Website',
        'portfolio_title': 'Portfolio - Portfolio Website',
        'internship1_title': 'Internship 1 - Portfolio Website',
        'internship2_title': 'Internship 2 - Portfolio Website',
        
        # Demo Notice
        'demo_notice_title': 'Demo Notice:',
        'demo_notice_register': 'This registration form serves demonstration purposes exclusively. No authentic account will be established, and no data will be permanently stored.',
        'demo_notice_login': 'This login form is designed purely for demonstration purposes. The authentication system exemplifies my Django development expertise.',
        
        # Home Page
        'about_tijme_heading': 'About Tijme Vervoort',
        'skills_and_learning': 'Skills and Projects',
        'welcome_message': 'Welcome. Here you can discover comprehensive information about Tijme',
        'home_bio_p1': 'I am 21 years old and currently reside with my parents and two siblings—one brother and one sister—in Nistelrode. Throughout my educational journey, I have attended multiple institutions. In 2007, I commenced my primary education at De Beekgraaf elementary school in Nistelrode. During my eighth year, I transferred to De Brinck to complete my primary education. Subsequently, I progressed to Udens College in Uden, pursuing studies at the kader-theoretisch level, which ultimately led me to KW1C in \'s-Hertogenbosch. Initially, I enrolled in the Architecture Construction program before transitioning to my current Software Developer program. I am presently in my third year of the Software Developer curriculum. I have successfully completed an internship with Omnilan, a company that provided valuable learning opportunities. Currently, I am undertaking an internship at AB Transport, a logistics company specializing in delivery and collection services for corporate clients. This position has proven exceptionally beneficial, as I am stationed within the IT department, where I am acquiring extensive knowledge about Python programming language and Django framework implementation.',
        'home_bio_p2': 'Throughout this educational program, I have accumulated substantial experience through various project-based assignments, including the development of a comprehensive website for a sports club. Currently, we are embarking on the creation of our portfolio website. During this period, I have significantly enhanced my understanding of C# and its practical application in project development. Additionally, I have gained considerable expertise in web development through both academic assignments and hands-on internship experience. This knowledge acquisition has been particularly rewarding, as I now possess the technical competency to construct websites and understand how to leverage these skills professionally in the future. Furthermore, during my previous educational program, I had the opportunity to engage in diverse and stimulating projects, including the design and construction of a restaurant featuring steel framework, a 1930s-era residential building, and a recreational facility for young people. I successfully completed the majority of these projects with commendable results. This comprehensive experience will undoubtedly prove invaluable in my future professional endeavors.',
        
        # Login Page
        'login_header': 'User Authentication',
        'username': 'Username',
        'password': 'Password',
        'login_error': 'The provided username and password combination is invalid. Please verify your credentials and attempt again.',
        'dont_have_account': 'Don\'t have an account yet?',
        'register_here': 'Create an account here',
        
        # Register Page
        'create_account': 'Create a New Account',
        'email': 'Email Address',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'confirm_password': 'Confirm Password',
        'username_requirements': 'Required field. Maximum 150 characters. Accepts letters, digits, and the following symbols: @/./+/-/_ only.',
        'password_req1': 'Your password must not closely resemble your other personal information.',
        'password_req2': 'Your password must comprise a minimum of 8 characters.',
        'password_req3': 'Your password cannot be a commonly utilized password.',
        'password_req4': 'Your password cannot consist entirely of numeric characters.',
        'password_confirm_help': 'Re-enter the identical password as specified above for verification purposes.',
        'register_button': 'Create Account',
        'already_account': 'Already possess an account?',
        
        # Portfolio Page
        'portfolio_projects': 'Portfolio Projects',
        'rainbow_project': 'Rainbow Project',
        'match_table': 'Match Table Project',
        'exercise_1_6': 'CSS Table Alignment Exercise',
        'exercise_2_1': 'Row and Column Span Project',
        'rainbow_desc': 'Rainbow Project: This represents assignment 3.2 from the first theme, which I found particularly engaging to develop. The challenge involved implementing span classes, a technique I was initially uncertain about. Overall, I believe the execution was highly successful.',
        'match_table_desc': 'Match Table: This screenshot originates from my inaugural project and demonstrates effective problem-solving. The objective was to display all Den Bosch matches comprehensively. After careful consideration, I implemented a table-based solution—a methodology we had not previously utilized. This marked my first successful application of tabular data presentation for this type of challenge.',
        'exercise_1_6_desc': 'realign tables using css I found this assignment reasonably manageable, as we received an HTML file that was completely disorganized and lacked CSS styling. The challenge required us to restore its visual appeal through strategic implementation of table structures and row organization.',
        'exercise_2_1_desc': 'working with rows and colums This proved to be an exceptionally enjoyable assignment, particularly because it allowed us to experiment with row-span and column-span properties. The final outcome was remarkably successful, clearly demonstrating the necessity of utilizing classes and IDs to achieve varied color schemes within the table structure.',
        
        # Stage 1 Page
        'omnilan': 'Omnilan',
        'ispconfig': 'ISPConfig',
        'ispconfig_desc': 'This represents the primary dashboard interface of ISPConfig',
        'email_domain_desc': 'This interface enables the creation of email domains for addresses associated with your website',
        'email_address_desc': 'This section facilitates the establishment of email addresses for your website\'s domain',
        'rememberz': 'Rememberz',
        'rememberz_menu_desc': 'This displays the primary navigation interface for Rememberz users',
        'milight_desc': 'These represent user configuration settings for lighting control, including color adjustment capabilities. These features are particularly prominent in the left-hand section of the interface.',
        'rememberz_main_desc': 'This constitutes the central navigation hub of the Rememberz platform',
        
        # Stage 2 Page
        'second_internship': 'AB Transport Internship: Web Development & Online Learning',
        'wagtail_desc': 'Conducted comprehensive exploration of the Wagtail CMS through structured online coursework, mastering the development of sophisticated dynamic content management systems for web applications.',
        'cms_desc': 'Collaborated extensively with content management systems to architect interactive blog publications, incorporating advanced features such as FAQ sections and dynamic carousel components.',
        'bootstrap_email_desc': 'Designed and implemented professional email template solutions utilizing Bootstrap Email framework for AB Transport, creating responsive email signatures and sophisticated layout designs.',
        'programming_skills': 'Advanced Programming Competency Development',
        'coding_topics_desc': 'Conducted in-depth exploration of diverse programming disciplines including Python, JavaScript, HTML & CSS, SQL, and additional technologies through methodically structured online learning programs.',
        'codecademy_desc': 'Successfully completed multiple comprehensive Python courses on Codecademy, encompassing intermediate and advanced Python programming concepts, as well as specialized Django web development frameworks.',
    },

 'nl': {
        # Navigation & Common Elements
        'portfolio_website': 'Portfolio Website',
        'home': 'Home',
        'internship_1': 'Stage 1',
        'internship_2': 'Stage 2',
        'portfolio': 'Portfolio',
        'admin_panel': 'Beheerderspaneel',
        'login': 'Inloggen',
        'register': 'Registreren',
        'logout': 'Uitloggen',
        'close': 'Sluiten',
        'profile_picture': 'Profielfoto',
        'toggle_navigation': 'Navigatie weergeven/verbergen',
        'copyright': 'Tijme Vervoort.',
        'language': 'Taal',
        
        # Page Titles
        'home_title': 'Home - Portfolio Website',
        'login_title': 'Inloggen - Portfolio Website',
        'register_title': 'Registreren - Portfolio Website',
        'portfolio_title': 'Portfolio - Portfolio Website',
        'internship1_title': 'Stage 1 - Portfolio Website',
        'internship2_title': 'Stage 2 - Portfolio Website',
        
        # Demo Notice
        'demo_notice_title': 'Demonstratie Kennisgeving:',
        'demo_notice_register': 'Dit registratieformulier dient uitsluitend demonstratiedoeleinden. Er zal geen authentiek account worden geëstableerd en geen gegevens zullen permanent worden opgeslagen.',
        'demo_notice_login': 'Dit inlogformulier is exclusief ontworpen voor demonstratiedoeleinden. Het authenticatiesysteem exemplificeert mijn Django-ontwikkelingsexpertise.',
        
        # Home Page
        'about_tijme_heading': 'Over Tijme Vervoort',
        'skills_and_learning': 'Vaardigheden en Projecten',
        'welcome_message': 'Welkom. Hier kunt u uitgebreide informatie over Tijme ontdekken',
        'home_bio_p1': 'Ik ben 21 jaar oud en resideer momenteel bij mijn ouders en twee siblings—één broer en één zus—in Nistelrode. Gedurende mijn educatieve traject heb ik meerdere onderwijsinstellingen bezocht. In 2007 initieerde ik mijn primaire onderwijs aan basisschool De Beekgraaf in Nistelrode. Tijdens mijn achtste leerjaar transfereerde ik naar De Brinck om mijn basisonderwijs aldaar te voltooien. Vervolgens progresseerde ik naar het Udens College in Uden, waar ik studies volgde op kader-theoretisch niveau, hetgeen mij uiteindelijk naar KW1C in \'s-Hertogenbosch leidde. Aanvankelijk schreef ik mij in voor het programma Bouwkunde Architectuur alvorens over te stappen naar mijn huidige Software Developer programma. Momenteel bevind ik mij in mijn derde jaar van het Software Developer curriculum. Ik heb succesvol een stage voltooid bij Omnilan, een onderneming die waardevolle leermogelijkheden bood. Thans onderneem ik een stage bij AB Transport, een logistiek bedrijf gespecialiseerd in leverings- en ophaaldiensten voor zakelijke klanten. Deze positie heeft zich buitengewoon voordelig bewezen, aangezien ik gestationeerd ben binnen de IT-afdeling, waar ik uitgebreide kennis opdoe betreffende de Python programmeertaal en Django framework implementatie.',
        'home_bio_p2': 'Gedurende dit educatieve programma heb ik substantiële ervaring geaccumuleerd door middel van diverse projectgebaseerde opdrachten, inclusief de ontwikkeling van een uitgebreide website voor een sportvereniging. Momenteel embarqueren wij op de creatie van onze portfolio website. Tijdens deze periode heb ik mijn begrip van C# aanzienlijk versterkt evenals de praktische toepassing ervan in projectontwikkeling. Daarnaast heb ik considerable expertise opgedaan in webontwikkeling door zowel academische opdrachten als hands-on stage-ervaring. Deze kennisacquisitie is bijzonder lonend geweest, aangezien ik thans de technische competentie bezit om websites te construeren en begrijp hoe deze vaardigheden professioneel in de toekomst te benutten. Voorts had ik tijdens mijn vorige educatieve programma de gelegenheid om diverse en stimulerende projecten aan te gaan, inclusief het ontwerp en de constructie van een restaurant met stalen framework, een residentieel gebouw uit de jaren 1930, en een recreatieve faciliteit voor jongeren. Ik voltooide de meerderheid van deze projecten met lovenswaardige resultaten. Deze uitgebreide ervaring zal ongetwijfeld van onschatbare waarde blijken in mijn toekomstige professionele ondernemingen.',
        
        # Login Page
        'login_header': 'Gebruikersauthenticatie',
        'username': 'Gebruikersnaam',
        'password': 'Wachtwoord',
        'login_error': 'De verstrekte gebruikersnaam en wachtwoord combinatie is ongeldig. Gelieve uw inloggegevens te verifiëren en opnieuw te proberen.',
        'dont_have_account': 'Beschikt u nog niet over een account?',
        'register_here': 'Creëer hier een account',
        
        # Register Page
        'create_account': 'Nieuw Account Creëren',
        'email': 'E-mailadres',
        'first_name': 'Voornaam',
        'last_name': 'Achternaam',
        'confirm_password': 'Wachtwoord Bevestigen',
        'username_requirements': 'Verplicht veld. Maximum 150 karakters. Accepteert letters, cijfers, en de volgende symbolen: @/./+/-/_ uitsluitend.',
        'password_req1': 'Uw wachtwoord mag niet nauw overeenkomen met uw andere persoonlijke informatie.',
        'password_req2': 'Uw wachtwoord dient minimaal 8 karakters te bevatten.',
        'password_req3': 'Uw wachtwoord kan geen veelgebruikt wachtwoord zijn.',
        'password_req4': 'Uw wachtwoord kan niet uitsluitend uit numerieke karakters bestaan.',
        'password_confirm_help': 'Voer het identieke wachtwoord zoals hierboven gespecificeerd in ter verificatie.',
        'register_button': 'Account Aanmaken',
        'already_account': 'Beschikt u reeds over een account?',
        
        # Portfolio Page
        'portfolio_projects': 'Portfolio Projecten',
        'rainbow_project': 'Regenboog Project',
        'match_table': 'Wedstrijdtabel Project',
        'exercise_1_6': 'CSS Tabel Uitlijning Oefening',
        'exercise_2_1': 'Rij en Kolom Span Project',
        'rainbow_desc': 'Regenboog Project: Dit representeert opdracht 3.2 van het eerste thema, welke ik bijzonder boeiend vond om te ontwikkelen. De uitdaging betrof het implementeren van span classes, een techniek waarover ik aanvankelijk onzeker was. Over het algemeen geloof ik dat de uitvoering zeer succesvol was.',
        'match_table_desc': 'Wedstrijdtabel: Deze screenshot origineert uit mijn inaugurele project en demonstreert effectieve probleemoplossing. Het objectief was om alle Den Bosch wedstrijden comprehensief weer te geven. Na zorgvuldige overweging implementeerde ik een tabel-gebaseerde oplossing—een methodologie die wij voorheen niet hadden benut. Dit markeerde mijn eerste succesvolle toepassing van tabulaire data presentatie voor dit type uitdaging.',
        'exercise_1_6_desc': 'Oefening 1.6: Ik vond deze opdracht redelijk beheersbaar, aangezien wij een HTML-bestand ontvingen dat volledig gedesorganiseerd was en CSS-styling miste. De uitdaging vereiste dat wij de visuele aantrekkelijkheid herstelden door strategische implementatie van tabelstructuren en rij-organisatie.',
        'exercise_2_1_desc': 'Oefening 2.1: Dit bewees een uitzonderlijk plezierige opdracht te zijn, met name omdat het ons toestond te experimenteren met row-span en column-span eigenschappen. Het finale resultaat was opmerkelijk succesvol, waarbij duidelijk de noodzaak werd gedemonstreerd van het benutten van classes en IDs om gevarieerde kleurenschema\'s binnen de tabelstructuur te realiseren.',
        
        # Stage 1 Page
        'omnilan': 'Omnilan',
        'ispconfig': 'ISPConfig',
        'ispconfig_desc': 'Dit representeert de primaire dashboard interface van ISPConfig',
        'email_domain_desc': 'Deze interface faciliteert de creatie van e-maildomeinen voor adressen geassocieerd met uw website',
        'email_address_desc': 'Deze sectie faciliteert de etablering van e-mailadressen voor het domein van uw website',
        'rememberz': 'Rememberz',
        'rememberz_menu_desc': 'Dit toont de primaire navigatie-interface voor Rememberz gebruikers',
        'milight_desc': 'Deze representeren gebruikersconfiguratie-instellingen voor verlichtingscontrole, inclusief kleuranpassingsmogelijkheden. Deze features zijn bijzonder prominent in de linkerhand sectie van de interface.',
        'rememberz_main_desc': 'Dit constitueert de centrale navigatiehub van het Rememberz platform',
        
        # Stage 2 Page
        'second_internship': 'Tweede Stage: Geavanceerde Webontwikkeling & Gestructureerd Online Leren',
        'wagtail_desc': 'Voerde uitgebreide exploratie uit van het Wagtail CMS door middel van gestructureerde online coursework, waarbij ik de ontwikkeling van gesofisticeerde dynamische content management systemen voor webapplicaties beheerste.',
        'cms_desc': 'Collaboreerde extensief met content management systemen om interactieve blog publicaties te architectureren, incorporerend geavanceerde features zoals FAQ secties en dynamische carousel componenten.',
        'bootstrap_email_desc': 'Ontwierp en implementeerde professionele e-mailtemplate oplossingen gebruikmakend van Bootstrap Email framework voor AB Transport, creërend responsieve e-mailhandtekeningen en gesofisticeerde layout designs.',
        'programming_skills': 'Geavanceerde Programmeercompetentie Ontwikkeling',
        'coding_topics_desc': 'Voerde diepgaande exploratie uit van diverse programmeer disciplines inclusief Python, JavaScript, HTML & CSS, SQL, en additionele technologieën door middel van methodisch gestructureerde online leerprogramma\'s.',
        'codecademy_desc': 'Voltooide succesvol meerdere uitgebreide Python cursussen op Codecademy, omvattend intermediate en geavanceerde Python programmeerconcepten, evenals gespecialiseerde Django webontwikkeling frameworks.',
    },
    'fr': {
        # Navigation & Common Elements
        'portfolio_website': 'Site de Portfolio',
        'home': 'Accueil',
        'internship_1': 'Stage 1',
        'internship_2': 'Stage 2',
        'portfolio': 'Portfolio',
        'admin_panel': 'Panneau d\'administration',
        'login': 'Connexion',
        'register': 'S\'inscrire',
        'logout': 'Déconnexion',
        'close': 'Fermer',
        'profile_picture': 'Photo de profil',
        'toggle_navigation': 'Basculer la navigation',
        'copyright': 'Tijme Vervoort.',
        'language': 'Langue',
        
        # Page Titles
        'home_title': 'Accueil - Site de Portfolio',
        'login_title': 'Connexion - Site de Portfolio',
        'register_title': 'Inscription - Site de Portfolio',
        'portfolio_title': 'Portfolio - Site de Portfolio',
        'internship1_title': 'Stage 1 - Site de Portfolio',
        'internship2_title': 'Stage 2 - Site de Portfolio',
        
        # Demo Notice
        'demo_notice_title': 'Avis de Démonstration:',
        'demo_notice_register': 'Ce formulaire d\'inscription sert exclusivement à des fins de démonstration. Aucun compte authentique ne sera établi et aucune donnée ne sera stockée de manière permanente.',
        'demo_notice_login': 'Ce formulaire de connexion est conçu uniquement à des fins de démonstration. Le système d\'authentification exemplifie mon expertise en développement Django.',
        
        # Home Page
        'about_tijme_heading': 'À Propos de Tijme Vervoort',
        'skills_and_learning': 'Compétences et Projets',
        'welcome_message': 'Bienvenue. Ici vous pouvez découvrir des informations exhaustives concernant Tijme',
        'home_bio_p1': 'J\'ai 21 ans et réside actuellement avec mes parents et deux fratries—un frère et une sœur—à Nistelrode. Tout au long de mon parcours éducatif, j\'ai fréquenté plusieurs établissements d\'enseignement. En 2007, j\'ai initié mon éducation primaire à l\'école élémentaire De Beekgraaf à Nistelrode. Durant ma huitième année, j\'ai effectué un transfert vers De Brinck afin d\'y achever mon enseignement primaire. Subséquemment, j\'ai progressé vers le Udens College à Uden, poursuivant des études au niveau kader-theoretisch, ce qui m\'a ultimement conduit au KW1C à \'s-Hertogenbosch. Initialement, je me suis inscrit au programme d\'Architecture Construction avant de transitionner vers mon programme actuel de Développeur de Logiciels. Je me trouve présentement en troisième année du curriculum Développeur de Logiciels. J\'ai accompli avec succès un stage chez Omnilan, une entreprise qui a fourni des opportunités d\'apprentissage précieuses. Actuellement, j\'entreprends un stage chez AB Transport, une compagnie logistique spécialisée dans les services de livraison et de collecte pour la clientèle corporative. Cette position s\'est avérée exceptionnellement bénéfique, étant donné que je suis stationné au sein du département informatique, où j\'acquiers des connaissances approfondies concernant le langage de programmation Python et l\'implémentation du framework Django.',
        'home_bio_p2': 'Tout au long de ce programme éducatif, j\'ai accumulé une expérience substantielle à travers diverses missions basées sur des projets, incluant le développement d\'un site web exhaustif pour un club sportif. Présentement, nous nous embarquons dans la création de notre site web de portfolio. Durant cette période, j\'ai considérablement renforcé ma compréhension du C# ainsi que son application pratique dans le développement de projets. De plus, j\'ai acquis une expertise considérable en développement web à travers tant les missions académiques que l\'expérience pratique de stage. Cette acquisition de connaissances s\'est révélée particulièrement gratifiante, puisque je possède désormais la compétence technique pour construire des sites web et comprends comment exploiter ces compétences professionnellement à l\'avenir. En outre, durant mon programme éducatif précédent, j\'ai eu l\'opportunité de m\'engager dans des projets diversifiés et stimulants, incluant la conception et la construction d\'un restaurant avec une charpente d\'acier, un bâtiment résidentiel des années 1930, et une installation récréative pour les jeunes. J\'ai achevé la majorité de ces projets avec des résultats louables. Cette expérience exhaustive s\'avérera indubitablement inestimable dans mes entreprises professionnelles futures.',
        
        # Login Page
        'login_header': 'Authentification Utilisateur',
        'username': 'Nom d\'utilisateur',
        'password': 'Mot de passe',
        'login_error': 'La combinaison nom d\'utilisateur et mot de passe fournie est invalide. Veuillez vérifier vos identifiants et réessayer.',
        'dont_have_account': 'Ne possédez-vous pas encore de compte?',
        'register_here': 'Créez un compte ici',
        
        # Register Page
        'create_account': 'Créer un Nouveau Compte',
        'email': 'Adresse électronique',
        'first_name': 'Prénom',
        'last_name': 'Nom de famille',
        'confirm_password': 'Confirmer le Mot de Passe',
        'username_requirements': 'Champ obligatoire. Maximum 150 caractères. Accepte les lettres, chiffres, et les symboles suivants: @/./+/-/_ exclusivement.',
        'password_req1': 'Votre mot de passe ne doit pas ressembler étroitement à vos autres informations personnelles.',
        'password_req2': 'Votre mot de passe doit comprendre un minimum de 8 caractères.',
        'password_req3': 'Votre mot de passe ne peut être un mot de passe communément utilisé.',
        'password_req4': 'Votre mot de passe ne peut consister entièrement en caractères numériques.',
        'password_confirm_help': 'Ressaisissez le mot de passe identique tel que spécifié ci-dessus à des fins de vérification.',
        'register_button': 'Créer le Compte',
        'already_account': 'Possédez-vous déjà un compte?',
        
        # Portfolio Page
        'portfolio_projects': 'Projets de Portfolio',
        'rainbow_project': 'Projet Arc-en-ciel',
        'match_table': 'Projet Tableau des Matchs',
        'exercise_1_6': 'Exercice d\'Alignement de Tableau CSS',
        'exercise_2_1': 'Projet Row-span et Column-span',
        'rainbow_desc': 'Projet Arc-en-ciel: Ceci représente l\'exercice 3.2 du premier thème, que j\'ai trouvé particulièrement captivant à développer. Le défi impliquait l\'implémentation de classes span, une technique sur laquelle j\'étais initialement incertain. Globalement, je crois que l\'exécution fut hautement réussie.',
        'match_table_desc': 'Tableau des Matchs: Cette capture d\'écran provient de mon projet inaugural et démontre une résolution de problème efficace. L\'objectif était d\'afficher tous les matchs de Den Bosch de manière exhaustive. Après considération attentive, j\'ai implémenté une solution basée sur tableau—une méthodologie que nous n\'avions pas précédemment utilisée. Ceci marqua ma première application réussie de présentation de données tabulaires pour ce type de défi.',
        'exercise_1_6_desc': 'Exercice 1.6: J\'ai trouvé cette mission raisonnablement gérable, puisque nous avons reçu un fichier HTML complètement désorganisé et dépourvu de style CSS. Le défi nécessitait que nous restaurions son attrait visuel à travers l\'implémentation stratégique de structures de tableau et d\'organisation de rangées.',
        'exercise_2_1_desc': 'Exercice 2.1: Ceci s\'est avéré être une mission exceptionnellement plaisante, particulièrement parce qu\'elle nous a permis d\'expérimenter avec les propriétés row-span et column-span. Le résultat final fut remarquablement réussi, démontrant clairement la nécessité d\'utiliser des classes et des IDs pour réaliser des schémas de couleurs variés au sein de la structure du tableau.',
        
        # Stage 1 Page
        'omnilan': 'Omnilan',
        'ispconfig': 'ISPConfig',
        'ispconfig_desc': 'Ceci représente l\'interface de tableau de bord principal d\'ISPConfig',
        'email_domain_desc': 'Cette interface facilite la création de domaines email pour les adresses associées à votre site web',
        'email_address_desc': 'Cette section facilite l\'établissement d\'adresses email pour le domaine de votre site web',
        'rememberz': 'Rememberz',
        'rememberz_menu_desc': 'Ceci affiche l\'interface de navigation principale pour les utilisateurs Rememberz',
        'milight_desc': 'Ceci représente les paramètres de configuration utilisateur pour le contrôle d\'éclairage, incluant les capacités d\'ajustement de couleur. Ces fonctionnalités sont particulièrement proéminentes dans la section gauche de l\'interface.',
        'rememberz_main_desc': 'Ceci constitue le hub de navigation central de la plateforme Rememberz',
        
        # Stage 2 Page
        'second_internship': 'Deuxième Stage: Développement Web Avancé & Apprentissage en Ligne Structuré',
        'wagtail_desc': 'Ai mené une exploration exhaustive du CMS Wagtail à travers des cours en ligne structurés, maîtrisant le développement de systèmes de gestion de contenu dynamiques sophistiqués pour les applications web.',
        'cms_desc': 'Ai collaboré extensivement avec les systèmes de gestion de contenu pour architecturer des publications de blog interactives, incorporant des fonctionnalités avancées telles que les sections FAQ et les composants de carrousel dynamiques.',
        'bootstrap_email_desc': 'Ai conçu et implémenté des solutions de modèles d\'email professionnels utilisant le framework Bootstrap Email pour AB Transport, créant des signatures d\'email responsives et des designs de mise en page sophistiqués.',
        'programming_skills': 'Développement de Compétences en Programmation Avancée',
        'coding_topics_desc': 'Ai mené une exploration approfondie de diverses disciplines de programmation incluant Python, JavaScript, HTML & CSS, SQL, et des technologies additionnelles à travers des programmes d\'apprentissage en ligne méthodiquement structurés.',
        'codecademy_desc': 'Ai complété avec succès plusieurs cours Python exhaustifs sur Codecademy, englobant les concepts de programmation Python intermédiaires et avancés, ainsi que les frameworks de développement web Django spécialisés.',
    },
    'de': {
        # Navigation & Common Elements
        'portfolio_website': 'Portfolio-Website',
        'home': 'Startseite',
        'internship_1': 'Praktikum 1',
        'internship_2': 'Praktikum 2',
        'portfolio': 'Portfolio',
        'admin_panel': 'Administrationspanel',
        'login': 'Anmelden',
        'register': 'Registrieren',
        'logout': 'Abmelden',
        'close': 'Schließen',
        'profile_picture': 'Profilbild',
        'toggle_navigation': 'Navigation umschalten',
        'copyright': 'Tijme Vervoort.',
        'language': 'Sprache',
        
        # Page Titles
        'home_title': 'Startseite - Portfolio-Website',
        'login_title': 'Anmelden - Portfolio-Website',
        'register_title': 'Registrieren - Portfolio-Website',
        'portfolio_title': 'Portfolio - Portfolio-Website',
        'internship1_title': 'Praktikum 1 - Portfolio-Website',
        'internship2_title': 'Praktikum 2 - Portfolio-Website',
        
        # Demo Notice
        'demo_notice_title': 'Demonstrationshinweis:',
        'demo_notice_register': 'Dieses Registrierungsformular dient ausschließlich Demonstrationszwecken. Es wird kein authentisches Konto etabliert und keine Daten werden permanent gespeichert.',
        'demo_notice_login': 'Dieses Anmeldeformular ist ausschließlich für Demonstrationszwecke konzipiert. Das Authentifizierungssystem exemplifiziert meine Django-Entwicklungsexpertise.',
        
        # Home Page
        'about_tijme_heading': 'Über Tijme Vervoort',
        'skills_and_learning': 'Fähigkeiten und Projekte',
        'welcome_message': 'Willkommen. Hier können Sie umfassende Informationen über Tijme entdecken',
        'home_bio_p1': 'Ich bin 21 Jahre alt und residiere gegenwärtig bei meinen Eltern und zwei Geschwistern—einem Bruder und einer Schwester—in Nistelrode. Während meines Bildungsweges habe ich mehrere Bildungseinrichtungen besucht. Im Jahr 2007 initiierte ich meine Primärbildung an der Grundschule De Beekgraaf in Nistelrode. Während meines achten Schuljahres transferierte ich zur De Brinck, um dort meine Grundschulbildung zu vollenden. Anschließend progressierte ich zum Udens College in Uden, wo ich Studien auf kader-theoretischem Niveau verfolgte, was mich schließlich zum KW1C in \'s-Hertogenbosch führte. Ursprünglich immatrikulierte ich mich für das Programm Architektur Konstruktion, bevor ich zu meinem aktuellen Software-Entwickler-Programm wechselte. Gegenwärtig befinde ich mich im dritten Jahr des Software-Entwickler-Curriculums. Ich habe erfolgreich ein Praktikum bei Omnilan absolviert, einem Unternehmen, das wertvolle Lernmöglichkeiten bot. Derzeit unternehme ich ein Praktikum bei AB Transport, einem Logistikunternehmen, das sich auf Liefer- und Abholungsdienste für Geschäftskunden spezialisiert hat. Diese Position hat sich als außerordentlich vorteilhaft erwiesen, da ich in der IT-Abteilung stationiert bin, wo ich umfangreiche Kenntnisse über die Programmiersprache Python und die Implementierung des Django-Frameworks erwerbe.',
        'home_bio_p2': 'Während dieses Bildungsprogramms habe ich substantielle Erfahrungen durch verschiedene projektbasierte Aufgaben akkumuliert, einschließlich der Entwicklung einer umfassenden Website für einen Sportverein. Gegenwärtig begeben wir uns an die Erstellung unserer Portfolio-Website. Während dieser Periode habe ich mein Verständnis von C# sowie dessen praktische Anwendung in der Projektentwicklung erheblich verstärkt. Darüber hinaus habe ich beträchtliche Expertise in der Webentwicklung sowohl durch akademische Aufgaben als auch durch praktische Praktikumserfahrung erworben. Diese Wissensaneignung war besonders lohnend, da ich nun die technische Kompetenz besitze, Websites zu konstruieren und verstehe, wie diese Fähigkeiten beruflich in der Zukunft zu nutzen sind. Ferner hatte ich während meines vorherigen Bildungsprogramms die Gelegenheit, mich in diverse und stimulierende Projekte zu engagieren, einschließlich des Entwurfs und der Konstruktion eines Restaurants mit Stahlrahmen, eines Wohngebäudes aus den 1930er Jahren und einer Freizeiteinrichtung für Jugendliche. Ich vollendete die Mehrheit dieser Projekte mit lobenswerten Resultaten. Diese umfassende Erfahrung wird sich zweifellos als unschätzbar wertvoll in meinen zukünftigen beruflichen Unternehmungen erweisen.',
        
        # Login Page
        'login_header': 'Benutzerauthentifizierung',
        'username': 'Benutzername',
        'password': 'Passwort',
        'login_error': 'Die bereitgestellte Benutzername-Passwort-Kombination ist ungültig. Bitte verifizieren Sie Ihre Anmeldedaten und versuchen Sie es erneut.',
        'dont_have_account': 'Verfügen Sie noch nicht über ein Konto?',
        'register_here': 'Erstellen Sie hier ein Konto',
        
        # Register Page
        'create_account': 'Neues Konto Erstellen',
        'email': 'E-Mail-Adresse',
        'first_name': 'Vorname',
        'last_name': 'Nachname',
        'confirm_password': 'Passwort Bestätigen',
        'username_requirements': 'Pflichtfeld. Maximum 150 Zeichen. Akzeptiert Buchstaben, Ziffern und folgende Symbole: @/./+/-/_ ausschließlich.',
        'password_req1': 'Ihr Passwort darf nicht eng mit Ihren anderen persönlichen Informationen übereinstimmen.',
        'password_req2': 'Ihr Passwort muss mindestens 8 Zeichen umfassen.',
        'password_req3': 'Ihr Passwort kann kein häufig verwendetes Passwort sein.',
        'password_req4': 'Ihr Passwort kann nicht ausschließlich aus numerischen Zeichen bestehen.',
        'password_confirm_help': 'Geben Sie das identische Passwort wie oben spezifiziert zur Verifikation ein.',
        'register_button': 'Konto Erstellen',
        'already_account': 'Besitzen Sie bereits ein Konto?',
        
        # Portfolio Page
        'portfolio_projects': 'Portfolio-Projekte',
        'rainbow_project': 'Regenbogen-Projekt',
        'match_table': 'Spieltabelle-Projekt',
        'exercise_1_6': 'CSS-Tabellenausrichtung Übung',
        'exercise_2_1': 'Row-span und Column-span Projekt',
        'rainbow_desc': 'Regenbogen-Projekt: Dies repräsentiert Aufgabe 3.2 des ersten Themas, welche ich besonders fesselnd zu entwickeln fand. Die Herausforderung involvierte die Implementierung von Span-Klassen, eine Technik, über die ich anfänglich unsicher war. Insgesamt glaube ich, dass die Ausführung höchst erfolgreich war.',
        'match_table_desc': 'Spieltabelle: Dieser Screenshot entstammt meinem inauguralen Projekt und demonstriert effektive Problemlösung. Das Ziel war es, alle Den Bosch Spiele umfassend darzustellen. Nach sorgfältiger Überlegung implementierte ich eine tabellenbasierte Lösung—eine Methodologie, die wir zuvor nicht genutzt hatten. Dies markierte meine erste erfolgreiche Anwendung tabularer Datenpräsentation für diese Art von Herausforderung.',
        'exercise_1_6_desc': 'Übung 1.6: Ich fand diese Aufgabe vernünftig handhabbar, da wir eine HTML-Datei erhielten, die vollständig desorganisiert war und CSS-Styling vermissen ließ. Die Herausforderung erforderte, dass wir ihre visuelle Attraktivität durch strategische Implementierung von Tabellenstrukturen und Zeilenorganisation wiederherstellten.',
        'exercise_2_1_desc': 'Übung 2.1: Dies erwies sich als außerordentlich vergnügliche Aufgabe, insbesondere weil sie uns erlaubte, mit row-span und column-span Eigenschaften zu experimentieren. Das finale Resultat war bemerkenswert erfolgreich und demonstrierte klar die Notwendigkeit, Klassen und IDs zu nutzen, um variierte Farbschemata innerhalb der Tabellenstruktur zu realisieren.',
        
        # Stage 1 Page
        'omnilan': 'Omnilan',
        'ispconfig': 'ISPConfig',
        'ispconfig_desc': 'Dies repräsentiert das primäre Dashboard-Interface von ISPConfig',
        'email_domain_desc': 'Diese Schnittstelle ermöglicht die Erstellung von E-Mail-Domänen für Adressen, die mit Ihrer Website assoziiert sind',
        'email_address_desc': 'Dieser Bereich erleichtert die Etablierung von E-Mail-Adressen für die Domäne Ihrer Website',
        'rememberz': 'Rememberz',
        'rememberz_menu_desc': 'Dies zeigt die primäre Navigationsschnittstelle für Rememberz-Benutzer',
        'milight_desc': 'Diese repräsentieren Benutzerkonfigurationseinstellungen für Beleuchtungssteuerung, einschließlich Farbanpassungsmöglichkeiten. Diese Features sind besonders prominent im linken Bereich der Schnittstelle.',
        'rememberz_main_desc': 'Dies konstituiert den zentralen Navigationshub der Rememberz-Plattform',
        
        # Stage 2 Page
        'second_internship': 'Zweites Praktikum: Fortgeschrittene Webentwicklung & Strukturiertes Online-Lernen',
        'wagtail_desc': 'Führte umfassende Exploration des Wagtail CMS durch strukturierte Online-Kursarbeit durch, wobei ich die Entwicklung sophistizierter dynamischer Content-Management-Systeme für Webanwendungen meisterte.',
        'cms_desc': 'Kollaborierte extensiv mit Content-Management-Systemen, um interaktive Blog-Publikationen zu architekturieren, wobei fortgeschrittene Features wie FAQ-Bereiche und dynamische Karussell-Komponenten inkorporiert wurden.',
        'bootstrap_email_desc': 'Entwarf und implementierte professionelle E-Mail-Template-Lösungen unter Verwendung des Bootstrap Email Frameworks für AB Transport, wobei responsive E-Mail-Signaturen und sophistizierte Layout-Designs erstellt wurden.',
        'programming_skills': 'Fortgeschrittene Programmierkompetenzen-Entwicklung',
        'coding_topics_desc': 'Führte tiefgreifende Exploration diverser Programmierdisziplinen einschließlich Python, JavaScript, HTML & CSS, SQL und zusätzlicher Technologien durch methodisch strukturierte Online-Lernprogramme durch.',
        'codecademy_desc': 'Vollendete erfolgreich mehrere umfassende Python-Kurse auf Codecademy, umfassend intermediate und fortgeschrittene Python-Programmierkonzepte sowie spezialisierte Django-Webentwicklungs-Frameworks.',
    },
    'es': {
        # Navigation & Common Elements
        'portfolio_website': 'Sitio Web de Portafolio',
        'home': 'Inicio',
        'internship_1': 'Prácticas 1',
        'internship_2': 'Prácticas 2',
        'portfolio': 'Portafolio',
        'admin_panel': 'Panel de Administración',
        'login': 'Iniciar Sesión',
        'register': 'Registrarse',
        'logout': 'Cerrar Sesión',
        'close': 'Cerrar',
        'profile_picture': 'Foto de Perfil',
        'toggle_navigation': 'Alternar navegación',
        'copyright': 'Tijme Vervoort.',
        'language': 'Idioma',
        
        # Page Titles
        'home_title': 'Inicio - Sitio Web de Portafolio',
        'login_title': 'Iniciar Sesión - Sitio Web de Portafolio',
        'register_title': 'Registrarse - Sitio Web de Portafolio',
        'portfolio_title': 'Portafolio - Sitio Web de Portafolio',
        'internship1_title': 'Prácticas 1 - Sitio Web de Portafolio',
        'internship2_title': 'Prácticas 2 - Sitio Web de Portafolio',
        
        # Demo Notice
        'demo_notice_title': 'Aviso de Demostración:',
        'demo_notice_register': 'Este formulario de registro sirve exclusivamente para fines demostrativos. No se establecerá ninguna cuenta auténtica y ningún dato será almacenado permanentemente.',
        'demo_notice_login': 'Este formulario de inicio de sesión está diseñado únicamente para propósitos demostrativos. El sistema de autenticación ejemplifica mi experiencia en desarrollo Django.',
        
        # Home Page
        'about_tijme_heading': 'Acerca de Tijme Vervoort',
        'skills_and_learning': 'Habilidades y Proyectos',
        'welcome_message': 'Bienvenido. Aquí puede descubrir información exhaustiva acerca de Tijme',
        'home_bio_p1': 'Tengo 21 años y resido actualmente con mis padres y dos hermanos—un hermano y una hermana—en Nistelrode. A lo largo de mi trayectoria educativa, he asistido a múltiples instituciones educativas. En 2007, inicié mi educación primaria en la escuela elemental De Beekgraaf en Nistelrode. Durante mi octavo año, me transferí a De Brinck para completar allí mi educación primaria. Subsecuentemente, progresé al Udens College en Uden, cursando estudios a nivel kader-theoretisch, lo cual me condujo finalmente al KW1C en \'s-Hertogenbosch. Inicialmente, me matriculé en el programa de Construcción Arquitectónica antes de transicionar a mi programa actual de Desarrollador de Software. Actualmente me encuentro en mi tercer año del currículum de Desarrollador de Software. He completado exitosamente unas prácticas en Omnilan, una empresa que proporcionó valiosas oportunidades de aprendizaje. Presentemente, emprendo unas prácticas en AB Transport, una compañía logística especializada en servicios de entrega y recolección para clientela corporativa. Esta posición ha demostrado ser excepcionalmente beneficiosa, dado que estoy estacionado dentro del departamento de TI, donde adquiero conocimientos extensivos concernientes al lenguaje de programación Python y la implementación del framework Django.',
        'home_bio_p2': 'A través de este programa educativo, he acumulado experiencia sustancial mediante diversas asignaciones basadas en proyectos, incluyendo el desarrollo de un sitio web exhaustivo para un club deportivo. Presentemente, nos embarcamos en la creación de nuestro sitio web de portafolio. Durante este período, he reforzado considerablemente mi comprensión de C# así como su aplicación práctica en el desarrollo de proyectos. Adicionalmente, he adquirido expertise considerable en desarrollo web tanto a través de asignaciones académicas como experiencia práctica de prácticas. Esta adquisición de conocimientos ha sido particularmente gratificante, puesto que ahora poseo la competencia técnica para construir sitios web y comprendo cómo explotar estas habilidades profesionalmente en el futuro. Además, durante mi programa educativo previo, tuve la oportunidad de involucrarme en proyectos diversificados y estimulantes, incluyendo el diseño y construcción de un restaurante con estructura de acero, un edificio residencial de los años 1930, y una instalación recreativa para jóvenes. Completé la mayoría de estos proyectos con resultados encomiables. Esta experiencia exhaustiva indudablemente resultará invaluable en mis emprendimientos profesionales futuros.',
        
        # Login Page
        'login_header': 'Autenticación de Usuario',
        'username': 'Nombre de usuario',
        'password': 'Contraseña',
        'login_error': 'La combinación de nombre de usuario y contraseña proporcionada es inválida. Por favor verifique sus credenciales e intente nuevamente.',
        'dont_have_account': '¿No posee aún una cuenta?',
        'register_here': 'Cree una cuenta aquí',
        
        # Register Page
        'create_account': 'Crear una Nueva Cuenta',
        'email': 'Dirección de correo electrónico',
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'confirm_password': 'Confirmar Contraseña',
        'username_requirements': 'Campo obligatorio. Máximo 150 caracteres. Acepta letras, dígitos, y los siguientes símbolos: @/./+/-/_ exclusivamente.',
        'password_req1': 'Su contraseña no debe asemejarse estrechamente a su otra información personal.',
        'password_req2': 'Su contraseña debe comprender un mínimo de 8 caracteres.',
        'password_req3': 'Su contraseña no puede ser una contraseña comúnmente utilizada.',
        'password_req4': 'Su contraseña no puede consistir enteramente en caracteres numéricos.',
        'password_confirm_help': 'Reingrese la contraseña idéntica como se especificó arriba para propósitos de verificación.',
        'register_button': 'Crear Cuenta',
        'already_account': '¿Ya posee una cuenta?',
        
        # Portfolio Page
        'portfolio_projects': 'Proyectos de Portafolio',
        'rainbow_project': 'Proyecto Arcoíris',
        'match_table': 'Proyecto Tabla de Partidos',
        'exercise_1_6': 'Ejercicio de Alineación de Tabla CSS',
        'exercise_2_1': 'Proyecto Row-span y Column-span',
        'rainbow_desc': 'Proyecto Arcoíris: Esto representa la asignación 3.2 del primer tema, la cual encontré particularmente cautivadora de desarrollar. El desafío involucró la implementación de clases span, una técnica sobre la cual inicialmente tenía incertidumbre. Globalmente, creo que la ejecución fue altamente exitosa.',
        'match_table_desc': 'Tabla de Partidos: Esta captura de pantalla se origina de mi proyecto inaugural y demuestra resolución efectiva de problemas. El objetivo era mostrar todos los partidos de Den Bosch comprehensivamente. Después de consideración cuidadosa, implementé una solución basada en tablas—una metodología que previamente no habíamos utilizado. Esto marcó mi primera aplicación exitosa de presentación de datos tabulares para este tipo de desafío.',
        'exercise_1_6_desc': 'Ejercicio 1.6: Encontré esta asignación razonablemente manejable, puesto que recibimos un archivo HTML completamente desorganizado y carente de estilización CSS. El desafío requería que restauráramos su atractivo visual a través de la implementación estratégica de estructuras de tabla y organización de filas.',
        'exercise_2_1_desc': 'Ejercicio 2.1: Esto demostró ser una asignación excepcionalmente placentera, particularmente porque nos permitió experimentar con propiedades row-span y column-span. El resultado final fue notablemente exitoso, demostrando claramente la necesidad de utilizar clases e IDs para lograr esquemas de colores variados dentro de la estructura de la tabla.',
        
        # Stage 1 Page
        'omnilan': 'Omnilan',
        'ispconfig': 'ISPConfig',
        'ispconfig_desc': 'Esto representa la interfaz de panel principal de ISPConfig',
        'email_domain_desc': 'Esta interfaz facilita la creación de dominios de correo electrónico para direcciones asociadas con su sitio web',
        'email_address_desc': 'Esta sección facilita el establecimiento de direcciones de correo electrónico para el dominio de su sitio web',
        'rememberz': 'Rememberz',
        'rememberz_menu_desc': 'Esto muestra la interfaz de navegación principal para usuarios de Rememberz',
        'milight_desc': 'Estos representan configuraciones de usuario para control de iluminación, incluyendo capacidades de ajuste de color. Estas características son particularmente prominentes en la sección izquierda de la interfaz.',
        'rememberz_main_desc': 'Esto constituye el hub de navegación central de la plataforma Rememberz',
        
        # Stage 2 Page
        'second_internship': 'Segundas Prácticas: Desarrollo Web Avanzado & Aprendizaje en Línea Estructurado',
        'wagtail_desc': 'Conduje exploración exhaustiva del CMS Wagtail a través de cursos en línea estructurados, dominando el desarrollo de sistemas sofisticados de gestión de contenido dinámico para aplicaciones web.',
        'cms_desc': 'Colaboré extensivamente con sistemas de gestión de contenido para arquitecturar publicaciones de blog interactivas, incorporando características avanzadas tales como secciones de FAQ y componentes de carrusel dinámicos.',
        'bootstrap_email_desc': 'Diseñé e implementé soluciones profesionales de plantillas de correo electrónico utilizando el framework Bootstrap Email para AB Transport, creando firmas de correo responsivas y diseños de layout sofisticados.',
        'programming_skills': 'Desarrollo de Competencias Avanzadas en Programación',
        'coding_topics_desc': 'Conduje exploración profunda de diversas disciplinas de programación incluyendo Python, JavaScript, HTML & CSS, SQL, y tecnologías adicionales a través de programas de aprendizaje en línea metódicamente estructurados.',
        'codecademy_desc': 'Completé exitosamente múltiples cursos exhaustivos de Python en Codecademy, abarcando conceptos de programación Python intermedios y avanzados, así como frameworks especializados de desarrollo web Django.',
    },
    'it': {
        # Navigation & Common Elements
        'portfolio_website': 'Sito Web del Portfolio',
        'home': 'Home',
        'internship_1': 'Tirocinio 1',
        'internship_2': 'Tirocinio 2',
        'portfolio': 'Portfolio',
        'admin_panel': 'Pannello di Amministrazione',
        'login': 'Accesso',
        'register': 'Registrazione',
        'logout': 'Uscita',
        'close': 'Chiudi',
        'profile_picture': 'Foto del Profilo',
        'toggle_navigation': 'Attiva/disattiva navigazione',
        'copyright': 'Tijme Vervoort.',
        'language': 'Lingua',
        
        # Page Titles
        'home_title': 'Home - Sito Web del Portfolio',
        'login_title': 'Accesso - Sito Web del Portfolio',
        'register_title': 'Registrazione - Sito Web del Portfolio',
        'portfolio_title': 'Portfolio - Sito Web del Portfolio',
        'internship1_title': 'Tirocinio 1 - Sito Web del Portfolio',
        'internship2_title': 'Tirocinio 2 - Sito Web del Portfolio',
        
        # Demo Notice
        'demo_notice_title': 'Avviso Dimostrativo:',
        'demo_notice_register': 'Questo modulo di registrazione serve esclusivamente a scopi dimostrativi. Non verrà stabilito alcun account autentico e nessun dato sarà memorizzato permanentemente.',
        'demo_notice_login': 'Questo modulo di accesso è progettato unicamente per finalità dimostrative. Il sistema di autenticazione esemplifica la mia competenza nello sviluppo Django.',
        
        # Home Page
        'about_tijme_heading': 'Su Tijme Vervoort',
        'skills_and_learning': 'Competenze e Progetti',
        'welcome_message': 'Benvenuto. Qui può scoprire informazioni esaustive riguardo Tijme',
        'home_bio_p1': 'Ho 21 anni e risiedo attualmente con i miei genitori e due fratelli—un fratello e una sorella—a Nistelrode. Nel corso della mia traiettoria educativa, ho frequentato molteplici istituzioni educative. Nel 2007, ho iniziato la mia educazione primaria presso la scuola elementare De Beekgraaf a Nistelrode. Durante il mio ottavo anno, mi sono trasferito a De Brinck per completare ivi la mia educazione primaria. Successivamente, sono progredito al Udens College a Uden, perseguendo studi a livello kader-theoretisch, il che mi ha condotto ultimamente al KW1C a \'s-Hertogenbosch. Inizialmente, mi sono immatricolato nel programma di Costruzione Architettonica prima di transizionare al mio attuale programma di Sviluppatore Software. Attualmente mi trovo nel mio terzo anno del curriculum Sviluppatore Software. Ho completato con successo un tirocinio presso Omnilan, un\'azienda che ha fornito preziose opportunità di apprendimento. Presentemente, sto intraprendendo un tirocinio presso AB Transport, una compagnia logistica specializzata in servizi di consegna e ritiro per clientela aziendale. Questa posizione si è dimostrata eccezionalmente vantaggiosa, dato che sono stazionato all\'interno del dipartimento IT, dove sto acquisendo conoscenze estensive riguardanti il linguaggio di programmazione Python e l\'implementazione del framework Django.',
        'home_bio_p2': 'Attraverso questo programma educativo, ho accumulato esperienza sostanziale mediante diverse assegnazioni basate su progetti, includendo lo sviluppo di un sito web esaustivo per un club sportivo. Presentemente, ci imbarchiamo nella creazione del nostro sito web portfolio. Durante questo periodo, ho rafforzato considerevolmente la mia comprensione del C# così come la sua applicazione pratica nello sviluppo di progetti. Addizionalmente, ho acquisito expertise considerevole nello sviluppo web tanto attraverso assegnazioni accademiche quanto esperienza pratica di tirocinio. Questa acquisizione di conoscenze è stata particolarmente gratificante, poiché ora possiedo la competenza tecnica per costruire siti web e comprendo come sfruttare queste abilità professionalmente nel futuro. Inoltre, durante il mio precedente programma educativo, ho avuto l\'opportunità di impegnarmi in progetti diversificati e stimolanti, includendo la progettazione e costruzione di un ristorante con struttura in acciaio, un edificio residenziale degli anni 1930, e un\'installazione ricreativa per giovani. Ho completato la maggioranza di questi progetti con risultati encomiabili. Questa esperienza esaustiva si dimostrerà indubbiamente inestimabile nelle mie future imprese professionali.',
        
        # Login Page
        'login_header': 'Autenticazione Utente',
        'username': 'Nome utente',
        'password': 'Password',
        'login_error': 'La combinazione nome utente e password fornita è invalida. Prego verificare le sue credenziali e tentare nuovamente.',
        'dont_have_account': 'Non possiede ancora un account?',
        'register_here': 'Crei un account qui',
        
        # Register Page
        'create_account': 'Creare un Nuovo Account',
        'email': 'Indirizzo email',
        'first_name': 'Nome',
        'last_name': 'Cognome',
        'confirm_password': 'Confermare Password',
        'username_requirements': 'Campo obbligatorio. Massimo 150 caratteri. Accetta lettere, cifre, e i seguenti simboli: @/./+/-/_ esclusivamente.',
        'password_req1': 'La sua password non deve assomigliare strettamente alle sue altre informazioni personali.',
        'password_req2': 'La sua password deve comprendere un minimo di 8 caratteri.',
        'password_req3': 'La sua password non può essere una password comunemente utilizzata.',
        'password_req4': 'La sua password non può consistere interamente in caratteri numerici.',
        'password_confirm_help': 'Reinserisca la password identica come specificato sopra per scopi di verifica.',
        'register_button': 'Creare Account',
        'already_account': 'Possiede già un account?',
        
        # Portfolio Page
        'portfolio_projects': 'Progetti Portfolio',
        'rainbow_project': 'Progetto Arcobaleno',
        'match_table': 'Progetto Tabella Partite',
        'exercise_1_6': 'Esercizio Allineamento Tabella CSS',
        'exercise_2_1': 'Progetto Row-span e Column-span',
        'rainbow_desc': 'Progetto Arcobaleno: Questo rappresenta l\'assegnazione 3.2 del primo tema, che ho trovato particolarmente accattivante da sviluppare. La sfida coinvolgeva l\'implementazione di classi span, una tecnica sulla quale inizialmente avevo incertezza. Globalmente, credo che l\'esecuzione sia stata altamente riuscita.',
        'match_table_desc': 'Tabella Partite: Questo screenshot origina dal mio progetto inaugurale e dimostra risoluzione efficace di problemi. L\'obiettivo era mostrare tutte le partite di Den Bosch comprensivamente. Dopo attenta considerazione, ho implementato una soluzione basata su tabelle—una metodologia che precedentemente non avevamo utilizzato. Questo ha segnato la mia prima applicazione riuscita di presentazione dati tabulari per questo tipo di sfida.',
        'exercise_1_6_desc': 'Esercizio 1.6: Ho trovato questa assegnazione ragionevolmente gestibile, poiché abbiamo ricevuto un file HTML completamente disorganizzato e privo di stilizzazione CSS. La sfida richiedeva che restaurassimo il suo appeal visivo attraverso l\'implementazione strategica di strutture tabellari e organizzazione di righe.',
        'exercise_2_1_desc': 'Esercizio 2.1: Questo si è dimostrato un\'assegnazione eccezionalmente piacevole, particolarmente perché ci ha permesso di sperimentare con proprietà row-span e column-span. Il risultato finale è stato notevolmente riuscito, dimostrando chiaramente la necessità di utilizzare classi e ID per realizzare schemi cromatici variati all\'interno della struttura tabellare.',
        
        # Stage 1 Page
        'omnilan': 'Omnilan',
        'ispconfig': 'ISPConfig',
        'ispconfig_desc': 'Questo rappresenta l\'interfaccia dashboard principale di ISPConfig',
        'email_domain_desc': 'Questa interfaccia facilita la creazione di domini email per indirizzi associati al suo sito web',
        'email_address_desc': 'Questa sezione facilita l\'istituzione di indirizzi email per il dominio del suo sito web',
        'rememberz': 'Rememberz',
        'rememberz_menu_desc': 'Questo mostra l\'interfaccia di navigazione principale per utenti Rememberz',
        'milight_desc': 'Questi rappresentano impostazioni di configurazione utente per controllo illuminazione, includendo capacità di regolazione colore. Queste caratteristiche sono particolarmente prominenti nella sezione sinistra dell\'interfaccia.',
        'rememberz_main_desc': 'Questo costituisce l\'hub di navigazione centrale della piattaforma Rememberz',
        
        # Stage 2 Page
        'second_internship': 'Secondo Tirocinio: Sviluppo Web Avanzato & Apprendimento Online Strutturato',
        'wagtail_desc': 'Ho condotto esplorazione esaustiva del CMS Wagtail attraverso corsi online strutturati, padroneggiando lo sviluppo di sistemi sofisticati di gestione contenuti dinamici per applicazioni web.',
        'cms_desc': 'Ho collaborato estensivamente con sistemi di gestione contenuti per architettare pubblicazioni blog interattive, incorporando caratteristiche avanzate quali sezioni FAQ e componenti carousel dinamici.',
        'bootstrap_email_desc': 'Ho progettato e implementato soluzioni professionali di template email utilizzando il framework Bootstrap Email per AB Transport, creando firme email responsive e design layout sofisticati.',
        'programming_skills': 'Sviluppo Competenze Programmazione Avanzate',
        'coding_topics_desc': 'Ho condotto esplorazione approfondita di diverse discipline di programmazione includendo Python, JavaScript, HTML & CSS, SQL, e tecnologie aggiuntive attraverso programmi di apprendimento online metodicamente strutturati.',
        'codecademy_desc': 'Ho completato con successo molteplici corsi Python esaustivi su Codecademy, comprendendo concetti di programmazione Python intermedi e avanzati, così come framework specializzati di sviluppo web Django.',
    },
    # Norwegian (no) translations
'no': {
    # Navigation & Common Elements
    'portfolio_website': 'Porteføljenettsted',
    'home': 'Hjem',
    'internship_1': 'Praksis 1',
    'internship_2': 'Praksis 2',
    'portfolio': 'Portefølje',
    'admin_panel': 'Administrasjonspanel',
    'login': 'Logg inn',
    'register': 'Registrer',
    'logout': 'Logg ut',
    'close': 'Lukk',
    'profile_picture': 'Profilbilde',
    'toggle_navigation': 'Bytt navigasjon',
    'copyright': 'Tijme Vervoort.',
    'language': 'Språk',
    
    # Page Titles
    'home_title': 'Hjem - Porteføljenettsted',
    'login_title': 'Logg inn - Porteføljenettsted',
    'register_title': 'Registrer - Porteføljenettsted',
    'portfolio_title': 'Portefølje - Porteføljenettsted',
    'internship1_title': 'Praksis 1 - Porteføljenettsted',
    'internship2_title': 'Praksis 2 - Porteføljenettsted',
    
    # Demo Notice
    'demo_notice_title': 'Demonstrasjonsvarsel:',
    'demo_notice_register': 'Dette registreringsskjemaet tjener utelukkende demonstrasjonsformål. Ingen autentisk konto vil bli etablert, og ingen data vil bli permanent lagret.',
    'demo_notice_login': 'Dette påloggingsskjemaet er eksklusivt designet for demonstrasjonsformål. Autentiseringssystemet eksemplifiserer min Django-utviklingsekspertise.',
    
    # Home Page
    'about_tijme_heading': 'Om Tijme Vervoort',
    'skills_and_learning': 'Ferdigheter og Prosjekter',
    'welcome_message': 'Velkommen. Her kan du oppdage omfattende informasjon angående Tijme',
    'home_bio_p1': 'Jeg er 21 år gammel og residerer for øyeblikket hos mine foreldre og to søsken—en bror og en søster—i Nistelrode. Gjennom min utdannelsesmessige bane har jeg besøkt flere utdanningsinstitusjoner. I 2007 initierte jeg min primærutdanning ved De Beekgraaf barneskole i Nistelrode. I løpet av mitt åttende år overførte jeg til De Brinck for å fullføre min grunnskoleutdanning der. Påfølgende progredierte jeg til Udens College i Uden, hvor jeg forfulgte studier på kader-theoretisch nivå, noe som til slutt førte meg til KW1C i \'s-Hertogenbosch. Opprinnelig immatrikulerte jeg meg i Arkitektur Konstruksjon-programmet før jeg transisjonerte til mitt nåværende Programvareutvikler-program. For øyeblikket befinner jeg meg i mitt tredje år av Programvareutvikler-pensumet. Jeg har vellykket fullført en praksisperiode hos Omnilan, et selskap som tilbød verdifulle læringsmuligheter. Presently, jeg gjennomfører en praksisperiode hos AB Transport, et logistikkselskap spesialisert i leverings- og hentingstjenester for bedriftskunder. Denne posisjonen har vist seg å være eksepsjonelt fordelaktig, ettersom jeg er stasjonert innenfor IT-avdelingen, hvor jeg tilegner meg omfattende kunnskap angående Python-programmeringsspråket og Django-rammeverk implementering.',
    'home_bio_p2': 'Gjennom dette utdanningsprogrammet har jeg akkumulert substansiell erfaring via diverse prosjektbaserte oppgaver, inkludert utviklingen av et omfattende nettsted for en sportsklubb. For øyeblikket embarkerer vi på skapelsen av vårt porteføljenettsted. I løpet av denne perioden har jeg betydelig forsterket min forståelse av C# samt dens praktiske anvendelse i prosjektutvikling. Ytterligere har jeg tilegnet meg betydelig ekspertise innen webutvikling gjennom både akademiske oppgaver og praktisk praksiserfaring. Denne kunnskapstilegnelsen har vært særlig givende, ettersom jeg nå besitter den tekniske kompetansen til å konstruere nettsteder og forstår hvordan å utnytte disse ferdighetene profesjonelt i fremtiden. Videre hadde jeg under mitt foregående utdanningsprogram anledningen til å engasjere meg i diversifiserte og stimulerende prosjekter, inkludert design og konstruksjon av en restaurant med stålramme, en residensiell bygning fra 1930-tallet, og en rekreasjonsfasilitet for ungdom. Jeg fullførte majoriteten av disse prosjektene med rosverdig resultater. Denne omfattende erfaringen vil utvilsomt vise seg uvurderlig i mine fremtidige profesjonelle foretak.',
    
    # Login Page
    'login_header': 'Brukerautentisering',
    'username': 'Brukernavn',
    'password': 'Passord',
    'login_error': 'Den oppgitte brukernavn-passord kombinasjonen er ugyldig. Vennligst verifiser dine legitimasjoner og forsøk på nytt.',
    'dont_have_account': 'Besitter du ikke en konto ennå?',
    'register_here': 'Opprett en konto her',
    
    # Register Page
    'create_account': 'Opprett en Ny Konto',
    'email': 'E-postadresse',
    'first_name': 'Fornavn',
    'last_name': 'Etternavn',
    'confirm_password': 'Bekreft Passord',
    'username_requirements': 'Obligatorisk felt. Maksimum 150 tegn. Aksepterer bokstaver, sifre, og følgende symboler: @/./+/-/_ eksklusivt.',
    'password_req1': 'Ditt passord må ikke ligne nært på din andre personlige informasjon.',
    'password_req2': 'Ditt passord må omfatte minimum 8 tegn.',
    'password_req3': 'Ditt passord kan ikke være et vanlig benyttet passord.',
    'password_req4': 'Ditt passord kan ikke bestå utelukkende av numeriske tegn.',
    'password_confirm_help': 'Gjeninntast det identiske passordet som spesifisert ovenfor for verifikasjonsformål.',
    'register_button': 'Opprett Konto',
    'already_account': 'Besitter du allerede en konto?',
    
    # Portfolio Page
    'portfolio_projects': 'Porteføljeprosjekter',
    'rainbow_project': 'Regnbueprosjekt',
    'match_table': 'Kamptabell-prosjekt',
    'exercise_1_6': 'CSS-tabellinjustering Øvelse',
    'exercise_2_1': 'Row-span og Column-span Prosjekt',
    'rainbow_desc': 'Regnbueprosjekt: Dette representerer oppgave 3.2 fra det første temaet, som jeg fant særlig fengslende å utvikle. Utfordringen involverte implementering av span-klasser, en teknikk jeg opprinnelig var usikker på. Overordnet mener jeg at gjennomføringen var høyst vellykket.',
    'match_table_desc': 'Kamptabell: Dette skjermbildet stammer fra mitt inaugurale prosjekt og demonstrerer effektiv problemløsning. Målet var å vise alle Den Bosch-kamper omfattende. Etter nøye overveielse implementerte jeg en tabellbasert løsning—en metodologi vi tidligere ikke hadde benyttet. Dette markerte min første vellykkede anvendelse av tabulær datapresentasjon for denne typen utfordring.',
    'exercise_1_6_desc': 'Øvelse 1.6: Jeg fant denne oppgaven rimelig håndterbar, ettersom vi mottok en HTML-fil som var fullstendig desorganisert og manglet CSS-styling. Utfordringen krevde at vi gjenopprettet dens visuelle appell gjennom strategisk implementering av tabellstrukturer og radorganisering.',
    'exercise_2_1_desc': 'Øvelse 2.1: Dette viste seg å være en eksepsjonelt fornøyelig oppgave, særlig fordi den tillot oss å eksperimentere med row-span og column-span egenskaper. Det endelige resultatet var bemerkelsesverdig vellykket, og demonstrerte tydelig nødvendigheten av å benytte klasser og ID-er for å realisere varierte fargeskjemaer innenfor tabellstrukturen.',
    
    # Stage 1 Page
    'omnilan': 'Omnilan',
    'ispconfig': 'ISPConfig',
    'ispconfig_desc': 'Dette representerer det primære dashbord-grensesnittet til ISPConfig',
    'email_domain_desc': 'Dette grensesnittet fasiliterer opprettelsen av e-postdomener for adresser assosiert med ditt nettsted',
    'email_address_desc': 'Denne seksjonen fasiliterer etablering av e-postadresser for ditt nettstedsdomene',
    'rememberz': 'Rememberz',
    'rememberz_menu_desc': 'Dette viser det primære navigasjonsgrensesnittet for Rememberz-brukere',
    'milight_desc': 'Disse representerer brukerkonfigurasjonsinnstillinger for belysningskontroll, inkludert fargetilpasningskapasiteter. Disse funksjonene er særlig fremtredende i venstre seksjon av grensesnittet.',
    'rememberz_main_desc': 'Dette konstituerer det sentrale navigasjonssenteret til Rememberz-plattformen',
    
    # Stage 2 Page
    'second_internship': 'Andre Praksis: Avansert Webutvikling & Strukturert Online Læring',
    'wagtail_desc': 'Gjennomførte omfattende utforskning av Wagtail CMS gjennom strukturerte online kurs, hvor jeg mestret utviklingen av sofistikerte dynamiske innholdsstyringssystemer for webapplikasjoner.',
    'cms_desc': 'Kollaborerte omfattende med innholdsstyringssystemer for å arkitekturere interaktive bloggpublikasjoner, inkorporerende avanserte funksjoner som FAQ-seksjoner og dynamiske karusellkomponenter.',
    'bootstrap_email_desc': 'Designet og implementerte profesjonelle e-postmal-løsninger ved bruk av Bootstrap Email-rammeverket for AB Transport, skapende responsive e-postsignaturer og sofistikerte layout-design.',
    'programming_skills': 'Avansert Programmeringskompetanse Utvikling',
    'coding_topics_desc': 'Gjennomførte dybdegående utforskning av diverse programmeringsdisipliner inkludert Python, JavaScript, HTML & CSS, SQL, og tilleggsteknologier gjennom metodisk strukturerte online læringsprogrammer.',
    'codecademy_desc': 'Fullførte vellykket flere omfattende Python-kurs på Codecademy, omfattende mellomliggende og avanserte Python-programmeringskonsepter, samt spesialiserte Django webutviklingsrammeverk.',
},

# Swedish (sv) translations
'sv': {
    # Navigation & Common Elements
    'portfolio_website': 'Portfoliowebbplats',
    'home': 'Hem',
    'internship_1': 'Praktik 1',
    'internship_2': 'Praktik 2',
    'portfolio': 'Portfolio',
    'admin_panel': 'Adminpanel',
    'login': 'Logga in',
    'register': 'Registrera',
    'logout': 'Logga ut',
    'close': 'Stäng',
    'profile_picture': 'Profilbild',
    'toggle_navigation': 'Växla navigering',
    'copyright': 'Tijme Vervoort.',
    'language': 'Språk',
    
    # Page Titles
    'home_title': 'Hem - Portfoliowebbplats',
    'login_title': 'Logga in - Portfoliowebbplats',
    'register_title': 'Registrera - Portfoliowebbplats',
    'portfolio_title': 'Portfolio - Portfoliowebbplats',
    'internship1_title': 'Praktik 1 - Portfoliowebbplats',
    'internship2_title': 'Praktik 2 - Portfoliowebbplats',
    
    # Demo Notice
    'demo_notice_title': 'Demonstrationsmeddelande:',
    'demo_notice_register': 'Detta registreringsformulär tjänar uteslutande demonstrationssyften. Inget autentiskt konto kommer att etableras och inga data kommer att lagras permanent.',
    'demo_notice_login': 'Detta inloggningsformulär är exklusivt designat för demonstrationssyften. Autentiseringssystemet exemplifierar min Django-utvecklingsexpertis.',
    
    # Home Page
    'about_tijme_heading': 'Om Tijme Vervoort',
    'skills_and_learning': 'Färdigheter och Projekt',
    'welcome_message': 'Välkommen. Här kan du upptäcka omfattande information angående Tijme',
    'home_bio_p1': 'Jag är 21 år gammal och residerar för närvarande hos mina föräldrar och två syskon—en bror och en syster—i Nistelrode. Genom min utbildningsbana har jag besökt flera utbildningsinstitutioner. År 2007 initierade jag min primärutbildning vid De Beekgraaf grundskola i Nistelrode. Under mitt åttonde år överförde jag till De Brinck för att fullborda min grundskoleutbildning där. Påföljande progrederade jag till Udens College i Uden, där jag bedrev studier på kader-theoretisch nivå, vilket slutligen ledde mig till KW1C i \'s-Hertogenbosch. Ursprungligen immatrikulerade jag mig i Arkitektur Konstruktion-programmet innan jag övergick till mitt nuvarande Mjukvaruutvecklare-program. För närvarande befinner jag mig i mitt tredje år av Mjukvaruutvecklare-läroplanen. Jag har framgångsrikt fullbordat en praktikperiod hos Omnilan, ett företag som erbjöd värdefulla lärandemöjligheter. För närvarande genomför jag en praktikperiod hos AB Transport, ett logistikföretag specialiserat på leverans- och upphämtningstjänster för företagskunder. Denna position har visat sig vara exceptionellt fördelaktig, eftersom jag är stationerad inom IT-avdelningen, där jag tillägnar mig omfattande kunskap angående Python-programmeringsspråket och Django-ramverksimplementering.',
    'home_bio_p2': 'Genom detta utbildningsprogram har jag ackumulerat substantiell erfarenhet via diverse projektbaserade uppgifter, inklusive utvecklingen av en omfattande webbplats för en sportsklubb. För närvarande embarkar vi på skapandet av vår portfoliowebbplats. Under denna period har jag betydligt förstärkt min förståelse av C# samt dess praktiska tillämpning inom projektutveckling. Ytterligare har jag förvärvat betydande expertis inom webbutveckling genom både akademiska uppgifter och praktisk praktikexperience. Denna kunskapsförvärv har varit särskilt givande, eftersom jag nu besitter den tekniska kompetensen att konstruera webbplatser och förstår hur att utnyttja dessa färdigheter professionellt i framtiden. Vidare hade jag under mitt föregående utbildningsprogram tillfället att engagera mig i diversifierade och stimulerande projekt, inklusive design och konstruktion av en restaurang med stålram, en residentiell byggnad från 1930-talet, och en rekreationsanläggning för ungdomar. Jag fullbordade majoriteten av dessa projekt med berömvärda resultat. Denna omfattande erfarenhet kommer otvivelaktigt att visa sig ovärderlig i mina framtida professionella företag.',
    
    # Login Page
    'login_header': 'Användarautentisering',
    'username': 'Användarnamn',
    'password': 'Lösenord',
    'login_error': 'Den angivna användarnamn-lösenord kombinationen är ogiltig. Vänligen verifiera dina legitimationer och försök igen.',
    'dont_have_account': 'Besitter du inte ett konto ännu?',
    'register_here': 'Skapa ett konto här',
    
    # Register Page
    'create_account': 'Skapa ett Nytt Konto',
    'email': 'E-postadress',
    'first_name': 'Förnamn',
    'last_name': 'Efternamn',
    'confirm_password': 'Bekräfta Lösenord',
    'username_requirements': 'Obligatoriskt fält. Maximum 150 tecken. Accepterar bokstäver, siffror, och följande symboler: @/./+/-/_ exklusivt.',
    'password_req1': 'Ditt lösenord får inte likna nära din andra personliga information.',
    'password_req2': 'Ditt lösenord måste omfatta minimum 8 tecken.',
    'password_req3': 'Ditt lösenord kan inte vara ett vanligt använt lösenord.',
    'password_req4': 'Ditt lösenord kan inte bestå uteslutande av numeriska tecken.',
    'password_confirm_help': 'Återinmatning av det identiska lösenordet som specificerat ovan för verifieringssyften.',
    'register_button': 'Skapa Konto',
    'already_account': 'Besitter du redan ett konto?',
    
    # Portfolio Page
    'portfolio_projects': 'Portfolioprojekt',
    'rainbow_project': 'Regnbågsprojekt',
    'match_table': 'Matchtabell-projekt',
    'exercise_1_6': 'CSS-tabelljustering Övning',
    'exercise_2_1': 'Row-span och Column-span Projekt',
    'rainbow_desc': 'Regnbågsprojekt: Detta representerar uppgift 3.2 från det första temat, vilket jag fann särskilt fängslande att utveckla. Utmaningen involverade implementering av span-klasser, en teknik jag ursprungligen var osäker på. Övergripande anser jag att genomförandet var högst framgångsrikt.',
    'match_table_desc': 'Matchtabell: Denna skärmbild härstammar från mitt inaugurala projekt och demonstrerar effektiv problemlösning. Målet var att visa alla Den Bosch-matcher omfattande. Efter noggrann övervägande implementerade jag en tabellbaserad lösning—en metodologi vi tidigare inte hade utnyttjat. Detta markerade min första framgångsrika tillämpning av tabulär datapresentation för denna typ av utmaning.',
    'exercise_1_6_desc': 'Övning 1.6: Jag fann denna uppgift rimligt hanterbar, eftersom vi erhöll en HTML-fil som var fullständigt desorganiserad och saknade CSS-styling. Utmaningen krävde att vi återställde dess visuella attraktion genom strategisk implementering av tabellstrukturer och radorganisering.',
    'exercise_2_1_desc': 'Övning 2.1: Detta visade sig vara en exceptionellt njutbar uppgift, särskilt eftersom den tillät oss att experimentera med row-span och column-span egenskaper. Det slutliga resultatet var anmärkningsvärt framgångsrikt, tydligt demonstrerande nödvändigheten av att utnyttja klasser och ID:n för att realisera varierade färgscheman inom tabellstrukturen.',
    
    # Stage 1 Page
    'omnilan': 'Omnilan',
    'ispconfig': 'ISPConfig',
    'ispconfig_desc': 'Detta representerar det primära dashboard-gränssnittet för ISPConfig',
    'email_domain_desc': 'Detta gränssnitt faciliterar skapandet av e-postdomäner för adresser associerade med din webbplats',
    'email_address_desc': 'Denna sektion faciliterar etablering av e-postadresser för din webbplatsdomän',
    'rememberz': 'Rememberz',
    'rememberz_menu_desc': 'Detta visar det primära navigationsgränssnittet för Rememberz-användare',
    'milight_desc': 'Dessa representerar användarkonfigurationsinställningar för belysningskontroll, inklusive färgjusteringskapaciteter. Dessa funktioner är särskilt framträdande i vänstra sektionen av gränssnittet.',
    'rememberz_main_desc': 'Detta konstituerar det centrala navigationscentret för Rememberz-plattformen',
    
    # Stage 2 Page
    'second_internship': 'Andra Praktik: Avancerad Webbutveckling & Strukturerad Online Lärande',
    'wagtail_desc': 'Genomförde omfattande utforskning av Wagtail CMS genom strukturerade online kurser, där jag bemästrade utvecklingen av sofistikerade dynamiska innehållshanteringssystem för webbapplikationer.',
    'cms_desc': 'Kollaborerade omfattande med innehållshanteringssystem för att arkitekturera interaktiva bloggpublikationer, inkorporerande avancerade funktioner såsom FAQ-sektioner och dynamiska karusellkomponenter.',
    'bootstrap_email_desc': 'Designade och implementerade professionella e-postmall-lösningar genom användning av Bootstrap Email-ramverket för AB Transport, skapande responsiva e-postsignaturer och sofistikerade layout-design.',
    'programming_skills': 'Avancerad Programmeringskompetens Utveckling',
    'coding_topics_desc': 'Genomförde djupgående utforskning av diverse programmeringsdiscipliner inklusive Python, JavaScript, HTML & CSS, SQL, och ytterligare teknologier genom metodiskt strukturerade online lärandeprogrammer.',
    'codecademy_desc': 'Fullbordade framgångsrikt flera omfattande Python-kurser på Codecademy, omfattande mellanliggande och avancerade Python-programmeringskoncept, samt specialiserade Django webbutvecklingsramverk.',
},

# Danish (da) translations
'da': {
    # Navigation & Common Elements
    'portfolio_website': 'Porteføljewebsite',
    'home': 'Hjem',
    'internship_1': 'Praktik 1',
    'internship_2': 'Praktik 2',
    'portfolio': 'Portefølje',
    'admin_panel': 'Adminpanel',
    'login': 'Log ind',
    'register': 'Tilmeld',
    'logout': 'Log ud',
    'close': 'Luk',
    'profile_picture': 'Profilbillede',
    'toggle_navigation': 'Skift navigation',
    'copyright': 'Tijme Vervoort.',
    'language': 'Sprog',
    
    # Page Titles
    'home_title': 'Hjem - Porteføljewebsite',
    'login_title': 'Log ind - Porteføljewebsite',
    'register_title': 'Tilmeld - Porteføljewebsite',
    'portfolio_title': 'Portefølje - Porteføljewebsite',
    'internship1_title': 'Praktik 1 - Porteføljewebsite',
    'internship2_title': 'Praktik 2 - Porteføljewebsite',
    
    # Demo Notice
    'demo_notice_title': 'Demonstrationsmeddelelse:',
    'demo_notice_register': 'Denne registreringsformular tjener udelukkende demonstrationsformål. Ingen autentisk konto vil blive etableret, og ingen data vil blive permanent lagret.',
    'demo_notice_login': 'Denne login-formular er eksklusivt designet til demonstrationsformål. Autentiseringssystemet eksemplificerer min Django-udviklingsekspertise.',
    
    # Home Page
    'about_tijme_heading': 'Om Tijme Vervoort',
    'skills_and_learning': 'Færdigheder og Projekter',
    'welcome_message': 'Velkommen. Her kan du opdage omfattende information angående Tijme',
    'home_bio_p1': 'Jeg er 21 år gammel og residerer for øjeblikket hos mine forældre og to søskende—en bror og en søster—i Nistelrode. Gennem min uddannelsesmæssige bane har jeg besøgt flere uddannelsesinstitutioner. I 2007 initierede jeg min primæruddannelse ved De Beekgraaf grundskole i Nistelrode. Under mit ottende år overførte jeg til De Brinck for at fuldføre min grundskoleuddannelse der. Efterfølgende progrederede jeg til Udens College i Uden, hvor jeg forfulgte studier på kader-theoretisch niveau, hvilket ultimativt førte mig til KW1C i \'s-Hertogenbosch. Oprindeligt immatrikulerede jeg mig i Arkitektur Konstruktion-programmet før jeg overgik til mit nuværende Softwareudvikler-program. For øjeblikket befinder jeg mig i mit tredje år af Softwareudvikler-pensumet. Jeg har succesfuldt fuldført en praktikperiode hos Omnilan, et selskab der tilbød værdifulde læringsmuligheder. Præsentement gennemfører jeg en praktikperiode hos AB Transport, et logistikselskab specialiseret i leverings- og afhentningsservice for erhvervskunder. Denne position har vist sig at være exceptionelt fordelagtig, eftersom jeg er stationeret inden for IT-afdelingen, hvor jeg tilegner mig omfattende viden angående Python-programmeringssproget og Django-framework implementering.',
    'home_bio_p2': 'Gennem dette uddannelsesprogram har jeg akkumuleret substantiel erfaring via diverse projektbaserede opgaver, inklusive udviklingen af et omfattende website for en sportsklubb. For øjeblikket embarker vi på skabelsen af vores porteføljewebsite. Under denne periode har jeg betydeligt forstærket min forståelse af C# samt dets praktiske anvendelse inden for projektudvikling. Yderligere har jeg erhvervet betydelig ekspertise inden for webudvikling gennem både akademiske opgaver og praktisk praktikerfaring. Denne videnstilegnelse har været særligt givende, eftersom jeg nu besidder den tekniske kompetence til at konstruere websites og forstår hvordan at udnytte disse færdigheder professionelt i fremtiden. Endvidere havde jeg under mit foregående uddannelsesprogram lejligheden til at engagere mig i diversificerede og stimulerende projekter, inklusive design og konstruktion af en restaurant med stålramme, en residentiell bygning fra 1930\'erne, og en rekreationsfacilitet for unge. Jeg fuldførte majoriteten af disse projekter med rosværdige resultater. Denne omfattende erfaring vil utvivlsomt vise sig uvurderlig i mine fremtidige professionelle foretagender.',
    
    # Login Page
    'login_header': 'Brugerautentificering',
    'username': 'Brugernavn',
    'password': 'Adgangskode',
    'login_error': 'Den angivne brugernavn-adgangskode kombination er ugyldig. Venligst verificer dine legitimationsoplysninger og forsøg igen.',
    'dont_have_account': 'Besidder du ikke en konto endnu?',
    'register_here': 'Opret en konto her',
    
    # Register Page
    'create_account': 'Opret en Ny Konto',
    'email': 'E-mailadresse',
    'first_name': 'Fornavn',
    'last_name': 'Efternavn',
    'confirm_password': 'Bekræft Adgangskode',
    'username_requirements': 'Obligatorisk felt. Maksimum 150 tegn. Accepterer bogstaver, cifre, og følgende symboler: @/./+/-/_ eksklusivt.',
    'password_req1': 'Din adgangskode må ikke ligne tæt på dine andre personlige informationer.',
    'password_req2': 'Din adgangskode skal omfatte minimum 8 tegn.',
    'password_req3': 'Din adgangskode kan ikke være en almindeligt anvendt adgangskode.',
    'password_req4': 'Din adgangskode kan ikke bestå udelukkende af numeriske tegn.',
    'password_confirm_help': 'Geninput den identiske adgangskode som specificeret ovenfor til verificeringsformål.',
    'register_button': 'Opret Konto',
    'already_account': 'Besidder du allerede en konto?',
    
    # Portfolio Page
    'portfolio_projects': 'Porteføljeprojekter',
    'rainbow_project': 'Regnbueprojekt',
    'match_table': 'Kamptabel-projekt',
    'exercise_1_6': 'CSS-tabeljustering Øvelse',
    'exercise_2_1': 'Row-span og Column-span Projekt',
    'rainbow_desc': 'Regnbueprojekt: Dette repræsenterer opgave 3.2 fra det første tema, hvilket jeg fandt særligt fængslende at udvikle. Udfordringen involverede implementering af span-klasser, en teknik jeg oprindeligt var usikker på. Overordnet mener jeg at gennemførelsen var højst vellykket.',
    'match_table_desc': 'Kamptabel: Dette skærmbillede stammer fra mit inaugurale projekt og demonstrerer effektiv problemløsning. Målet var at vise alle Den Bosch-kampe omfattende. Efter omhyggelig overvejelse implementerede jeg en tabelbaseret løsning—en metodologi vi tidligere ikke havde udnyttet. Dette markerede min første vellykkede anvendelse af tabulær datapræsentation for denne type udfordring.',
    'exercise_1_6_desc': 'Øvelse 1.6: Jeg fandt denne opgave rimeligt håndterbar, eftersom vi modtog en HTML-fil der var fuldstændigt desorganiseret og manglede CSS-styling. Udfordringen krævede at vi genoprettede dens visuelle appel gennem strategisk implementering af tabelstrukturer og rækkeorganisering.',
    'exercise_2_1_desc': 'Øvelse 2.1: Dette viste sig at være en exceptionelt fornøjelig opgave, særligt fordi den tillod os at eksperimentere med row-span og column-span egenskaber. Det endelige resultat var bemærkelsesværdigt vellykket, tydeligt demonstrerende nødvendigheden af at udnytte klasser og ID\'er for at realisere varierede farveskemaer inden for tabelstrukturen.',
    
    # Stage 1 Page
    'omnilan': 'Omnilan',
    'ispconfig': 'ISPConfig',
    'ispconfig_desc': 'Dette repræsenterer det primære dashboard-interface for ISPConfig',
    'email_domain_desc': 'Dette interface faciliterer oprettelsen af e-maildomæner for adresser associeret med dit website',
    'email_address_desc': 'Denne sektion faciliterer etablering af e-mailadresser for dit websitedomæne',
    'rememberz': 'Rememberz',
    'rememberz_menu_desc': 'Dette viser det primære navigationsinterface for Rememberz-brugere',
    'milight_desc': 'Disse repræsenterer brugerkonfigurationsindstillinger for belysningskontrol, inklusive farvetilpasningskapaciteter. Disse funktioner er særligt fremtrædende i venstre sektion af interfacet.',
    'rememberz_main_desc': 'Dette konstituerer det centrale navigationscenter for Rememberz-platformen',
    
    # Stage 2 Page
    'second_internship': 'Anden Praktik: Avanceret Webudvikling & Struktureret Online Læring',
    'wagtail_desc': 'Gennemførte omfattende udforskning af Wagtail CMS gennem strukturerede online kurser, hvor jeg mestrede udviklingen af sofistikerede dynamiske indholdsstyringssystemer for webapplikationer.',
    'cms_desc': 'Kollaborerede omfattende med indholdsstyringssystemer for at arkitekturere interaktive blogpublikationer, inkorporerende avancerede funktioner såsom FAQ-sektioner og dynamiske karruselkomponenter.',
    'bootstrap_email_desc': 'Designede og implementerede professionelle e-mailskabelon-løsninger ved anvendelse af Bootstrap Email-frameworket for AB Transport, skabende responsive e-mailsignaturer og sofistikerede layout-design.',
    'programming_skills': 'Avanceret Programmeringskompetence Udvikling',
    'coding_topics_desc': 'Gennemførte dybdegående udforskning af diverse programmeringsdiscipliner inklusive Python, JavaScript, HTML & CSS, SQL, og yderligere teknologier gennem metodisk strukturerede online læringsprogrammer.',
    'codecademy_desc': 'Fuldførte succesfuldt flere omfattende Python-kurser på Codecademy, omfattende mellemliggende og avancerede Python-programmeringskoncepter, samt specialiserede Django webudviklingsframeworks.',
},

# Finnish (fi) translations
'fi': {
    # Navigation & Common Elements
    'portfolio_website': 'Portfolio-sivusto',
    'home': 'Koti',
    'internship_1': 'Harjoittelu 1',
    'internship_2': 'Harjoittelu 2',
    'portfolio': 'Portfolio',
    'admin_panel': 'Hallintapaneeli',
    'login': 'Kirjaudu sisään',
    'register': 'Rekisteröidy',
    'logout': 'Kirjaudu ulos',
    'close': 'Sulje',
    'profile_picture': 'Profiilikuva',
    'toggle_navigation': 'Vaihda navigointia',
    'copyright': 'Tijme Vervoort.',
    'language': 'Kieli',
    
    # Page Titles
    'home_title': 'Koti - Portfolio-sivusto',
    'login_title': 'Kirjaudu sisään - Portfolio-sivusto',
    'register_title': 'Rekisteröidy - Portfolio-sivusto',
    'portfolio_title': 'Portfolio - Portfolio-sivusto',
    'internship1_title': 'Harjoittelu 1 - Portfolio-sivusto',
    'internship2_title': 'Harjoittelu 2 - Portfolio-sivusto',
    
    # Demo Notice
    'demo_notice_title': 'Demonstraatio-ilmoitus:',
    'demo_notice_register': 'Tämä rekisteröintilomake palvelee yksinomaan demonstraatiotarkoituksia. Mitään autenttista tiliä ei tulla perustamaan eikä mitään tietoja tallenneta pysyvästi.',
    'demo_notice_login': 'Tämä kirjautumislomake on suunniteltu eksklusiivisesti demonstraatiotarkoituksiin. Autentikointijärjestelmä eksemplifoi Django-kehitysasiantuntemustani.',
    
    # Home Page
    'about_tijme_heading': 'Tijme Vervoortista',
    'skills_and_learning': 'Taidot ja Projektit',
    'welcome_message': 'Tervetuloa. Täältä voitte löytää kattavaa tietoa Tijmesta',
    'home_bio_p1': 'Olen 21-vuotias ja asun tällä hetkellä vanhempieni ja kahden sisaruksen—yhden veljen ja yhden sisaren—kanssa Nistelrodessa. Koulutuspolkuni aikana olen käynyt useita oppilaitoksia. Vuonna 2007 aloitin perusopetukseni De Beekgraaf-peruskoulussa Nistelrodessa. Kahdeksannen vuoden aikana siirrin De Brinckiin suorittaakseni peruskoulutukseni siellä. Myöhemmin edistyin Udens Collegeen Udenissa, jossa harjoitin opintoja kader-theoretisch-tasolla, mikä lopulta johti minut KW1C:hen \'s-Hertogenboschissa. Alun perin ilmoittauduin Arkkitehtuuri Rakentaminen -ohjelmaan ennen siirtymistäni nykyiseen Ohjelmistokehittäjä-ohjelmaani. Tällä hetkellä olen kolmannella vuodellani Ohjelmistokehittäjä-opetussuunnitelmassa. Olen menestyksekkäästi suorittanut harjoittelujakson Omnilanissa, yrityksessä joka tarjosi arvokkaita oppimismahdollisuuksia. Tällä hetkellä suoritan harjoittelua AB Transportissa, logistiikkayrityksessä joka erikoistuu toimitus- ja noutamispalveluihin yritysasiakkaille. Tämä asema on osoittautunut poikkeuksellisen edulliseksi, koska olen sijoitettuna IT-osastolla, jossa hankin laajaa tietämystä Python-ohjelmointikielestä ja Django-kehyksen implementoinnista.',
    'home_bio_p2': 'Tämän koulutusohjelma aikana olen kerännyt merkittävää kokemusta erilaisten projektipohjaisien tehtävien kautta, mukaan lukien kattavan verkkosivuston kehittäminen urheiluseuralle. Tällä hetkellä ryhdymme portfolio-verkkosivustomme luomiseen. Tämän ajanjakson aikana olen merkittävästi vahvistanut C#-ymmärrystäni sekä sen käytännöllistä soveltamista projektikehityksessä. Lisäksi olen hankkinut huomattavaa asiantuntemusta web-kehityksessä sekä akateemisten tehtävien että käytännön harjoittelukokemuksen kautta. Tämä tiedonhankinta on ollut erityisen palkitsevaa, koska minulla on nyt tekninen pätevyys rakentaa verkkosivustoja ja ymmärrän kuinka hyödyntää näitä taitoja ammatillisesti tulevaisuudessa. Edelleen minulla oli edellisen koutusohjelmani aikana tilaisuus osallistua monipuolisiin ja stimuloiviin projekteihin, mukaan lukien ravintolan suunnittelu ja rakentaminen teräsrungolla, 1930-luvun asuinrakennus, ja virkistyslaitos nuorille. Suoritin suurimman osan näistä projekteista kiitettävin tuloksin. Tämä kattava kokemus tulee epäilemättä osoittautumaan korvaamattomaksi tulevissa ammatillisissa yrityksissäni.',
    
    # Login Page
    'login_header': 'Käyttäjäautentikointi',
    'username': 'Käyttäjätunnus',
    'password': 'Salasana',
    'login_error': 'Annettu käyttäjätunnus-salasana yhdistelmä on virheellinen. Olkaa hyvä ja varmistakaa tunnistetietonne ja yrittäkää uudelleen.',
    'dont_have_account': 'Eikö teillä ole vielä tiliä?',
    'register_here': 'Luokaa tili tässä',
    
    # Register Page
    'create_account': 'Luo Uusi Tili',
    'email': 'Sähköpostiosoite',
    'first_name': 'Etunimi',
    'last_name': 'Sukunimi',
    'confirm_password': 'Vahvista Salasana',
    'username_requirements': 'Pakollinen kenttä. Enintään 150 merkkiä. Hyväksyy kirjaimet, numerot, ja seuraavat symbolit: @/./+/-/_ yksinomaan.',
    'password_req1': 'Salasananne ei saa muistuttaa läheisesti muita henkilökohtaisia tietojanne.',
    'password_req2': 'Salasananne tulee käsittää vähintään 8 merkkiä.',
    'password_req3': 'Salasananne ei voi olla yleisesti käytetty salasana.',
    'password_req4': 'Salasananne ei voi koostua yksinomaan numeerisista merkeistä.',
    'password_confirm_help': 'Syöttäkää uudelleen identtinen salasana kuten yllä määritelty varmistustarkoituksiin.',
    'register_button': 'Luo Tili',
    'already_account': 'Omistatko jo tilin?',
    
    # Portfolio Page
    'portfolio_projects': 'Portfolio-projektit',
    'rainbow_project': 'Sateenkaari-projekti',
    'match_table': 'Ottelutaulukko-projekti',
    'exercise_1_6': 'CSS-taulukon Tasaus Harjoitus',
    'exercise_2_1': 'Row-span ja Column-span Projekti',
    'rainbow_desc': 'Sateenkaari-projekti: Tämä edustaa tehtävää 3.2 ensimmäisestä teemasta, jonka koin erityisen kiehtovaksi kehittää. Haaste sisälsi span-luokkien implementoinnin, tekniikka josta olin alun perin epävarma. Kokonaisuudessaan uskon että toteutus oli erittäin menestyksekas.',
    'match_table_desc': 'Ottelutaulukko: Tämä kuvakaappaus on peräisin ensimmäisestä projektistani ja demonstroi tehokasta ongelmanratkaisua. Tavoite oli näyttää kaikki Den Boschin ottelut kattavasti. Huolellisen harkinnan jälkeen implementoin taulukkopohjaisen ratkaisun—metodologian jota emme olleet aiemmin hyödyntäneet. Tämä merkitsi ensimmäistä menestyksellistä soveltamistani taulukkomuotoisen datan esittämisestä tämäntyyppiseen haasteeseen.',
    'exercise_1_6_desc': 'Harjoitus 1.6: Koin tämän tehtävän kohtuullisen hallittavaksi, koska saimme HTML-tiedoston joka oli täysin järjestäytymätön ja puuttui CSS-tyylittely. Haaste vaati että palautimme sen visuaalisen vetovoiman strategisen taulukkorakenteiden ja riviorganisaation implementoinnin kautta.',
    'exercise_2_1_desc': 'Harjoitus 2.1: Tämä osoittautui poikkeuksellisen nautinnolliseksi tehtäväksi, erityisesti koska se salli meidän kokeilla row-span ja column-span ominaisuuksia. Lopullinen tulos oli huomattavan menestyksekas, selvästi demonstroiden tarvetta hyödyntää luokkia ja ID:itä vaihtelevien väriteemojen toteuttamiseksi taulukkorakenteen sisällä.',
    
    # Stage 1 Page
    'omnilan': 'Omnilan',
    'ispconfig': 'ISPConfig',
    'ispconfig_desc': 'Tämä edustaa ISPConfigin ensisijaista hallintapaneeli-käyttöliittymää',
    'email_domain_desc': 'Tämä käyttöliittymä helpottaa sähköpostidomainien luomista osoitteille jotka liittyvät verkkosivustoonne',
    'email_address_desc': 'Tämä osio helpottaa sähköpostiosoitteiden perustamista verkkosivustonne domainille',
    'rememberz': 'Rememberz',
    'rememberz_menu_desc': 'Tämä näyttää ensisijaisen navigointikäyttöliittymän Rememberz-käyttäjille',
    'milight_desc': 'Nämä edustavat käyttäjäkonfiguraatioasetuksia valaistuksen hallintaan, mukaan lukien värisäätökapasiteetit. Nämä ominaisuudet ovat erityisen näkyviä käyttöliittymän vasemmassa osiossa.',
    'rememberz_main_desc': 'Tämä muodostaa Rememberz-alustan keskusnavigointikeskuksen',
    
    # Stage 2 Page
    'second_internship': 'Toinen Harjoittelu: Edistynyt Web-kehitys & Strukturoitu Verkko-oppiminen',
    'wagtail_desc': 'Suoritin kattavan tutkimuksen Wagtail CMS:stä strukturoitujen verkkokurssien kautta, jossa hallitsin kehittyneiden dynaamisten sisällönhallintajärjestelmien kehittämisen web-sovelluksille.',
    'cms_desc': 'Tein laajaa yhteistyötä sisällönhallintajärjestelmien kanssa interaktiivisten blogijulkaisujen arkkitehtuurin luomiseksi, sisällyttäen edistyneitä ominaisuuksia kuten FAQ-osiot ja dynaamiset karuselli-komponentit.',
    'bootstrap_email_desc': 'Suunnittelin ja implementoin ammattimaisia sähköpostimalli-ratkaisuja käyttäen Bootstrap Email -kehystä AB Transportille, luoden responsiivisia sähköpostiallekirjoituksia ja kehittyneitä layout-suunnitteluja.',
    'programming_skills': 'Edistynyt Ohjelmointikompetenssien Kehittäminen',
    'coding_topics_desc': 'Suoritin syvällistä tutkimusta erilaisista ohjelmointidisipliineistä mukaan lukien Python, JavaScript, HTML & CSS, SQL, ja lisäteknologioita metodisesti strukturoitujen verkko-oppimisohjelmien kautta.',
    'codecademy_desc': 'Suoritin menestyksekkäästi useita kattavia Python-kursseja Codecademyssa, käsittäen keskitason ja edistyneet Python-ohjelmointikonseptit, sekä erikoistuneet Django web-kehityskehykset.',
}

}


# Default language
DEFAULT_LANGUAGE = 'en'

def translate(key, language=None):
    """
    Translate a key to the specified language.
    If language is None, use the session language or default.
    If key is not found, return the key itself.
    """
    if not language:
        # Default to English if no language specified
        language = DEFAULT_LANGUAGE
    
    # If language doesn't exist in our translations, fall back to default
    if language not in TRANSLATIONS:
        language = DEFAULT_LANGUAGE
    
    # Return the translation or the key itself if not found
    return TRANSLATIONS.get(language, {}).get(key, key)
