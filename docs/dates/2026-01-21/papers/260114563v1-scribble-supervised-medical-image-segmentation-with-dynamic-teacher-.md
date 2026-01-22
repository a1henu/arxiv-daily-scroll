---
layout: default
title: Scribble-Supervised Medical Image Segmentation with Dynamic Teacher Switching and Hierarchical Consistency
---

# Scribble-Supervised Medical Image Segmentation with Dynamic Teacher Switching and Hierarchical Consistency
**arXiv**：[2601.14563v1](https://arxiv.org/abs/2601.14563) · [PDF](https://arxiv.org/pdf/2601.14563.pdf)  
**作者**：Thanh-Huy Nguyen, Hoang-Loc Cao, Dat T. Chung, Mai-Anh Vu, Thanh-Minh Nguyen, Minh Le, Phat K. Huynh, Ulas Bagci  

**一句话要点**：提出SDT-Net以解决涂鸦监督医学图像分割中的噪声传播和边界学习问题

**关键词**：涂鸦监督分割, 动态教师切换, 多级一致性, 医学图像分割, 伪标签优化

## 3 点简述
- 核心问题：涂鸦标注稀疏导致伪标签噪声和解剖边界学习困难
- 方法要点：动态教师切换模块自适应选择可靠教师，结合高置信伪标签和多级特征对齐
- 实验或效果：在ACDC和MSCMRseg数据集上实现最先进性能，分割更准确和符合解剖结构

## 摘要（原文）

> Scribble-supervised methods have emerged to mitigate the prohibitive annotation burden in medical image segmentation. However, the inherent sparsity of these annotations introduces significant ambiguity, which results in noisy pseudo-label propagation and hinders the learning of robust anatomical boundaries. To address this challenge, we propose SDT-Net, a novel dual-teacher, single-student framework designed to maximize supervision quality from these weak signals. Our method features a Dynamic Teacher Switching (DTS) module to adaptively select the most reliable teacher. This selected teacher then guides the student via two synergistic mechanisms: high-confidence pseudo-labels, refined by a Pick Reliable Pixels (PRP) mechanism, and multi-level feature alignment, enforced by a Hierarchical Consistency (HiCo) module. Extensive experiments on the ACDC and MSCMRseg datasets demonstrate that SDT-Net achieves state-of-the-art performance, producing more accurate and anatomically plausible segmentation.

