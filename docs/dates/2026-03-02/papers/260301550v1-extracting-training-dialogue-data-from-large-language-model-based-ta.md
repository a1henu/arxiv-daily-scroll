---
layout: default
title: Extracting Training Dialogue Data from Large Language Model based Task Bots
---

# Extracting Training Dialogue Data from Large Language Model based Task Bots
**arXiv**：[2603.01550v1](https://arxiv.org/abs/2603.01550) · [PDF](https://arxiv.org/pdf/2603.01550.pdf)  
**作者**：Shuo Zhang, Junzhou Zhao, Junji Hou, Pinghui Wang, Chenxu Wang, Jing Tao  

**一句话要点**：提出针对LLM任务机器人的训练数据提取攻击方法，以解决隐私泄露风险。

**关键词**：大型语言模型, 任务导向对话系统, 数据提取攻击, 隐私保护, 成员推断, 对话状态标签

## 3 点简述
- 核心问题：LLM集成到任务对话系统时，可能记忆训练数据，导致隐私泄露。
- 方法要点：系统评估现有攻击，分析任务对话建模特点，提出增强采样和成员推断的新攻击技术。
- 实验或效果：方法能提取数千训练标签，最佳精度超70%，并分析影响因素和缓解策略。

## 摘要（原文）

> Large Language Models (LLMs) have been widely adopted to enhance Task-Oriented Dialogue Systems (TODS) by modeling complex language patterns and delivering contextually appropriate responses. However, this integration introduces significant privacy risks, as LLMs, functioning as soft knowledge bases that compress extensive training data into rich knowledge representations, can inadvertently memorize training dialogue data containing not only identifiable information such as phone numbers but also entire dialogue-level events like complete travel schedules. Despite the critical nature of this privacy concern, how LLM memorization is inherited in developing task bots remains unexplored. In this work, we address this gap through a systematic quantitative study that involves evaluating existing training data extraction attacks, analyzing key characteristics of task-oriented dialogue modeling that render existing methods ineffective, and proposing novel attack techniques tailored for LLM-based TODS that enhance both response sampling and membership inference. Experimental results demonstrate the effectiveness of our proposed data extraction attack. Our method can extract thousands of training labels of dialogue states with best-case precision exceeding 70%. Furthermore, we provide an in-depth analysis of training data memorization in LLM-based TODS by identifying and quantifying key influencing factors and discussing targeted mitigation strategies.

