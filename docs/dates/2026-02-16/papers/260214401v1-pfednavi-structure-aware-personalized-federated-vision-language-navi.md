---
layout: default
title: pFedNavi: Structure-Aware Personalized Federated Vision-Language Navigation for Embodied AI
---

# pFedNavi: Structure-Aware Personalized Federated Vision-Language Navigation for Embodied AI
**arXiv**：[2602.14401v1](https://arxiv.org/abs/2602.14401) · [PDF](https://arxiv.org/pdf/2602.14401.pdf)  
**作者**：Qingqian Yang, Hao Wang, Sai Qian Zhang, Jian Li, Yang Hua, Miao Pan, Tao Song, Zhengwei Qi, Haibing Guan  

**一句话要点**：提出pFedNavi，一种结构感知的个性化联邦学习框架，以解决视觉语言导航中的隐私和异构性问题。

**关键词**：视觉语言导航, 个性化联邦学习, 结构感知, 参数融合, 异构数据, 隐私保护

## 3 点简述
- 核心问题：视觉语言导航需私有室内数据，传统联邦学习在环境与指令异构下性能受限。
- 方法要点：通过层间混合系数自适应识别客户端特定层，进行细粒度参数融合以平衡全局共享与本地专业化。
- 实验或效果：在R2R和RxR基准上，pFedNavi优于FedAvg基线，导航成功率提升达7.5%，收敛速度加快1.38倍。

## 摘要（原文）

> Vision-Language Navigation VLN requires large-scale trajectory instruction data from private indoor environments, raising significant privacy concerns. Federated Learning FL mitigates this by keeping data on-device, but vanilla FL struggles under VLNs' extreme cross-client heterogeneity in environments and instruction styles, making a single global model suboptimal. This paper proposes pFedNavi, a structure-aware and dynamically adaptive personalized federated learning framework tailored for VLN. Our key idea is to personalize where it matters: pFedNavi adaptively identifies client-specific layers via layer-wise mixing coefficients, and performs fine-grained parameter fusion on the selected components (e.g., the encoder-decoder projection and environment-sensitive decoder layers) to balance global knowledge sharing with local specialization. We evaluate pFedNavi on two standard VLN benchmarks, R2R and RxR, using both ResNet and CLIP visual representations. Across all metrics, pFedNavi consistently outperforms the FedAvg-based VLN baseline, achieving up to 7.5% improvement in navigation success rate and up to 7.8% gain in trajectory fidelity, while converging 1.38x faster under non-IID conditions.

