---
layout: default
title: PEPR: Privileged Event-based Predictive Regularization for Domain Generalization
---

# PEPR: Privileged Event-based Predictive Regularization for Domain Generalization
**arXiv**：[2602.04583v1](https://arxiv.org/abs/2602.04583) · [PDF](https://arxiv.org/pdf/2602.04583.pdf)  
**作者**：Gabriele Magrini, Federico Becattini, Niccolò Biondi, Pietro Pala  

**一句话要点**：提出PEPR框架，利用事件相机作为特权信息训练鲁棒RGB模型以解决域泛化问题。

**关键词**：域泛化, 特权学习, 事件相机, 跨模态训练, 预测正则化

## 3 点简述
- 核心问题：深度视觉模型易受域偏移影响，RGB数据语义密集但域依赖性强。
- 方法要点：基于特权学习范式，通过预测事件流潜在特征来正则化RGB编码器，避免直接特征对齐。
- 实验或效果：在目标检测和语义分割任务中，提升日间到夜间等域偏移的鲁棒性，优于对齐基线。

## 摘要（原文）

> Deep neural networks for visual perception are highly susceptible to domain shift, which poses a critical challenge for real-world deployment under conditions that differ from the training data. To address this domain generalization challenge, we propose a cross-modal framework under the learning using privileged information (LUPI) paradigm for training a robust, single-modality RGB model. We leverage event cameras as a source of privileged information, available only during training. The two modalities exhibit complementary characteristics: the RGB stream is semantically dense but domain-dependent, whereas the event stream is sparse yet more domain-invariant. Direct feature alignment between them is therefore suboptimal, as it forces the RGB encoder to mimic the sparse event representation, thereby losing semantic detail. To overcome this, we introduce Privileged Event-based Predictive Regularization (PEPR), which reframes LUPI as a predictive problem in a shared latent space. Instead of enforcing direct cross-modal alignment, we train the RGB encoder with PEPR to predict event-based latent features, distilling robustness without sacrificing semantic richness. The resulting standalone RGB model consistently improves robustness to day-to-night and other domain shifts, outperforming alignment-based baselines across object detection and semantic segmentation.

