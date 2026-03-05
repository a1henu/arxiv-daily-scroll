---
layout: default
title: Data-Aware Random Feature Kernel for Transformers
---

# Data-Aware Random Feature Kernel for Transformers
**arXiv**：[2603.04127v1](https://arxiv.org/abs/2603.04127) · [PDF](https://arxiv.org/pdf/2603.04127.pdf)  
**作者**：Amirhossein Farzam, Hossein Mobahi, Nolan Andrew Miller, Luke Sernau  

**一句话要点**：提出DARKFormer，通过数据对齐核与重要性采样，提升随机特征注意力在预训练模型中的效率与性能。

**关键词**：Transformer注意力, 随机特征核, 重要性采样, 数据对齐核, 预训练模型微调, 线性复杂度注意力

## 3 点简述
- 核心问题：Transformer注意力二次复杂度高，随机特征方法在预训练模型各向异性查询/键下蒙特卡洛方差大。
- 方法要点：数据对齐softmax核，实现可处理的最小方差重要性采样分布，学习随机投影协方差。
- 实验或效果：DARKFormer在微调场景缩小与精确注意力性能差距，提升训练稳定性与资源效率。

## 摘要（原文）

> Transformers excel across domains, yet their quadratic attention complexity poses a barrier to scaling. Random-feature attention, as in Performers, can reduce this cost to linear in the sequence length by approximating the softmax kernel with positive random features drawn from an isotropic distribution. In pretrained models, however, queries and keys are typically anisotropic. This induces high Monte Carlo variance in isotropic sampling schemes unless one retrains the model or uses a large feature budget. Importance sampling can address this by adapting the sampling distribution to the input geometry, but complex data-dependent proposal distributions are often intractable. We show that by data aligning the softmax kernel, we obtain an attention mechanism which can both admit a tractable minimal-variance proposal distribution for importance sampling, and exhibits better training stability. Motivated by this finding, we introduce DARKFormer, a Data-Aware Random-feature Kernel transformer that features a data-aligned kernel geometry. DARKFormer learns the random-projection covariance, efficiently realizing an importance-sampled positive random-feature estimator for its data-aligned kernel. Empirically, DARKFormer narrows the performance gap with exact softmax attention, particularly in finetuning regimes where pretrained representations are anisotropic. By combining random-feature efficiency with data-aware kernels, DARKFormer advances kernel-based attention in resource-constrained settings.

