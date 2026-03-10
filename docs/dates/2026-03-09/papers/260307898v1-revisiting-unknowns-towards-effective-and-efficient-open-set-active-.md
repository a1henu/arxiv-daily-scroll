---
layout: default
title: Revisiting Unknowns: Towards Effective and Efficient Open-Set Active Learning
---

# Revisiting Unknowns: Towards Effective and Efficient Open-Set Active Learning
**arXiv**：[2603.07898v1](https://arxiv.org/abs/2603.07898) · [PDF](https://arxiv.org/pdf/2603.07898.pdf)  
**作者**：Chen-Chen Zong, Yu-Qi Chi, Xie-Yang Wang, Yan Cui, Sheng-Jun Huang  

**一句话要点**：提出E²OAL框架以解决开放集主动学习中未知类样本的有效利用与高效查询问题

**关键词**：开放集主动学习, 未知类识别, 对比学习特征空间, 狄利克雷校准, 两阶段查询策略, 高效标注

## 3 点简述
- 核心问题：开放集主动学习中未知类样本的识别与标注效率低，现有方法依赖独立检测器且忽略未知类监督价值
- 方法要点：通过标签引导聚类和狄利克雷校准辅助头统一建模已知与未知类，结合两阶段查询策略提升精度与效率
- 实验或效果：在多个基准测试中，E²OAL在准确性、效率和查询精度上超越现有方法，代码已开源

## 摘要（原文）

> Open-set active learning (OSAL) aims to identify informative samples for annotation when unlabeled data may contain previously unseen classes-a common challenge in safety-critical and open-world scenarios. Existing approaches typically rely on separately trained open-set detectors, introducing substantial training overhead and overlooking the supervisory value of labeled unknowns for improving known-class learning. In this paper, we propose E$^2$OAL (Effective and Efficient Open-set Active Learning), a unified and detector-free framework that fully exploits labeled unknowns for both stronger supervision and more reliable querying. E$^2$OAL first uncovers the latent class structure of unknowns through label-guided clustering in a frozen contrastively pre-trained feature space, optimized by a structure-aware F1-product objective. To leverage labeled unknowns, it employs a Dirichlet-calibrated auxiliary head that jointly models known and unknown categories, improving both confidence calibration and known-class discrimination. Building on this, a logit-margin purity score estimates the likelihood of known classes to construct a high-purity candidate pool, while an OSAL-specific informativeness metric prioritizes partially ambiguous yet reliable samples. These components together form a flexible two-stage query strategy with adaptive precision control and minimal hyperparameter sensitivity. Extensive experiments across multiple OSAL benchmarks demonstrate that E$^2$OAL consistently surpasses state-of-the-art methods in accuracy, efficiency, and query precision, highlighting its effectiveness and practicality for real-world applications. The code is available at github.com/chenchenzong/E2OAL.

