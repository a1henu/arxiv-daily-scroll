---
layout: default
title: PersonaDual: Balancing Personalization and Objectivity via Adaptive Reasoning
---

# PersonaDual: Balancing Personalization and Objectivity via Adaptive Reasoning
**arXiv**：[2601.08679v1](https://arxiv.org/abs/2601.08679) · [PDF](https://arxiv.org/pdf/2601.08679.pdf)  
**作者**：Xiaoyou Liu, Xinyi Mou, Shengbin Yue, Liang Wang, Yuqing Wang, Qiexiang Wang, Tianrui Qin, Wangchunshu Zhou, Zhongyu Wei  

**一句话要点**：提出PersonaDual框架，通过自适应推理平衡个性化与客观性，以解决LLMs中个性化信息干扰问题。

**关键词**：个性化推理, 自适应模式切换, 强化学习优化, 客观性保持, LLMs框架

## 3 点简述
- 核心问题：个性化信息可能损害LLMs的客观性和事实正确性，尤其在信息与问题不匹配时。
- 方法要点：训练单一模型支持通用客观推理和个性化推理，基于上下文自适应切换模式，使用SFT和DualGRPO强化学习优化。
- 实验或效果：在客观和个性化基准测试中，减少干扰，实现接近无干扰性能，并利用有益个性化信号提升客观问题解决能力。

## 摘要（原文）

> As users increasingly expect LLMs to align with their preferences, personalized information becomes valuable. However, personalized information can be a double-edged sword: it can improve interaction but may compromise objectivity and factual correctness, especially when it is misaligned with the question. To alleviate this problem, we propose PersonaDual, a framework that supports both general-purpose objective reasoning and personalized reasoning in a single model, and adaptively switches modes based on context. PersonaDual is first trained with SFT to learn two reasoning patterns, and then further optimized via reinforcement learning with our proposed DualGRPO to improve mode selection. Experiments on objective and personalized benchmarks show that PersonaDual preserves the benefits of personalization while reducing interference, achieving near interference-free performance and better leveraging helpful personalized signals to improve objective problem-solving.

