---
layout: default
title: CORP: Closed-Form One-shot Representation-Preserving Structured Pruning for Vision Transformers
---

# CORP: Closed-Form One-shot Representation-Preserving Structured Pruning for Vision Transformers
**arXiv**：[2602.05243v1](https://arxiv.org/abs/2602.05243) · [PDF](https://arxiv.org/pdf/2602.05243.pdf)  
**作者**：Boxiang Zhang, Baijian Yang  

**一句话要点**：提出CORP以解决Vision Transformers后训练结构化剪枝问题，无需标签或微调。

**关键词**：Vision Transformers, 结构化剪枝, 后训练优化, 闭式解, 表示恢复, 单次剪枝

## 3 点简述
- Vision Transformers计算成本高，结构化剪枝依赖重训练或优化，限制后训练部署。
- CORP通过闭式单次剪枝，建模移除组件为保留组件的仿射函数，补偿权重最小化表示误差。
- 在ImageNet上，CORP对DeiT模型剪枝50%结构，保持高精度，快速完成并提升效率。

## 摘要（原文）

> Vision Transformers achieve strong accuracy but incur high compute and memory cost. Structured pruning can reduce inference cost, but most methods rely on retraining or multi-stage optimization. These requirements limit post-training deployment. We propose \textbf{CORP}, a closed-form one-shot structured pruning framework for Vision Transformers. CORP removes entire MLP hidden dimensions and attention substructures without labels, gradients, or fine-tuning. It operates under strict post-training constraints using only a small unlabeled calibration set. CORP formulates structured pruning as a representation recovery problem. It models removed activations and attention logits as affine functions of retained components and derives closed-form ridge regression solutions that fold compensation into model weights. This minimizes expected representation error under the calibration distribution. Experiments on ImageNet with DeiT models show strong redundancy in MLP and attention representations. Without compensation, one-shot structured pruning causes severe accuracy degradation. With CORP, models preserve accuracy under aggressive sparsity. On DeiT-Huge, CORP retains 82.8\% Top-1 accuracy after pruning 50\% of both MLP and attention structures. CORP completes pruning in under 20 minutes on a single GPU and delivers substantial real-world efficiency gains.

