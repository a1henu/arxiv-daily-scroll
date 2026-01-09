---
layout: default
title: Sequential Subspace Noise Injection Prevents Accuracy Collapse in Certified Unlearning
---

# Sequential Subspace Noise Injection Prevents Accuracy Collapse in Certified Unlearning
**arXiv**：[2601.05134v1](https://arxiv.org/abs/2601.05134) · [PDF](https://arxiv.org/pdf/2601.05134.pdf)  
**作者**：Polina Dolgova, Sebastian U. Stich  

**一句话要点**：提出顺序子空间噪声调度以解决认证遗忘中的精度崩溃问题

**关键词**：认证遗忘, 差分隐私, 噪声调度, 子空间优化, 模型精度, 成员推理攻击

## 3 点简述
- 基于差分隐私的认证遗忘提供强保证但降低模型精度
- 方法将噪声预算分配到参数空间的正交子空间而非一次性注入
- 实验显示在图像分类基准上显著提升遗忘后精度并保持隐私保证

## 摘要（原文）

> Certified unlearning based on differential privacy offers strong guarantees but remains largely impractical: the noisy fine-tuning approaches proposed so far achieve these guarantees but severely reduce model accuracy. We propose sequential noise scheduling, which distributes the noise budget across orthogonal subspaces of the parameter space, rather than injecting it all at once. This simple modification mitigates the destructive effect of noise while preserving the original certification guarantees. We extend the analysis of noisy fine-tuning to the subspace setting, proving that the same $(\varepsilon,δ)$ privacy budget is retained. Empirical results on image classification benchmarks show that our approach substantially improves accuracy after unlearning while remaining robust to membership inference attacks. These results show that certified unlearning can achieve both rigorous guarantees and practical utility.

