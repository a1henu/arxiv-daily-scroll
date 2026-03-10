---
layout: default
title: IMSE: Intrinsic Mixture of Spectral Experts Fine-tuning for Test-Time Adaptation
---

# IMSE: Intrinsic Mixture of Spectral Experts Fine-tuning for Test-Time Adaptation
**arXiv**：[2603.07926v1](https://arxiv.org/abs/2603.07926) · [PDF](https://arxiv.org/pdf/2603.07926.pdf)  
**作者**：Sunghyun Baek, Jaemyung Yu, Seunghee Koh, Minsu Kim, Hyeonseong Jeon, Junmo Kim  

**一句话要点**：提出IMSE方法，通过谱专家混合与多样性最大化，优化测试时适应性能。

**关键词**：测试时适应, 谱分解, 多样性最大化, 域感知检索, 视觉Transformer, 参数高效

## 3 点简述
- 核心问题：测试时适应中，熵最小化易导致特征崩溃，影响模型泛化能力。
- 方法要点：基于SVD分解线性层，仅调整奇异值，并引入专家对齐的多样性损失。
- 实验效果：在TTA和CTTA场景下，显著提升准确率，参数效率高。

## 摘要（原文）

> Test-time adaptation (TTA) has been widely explored to prevent performance degradation when test data differ from the training distribution. However, fully leveraging the rich representations of large pretrained models with minimal parameter updates remains underexplored. In this paper, we propose Intrinsic Mixture of Spectral Experts (IMSE) that leverages the spectral experts inherently embedded in Vision Transformers. We decompose each linear layer via singular value decomposition (SVD) and adapt only the singular values, while keeping the singular vectors fixed. We further identify a key limitation of entropy minimization in TTA: it often induces feature collapse, causing the model to rely on domain-specific features rather than class-discriminative features. To address this, we propose a diversity maximization loss based on expert-input alignment, which encourages diverse utilization of spectral experts during adaptation. In the continual test-time adaptation (CTTA) scenario, beyond preserving pretrained knowledge, it is crucial to retain and reuse knowledge from previously observed domains. We introduce Domain-Aware Spectral Code Retrieval, which estimates input distributions to detect domain shifts, and retrieves adapted singular values for rapid adaptation. Consequently, our method achieves state-of-the-art performance on various distribution-shift benchmarks under the TTA setting. In CTTA and Gradual CTTA, it further improves accuracy by 3.4 percentage points (pp) and 2.4 pp, respectively, while requiring 385 times fewer trainable parameters. Our code is available at https://github.com/baek85/IMSE.

