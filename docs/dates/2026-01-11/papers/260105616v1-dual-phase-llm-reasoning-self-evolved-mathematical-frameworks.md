---
layout: default
title: Dual-Phase LLM Reasoning: Self-Evolved Mathematical Frameworks
---

# Dual-Phase LLM Reasoning: Self-Evolved Mathematical Frameworks
**arXiv**：[2601.05616v1](https://arxiv.org/abs/2601.05616) · [PDF](https://arxiv.org/pdf/2601.05616.pdf)  
**作者**：ShaoZhen Liu, Xinting Huang, Houwen Peng, Xin Chen, Xinyang Song, Qi Li, Zhenan Sun  

**一句话要点**：提出双阶段LLM推理框架，通过自生成长思维链数据增强模型自校正能力，优化数学问题求解。

**关键词**：大型语言模型, 数学推理, 监督微调, 思维链生成, 自校正能力, 难度感知采样

## 3 点简述
- 现有研究依赖强化学习，忽视监督微调在复杂推理任务中的潜力。
- 采用多轮对话策略生成含验证、回溯等元素的思维链数据，结合规则过滤进行监督微调。
- 在GSM8K和MATH500等基准上性能提升，AIME24竞赛级问题表现显著改进。

## 摘要（原文）

> In recent years, large language models (LLMs) have demonstrated significant potential in complex reasoning tasks like mathematical problem-solving. However, existing research predominantly relies on reinforcement learning (RL) frameworks while overlooking supervised fine-tuning (SFT) methods. This paper proposes a new two-stage training framework that enhances models' self-correction capabilities through self-generated long chain-of-thought (CoT) data. During the first stage, a multi-turn dialogue strategy guides the model to generate CoT data incorporating verification, backtracking, subgoal decomposition, and backward reasoning, with predefined rules filtering high-quality samples for supervised fine-tuning. The second stage employs a difficulty-aware rejection sampling mechanism to dynamically optimize data distribution, strengthening the model's ability to handle complex problems. The approach generates reasoning chains extended over 4 times longer while maintaining strong scalability, proving that SFT effectively activates models' intrinsic reasoning capabilities and provides a resource-efficient pathway for complex task optimization. Experimental results demonstrate performance improvements on mathematical benchmarks including GSM8K and MATH500, with the fine-tuned model achieving a substantial improvement on competition-level problems like AIME24. Code will be open-sourced.

