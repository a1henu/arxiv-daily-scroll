---
layout: default
title: MobileWorldBench: Towards Semantic World Modeling For Mobile Agents
---

# MobileWorldBench: Towards Semantic World Modeling For Mobile Agents
**arXiv**：[2512.14014v1](https://arxiv.org/abs/2512.14014) · [PDF](https://arxiv.org/pdf/2512.14014.pdf)  
**作者**：Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover  

**一句话要点**：提出MobileWorldBench基准与数据集，以自然语言世界模型提升移动GUI代理任务性能

**关键词**：移动GUI代理, 语义世界建模, 视觉语言模型, 自然语言状态转移, 任务规划框架

## 3 点简述
- 核心问题：像素空间世界模型在GUI环境中预测复杂视觉元素困难，限制移动代理性能
- 方法要点：探索自然语言描述状态转移的世界模型，替代像素预测，并集成到代理规划框架
- 实验或效果：发布大规模数据集MobileWorld，提升视觉语言模型世界建模能力，提高任务成功率

## 摘要（原文）

> World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision-language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available at https://github.com/jacklishufan/MobileWorld

