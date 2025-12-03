---
layout: default
title: Target-specific Adaptation and Consistent Degradation Alignment for Cross-Domain Remaining Useful Life Prediction
---

# Target-specific Adaptation and Consistent Degradation Alignment for Cross-Domain Remaining Useful Life Prediction
**arXiv**：[2512.02610v1](https://arxiv.org/abs/2512.02610) · [PDF](https://arxiv.org/pdf/2512.02610.pdf)  
**作者**：Yubo Hou, Mohamed Ragab, Min Wu, Chee-Keong Kwoh, Xiaoli Li, Zhenghua Chen  

**一句话要点**：提出TACDA方法以解决跨域剩余使用寿命预测中的目标特定信息缺失和退化阶段不一致问题。

**关键词**：剩余使用寿命预测, 跨域适应, 对抗学习, 退化阶段对齐, 目标域重构

## 3 点简述
- 核心问题：现有对抗域适应方法忽略目标域特定信息和退化阶段一致性，导致跨域RUL预测性能不佳。
- 方法要点：结合目标域重构策略保留目标特定信息，并采用聚类配对策略对齐相似退化阶段。
- 实验或效果：在两种评价指标上超越现有方法，代码已开源。

## 摘要（原文）

> Accurate prediction of the Remaining Useful Life (RUL) in machinery can significantly diminish maintenance costs, enhance equipment up-time, and mitigate adverse outcomes. Data-driven RUL prediction techniques have demonstrated commendable performance. However, their efficacy often relies on the assumption that training and testing data are drawn from the same distribution or domain, which does not hold in real industrial settings. To mitigate this domain discrepancy issue, prior adversarial domain adaptation methods focused on deriving domain-invariant features. Nevertheless, they overlook target-specific information and inconsistency characteristics pertinent to the degradation stages, resulting in suboptimal performance. To tackle these issues, we propose a novel domain adaptation approach for cross-domain RUL prediction named TACDA. Specifically, we propose a target domain reconstruction strategy within the adversarial adaptation process, thereby retaining target-specific information while learning domain-invariant features. Furthermore, we develop a novel clustering and pairing strategy for consistent alignment between similar degradation stages. Through extensive experiments, our results demonstrate the remarkable performance of our proposed TACDA method, surpassing state-of-the-art approaches with regard to two different evaluation metrics. Our code is available at https://github.com/keyplay/TACDA.

