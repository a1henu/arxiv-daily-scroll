---
layout: default
title: Constraint-Rectified Training for Efficient Chain-of-Thought
---

# Constraint-Rectified Training for Efficient Chain-of-Thought
**arXiv**：[2602.12526v1](https://arxiv.org/abs/2602.12526) · [PDF](https://arxiv.org/pdf/2602.12526.pdf)  
**作者**：Qinhang Wu, Sen Lin, Ming Zhang, Yingbin Liang, Ness B. Shroff  

**一句话要点**：提出约束校正训练以优化思维链推理效率

**关键词**：思维链推理, 约束优化, 后训练, 推理效率, 语言冗余, 两阶段训练

## 3 点简述
- 问题：思维链推理过长导致高推理成本与冗余步骤，现有启发式方法不稳定且易精度下降。
- 方法：基于参考引导约束优化的后训练框架，交替最小化推理长度与校正精度，并采用两阶段训练方案。
- 效果：在保持答案质量的同时显著减少令牌使用，提升推理效率并减少语言冗余，支持细粒度控制推理长度。

## 摘要（原文）

> Chain-of-Thought (CoT) has significantly enhanced the reasoning capabilities of Large Language Models (LLMs), especially when combined with reinforcement learning (RL) based post-training methods. While longer reasoning traces can improve answer quality and unlock abilities such as self-correction, they also incur high inference costs and often introduce redundant steps, known as overthinking. Recent research seeks to develop efficient reasoning strategies that balance reasoning length and accuracy, either through length-aware reward design or prompt-based calibration. However, these heuristic-based approaches may suffer from severe accuracy drop and be very sensitive to hyperparameters. To address these problems, we introduce CRT (Constraint-Rectified Training), a principled post-training framework based on reference-guarded constrained optimization, yielding a more stable and interpretable formulation for efficient reasoning. CRT alternates between minimizing reasoning length and rectifying accuracy only when performance falls below the reference, enabling stable and effective pruning of redundant reasoning. We further extend CRT with a two-stage training scheme that first discovers the shortest reliable reasoning patterns and then refines accuracy under a learnt length budget, preventing the re-emergence of verbose CoT. Our comprehensive evaluation shows that this framework consistently reduces token usage while maintaining answer quality at a robust and reliable level. Further analysis reveals that CRT improves reasoning efficiency not only by shortening responses but also by reducing internal language redundancy, leading to a new evaluation metric. Moreover, CRT-based training naturally yields a sequence of intermediate checkpoints that span a spectrum of explanation lengths while preserving correctness, enabling fine-grained control over reasoning verbosity without retraining.

