---
layout: default
title: The Secretary Problem with Predictions and a Chosen Order
---

# The Secretary Problem with Predictions and a Chosen Order
**arXiv**：[2601.07482v1](https://arxiv.org/abs/2601.07482) · [PDF](https://arxiv.org/pdf/2601.07482.pdf)  
**作者**：Helia Karisani, Mohammadreza Daneshvaramoli, Hedyeh Beyhaghi, Mohammad Hajiesmaili, Cameron Musco  

**一句话要点**：提出基于预测与选择顺序的秘书问题算法，提升在线决策的竞争比。

**关键词**：秘书问题, 学习增强算法, 在线决策, 预测误差, 竞争比优化, 随机顺序模型

## 3 点简述
- 研究学习增强型秘书问题，结合机器学习预测与候选者顺序控制。
- 提出随机算法，通过检测预测偏差切换信任策略，平衡一致性与鲁棒性。
- 在随机顺序和选择顺序模型中，分别改进竞争比至0.221和0.262，优于先前方法。

## 摘要（原文）

> We study a learning-augmented variant of the secretary problem, recently introduced by Fujii and Yoshida (2023), in which the decision-maker has access to machine-learned predictions of candidate values. The central challenge is to balance consistency and robustness: when predictions are accurate, the algorithm should select a near-optimal secretary, while under inaccurate predictions it should still guarantee a bounded competitive ratio.
>   We consider both the classical Random Order Secretary Problem (ROSP), where candidates arrive in a uniformly random order, and a more natural learning-augmented model in which the decision-maker may choose the arrival order based on predicted values. We call this model the Chosen Order Secretary Problem (COSP), capturing scenarios such as interview schedules set in advance.
>   We propose a new randomized algorithm applicable to both ROSP and COSP. Our method switches from fully trusting predictions to a threshold-based rule once a large prediction deviation is detected. Let $ε\in [0,1]$ denote the maximum multiplicative prediction error. For ROSP, our algorithm achieves a competitive ratio of $\max\{0.221, (1-ε)/(1+ε)\}$, improving upon the prior bound of $\max\{0.215, (1-ε)/(1+ε)\}$. For COSP, we achieve $\max\{0.262, (1-ε)/(1+ε)\}$, surpassing the $0.25$ worst-case bound for prior approaches and moving closer to the classical secretary benchmark of $1/e \approx 0.368$. These results highlight the benefit of combining predictions with arrival-order control in online decision-making.

