---
layout: default
title: Rewarding Creativity: A Human-Aligned Generative Reward Model for Reinforcement Learning in Storytelling
---

# Rewarding Creativity: A Human-Aligned Generative Reward Model for Reinforcement Learning in Storytelling
**arXiv**：[2601.07149v1](https://arxiv.org/abs/2601.07149) · [PDF](https://arxiv.org/pdf/2601.07149.pdf)  
**作者**：Zhaoyan Li, Hang Lei, Yujia Wang, Lanbo Liu, Hao Liu, Liang Yu  

**一句话要点**：提出RLCS框架，通过生成奖励模型和熵奖励塑形解决创意故事生成中的奖励信号设计和训练稳定性问题。

**关键词**：创意故事生成, 强化学习, 奖励模型, 熵奖励塑形, 多维度分析, 训练稳定性

## 3 点简述
- 核心问题：LLM生成创意故事时，主观质量评估和RL训练不稳定性是两大挑战。
- 方法要点：开发GenRM进行多维度分析和显式推理，结合熵奖励塑形动态优化学习过程。
- 实验或效果：GenRM与人类创造力判断对齐度达68%，RLCS在故事质量上超越包括Gemini-2.5-Pro在内的基线。

## 摘要（原文）

> While Large Language Models (LLMs) can generate fluent text, producing high-quality creative stories remains challenging. Reinforcement Learning (RL) offers a promising solution but faces two critical obstacles: designing reliable reward signals for subjective storytelling quality and mitigating training instability. This paper introduces the Reinforcement Learning for Creative Storytelling (RLCS) framework to systematically address both challenges. First, we develop a Generative Reward Model (GenRM) that provides multi-dimensional analysis and explicit reasoning about story preferences, trained through supervised fine-tuning on demonstrations with reasoning chains distilled from strong teacher models, followed by GRPO-based refinement on expanded preference data. Second, we introduce an entropy-based reward shaping strategy that dynamically prioritizes learning on confident errors and uncertain correct predictions, preventing overfitting on already-mastered patterns. Experiments demonstrate that GenRM achieves 68\% alignment with human creativity judgments, and RLCS significantly outperforms strong baselines including Gemini-2.5-Pro in overall story quality. This work provides a practical pipeline for applying RL to creative domains, effectively navigating the dual challenges of reward modeling and training stability.

