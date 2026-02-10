---
layout: default
title: Two-Stage Data Synthesization: A Statistics-Driven Restricted Trade-off between Privacy and Prediction
---

# Two-Stage Data Synthesization: A Statistics-Driven Restricted Trade-off between Privacy and Prediction
**arXiv**：[2602.08657v1](https://arxiv.org/abs/2602.08657) · [PDF](https://arxiv.org/pdf/2602.08657.pdf)  
**作者**：Xiaotong Liu, Shao-Bo Lin, Jun Fan, Ding-Xuan Zhou  

**一句话要点**：提出两阶段数据合成策略，以统计驱动方式平衡隐私保护与预测性能的受限权衡。

**关键词**：数据合成, 隐私保护, 预测性能, 核岭回归, 统计驱动, 两阶段策略

## 3 点简述
- 核心问题：单阶段合成难以平衡隐私扰动需求与预测性能敏感度。
- 方法要点：第一阶段合成-混合生成数据，第二阶段基于核岭回归合成输出。
- 实验或效果：理论数值验证统计驱动受限权衡，应用于营销问题和真实数据集。

## 摘要（原文）

> Synthetic data have gained increasing attention across various domains, with a growing emphasis on their performance in downstream prediction tasks. However, most existing synthesis strategies focus on maintaining statistical information. Although some studies address prediction performance guarantees, their single-stage synthesis designs make it challenging to balance the privacy requirements that necessitate significant perturbations and the prediction performance that is sensitive to such perturbations. We propose a two-stage synthesis strategy. In the first stage, we introduce a synthesis-then-hybrid strategy, which involves a synthesis operation to generate pure synthetic data, followed by a hybrid operation that fuses the synthetic data with the original data. In the second stage, we present a kernel ridge regression (KRR)-based synthesis strategy, where a KRR model is first trained on the original data and then used to generate synthetic outputs based on the synthetic inputs produced in the first stage. By leveraging the theoretical strengths of KRR and the covariant distribution retention achieved in the first stage, our proposed two-stage synthesis strategy enables a statistics-driven restricted privacy--prediction trade-off and guarantee optimal prediction performance. We validate our approach and demonstrate its characteristics of being statistics-driven and restricted in achieving the privacy--prediction trade-off both theoretically and numerically. Additionally, we showcase its generalizability through applications to a marketing problem and five real-world datasets.

