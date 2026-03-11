---
layout: default
title: Adaptive Active Learning for Online Reliability Prediction of Satellite Electronics
---

# Adaptive Active Learning for Online Reliability Prediction of Satellite Electronics
**arXiv**：[2603.09058v1](https://arxiv.org/abs/2603.09058) · [PDF](https://arxiv.org/pdf/2603.09058.pdf)  
**作者**：Shixiang Li, Yubin Tian, Dianpeng Wang, Piao Chen, Mengying Ren  

**一句话要点**：提出自适应主动学习框架，用于卫星电子设备在线可靠性预测，以解决数据有限和变异性问题。

**关键词**：可靠性预测, Wiener过程, 主动学习, 卫星电子设备, 退化建模, 空间相关性

## 3 点简述
- 核心问题：卫星电子设备可靠性预测受数据不足、工况变化和单元间差异影响。
- 方法要点：基于Wiener过程的退化模型结合广义Arrhenius函数和空间相关性，并设计两阶段主动学习采样策略。
- 实验或效果：通过数值实验和天宫空间站案例，显著提升预测精度并减少数据需求。

## 摘要（原文）

> Accurate on-orbit reliability prediction for satellite electronics is often hindered by limited data availability, varying operational conditions, and considerable unit-to-unit variability. To overcome these obstacles, this paper proposes a novel integrated online reliability prediction framework. The main contributions are twofold. First, a Wiener process-based degradation model is developed, incorporating a generalized Arrhenius link function, individual random effects, and spatial correlations among adjacent units. A customized maximum likelihood estimation method is further devised to facilitate efficient and accurate parameter inference. Second, a two-stage active learning sampling scheme is designed to adaptively enhance prediction accuracy. This strategy initially selects representative units based on spatial configuration, and subsequently determines optimal sampling times using a comprehensive criterion that balances unit-specific information, model uncertainty, and degradation dynamics. Numerical experiments and a practical case study from the Tiangong space station demonstrate that the proposed method markedly improves reliability prediction accuracy while significantly reducing data requirements, offering an efficient solution for the prognostic and health management of complex satellite electronic systems.

