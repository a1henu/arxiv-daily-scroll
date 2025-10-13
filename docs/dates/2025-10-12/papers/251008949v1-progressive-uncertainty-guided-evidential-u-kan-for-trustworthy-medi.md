---
layout: default
title: Progressive Uncertainty-Guided Evidential U-KAN for Trustworthy Medical Image Segmentation
---

# Progressive Uncertainty-Guided Evidential U-KAN for Trustworthy Medical Image Segmentation
**arXiv**：[2510.08949v1](https://arxiv.org/abs/2510.08949) · [PDF](https://arxiv.org/pdf/2510.08949.pdf)  
**作者**：Zhen Yang, Yansong Ma, Lei Chen  
**一句话要点**：提出Evidential U-KAN以解决可信医学图像分割中边界模糊问题

**关键词**：医学图像分割, 证据深度学习, 不确定性引导, 注意力机制, 语义保持学习

## 3 点简述
- 核心问题：现有证据深度学习方法忽视不确定性图对边界分割的注意力引导
- 方法要点：引入渐进证据不确定性引导注意力和语义保持证据学习策略
- 实验或效果：在4个数据集上验证了准确性和可靠性优于现有方法

## 摘要（原文）

> Trustworthy medical image segmentation aims at deliver accurate and reliable
> results for clinical decision-making. Most existing methods adopt the evidence
> deep learning (EDL) paradigm due to its computational efficiency and
> theoretical robustness. However, the EDL-based methods often neglect leveraging
> uncertainty maps rich in attention cues to refine ambiguous boundary
> segmentation. To address this, we propose a progressive evidence uncertainty
> guided attention (PEUA) mechanism to guide the model to focus on the feature
> representation learning of hard regions. Unlike conventional approaches, PEUA
> progressively refines attention using uncertainty maps while employing low-rank
> learning to denoise attention weights, enhancing feature learning for
> challenging regions. Concurrently, standard EDL methods suppress evidence of
> incorrect class indiscriminately via Kullback-Leibler (KL) regularization,
> impairing the uncertainty assessment in ambiguous areas and consequently
> distorts the corresponding attention guidance. We thus introduce a
> semantic-preserving evidence learning (SAEL) strategy, integrating a
> semantic-smooth evidence generator and a fidelity-enhancing regularization term
> to retain critical semantics. Finally, by embedding PEUA and SAEL with the
> state-of-the-art U-KAN, we proposes Evidential U-KAN, a novel solution for
> trustworthy medical image segmentation. Extensive experiments on 4 datasets
> demonstrate superior accuracy and reliability over the competing methods. The
> code is available at
> \href{https://anonymous.4open.science/r/Evidence-U-KAN-BBE8}{github}.

