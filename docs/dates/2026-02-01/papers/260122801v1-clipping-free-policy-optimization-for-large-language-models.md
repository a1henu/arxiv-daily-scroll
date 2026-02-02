---
layout: default
title: Clipping-Free Policy Optimization for Large Language Models
---

# Clipping-Free Policy Optimization for Large Language Models
**arXiv**：[2601.22801v1](https://arxiv.org/abs/2601.22801) · [PDF](https://arxiv.org/pdf/2601.22801.pdf)  
**作者**：Ömer Veysel Çağatan, Barış Akgün, Gözde Gül Şahin, Xuandong Zhao  

**一句话要点**：提出CFPO以解决大语言模型后训练中基于裁剪方法的优化问题

**关键词**：大语言模型, 强化学习, 后训练, 策略优化, 总变差散度, 训练稳定性

## 3 点简述
- 核心问题：基于裁剪的强化学习算法在大规模应用中存在零梯度区域、奖励黑客和训练不稳定等优化问题
- 方法要点：用总变差散度约束导出的凸二次惩罚替代启发式裁剪，实现处处可微的目标函数
- 实验或效果：在推理任务中匹配基准性能并扩展稳定训练范围，在对齐任务中缓解冗长利用并减少能力退化

## 摘要（原文）

> Reinforcement learning has become central to post-training large language models, yet dominant algorithms rely on clipping mechanisms that introduce optimization issues at scale, including zero-gradient regions, reward hacking, and training instability. We propose Clipping-Free Policy Optimization (CFPO), which replaces heuristic clipping with a convex quadratic penalty derived from Total Variation divergence constraints, yielding an everywhere-differentiable objective that enforces stable policy updates without hard boundaries. We evaluate CFPO across both reasoning and alignment settings. In reasoning, CFPO matches clipping-based methods on downstream benchmarks while extending the stable training regime. In alignment, CFPO mitigates verbosity exploitation and reduces capability degradation, while achieving competitive instruction-following performance. CFPO requires only a one-line code change and no additional hyperparameters. Our results suggest that CFPO is a promising drop-in alternative to clipping-based methods for LLM post-training.

