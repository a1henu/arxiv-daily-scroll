---
layout: default
title: Training-Trajectory-Aware Token Selection
---

# Training-Trajectory-Aware Token Selection
**arXiv**：[2601.10348v1](https://arxiv.org/abs/2601.10348) · [PDF](https://arxiv.org/pdf/2601.10348.pdf)  
**作者**：Zhanming Shen, Jiaqi Hu, Zeyu Qin, Hao Chen, Wentao Ye, Zenan Huang, Yihong Zhuang, Guoshan Lu, Junlin Zhou, Junbo Zhao  

**一句话要点**：提出训练轨迹感知的令牌选择方法，以解决前沿蒸馏中性能瓶颈问题。

**关键词**：令牌选择, 蒸馏训练, 训练轨迹, 推理能力, 性能瓶颈, 模型优化

## 3 点简述
- 核心问题：前沿蒸馏中，学生模型已有强推理能力时，持续蒸馏常导致性能下降或增益有限。
- 方法要点：基于训练轨迹分析令牌级机制，选择性地重构训练目标，清除未学习令牌的优化路径。
- 实验或效果：在AR和dLLM设置下，使用少量示例提升模型性能，在多个基准上达到先进水平。

## 摘要（原文）

> Efficient distillation is a key pathway for converting expensive reasoning capability into deployable efficiency, yet in the frontier regime where the student already has strong reasoning ability, naive continual distillation often yields limited gains or even degradation. We observe a characteristic training phenomenon: even as loss decreases monotonically, all performance metrics can drop sharply at almost the same bottleneck, before gradually recovering. We further uncover a token-level mechanism: confidence bifurcates into steadily increasing Imitation-Anchor Tokens that quickly anchor optimization and other yet-to-learn tokens whose confidence is suppressed until after the bottleneck. And the characteristic that these two types of tokens cannot coexist is the root cause of the failure in continual distillation. To this end, we propose Training-Trajectory-Aware Token Selection (T3S) to reconstruct the training objective at the token level, clearing the optimization path for yet-to-learn tokens. T3 yields consistent gains in both AR and dLLM settings: with only hundreds of examples, Qwen3-8B surpasses DeepSeek-R1 on competitive reasoning benchmarks, Qwen3-32B approaches Qwen3-235B, and T3-trained LLaDA-2.0-Mini exceeds its AR baseline, achieving state-of-the-art performance among all of 16B-scale no-think models.

