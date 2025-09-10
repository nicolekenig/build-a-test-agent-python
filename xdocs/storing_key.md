Here are the main ways to store API keys securely in PyCharm:

## 1. Environment Variables (Recommended)

**Set in PyCharm:**
- Go to **Run → Edit Configurations**
- Select your Python script/configuration
- In **Environment Variables** section, click the folder icon
- Add: `GEMINI_API_KEY` = `your_actual_key_here`
- Click OK

**Access in code:**
```python
import os
api_key = os.getenv('GEMINI_API_KEY')
```

## 2. .env File (Most Popular)

**Create .env file:**
- Right-click project root → New → File → `.env`
- Add: `GEMINI_API_KEY=your_actual_key_here`
- **Important:** Add `.env` to your `.gitignore` file

**Install python-dotenv:**
```bash
pip install python-dotenv
```

**Use in code:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
```

## 3. PyCharm's Built-in Environment Variables

**System-wide:**
- File → Settings → Build, Execution, Deployment → Console → Python Console
- Add environment variables there
- Or use your system's environment variables

## 4. For Workshop Participants (Simplest)

Since it's a workshop, you might want the simplest approach:

**Option A - Direct in code (temporarily):**
```python
# Only for workshop - NOT for production
api_key = "your_key_here"
```

**Option B - Input prompt:**
```python
import getpass
api_key = getpass.getpass("Enter your API key: ")
```

## Security Best Practices

- **Never commit API keys to version control**
- Add `.env` to `.gitignore`
- Use environment variables for production
- For workshops, consider the input prompt method so participants enter their own keys

For your workshop, I'd recommend either the `.env` file method (teach good practices) or the input prompt method (simplest for participants to follow along).