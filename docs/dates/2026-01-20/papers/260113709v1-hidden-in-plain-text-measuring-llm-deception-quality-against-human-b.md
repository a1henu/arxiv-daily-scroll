---
layout: default
title: Hidden in Plain Text: Measuring LLM Deception Quality Against Human Baselines Using Social Deduction Games
---

# Hidden in Plain Text: Measuring LLM Deception Quality Against Human Baselines Using Social Deduction Games
**arXiv**：[2601.13709v1](https://arxiv.org/abs/2601.13709) · [PDF](https://arxiv.org/pdf/2601.13709.pdf)  
**作者**：Christopher Kao, Vanshika Vats, James Davis  

**一句话要点**：提出基于社交推理游戏的异步多智能体框架，评估LLM在自然语言中的欺骗能力

**关键词**：大型语言模型, 社交推理游戏, 欺骗评估, 多智能体模拟, 自然语言处理

## 3 点简述
- 研究LLM在社交推理游戏Mafia中的欺骗能力，以自然语言对话为场景
- 采用异步多智能体框架模拟真实社交环境，使用GPT-4o智能体进行游戏模拟
- 通过GPT-4-Turbo构建Mafia检测器分析游戏文本，预测准确率低于人类基线，表明LLM欺骗更有效

## 摘要（原文）

> Large Language Model (LLM) agents are increasingly used in many applications, raising concerns about their safety. While previous work has shown that LLMs can deceive in controlled tasks, less is known about their ability to deceive using natural language in social contexts. In this paper, we study deception in the Social Deduction Game (SDG) Mafia, where success is dependent on deceiving others through conversation. Unlike previous SDG studies, we use an asynchronous multi-agent framework which better simulates realistic social contexts. We simulate 35 Mafia games with GPT-4o LLM agents. We then create a Mafia Detector using GPT-4-Turbo to analyze game transcripts without player role information to predict the mafia players. We use prediction accuracy as a surrogate marker for deception quality. We compare this prediction accuracy to that of 28 human games and a random baseline. Results show that the Mafia Detector's mafia prediction accuracy is lower on LLM games than on human games. The result is consistent regardless of the game days and the number of mafias detected. This indicates that LLMs blend in better and thus deceive more effectively. We also release a dataset of LLM Mafia transcripts to support future research. Our findings underscore both the sophistication and risks of LLM deception in social contexts.

