---
layout: default
title: EntroCut: Entropy-Guided Adaptive Truncation for Efficient Chain-of-Thought Reasoning in Small-scale Large Reasoning Models
---

# EntroCut: Entropy-Guided Adaptive Truncation for Efficient Chain-of-Thought Reasoning in Small-scale Large Reasoning Models
**arXiv**：[2601.22617v1](https://arxiv.org/abs/2601.22617) · [PDF](https://arxiv.org/pdf/2601.22617.pdf)  
**作者**：Hongxi Yan, Qingjie Liu, Yunhong Wang  

**一句话要点**：提出EntroCut方法，通过熵引导的动态截断提升小规模大推理模型的推理效率

**关键词**：大推理模型, 链式思维推理, 熵引导截断, 训练免费方法, 效率-性能比, 动态推理优化

## 3 点简述
- 大推理模型依赖长链式思维生成，计算成本高，早期推理步骤的熵可区分正确与错误推理
- EntroCut无需训练，动态识别高置信状态以安全终止推理，引入效率-性能比统一评估指标
- 在四个基准测试中，EntroCut最多减少40%令牌使用，精度损失小，效率-性能权衡优于现有方法

## 摘要（原文）

> Large Reasoning Models (LRMs) excel at complex reasoning tasks through extended chain-of-thought generation, but their reliance on lengthy intermediate steps incurs substantial computational cost. We find that the entropy of the model's output distribution in early reasoning steps reliably distinguishes correct from incorrect reasoning. Motivated by this observation, we propose EntroCut, a training-free method that dynamically truncates reasoning by identifying high-confidence states where reasoning can be safely terminated. To comprehensively evaluate the trade-off between efficiency and accuracy, we introduce the Efficiency-Performance Ratio (EPR), a unified metric that quantifies relative token savings per unit accuracy loss. Experiments on four benchmarks show that EntroCut reduces token usage by up to 40\% with minimal accuracy sacrifice, achieving superior efficiency-performance trade-offs compared with existing training-free methods. These results demonstrate that entropy-guided dynamic truncation provides a practical approach to mitigate the inefficiency of LRMs.

