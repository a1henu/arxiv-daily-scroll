---
layout: default
title: LAD: Learning Advantage Distribution for Reasoning
---

# LAD: Learning Advantage Distribution for Reasoning
**arXiv**：[2602.20132v1](https://arxiv.org/abs/2602.20132) · [PDF](https://arxiv.org/pdf/2602.20132.pdf)  
**作者**：Wendi Li, Sharon Li  

**一句话要点**：提出学习优势分布框架以解决大模型推理中奖励过拟合与多样性不足问题

**关键词**：强化学习, 大模型推理, 分布匹配, 优势分布, 多样性提升, 无额外训练成本

## 3 点简述
- 核心问题：当前强化学习目标过度关注期望奖励最大化，导致推理轨迹多样性受限和探索不足
- 方法要点：通过分布匹配框架，将优势最大化替换为学习优势诱导分布，避免过拟合且无需额外熵正则化
- 实验或效果：在数学和代码推理任务中，LAD 可靠提升准确性和生成多样性，验证了理论有效性

## 摘要（原文）

> Current reinforcement learning objectives for large-model reasoning primarily focus on maximizing expected rewards. This paradigm can lead to overfitting to dominant reward signals, while neglecting alternative yet valid reasoning trajectories, thereby limiting diversity and exploration. To address this issue, we introduce Learning Advantage Distributions (LAD), a distribution-matching framework that replaces advantage maximization with learning the advantage-induced distribution. By establishing the equivalence between the optimal policy update and an advantage-based target distribution, we derive a practical LAD objective formulated as minimizing an $f$-divergence between the policy-induced and advantage-induced distributions. This yields a gradient update that increases likelihood for high-advantage responses while suppressing over-confident probability growth, preventing collapse without requiring auxiliary entropy regularization. LAD incurs no extra training cost compared to GRPO and scales naturally to LLM post-training. In a controlled bandit setting, LAD faithfully recovers the multimodal advantage distribution, validating the theoretical formulation. Experiments on math and code reasoning tasks across several LLM backbones show that LAD reliably improves both accuracy and generative diversity.

