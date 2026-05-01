# skills_data.py

SKILL_CATEGORIES = {
    "programming_languages": [
        "python", "java", "javascript", "typescript", "c", "c++", "c#",
        "php", "ruby", "go", "golang", "kotlin", "swift", "r", "scala",
        "perl", "rust", "dart", "lua", "haskell", "elixir", "objective-c",
        "matlab", "vb.net", "visual basic", "shell scripting", "bash",
        "powershell", "assembly language", "solidity"
    ],

    "markup_and_styling": [
        "html", "html5", "css", "css3", "sass", "scss", "less",
        "xml", "json", "yaml", "markdown", "bootstrap", "tailwind css",
        "material ui", "bulma", "foundation", "styled-components"
    ],

    "frontend_development": [
        "responsive design", "web accessibility", "seo", "dom manipulation",
        "browser developer tools", "cross-browser compatibility",
        "single page application", "spa", "progressive web app", "pwa",
        "web performance optimization", "lazy loading", "client-side rendering",
        "server-side rendering", "static site generation"
    ],

    "frontend_frameworks_libraries": [
        "react", "react.js", "next.js", "angular", "vue", "vue.js",
        "nuxt.js", "svelte", "sveltekit", "jquery", "redux", "redux toolkit",
        "zustand", "recoil", "mobx", "rxjs", "vite", "webpack", "babel",
        "parcel", "eslint", "prettier"
    ],

    "backend_development": [
        "backend development", "server-side development", "rest api",
        "api development", "api integration", "authentication", "authorization",
        "jwt", "oauth", "oauth2", "session management", "cors",
        "middleware", "microservices", "monolithic architecture",
        "web sockets", "socket.io", "grpc", "graphql", "webhooks",
        "rate limiting", "caching", "load balancing"
    ],

    "backend_frameworks": [
        "flask", "django", "fastapi", "spring boot", "spring mvc",
        "node.js", "express.js", "nestjs", "laravel", "codeigniter",
        "asp.net", "asp.net core", "ruby on rails", "rails", "gin",
        "fiber", "phoenix", "actix", "rocket", "ktor"
    ],

    "databases_sql": [
        "mysql", "postgresql", "sqlite", "oracle", "microsoft sql server",
        "sql server", "mariadb", "db2", "stored procedures", "triggers",
        "views", "joins", "indexing", "query optimization",
        "database normalization", "acid properties", "transactions"
    ],

    "databases_nosql": [
        "mongodb", "firebase", "firestore", "redis", "cassandra",
        "dynamodb", "couchdb", "neo4j", "elasticsearch", "opensearch",
        "influxdb", "hbase", "arangodb", "document database",
        "key-value database", "graph database", "wide-column database"
    ],

    "data_engineering": [
        "etl", "elt", "data pipeline", "data warehousing", "data lake",
        "data lakehouse", "apache spark", "pyspark", "apache kafka",
        "apache airflow", "dbt", "hadoop", "hive", "pig", "snowflake",
        "bigquery", "redshift", "databricks", "data modeling",
        "data integration", "data migration", "data quality",
        "data governance"
    ],

    "data_analysis": [
        "data analysis", "data cleaning", "data preprocessing",
        "data wrangling", "exploratory data analysis", "eda",
        "data visualization", "statistical analysis", "descriptive statistics",
        "inferential statistics", "hypothesis testing", "a/b testing",
        "regression analysis", "correlation analysis", "time series analysis",
        "dashboard development", "reporting"
    ],

    "data_science_libraries": [
        "pandas", "numpy", "matplotlib", "seaborn", "plotly", "bokeh",
        "scipy", "statsmodels", "scikit-learn", "sklearn", "xgboost",
        "lightgbm", "catboost", "nltk", "spacy"
    ],

    "machine_learning": [
        "machine learning", "supervised learning", "unsupervised learning",
        "semi-supervised learning", "reinforcement learning",
        "classification", "regression", "clustering", "decision tree",
        "random forest", "support vector machine", "svm",
        "naive bayes", "knn", "k-nearest neighbors", "linear regression",
        "logistic regression", "gradient boosting", "feature engineering",
        "feature selection", "model training", "model evaluation",
        "cross validation", "hyperparameter tuning", "overfitting",
        "underfitting", "confusion matrix", "precision", "recall",
        "f1 score", "roc auc", "accuracy", "mlops"
    ],

    "deep_learning": [
        "deep learning", "neural networks", "artificial neural network",
        "ann", "cnn", "convolutional neural network", "rnn",
        "recurrent neural network", "lstm", "gru", "transformers",
        "autoencoders", "gan", "generative adversarial networks",
        "backpropagation", "activation functions", "dropout",
        "batch normalization", "tensorflow", "keras", "pytorch",
        "torch", "onnx"
    ],

    "natural_language_processing": [
        "natural language processing", "nlp", "text preprocessing",
        "tokenization", "stemming", "lemmatization", "named entity recognition",
        "ner", "sentiment analysis", "text classification",
        "topic modeling", "word embeddings", "word2vec", "glove",
        "bert", "roberta", "gpt", "transformer models",
        "question answering", "text summarization", "machine translation"
    ],

    "generative_ai": [
        "generative ai", "large language models", "llm", "prompt engineering",
        "rag", "retrieval augmented generation", "vector database",
        "embedding models", "semantic search", "langchain", "llamaindex",
        "openai api", "gemini api", "claude api", "hugging face",
        "fine tuning", "chatbot development", "ai agents"
    ],

    "computer_vision": [
        "computer vision", "image processing", "opencv", "object detection",
        "image classification", "image segmentation", "face recognition",
        "ocr", "optical character recognition", "yolo", "rcnn",
        "faster rcnn", "mediapipe", "image augmentation"
    ],

    "cloud_platforms": [
        "aws", "amazon web services", "azure", "microsoft azure",
        "google cloud", "gcp", "digitalocean", "heroku", "vercel",
        "netlify", "firebase hosting", "cloudflare", "oracle cloud",
        "ibm cloud"
    ],

    "aws_services": [
        "ec2", "s3", "lambda", "rds", "dynamodb", "cloudfront",
        "cloudwatch", "iam", "vpc", "route 53", "ecs", "eks",
        "elastic beanstalk", "api gateway", "sns", "sqs", "glue",
        "athena", "redshift", "sagemaker"
    ],

    "azure_services": [
        "azure vm", "azure functions", "azure app service",
        "azure sql database", "azure blob storage", "azure devops",
        "azure active directory", "azure kubernetes service", "aks",
        "azure data factory", "synapse analytics"
    ],

    "gcp_services": [
        "compute engine", "cloud storage", "cloud functions",
        "cloud run", "app engine", "bigquery", "cloud sql",
        "firebase", "pub/sub", "vertex ai", "kubernetes engine", "gke"
    ],

    "devops": [
        "devops", "docker", "kubernetes", "containerization",
        "jenkins", "github actions", "gitlab ci", "circleci",
        "travis ci", "ci/cd", "terraform", "ansible", "chef",
        "puppet", "helm", "nginx", "apache server", "linux",
        "ubuntu", "centos", "monitoring", "logging", "prometheus",
        "grafana", "elk stack", "sonarqube"
    ],

    "version_control": [
        "git", "github", "gitlab", "bitbucket", "svn",
        "branching", "merging", "pull requests", "code review",
        "github workflow"
    ],

    "software_testing": [
        "software testing", "manual testing", "automation testing",
        "unit testing", "integration testing", "system testing",
        "regression testing", "smoke testing", "sanity testing",
        "performance testing", "load testing", "stress testing",
        "security testing", "selenium", "cypress", "playwright",
        "jest", "mocha", "chai", "pytest", "unittest", "junit",
        "testng", "postman testing", "api testing", "bug tracking",
        "test cases", "test planning"
    ],

    "cybersecurity": [
        "cybersecurity", "information security", "network security",
        "application security", "web security", "penetration testing",
        "vulnerability assessment", "ethical hacking", "owasp",
        "owasp top 10", "sql injection", "xss", "csrf",
        "cryptography", "encryption", "hashing", "firewall",
        "ids", "ips", "siem", "splunk", "wireshark", "nmap",
        "metasploit", "burp suite", "kali linux"
    ],

    "networking": [
        "computer networks", "tcp/ip", "http", "https", "dns",
        "dhcp", "ftp", "smtp", "ssh", "ssl", "tls", "vpn",
        "lan", "wan", "routing", "switching", "subnetting",
        "network troubleshooting"
    ],

    "mobile_development": [
        "android development", "ios development", "flutter",
        "react native", "swiftui", "kotlin android", "java android",
        "xcode", "android studio", "mobile app development",
        "firebase cloud messaging", "push notifications"
    ],

    "ui_ux_design": [
        "ui design", "ux design", "user interface design",
        "user experience design", "wireframing", "prototyping",
        "user research", "usability testing", "figma", "adobe xd",
        "sketch", "invision", "design systems", "interaction design",
        "visual design"
    ],

    "project_management": [
        "project management", "agile", "scrum", "kanban",
        "waterfall model", "sdlc", "software development life cycle",
        "jira", "trello", "asana", "notion", "risk management",
        "stakeholder management", "sprint planning", "daily standup",
        "retrospective", "requirement analysis"
    ],

    "business_analysis": [
        "business analysis", "requirement gathering",
        "requirement documentation", "brd", "frd", "use cases",
        "user stories", "process mapping", "gap analysis",
        "stakeholder communication", "business process modeling",
        "uml", "bpmn"
    ],

    "office_productivity": [
        "microsoft excel", "excel", "advanced excel", "google sheets",
        "microsoft word", "microsoft powerpoint", "powerpoint",
        "microsoft office", "google docs", "google slides",
        "vlookup", "xlookup", "pivot tables", "macros", "vba"
    ],

    "business_intelligence": [
        "power bi", "tableau", "looker", "qlik", "google data studio",
        "looker studio", "dashboard", "business intelligence",
        "kpi reporting", "data storytelling", "data interpretation"
    ],

    "accounting_finance": [
        "accounting", "financial accounting", "cost accounting",
        "tally", "tally erp", "tally prime", "gst", "taxation",
        "income tax", "tds", "audit", "bookkeeping",
        "financial analysis", "budgeting", "forecasting",
        "accounts payable", "accounts receivable", "payroll"
    ],

    "digital_marketing": [
        "digital marketing", "seo", "sem", "google ads",
        "facebook ads", "instagram ads", "social media marketing",
        "content marketing", "email marketing", "copywriting",
        "google analytics", "keyword research", "on-page seo",
        "off-page seo", "technical seo", "affiliate marketing"
    ],

    "content_and_media": [
        "content writing", "technical writing", "blog writing",
        "copy editing", "proofreading", "video editing",
        "adobe premiere pro", "after effects", "photoshop",
        "illustrator", "canva", "content creation",
        "script writing", "storyboarding"
    ],

    "mechanical_engineering": [
        "autocad", "solidworks", "catia", "creo", "ansys",
        "fusion 360", "manufacturing", "cnc", "gd&t",
        "thermodynamics", "fluid mechanics", "machine design",
        "maintenance engineering", "quality control"
    ],

    "electrical_electronics": [
        "electrical engineering", "electronics", "circuit design",
        "pcb design", "embedded systems", "microcontroller",
        "arduino", "raspberry pi", "iot", "plc", "scada",
        "power systems", "control systems", "vlsi", "verilog",
        "vhdl", "matlab simulink"
    ],

    "civil_engineering": [
        "civil engineering", "autocad civil", "staad pro",
        "revit", "etabs", "construction management",
        "structural analysis", "estimation", "surveying",
        "quantity surveying", "building planning", "site supervision"
    ],

    "soft_skills": [
        "communication", "written communication", "verbal communication",
        "teamwork", "leadership", "problem solving", "critical thinking",
        "analytical thinking", "time management", "adaptability",
        "creativity", "decision making", "conflict resolution",
        "attention to detail", "collaboration", "presentation skills",
        "negotiation", "emotional intelligence", "work ethic",
        "self motivation", "customer service"
    ]
}

