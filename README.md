# Mistral-Pokemon
This is our entry for the [Mistral Finetune hackathon] (https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://mistral.ai/news/2024-ft-hackathon/)

# Goal

We want to build an agent based on Mistral Small to play [online pokemon battle](https://play.pokemonshowdown.com/), with random pokemon of fifth-generation (because it's the best one)

This repo contains code for up until the creation of the agent, the integration with pkm-showdown API will come later!

## File description

- scrape_dataset.py --> scrape all the replays from pokemon showdown
- format_dataset.ipynb --> it parse the replays in a way that is more LLM-friendly
- finetune.ipynb --> where the magic happens 

## Getting the environment set up

todo
