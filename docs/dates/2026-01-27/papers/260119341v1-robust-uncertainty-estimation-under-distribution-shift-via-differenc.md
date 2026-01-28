---
layout: default
title: Robust Uncertainty Estimation under Distribution Shift via Difference Reconstruction
---

# Robust Uncertainty Estimation under Distribution Shift via Difference Reconstruction
**arXiv**：[2601.19341v1](https://arxiv.org/abs/2601.19341) · [PDF](https://arxiv.org/pdf/2601.19341.pdf)  
**作者**：Xinran Xu, Li Rong Wang, Xiuyi Fan  

**一句话要点**：提出差异重建不确定性估计方法，以增强深度学习模型在分布偏移下的可靠性。

**关键词**：不确定性估计, 分布偏移, 重建差异, 深度学习可靠性, 医学影像

## 3 点简述
- 核心问题：现有基于重建差异的不确定性估计方法受信息损失和表面细节敏感性的限制。
- 方法要点：通过重建两个中间层输出并测量其差异作为不确定性分数。
- 实验或效果：在青光眼检测任务中，DRUE在多个分布外数据集上实现更高的AUC和AUPR。

## 摘要（原文）

> Estimating uncertainty in deep learning models is critical for reliable decision-making in high-stakes applications such as medical imaging. Prior research has established that the difference between an input sample and its reconstructed version produced by an auxiliary model can serve as a useful proxy for uncertainty. However, directly comparing reconstructions with the original input is degraded by information loss and sensitivity to superficial details, which limits its effectiveness. In this work, we propose Difference Reconstruction Uncertainty Estimation (DRUE), a method that mitigates this limitation by reconstructing inputs from two intermediate layers and measuring the discrepancy between their outputs as the uncertainty score. To evaluate uncertainty estimation in practice, we follow the widely used out-of-distribution (OOD) detection paradigm, where in-distribution (ID) training data are compared against datasets with increasing domain shift. Using glaucoma detection as the ID task, we demonstrate that DRUE consistently achieves superior AUC and AUPR across multiple OOD datasets, highlighting its robustness and reliability under distribution shift. This work provides a principled and effective framework for enhancing model reliability in uncertain environments.

