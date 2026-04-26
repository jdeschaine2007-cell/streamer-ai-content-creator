#!/usr/bin/env python3
"""
AI Content Generator for Streamers
Uses GitHub Models API to generate titles, descriptions, and social media content
"""

import os
import requests
import json
from typing import Dict, List, Optional

class GitHubModelsClient:
    """Client for GitHub Models API"""
    
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GITHUB_TOKEN environment variable must be set")
        self.base_url = "https://models.github.ai/inference/chat/completions"
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json"
        }
    
    def generate_response(self, prompt: str, model: str = "openai/gpt-4o") -> str:
        """Generate a response from the AI model"""
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.base_url, headers=self.headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        return data["choices"][0]["message"]["content"]

class ContentGenerator:
    """AI-powered content generator for streamers"""
    
    def __init__(self, token: Optional[str] = None):
        self.client = GitHubModelsClient(token)
    
    def generate_video_title(self, game_name: str, content_type: str, highlights: str) -> str:
        """Generate an engaging video title"""
        prompt = f"""Generate a catchy, engaging YouTube video title for a gaming stream.
        
Game: {game_name}
Content Type: {content_type}
Highlights: {highlights}

Requirements:
- Make it exciting and click-worthy
- Keep it under 60 characters
- Include relevant keywords for SEO
- Make it specific to the content

Return only the title, nothing else."""
        
        return self.client.generate_response(prompt)
    
    def generate_video_description(self, game_name: str, title: str, highlights: str) -> str:
        """Generate a detailed video description"""
        prompt = f"""Generate an engaging YouTube video description for a gaming stream.

Game: {game_name}
Title: {title}
Highlights: {highlights}

Requirements:
- Include a hook in the first 2 lines
- Add relevant timestamps placeholder (0:00 - Intro, etc.)
- Include SEO keywords naturally
- Add a call to action (subscribe, like, etc.)
- Mention the stream schedule
- Keep it under 2000 characters

Return only the description, nothing else."""
        
        return self.client.generate_response(prompt)
    
    def generate_twitter_post(self, title: str, game_name: str, clip_url: str = "") -> str:
        """Generate a Twitter/X post"""
        prompt = f"""Generate an engaging Twitter/X post to promote a stream clip.

Video Title: {title}
Game: {game_name}
Clip URL: {clip_url if clip_url else '[LINK]'}

Requirements:
- Under 280 characters
- Include relevant hashtags
- Make it exciting and shareable
- Include a call to action

Return only the tweet text, nothing else."""
        
        return self.client.generate_response(prompt)
    
    def generate_instagram_caption(self, title: str, game_name: str) -> str:
        """Generate an Instagram caption"""
        prompt = f"""Generate an engaging Instagram caption for a gaming clip.

Video Title: {title}
Game: {game_name}

Requirements:
- Under 2200 characters
- Include relevant hashtags
- Make it visually descriptive
- Add emoji appropriate for gaming
- Include a call to action

Return only the caption, nothing else."""
        
        return self.client.generate_response(prompt)
    
    def generate_tiktok_description(self, title: str, game_name: str) -> str:
        """Generate a TikTok description"""
        prompt = f"""Generate a catchy TikTok description for a gaming clip.

Video Title: {title}
Game: {game_name}

Requirements:
- Under 150 characters
- Include trending hashtags
- Make it punchy and exciting
- Focus on the most exciting moment

Return only the description, nothing else."""
        
        return self.client.generate_response(prompt)
    
    def generate_thumbnail_prompt(self, game_name: str, title: str, mood: str = "exciting") -> str:
        """Generate a detailed prompt for AI image generation (for thumbnails)"""
        prompt = f"""Generate a detailed image generation prompt for creating a YouTube thumbnail.

Game: {game_name}
Title: {title}
Mood: {mood}

Requirements:
- Describe the scene vividly
- Include character expressions
- Specify lighting and colors
- Mention text overlay suggestions
- Make it eye-catching and high-contrast
- Style: professional gaming thumbnail

Return only the image prompt, nothing else."""
        
        return self.client.generate_response(prompt)

def main():
    """Example usage"""
    import sys
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    # Initialize generator
    generator = ContentGenerator()
    
    # Example: Generate content for a stream
    game_name = "Valorant"
    content_type = "Clutch Moment"
    highlights = "Won a 1v5 clutch with amazing aim"
    
    print("Generating content...")
    print("\n" + "="*50)
    
    # Generate title
    title = generator.generate_video_title(game_name, content_type, highlights)
    print(f"Title: {title}")
    
    # Generate description
    description = generator.generate_video_description(game_name, title, highlights)
    print(f"\nDescription:\n{description}")
    
    # Generate social media posts
    twitter = generator.generate_twitter_post(title, game_name)
    print(f"\nTwitter Post:\n{twitter}")
    
    instagram = generator.generate_instagram_caption(title, game_name)
    print(f"\nInstagram Caption:\n{instagram}")
    
    tiktok = generator.generate_tiktok_description(title, game_name)
    print(f"\nTikTok Description:\n{tiktok}")
    
    # Generate thumbnail prompt
    thumbnail_prompt = generator.generate_thumbnail_prompt(game_name, title)
    print(f"\nThumbnail Prompt:\n{thumbnail_prompt}")

if __name__ == "__main__":
    main()
