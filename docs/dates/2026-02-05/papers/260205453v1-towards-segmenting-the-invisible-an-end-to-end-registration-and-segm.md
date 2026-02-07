---
layout: default
title: Towards Segmenting the Invisible: An End-to-End Registration and Segmentation Framework for Weakly Supervised Tumour Analysis
---

# Towards Segmenting the Invisible: An End-to-End Registration and Segmentation Framework for Weakly Supervised Tumour Analysis
**arXiv**：[2602.05453v1](https://arxiv.org/abs/2602.05453) · [PDF](https://arxiv.org/pdf/2602.05453.pdf)  
**作者**：Budhaditya Mukhopadhyay, Chirag Mandal, Pavan Tummala, Naghmeh Mahmoodian, Andreas Nürnberger, Soumick Chatterjee  

**一句话要点**：提出混合配准-分割框架，以跨模态弱监督解决肿瘤在CT中不可见的分割挑战。

**关键词**：跨模态弱监督, 图像配准, 肿瘤分割, 医学图像分析, 伪标签生成, 特征缺失问题

## 3 点简述
- 核心问题：肝脏肿瘤在术前MRI可见，但在术中CT中因对比度低而不可见，导致跨模态分割困难。
- 方法要点：结合MSCGUNet进行模态间图像配准和UNet分割模块，通过配准辅助生成CT伪标签。
- 实验或效果：在CHAOS数据集上，健康肝脏分割Dice分数达0.72，但含肿瘤临床数据性能降至0.16，揭示特征缺失的局限性。

## 摘要（原文）

> Liver tumour ablation presents a significant clinical challenge: whilst tumours are clearly visible on pre-operative MRI, they are often effectively invisible on intra-operative CT due to minimal contrast between pathological and healthy tissue. This work investigates the feasibility of cross-modality weak supervision for scenarios where pathology is visible in one modality (MRI) but absent in another (CT). We present a hybrid registration-segmentation framework that combines MSCGUNet for inter-modal image registration with a UNet-based segmentation module, enabling registration-assisted pseudo-label generation for CT images. Our evaluation on the CHAOS dataset demonstrates that the pipeline can successfully register and segment healthy liver anatomy, achieving a Dice score of 0.72. However, when applied to clinical data containing tumours, performance degrades substantially (Dice score of 0.16), revealing the fundamental limitations of current registration methods when the target pathology lacks corresponding visual features in the target modality. We analyse the "domain gap" and "feature absence" problems, demonstrating that whilst spatial propagation of labels via registration is feasible for visible structures, segmenting truly invisible pathology remains an open challenge. Our findings highlight that registration-based label transfer cannot compensate for the absence of discriminative features in the target modality, providing important insights for future research in cross-modality medical image analysis. Code an weights are available at: https://github.com/BudhaTronix/Weakly-Supervised-Tumour-Detection

