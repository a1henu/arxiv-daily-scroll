---
layout: default
title: SFP: Real-World Scene Recovery Using Spatial and Frequency Priors
---

# SFP: Real-World Scene Recovery Using Spatial and Frequency Priors
**arXiv**：[2512.08254v1](https://arxiv.org/abs/2512.08254) · [PDF](https://arxiv.org/pdf/2512.08254.pdf)  
**作者**：Yun Liu, Tao Li, Cosmin Ancuti, Wenqi Ren, Weisi Lin  

**一句话要点**：提出空间与频率先验方法以解决真实场景恢复中的多重退化问题

**关键词**：场景恢复, 空间先验, 频率先验, 真实世界图像, 退化处理, 加权融合

## 3 点简述
- 核心问题：现有方法依赖单一先验或合成数据训练，难以泛化处理真实场景的多重退化。
- 方法要点：利用空间先验估计透射图恢复散射退化，基于频率先验构建自适应增强掩码。
- 实验或效果：通过加权融合策略整合空间恢复、频率增强和显著特征，在各种退化条件下表现优越。

## 摘要（原文）

> Scene recovery serves as a critical task for various computer vision applications. Existing methods typically rely on a single prior, which is inherently insufficient to handle multiple degradations, or employ complex network architectures trained on synthetic data, which suffer from poor generalization for diverse real-world scenarios. In this paper, we propose Spatial and Frequency Priors (SFP) for real-world scene recovery. In the spatial domain, we observe that the inverse of the degraded image exhibits a projection along its spectral direction that resembles the scene transmission. Leveraging this spatial prior, the transmission map is estimated to recover the scene from scattering degradation. In the frequency domain, a mask is constructed for adaptive frequency enhancement, with two parameters estimated using our proposed novel priors. Specifically, one prior assumes that the mean intensity of the degraded image's direct current (DC) components across three channels in the frequency domain closely approximates that of each channel in the clear image. The second prior is based on the observation that, for clear images, the magnitude of low radial frequencies below 0.001 constitutes approximately 1% of the total spectrum. Finally, we design a weighted fusion strategy to integrate spatial-domain restoration, frequency-domain enhancement, and salient features from the input image, yielding the final recovered result. Extensive evaluations demonstrate the effectiveness and superiority of our proposed SFP for scene recovery under various degradation conditions.

