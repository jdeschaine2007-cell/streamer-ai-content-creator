# Streamer AI Content Creator

AI-powered content creation tools for game streamers using GitHub Models API. Generate titles, descriptions, social media posts, and thumbnail prompts automatically.

## Features

- **Video Title Generation**: Create catchy, SEO-optimized YouTube titles
- **Video Description Generation**: Generate engaging descriptions with hooks and CTAs
- **Social Media Content**: Auto-generate posts for Twitter/X, Instagram, and TikTok
- **Thumbnail Prompts**: Get detailed prompts for AI image generators
- **Batch Processing**: Generate content for multiple clips at once
- **GitHub Actions Integration**: Run content generation directly from GitHub

## Prerequisites

1. GitHub account
2. GitHub Personal Access Token (PAT) with `models` scope
   - Go to https://github.com/settings/tokens
   - Create a new token
   - Select the `models` scope

## Setup

### Option 1: Local Usage

1. Clone this repository:
```bash
git clone https://github.com/jdeschaine2007-cell/streamer-ai-content-creator.git
cd streamer-ai-content-creator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```bash
cp .env.example .env
```

4. Add your GitHub token to `.env`:
```
GITHUB_TOKEN=your_github_personal_access_token_here
```

5. Run the generator:
```bash
python ai_content_generator.py
```

### Option 2: GitHub Actions (Recommended)

1. Fork this repository to your GitHub account

2. Go to the **Actions** tab in your repository

3. Select either workflow:
   - **AI Content Generator**: Full content generation
   - **AI Thumbnail Prompt Generator**: Thumbnail prompts only

4. Click **Run workflow** and fill in the required fields:
   - Game name
   - Content type
   - Highlights
   - Choose AI model (optional, defaults to GPT-4o)

5. The generated content will be saved in the `output/` directory

## Usage Examples

### Python Script

```python
from ai_content_generator import ContentGenerator

# Initialize with your token
generator = ContentGenerator()

# Generate content
title = generator.generate_video_title(
    game_name="Valorant",
    content_type="Clutch Moment",
    highlights="Won a 1v5 clutch with amazing aim"
)

description = generator.generate_video_description(
    game_name="Valorant",
    title=title,
    highlights="Won a 1v5 clutch with amazing aim"
)

twitter_post = generator.generate_twitter_post(title, "Valorant")
instagram_caption = generator.generate_instagram_caption(title, "Valorant")
tiktok_description = generator.generate_tiktok_description(title, "Valorant")
thumbnail_prompt = generator.generate_thumbnail_prompt("Valorant", title)
```

### Batch Processing

```python
from batch_content_generator import BatchContentGenerator

# Define your clips
clips = [
    {
        "game_name": "Valorant",
        "content_type": "Clutch Moment",
        "highlights": "Won a 1v5 clutch"
    },
    {
        "game_name": "Minecraft",
        "content_type": "Building Tutorial",
        "highlights": "Built an epic castle"
    }
]

# Process all clips
batch_gen = BatchContentGenerator()
results = batch_gen.process_batch(clips)
batch_gen.save_results(results)
```

## Available AI Models

- `openai/gpt-4o` (default)
- `openai/gpt-4.1`
- `meta/llama-3.1-70b-instruct`

You can change the model in the GitHub Actions workflow or by modifying the Python script.

## Output Format

Generated content includes:

- **Video Title**: Catchy, under 60 characters, SEO-optimized
- **Video Description**: Engaging with hooks, timestamps, and CTAs
- **Twitter Post**: Under 280 characters with hashtags
- **Instagram Caption**: Under 2200 characters with emojis
- **TikTok Description**: Under 150 characters, punchy and exciting
- **Thumbnail Prompt**: Detailed image generation prompt for AI art tools

## Thumbnail Image Generation

Use the generated thumbnail prompts with these AI image generators:

- **Midjourney**: https://www.midjourney.com/
- **DALL-E 3**: Available through ChatGPT Plus
- **Stable Diffusion**: https://stability.ai/
- **Leonardo.ai**: https://leonardo.ai/

## Workflow Examples

### Generate Content for a Valorant Clip

**GitHub Actions:**
1. Go to Actions → AI Content Generator
2. Click "Run workflow"
3. Fill in:
   - Game name: `Valorant`
   - Content type: `Clutch Moment`
   - Highlights: `Won a 1v5 clutch with amazing aim`
4. Select model: `openai/gpt-4o`
5. Click "Run workflow"

**Python:**
```python
from ai_content_generator import ContentGenerator

gen = ContentGenerator()
title = gen.generate_video_title("Valorant", "Clutch Moment", "Won a 1v5 clutch")
print(title)
```

## Troubleshooting

### "GITHUB_TOKEN environment variable must be set"
- Make sure you created a `.env` file with your token
- For GitHub Actions, the token is provided automatically

### Rate Limiting
- GitHub Models has usage limits
- If you hit limits, wait a few minutes before trying again
- Consider upgrading to paid tier for higher limits

### Workflow Fails
- Check that you have the `models` permission in your repository settings
- Ensure your PAT has the `models` scope

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this for your streaming content creation needs.

## Support

For issues with GitHub Models API, check the official documentation:
- GitHub Models Docs: https://docs.github.com/en/github-models
- GitHub Models Playground: https://github.com/marketplace/models
