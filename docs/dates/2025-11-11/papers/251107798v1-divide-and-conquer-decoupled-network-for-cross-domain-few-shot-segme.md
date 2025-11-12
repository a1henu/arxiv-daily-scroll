---
layout: default
title: Divide-and-Conquer Decoupled Network for Cross-Domain Few-Shot Segmentation
---

# Divide-and-Conquer Decoupled Network for Cross-Domain Few-Shot Segmentation
**arXiv**：[2511.07798v1](https://arxiv.org/abs/2511.07798) · [PDF](https://arxiv.org/pdf/2511.07798.pdf)  
**作者**：Runmin Cong, Anpeng Wang, Bin Wan, Cong Zhang, Xiaofei Zhou, Wei Zhang  

**一句话要点**：提出DCDNet以解决跨域少样本分割中的特征纠缠问题

**关键词**：跨域少样本分割, 特征解耦, 对抗学习, 对比学习, 动态特征融合, 跨域适应

## 3 点简述
- 核心问题：编码器特征纠缠域相关和类别相关信息，限制跨域泛化和快速适应
- 方法要点：使用ACFD模块解耦特征，MGDF模块动态融合，CAM模块在微调中调制特征
- 实验或效果：在四个数据集上超越现有方法，实现新的最优性能

## 摘要（原文）

> Cross-domain few-shot segmentation (CD-FSS) aims to tackle the dual challenge of recognizing novel classes and adapting to unseen domains with limited annotations. However, encoder features often entangle domain-relevant and category-relevant information, limiting both generalization and rapid adaptation to new domains. To address this issue, we propose a Divide-and-Conquer Decoupled Network (DCDNet). In the training stage, to tackle feature entanglement that impedes cross-domain generalization and rapid adaptation, we propose the Adversarial-Contrastive Feature Decomposition (ACFD) module. It decouples backbone features into category-relevant private and domain-relevant shared representations via contrastive learning and adversarial learning. Then, to mitigate the potential degradation caused by the disentanglement, the Matrix-Guided Dynamic Fusion (MGDF) module adaptively integrates base, shared, and private features under spatial guidance, maintaining structural coherence. In addition, in the fine-tuning stage, to enhanced model generalization, the Cross-Adaptive Modulation (CAM) module is placed before the MGDF, where shared features guide private features via modulation ensuring effective integration of domain-relevant information. Extensive experiments on four challenging datasets show that DCDNet outperforms existing CD-FSS methods, setting a new state-of-the-art for cross-domain generalization and few-shot adaptation.

