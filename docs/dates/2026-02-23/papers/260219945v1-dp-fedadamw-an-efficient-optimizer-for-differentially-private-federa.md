---
layout: default
title: DP-FedAdamW: An Efficient Optimizer for Differentially Private Federated Large Models
---

# DP-FedAdamW: An Efficient Optimizer for Differentially Private Federated Large Models
**arXiv**：[2602.19945v1](https://arxiv.org/abs/2602.19945) · [PDF](https://arxiv.org/pdf/2602.19945.pdf)  
**作者**：Jin Liu, Yinbin Miao, Ning Xi, Junkang Liu  

**一句话要点**：提出DP-FedAdamW以解决差分隐私联邦学习中AdamW优化器的效率与鲁棒性问题

**关键词**：差分隐私联邦学习, AdamW优化器, 二阶矩估计, 客户端漂移, 收敛加速, Transformer模型

## 3 点简述
- 核心问题：差分隐私联邦学习中，AdamW因数据异质性和隐私噪声导致二阶矩估计方差大、偏差大，并加剧客户端漂移
- 方法要点：通过稳定二阶矩方差、消除差分隐私偏差和对齐本地更新，恢复AdamW在差分隐私下的性能
- 实验或效果：在语言和视觉Transformer及ResNet-18上验证，Tiny-ImageNet上Swin-Base模型在ε=1时优于SOTA 5.83%

## 摘要（原文）

> Balancing convergence efficiency and robustness under Differential Privacy (DP) is a central challenge in Federated Learning (FL). While AdamW accelerates training and fine-tuning in large-scale models, we find that directly applying it to Differentially Private FL (DPFL) suffers from three major issues: (i) data heterogeneity and privacy noise jointly amplify the variance of second-moment estimator, (ii) DP perturbations bias the second-moment estimator, and (iii) DP amplify AdamW sensitivity to local overfitting, worsening client drift. We propose DP-FedAdamW, the first AdamW-based optimizer for DPFL. It restores AdamW under DP by stabilizing second-moment variance, removing DP-induced bias, and aligning local updates to the global descent to curb client drift. Theoretically, we establish an unbiased second-moment estimator and prove a linearly accelerated convergence rate without any heterogeneity assumption, while providing tighter $(\varepsilon,δ)$-DP guarantees. Our empirical results demonstrate the effectiveness of DP-FedAdamW across language and vision Transformers and ResNet-18. On Tiny-ImageNet (Swin-Base, $\varepsilon=1$), DP-FedAdamW outperforms the state-of-the-art (SOTA) by 5.83\%. The code is available in Appendix.

