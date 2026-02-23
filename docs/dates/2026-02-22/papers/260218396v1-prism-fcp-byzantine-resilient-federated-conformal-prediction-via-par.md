---
layout: default
title: PRISM-FCP: Byzantine-Resilient Federated Conformal Prediction via Partial Sharing
---

# PRISM-FCP: Byzantine-Resilient Federated Conformal Prediction via Partial Sharing
**arXiv**：[2602.18396v1](https://arxiv.org/abs/2602.18396) · [PDF](https://arxiv.org/pdf/2602.18396.pdf)  
**作者**：Ehsan Lari, Reza Arablouei, Stefan Werner  

**一句话要点**：提出PRISM-FCP，通过部分共享实现拜占庭鲁棒的联邦保形预测

**关键词**：联邦学习, 保形预测, 拜占庭鲁棒性, 部分参数共享, 不确定性量化

## 3 点简述
- 核心问题：现有方法仅在校准阶段处理对抗行为，训练模型易受中毒更新影响。
- 方法要点：训练时部分共享参数以降低扰动能量，校准时基于距离评分过滤拜占庭贡献。
- 实验效果：在合成数据和UCI数据集上保持名义覆盖保证，减少通信并避免区间膨胀。

## 摘要（原文）

> We propose PRISM-FCP (Partial shaRing and robust calIbration with Statistical Margins for Federated Conformal Prediction), a Byzantine-resilient federated conformal prediction framework that utilizes partial model sharing to improve robustness against Byzantine attacks during both model training and conformal calibration. Existing approaches address adversarial behavior only in the calibration stage, leaving the learned model susceptible to poisoned updates. In contrast, PRISM-FCP mitigates attacks end-to-end. During training, clients partially share updates by transmitting only $M$ of $D$ parameters per round. This attenuates the expected energy of an adversary's perturbation in the aggregated update by a factor of $M/D$, yielding lower mean-square error (MSE) and tighter prediction intervals. During calibration, clients convert nonconformity scores into characterization vectors, compute distance-based maliciousness scores, and downweight or filter suspected Byzantine contributions before estimating the conformal quantile. Extensive experiments on both synthetic data and the UCI Superconductivity dataset demonstrate that PRISM-FCP maintains nominal coverage guarantees under Byzantine attacks while avoiding the interval inflation observed in standard FCP with reduced communication, providing a robust and communication-efficient approach to federated uncertainty quantification.

