---
layout: default
title: Rethinking Self-Training Based Cross-Subject Domain Adaptation for SSVEP Classification
---

# Rethinking Self-Training Based Cross-Subject Domain Adaptation for SSVEP Classification
**arXiv**：[2601.21203v1](https://arxiv.org/abs/2601.21203) · [PDF](https://arxiv.org/pdf/2601.21203.pdf)  
**作者**：Weiguang Wang, Yong Liu, Yingjie Gao, Guangyuan Xu  

**一句话要点**：提出基于自训练的跨被试域适应方法，以提升SSVEP分类性能。

**关键词**：稳态视觉诱发电位分类, 跨被试域适应, 自训练, 对抗学习, 对比学习, 脑机接口

## 3 点简述
- 核心问题：SSVEP信号存在被试间变异性，且用户特定标注成本高，限制识别性能。
- 方法要点：设计FBEA策略利用频率信息，构建CSST框架包括PTAL和DEST阶段，并引入TFA-CL模块增强特征判别性。
- 实验或效果：在Benchmark和BETA数据集上验证，在不同信号长度下达到先进性能。

## 摘要（原文）

> Steady-state visually evoked potentials (SSVEP)-based brain-computer interfaces (BCIs) are widely used due to their high signal-to-noise ratio and user-friendliness. Accurate decoding of SSVEP signals is crucial for interpreting user intentions in BCI applications. However, signal variability across subjects and the costly user-specific annotation limit recognition performance. Therefore, we propose a novel cross-subject domain adaptation method built upon the self-training paradigm. Specifically, a Filter-Bank Euclidean Alignment (FBEA) strategy is designed to exploit frequency information from SSVEP filter banks. Then, we propose a Cross-Subject Self-Training (CSST) framework consisting of two stages: Pre-Training with Adversarial Learning (PTAL), which aligns the source and target distributions, and Dual-Ensemble Self-Training (DEST), which refines pseudo-label quality. Moreover, we introduce a Time-Frequency Augmented Contrastive Learning (TFA-CL) module to enhance feature discriminability across multiple augmented views. Extensive experiments on the Benchmark and BETA datasets demonstrate that our approach achieves state-of-the-art performance across varying signal lengths, highlighting its superiority.

