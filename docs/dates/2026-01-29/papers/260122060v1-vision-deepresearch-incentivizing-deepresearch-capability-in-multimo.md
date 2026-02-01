---
layout: default
title: Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models
---

# Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models
**arXiv**：[2601.22060v1](https://arxiv.org/abs/2601.22060) · [PDF](https://arxiv.org/pdf/2601.22060.pdf)  
**作者**：Wenxuan Huang, Yu Zeng, Qiuchen Wang, Zhen Fang, Shaosheng Cao, Zheng Chu, Qingyu Yin, Shuang Chen, Zhenfei Yin, Lin Chen, Zehui Chen, Yao Hu, Philip Torr, Feng Zhao, Wanli Ouyang  

**一句话要点**：提出Vision-DeepResearch以增强多模态大语言模型在噪声环境下的深度研究能力

**关键词**：多模态大语言模型, 深度研究能力, 多尺度视觉搜索, 强化学习训练, 噪声鲁棒性

## 3 点简述
- 核心问题：现有方法在视觉噪声下搜索深度和广度不足，难以处理复杂多源证据问题
- 方法要点：引入多轮、多实体、多尺度视觉与文本搜索范式，通过冷启动监督和强化学习训练
- 实验或效果：在复杂任务上超越现有多模态深度研究模型及基于GPT-5等的工作流

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved remarkable success across a broad range of vision tasks. However, constrained by the capacity of their internal world knowledge, prior work has proposed augmenting MLLMs by ``reasoning-then-tool-call'' for visual and textual search engines to obtain substantial gains on tasks requiring extensive factual information. However, these approaches typically define multimodal search in a naive setting, assuming that a single full-level or entity-level image query and few text query suffices to retrieve the key evidence needed to answer the question, which is unrealistic in real-world scenarios with substantial visual noise. Moreover, they are often limited in the reasoning depth and search breadth, making it difficult to solve complex questions that require aggregating evidence from diverse visual and textual sources. Building on this, we propose Vision-DeepResearch, which proposes one new multimodal deep-research paradigm, i.e., performs multi-turn, multi-entity and multi-scale visual and textual search to robustly hit real-world search engines under heavy noise. Our Vision-DeepResearch supports dozens of reasoning steps and hundreds of engine interactions, while internalizing deep-research capabilities into the MLLM via cold-start supervision and RL training, resulting in a strong end-to-end multimodal deep-research MLLM. It substantially outperforming existing multimodal deep-research MLLMs, and workflows built on strong closed-source foundation model such as GPT-5, Gemini-2.5-pro and Claude-4-Sonnet. The code will be released in https://github.com/Osilly/Vision-DeepResearch.

