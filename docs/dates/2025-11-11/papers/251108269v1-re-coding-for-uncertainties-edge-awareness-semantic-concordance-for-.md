---
layout: default
title: Re-coding for Uncertainties: Edge-awareness Semantic Concordance for Resilient Event-RGB Segmentation
---

# Re-coding for Uncertainties: Edge-awareness Semantic Concordance for Resilient Event-RGB Segmentation
**arXiv**：[2511.08269v1](https://arxiv.org/abs/2511.08269) · [PDF](https://arxiv.org/pdf/2511.08269.pdf)  
**作者**：Nan Bao, Yifan Zhao, Lin Zhu, Jia Li  

**一句话要点**：提出边缘感知语义一致性框架以解决极端条件下事件-RGB分割的异构特征融合问题

**关键词**：事件-RGB分割, 异构特征融合, 边缘感知, 不确定性优化, 极端条件语义分割

## 3 点简述
- 核心问题：极端条件下RGB信息丢失，事件与RGB模态异构导致特征不匹配和优化困难。
- 方法要点：通过边缘感知潜在重编码和不确定性优化，统一异构特征并提升融合鲁棒性。
- 实验或效果：在合成和真实数据集上优于现有方法，mIoU提升2.55%，具有空间遮挡鲁棒性。

## 摘要（原文）

> Semantic segmentation has achieved great success in ideal conditions. However, when facing extreme conditions (e.g., insufficient light, fierce camera motion), most existing methods suffer from significant information loss of RGB, severely damaging segmentation results. Several researches exploit the high-speed and high-dynamic event modality as a complement, but event and RGB are naturally heterogeneous, which leads to feature-level mismatch and inferior optimization of existing multi-modality methods. Different from these researches, we delve into the edge secret of both modalities for resilient fusion and propose a novel Edge-awareness Semantic Concordance framework to unify the multi-modality heterogeneous features with latent edge cues. In this framework, we first propose Edge-awareness Latent Re-coding, which obtains uncertainty indicators while realigning event-RGB features into unified semantic space guided by re-coded distribution, and transfers event-RGB distributions into re-coded features by utilizing a pre-established edge dictionary as clues. We then propose Re-coded Consolidation and Uncertainty Optimization, which utilize re-coded edge features and uncertainty indicators to solve the heterogeneous event-RGB fusion issues under extreme conditions. We establish two synthetic and one real-world event-RGB semantic segmentation datasets for extreme scenario comparisons. Experimental results show that our method outperforms the state-of-the-art by a 2.55% mIoU on our proposed DERS-XS, and possesses superior resilience under spatial occlusion. Our code and datasets are publicly available at https://github.com/iCVTEAM/ESC.

