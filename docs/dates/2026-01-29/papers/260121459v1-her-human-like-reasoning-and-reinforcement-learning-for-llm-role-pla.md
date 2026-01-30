---
layout: default
title: HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing
---

# HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing
**arXiv**：[2601.21459v1](https://arxiv.org/abs/2601.21459) · [PDF](https://arxiv.org/pdf/2601.21459.pdf)  
**作者**：Chengyu Du, Xintao Wang, Aili Chen, Weiyuan Li, Rui Xu, Junteng Liu, Zishan Huang, Rong Tian, Zijun Sun, Yuhao Li, Liheng Feng, Deming Ding, Pengyu Zhao, Yanghua Xiao  

**一句话要点**：提出HER框架，通过双层思维和强化学习解决LLM角色扮演中的认知模拟问题

**关键词**：LLM角色扮演, 认知模拟, 双层思维, 强化学习, 推理增强数据, 奖励模型

## 3 点简述
- 核心问题：LLM角色扮演中模拟角色内在思维与人类偏好对齐的挑战
- 方法要点：引入双层思维区分角色第一人称与LLM第三人称思维，构建推理增强数据和奖励模型
- 实验或效果：在CoSER基准上提升30.26分，Minimax Role-Play Bench上提升14.97分

## 摘要（原文）

> LLM role-playing, i.e., using LLMs to simulate specific personas, has emerged as a key capability in various applications, such as companionship, content creation, and digital games. While current models effectively capture character tones and knowledge, simulating the inner thoughts behind their behaviors remains a challenge. Towards cognitive simulation in LLM role-play, previous efforts mainly suffer from two deficiencies: data with high-quality reasoning traces, and reliable reward signals aligned with human preferences. In this paper, we propose HER, a unified framework for cognitive-level persona simulation. HER introduces dual-layer thinking, which distinguishes characters' first-person thinking from LLMs' third-person thinking. To bridge these gaps, we curate reasoning-augmented role-playing data via reverse engineering and construct human-aligned principles and reward models. Leveraging these resources, we train \method models based on Qwen3-32B via supervised and reinforcement learning. Extensive experiments validate the effectiveness of our approach. Notably, our models significantly outperform the Qwen3-32B baseline, achieving a 30.26 improvement on the CoSER benchmark and a 14.97 gain on the Minimax Role-Play Bench. Our datasets, principles, and models will be released to facilitate future research.

