#!/usr/bin/env python3
"""
Batch Content Generator for Streamers
Process multiple stream clips and generate content for all
"""

import os
import json
from typing import List, Dict
from ai_content_generator import ContentGenerator

class BatchContentGenerator:
    """Generate content for multiple stream clips"""
    
    def __init__(self, token: str = None):
        self.generator = ContentGenerator(token)
    
    def process_clip(self, clip_data: Dict) -> Dict:
        """Process a single clip and generate all content"""
        game_name = clip_data.get("game_name", "Unknown Game")
        content_type = clip_data.get("content_type", "Clip")
        highlights = clip_data.get("highlights", "")
        
        results = {
            "clip_info": clip_data,
            "title": self.generator.generate_video_title(game_name, content_type, highlights),
            "description": self.generator.generate_video_description(game_name, "", highlights),
            "twitter": self.generator.generate_twitter_post("", game_name),
            "instagram": self.generator.generate_instagram_caption("", game_name),
            "tiktok": self.generator.generate_tiktok_description("", game_name),
            "thumbnail_prompt": self.generator.generate_thumbnail_prompt(game_name, "")
        }
        
        return results
    
    def process_batch(self, clips: List[Dict]) -> List[Dict]:
        """Process multiple clips"""
        results = []
        for i, clip in enumerate(clips, 1):
            print(f"Processing clip {i}/{len(clips)}: {clip.get('game_name', 'Unknown')}")
            result = self.process_clip(clip)
            results.append(result)
        return results
    
    def save_results(self, results: List[Dict], output_file: str = "batch_output.json"):
        """Save results to JSON file"""
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {output_file}")

def load_clips_from_file(input_file: str) -> List[Dict]:
    """Load clip data from JSON file"""
    with open(input_file, 'r') as f:
        return json.load(f)

def main():
    """Example usage"""
    import sys
    from dotenv import load_dotenv
    
    load_dotenv()
    
    # Example batch data
    example_clips = [
        {
            "game_name": "Valorant",
            "content_type": "Clutch Moment",
            "highlights": "Won a 1v5 clutch with amazing aim"
        },
        {
            "game_name": "Minecraft",
            "content_type": "Building Tutorial",
            "highlights": "Built an epic castle with redstone automation"
        },
        {
            "game_name": "Fortnite",
            "content_type": "Victory Royale",
            "highlights": "Won with only 1 HP remaining"
        }
    ]
    
    # Initialize batch generator
    batch_gen = BatchContentGenerator()
    
    # Process batch
    print("Processing batch of clips...")
    results = batch_gen.process_batch(example_clips)
    
    # Save results
    batch_gen.save_results(results)
    
    print("\nBatch processing complete!")

if __name__ == "__main__":
    main()
