---
layout: default
title: VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning
---

# VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning
**arXiv**：[2603.02795v1](https://arxiv.org/abs/2603.02795) · [PDF](https://arxiv.org/pdf/2603.02795.pdf)  
**作者**：Ruiyang Zhang, Qianguo Sun, Chao Song, Yiyan Qi, Zhedong Zheng  

**一句话要点**：提出VSearcher，通过强化学习将静态多模态模型转变为长时域多模态搜索代理，以解决多模态模型无法实时访问网络信息的问题。

**关键词**：多模态搜索代理, 强化学习, 长时域工具调用, 数据合成, 网络环境交互, 多模态基准评估

## 3 点简述
- 核心问题：多模态大模型依赖静态知识，缺乏实时网络信息访问能力，应用场景受限。
- 方法要点：采用迭代注入数据合成生成高质量多模态QA，结合SFT和RL训练实现多轮工具调用。
- 实验或效果：在MM-SearchExam等基准上评估，VSearcher优于现有代理，部分超越专有模型。

## 摘要（原文）

> Large models are increasingly becoming autonomous agents that interact with real-world environments and use external tools to augment their static capabilities. However, most recent progress has focused on text-only large language models, which are limited to a single modality and therefore have narrower application scenarios. On the other hand, multimodal large models, while offering stronger perceptual capabilities, remain limited to static knowledge and lack the ability to access and leverage up-to-date web information. In this paper, we propose VSearcher, turning static multimodal model into multimodal search agent capable of long-horizon, multi-turn tool use in real-world web environments, including text search, image search, and web browsing, via reinforcement learning. Specifically, we introduce Iterative Injection Data Synthesis pipeline to generate large-scale, complex multimodal QA questions, which are further filtered with comprehensive metrics to ensure high quality and sufficient difficulty. We then adopt an SFT-then-RL training pipeline to turn base multimodal models to agent capable of multi-turn tool calling in real-world web environments. Besides, we propose a multimodal search benchmark MM-SearchExam dedicated to evaluating search capabilities of multimodal search agents, which proves highly challenging for recent proprietary models. Extensive evaluations across multiple multimodal search benchmarks reveal effectiveness of our method. VSearcher achieves superior performance compared to recent multimodal search agents and even surpasses several proprietary models on multimodal web search tasks.

