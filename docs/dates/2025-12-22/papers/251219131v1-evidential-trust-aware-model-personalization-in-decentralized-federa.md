---
layout: default
title: Evidential Trust-Aware Model Personalization in Decentralized Federated Learning for Wearable IoT
---

# Evidential Trust-Aware Model Personalization in Decentralized Federated Learning for Wearable IoT
**arXiv**：[2512.19131v1](https://arxiv.org/abs/2512.19131) · [PDF](https://arxiv.org/pdf/2512.19131.pdf)  
**作者**：Murtaza Rangwala, Richard O. Sinnott, Rajkumar Buyya  

**一句话要点**：提出Murmura框架，利用证据深度学习实现去中心化联邦学习中信任感知的模型个性化

**关键词**：去中心化联邦学习, 模型个性化, 证据深度学习, 信任感知聚合, 可穿戴物联网

## 3 点简述
- 核心问题：去中心化联邦学习中统计异构性导致节点需个性化模型，但现有方法难以区分不兼容与互补的节点
- 方法要点：基于狄利克雷证据模型，利用认知不确定性评估节点兼容性，实现信任感知的聚合机制
- 实验或效果：在三个可穿戴物联网数据集上验证，相比基线减少非IID性能下降，加速收敛并保持稳定精度

## 摘要（原文）

> Decentralized federated learning (DFL) enables collaborative model training across edge devices without centralized coordination, offering resilience against single points of failure. However, statistical heterogeneity arising from non-identically distributed local data creates a fundamental challenge: nodes must learn personalized models adapted to their local distributions while selectively collaborating with compatible peers. Existing approaches either enforce a single global model that fits no one well, or rely on heuristic peer selection mechanisms that cannot distinguish between peers with genuinely incompatible data distributions and those with valuable complementary knowledge. We present Murmura, a framework that leverages evidential deep learning to enable trust-aware model personalization in DFL. Our key insight is that epistemic uncertainty from Dirichlet-based evidential models directly indicates peer compatibility: high epistemic uncertainty when a peer's model evaluates local data reveals distributional mismatch, enabling nodes to exclude incompatible influence while maintaining personalized models through selective collaboration. Murmura introduces a trust-aware aggregation mechanism that computes peer compatibility scores through cross-evaluation on local validation samples and personalizes model aggregation based on evidential trust with adaptive thresholds. Evaluation on three wearable IoT datasets (UCI HAR, PAMAP2, PPG-DaLiA) demonstrates that Murmura reduces performance degradation from IID to non-IID conditions compared to baseline (0.9% vs. 19.3%), achieves 7.4$\times$ faster convergence, and maintains stable accuracy across hyperparameter choices. These results establish evidential uncertainty as a principled foundation for compatibility-aware personalization in decentralized heterogeneous environments.