SKILL_ALIASES = {
    # Programming
    "js": "javascript",
    "ts": "typescript",
    "py": "python",
    "golang": "go",
    "cpp": "c++",
    "c sharp": "c#",
    "c-sharp": "c#",
    "objc": "objective-c",
    "shell": "shell scripting",

    # Frontend
    "reactjs": "react",
    "react.js": "react",
    "vuejs": "vue",
    "vue.js": "vue",
    "nextjs": "next.js",
    "nuxtjs": "nuxt.js",
    "tailwind": "tailwind css",
    "mui": "material ui",
    "material-ui": "material ui",
    "scss": "sass",

    # Backend
    "node": "node.js",
    "nodejs": "node.js",
    "express": "express.js",
    "expressjs": "express.js",
    "rest": "rest api",
    "restful api": "rest api",
    "apis": "api development",
    "jwt token": "jwt",
    "auth": "authentication",
    "oauth 2": "oauth2",

    # Databases
    "postgres": "postgresql",
    "postgre": "postgresql",
    "mongo": "mongodb",
    "ms sql": "microsoft sql server",
    "mssql": "microsoft sql server",
    "sqlserver": "sql server",
    "elastic search": "elasticsearch",

    # Data Science
    "eda": "exploratory data analysis",
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "data viz": "data visualization",
    "stats": "statistics",
    "a b testing": "a/b testing",

    # AI / ML
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "ann": "artificial neural network",
    "cnn": "convolutional neural network",
    "rnn": "recurrent neural network",
    "svm": "support vector machine",
    "knn": "k-nearest neighbors",
    "xgb": "xgboost",
    "gen ai": "generative ai",
    "genai": "generative ai",
    "llms": "large language models",
    "llm": "large language models",
    "rag": "retrieval augmented generation",
    "cv": "computer vision",
    "ocr": "optical character recognition",
    "nlp": "natural language processing",
    "ner": "named entity recognition",

    # Cloud
    "amazon web services": "aws",
    "microsoft azure": "azure",
    "google cloud platform": "google cloud",
    "gcp": "google cloud",
    "k8s": "kubernetes",
    "eks": "elastic kubernetes service",
    "aks": "azure kubernetes service",
    "gke": "google kubernetes engine",

    # DevOps
    "cicd": "ci/cd",
    "ci cd": "ci/cd",
    "gh actions": "github actions",
    "infra as code": "infrastructure as code",
    "iac": "infrastructure as code",

    # Testing
    "qa": "quality assurance",
    "sdet": "software development engineer in test",
    "automation qa": "automation testing",
    "manual qa": "manual testing",
    "api test": "api testing",

    # Cybersecurity
    "infosec": "information security",
    "pen testing": "penetration testing",
    "pentesting": "penetration testing",
    "vapt": "vulnerability assessment",
    "x-site scripting": "xss",

    # Project management
    "pm": "project management",
    "ba": "business analysis",
    "sdlc": "software development life cycle",
    "req gathering": "requirement gathering",

    # BI / Office
    "ms excel": "microsoft excel",
    "ms word": "microsoft word",
    "ms powerpoint": "microsoft powerpoint",
    "ppt": "powerpoint",
    "gds": "google data studio",

    # Design
    "ux": "ux design",
    "ui": "ui design",
    "ui/ux": "ui ux design",
    "adobe photoshop": "photoshop",
    "adobe illustrator": "illustrator",
    "adobe premiere": "adobe premiere pro",

    # Engineering
    "cad": "autocad",
    "computer aided design": "autocad",
    "plc programming": "plc",
    "internet of things": "iot"
}

