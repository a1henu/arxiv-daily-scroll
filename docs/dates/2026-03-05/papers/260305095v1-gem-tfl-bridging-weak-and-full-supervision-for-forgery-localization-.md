---
layout: default
title: GEM-TFL: Bridging Weak and Full Supervision for Forgery Localization through EM-Guided Decomposition and Temporal Refinement
---

# GEM-TFL: Bridging Weak and Full Supervision for Forgery Localization through EM-Guided Decomposition and Temporal Refinement
**arXiv**：[2603.05095v1](https://arxiv.org/abs/2603.05095) · [PDF](https://arxiv.org/pdf/2603.05095.pdf)  
**作者**：Xiaodong Zhu, Yuanming Zheng, Suting Wang, Junqi Yang, Yuhong Yang, Weiping Tu, Zhongyuan Wang  

**一句话要点**：提出GEM-TFL框架，通过EM引导分解与时间细化，桥接弱监督与全监督以提升伪造定位精度

**关键词**：时间伪造定位, 弱监督学习, EM优化, 图神经网络, 多媒体取证

## 3 点简述
- 核心问题：弱监督时间伪造定位存在训练-推理目标不匹配、二元标签监督有限、梯度阻塞及提案间关系建模缺失。
- 方法要点：采用两阶段分类-回归框架，通过EM优化增强弱监督，引入无训练时间一致性细化，设计基于图的提案细化模块。
- 实验或效果：在基准数据集上验证，GEM-TFL实现更准确鲁棒的伪造定位，显著缩小与全监督方法的差距。

## 摘要（原文）

> Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within videos or audio streams, providing interpretable evidence for multimedia forensics and security. While most existing TFL methods rely on dense frame-level labels in a fully supervised manner, Weakly Supervised TFL (WS-TFL) reduces labeling cost by learning only from binary video-level labels. However, current WS-TFL approaches suffer from mismatched training and inference objectives, limited supervision from binary labels, gradient blockage caused by non-differentiable top-k aggregation, and the absence of explicit modeling of inter-proposal relationships. To address these issues, we propose GEM-TFL (Graph-based EM-powered Temporal Forgery Localization), a two-phase classification-regression framework that effectively bridges the supervision gap between training and inference. Built upon this foundation, (1) we enhance weak supervision by reformulating binary labels into multi-dimensional latent attributes through an EM-based optimization process; (2) we introduce a training-free temporal consistency refinement that realigns frame-level predictions for smoother temporal dynamics; and (3) we design a graph-based proposal refinement module that models temporal-semantic relationships among proposals for globally consistent confidence estimation. Extensive experiments on benchmark datasets demonstrate that GEM-TFL achieves more accurate and robust temporal forgery localization, substantially narrowing the gap with fully supervised methods.