JOB_ROLE_SKILLS = {
    "frontend_developer": [
        "html", "css", "javascript", "typescript", "bootstrap",
        "tailwind css", "react", "next.js", "redux", "responsive design",
        "web accessibility", "seo", "git", "github", "api integration"
    ],

    "backend_developer": [
        "python", "java", "node.js", "flask", "django", "fastapi",
        "spring boot", "express.js", "rest api", "graphql", "mysql",
        "postgresql", "mongodb", "authentication", "jwt", "oauth2",
        "microservices", "docker", "git", "postman"
    ],

    "full_stack_developer": [
        "html", "css", "javascript", "typescript", "react", "next.js",
        "node.js", "express.js", "python", "flask", "django", "mysql",
        "mongodb", "rest api", "authentication", "git", "github",
        "docker", "api integration"
    ],

    "python_developer": [
        "python", "oops", "data structures", "algorithms", "flask",
        "django", "fastapi", "mysql", "postgresql", "rest api",
        "git", "unit testing", "pytest"
    ],

    "java_developer": [
        "java", "oops", "data structures", "algorithms", "spring boot",
        "spring mvc", "hibernate", "mysql", "postgresql", "rest api",
        "microservices", "maven", "junit", "git"
    ],

    "mern_stack_developer": [
        "mongodb", "express.js", "react", "node.js", "javascript",
        "html", "css", "rest api", "jwt", "redux", "git", "github"
    ],

    "mean_stack_developer": [
        "mongodb", "express.js", "angular", "node.js", "typescript",
        "javascript", "html", "css", "rest api", "git"
    ],

    "mobile_app_developer": [
        "mobile app development", "android development", "ios development",
        "flutter", "react native", "kotlin", "swift", "firebase",
        "api integration", "push notifications", "android studio", "xcode"
    ],

    "android_developer": [
        "android development", "kotlin", "java", "android studio",
        "xml", "firebase", "sqlite", "api integration",
        "push notifications", "material design"
    ],

    "flutter_developer": [
        "flutter", "dart", "firebase", "rest api", "state management",
        "mobile app development", "android development", "ios development"
    ],

    "data_analyst": [
        "data analysis", "data cleaning", "excel", "advanced excel",
        "sql", "python", "pandas", "numpy", "power bi", "tableau",
        "data visualization", "dashboard development", "statistics",
        "reporting"
    ],

    "business_analyst": [
        "business analysis", "requirement gathering", "requirement documentation",
        "brd", "frd", "user stories", "use cases", "gap analysis",
        "process mapping", "sql", "excel", "power bi", "stakeholder communication"
    ],

    "data_scientist": [
        "python", "sql", "pandas", "numpy", "matplotlib", "seaborn",
        "scikit-learn", "machine learning", "statistics",
        "exploratory data analysis", "feature engineering",
        "model training", "model evaluation", "data visualization"
    ],

    "machine_learning_engineer": [
        "python", "machine learning", "deep learning", "scikit-learn",
        "tensorflow", "pytorch", "numpy", "pandas", "feature engineering",
        "model training", "model evaluation", "mlops", "docker",
        "rest api"
    ],

    "ai_engineer": [
        "python", "artificial intelligence", "machine learning",
        "deep learning", "natural language processing", "generative ai",
        "large language models", "prompt engineering",
        "retrieval augmented generation", "vector database",
        "langchain", "llamaindex", "openai api", "gemini api"
    ],

    "nlp_engineer": [
        "python", "natural language processing", "tokenization",
        "text classification", "sentiment analysis", "named entity recognition",
        "bert", "transformers", "spacy", "nltk", "hugging face",
        "machine learning", "deep learning"
    ],

    "computer_vision_engineer": [
        "python", "computer vision", "opencv", "image processing",
        "object detection", "image classification", "image segmentation",
        "yolo", "tensorflow", "pytorch", "deep learning"
    ],

    "data_engineer": [
        "python", "sql", "etl", "elt", "data pipeline",
        "apache spark", "pyspark", "apache kafka", "airflow",
        "hadoop", "snowflake", "bigquery", "redshift",
        "data warehousing", "data lake", "dbt"
    ],

    "devops_engineer": [
        "linux", "docker", "kubernetes", "jenkins", "github actions",
        "gitlab ci", "ci/cd", "terraform", "ansible", "aws",
        "azure", "google cloud", "nginx", "prometheus", "grafana",
        "monitoring", "logging"
    ],

    "cloud_engineer": [
        "aws", "azure", "google cloud", "cloud computing", "ec2",
        "s3", "lambda", "iam", "vpc", "rds", "docker",
        "kubernetes", "terraform", "monitoring", "networking"
    ],

    "aws_cloud_engineer": [
        "aws", "ec2", "s3", "lambda", "rds", "dynamodb",
        "cloudfront", "cloudwatch", "iam", "vpc", "route 53",
        "api gateway", "terraform", "docker", "kubernetes"
    ],

    "software_tester": [
        "software testing", "manual testing", "test cases",
        "test planning", "bug tracking", "regression testing",
        "smoke testing", "sanity testing", "api testing",
        "postman testing", "jira"
    ],

    "automation_tester": [
        "automation testing", "selenium", "cypress", "playwright",
        "java", "python", "pytest", "junit", "testng",
        "api testing", "postman testing", "ci/cd", "git"
    ],

    "cybersecurity_analyst": [
        "cybersecurity", "information security", "network security",
        "vulnerability assessment", "penetration testing", "owasp top 10",
        "wireshark", "nmap", "burp suite", "siem", "splunk",
        "firewall", "incident response"
    ],

    "network_engineer": [
        "computer networks", "tcp/ip", "dns", "dhcp", "routing",
        "switching", "subnetting", "vpn", "firewall",
        "network troubleshooting", "cisco", "lan", "wan"
    ],

    "ui_ux_designer": [
        "ui design", "ux design", "figma", "adobe xd",
        "wireframing", "prototyping", "user research",
        "usability testing", "design systems", "interaction design",
        "visual design"
    ],

    "project_manager": [
        "project management", "agile", "scrum", "kanban",
        "sdlc", "jira", "risk management", "stakeholder management",
        "sprint planning", "team management", "communication",
        "leadership"
    ],

    "digital_marketing_executive": [
        "digital marketing", "seo", "sem", "google ads",
        "social media marketing", "content marketing", "email marketing",
        "google analytics", "keyword research", "copywriting"
    ],

    "accountant": [
        "accounting", "financial accounting", "tally", "tally prime",
        "gst", "taxation", "tds", "bookkeeping", "payroll",
        "accounts payable", "accounts receivable", "excel"
    ],

    "mechanical_engineer": [
        "mechanical engineering", "autocad", "solidworks", "catia",
        "ansys", "manufacturing", "cnc", "gd&t",
        "thermodynamics", "machine design", "quality control"
    ],

    "electrical_engineer": [
        "electrical engineering", "power systems", "control systems",
        "circuit design", "plc", "scada", "autocad",
        "matlab simulink", "maintenance engineering"
    ],

    "embedded_systems_engineer": [
        "embedded systems", "c", "c++", "microcontroller",
        "arduino", "raspberry pi", "iot", "pcb design",
        "circuit design", "rtos", "uart", "spi", "i2c"
    ],

    "civil_engineer": [
        "civil engineering", "autocad civil", "staad pro",
        "revit", "etabs", "construction management",
        "structural analysis", "estimation", "surveying",
        "site supervision"
    ]
}

def get_all_skills():
    """
    Returns all skills from all categories and aliases.
    """
    all_skills = []

    for skills in SKILL_CATEGORIES.values():
        all_skills.extend(skills)

    all_skills.extend(SKILL_ALIASES.keys())
    all_skills.extend(SKILL_ALIASES.values())

    return sorted(list(set(all_skills)))


def get_skills_by_category(category_name):
    """
    Returns skills from a specific category.
    """
    return SKILL_CATEGORIES.get(category_name, [])


def get_role_skills(role_name):
    """
    Returns required skills for a specific job role.
    """
    return JOB_ROLE_SKILLS.get(role_name, [])


def normalize_skill(skill):
    """
    Converts aliases into standard skill names.
    Example: js -> javascript
    """
    skill = skill.lower().strip()
    return SKILL_ALIASES.get(skill, skill)