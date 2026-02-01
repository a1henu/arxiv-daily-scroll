---
layout: default
title: Goal-Driven Adaptive Sampling Strategies for Machine Learning Models Predicting Fields
---

# Goal-Driven Adaptive Sampling Strategies for Machine Learning Models Predicting Fields
**arXiv**：[2601.21832v1](https://arxiv.org/abs/2601.21832) · [PDF](https://arxiv.org/pdf/2601.21832.pdf)  
**作者**：Jigar Parekh, Philipp Bekemeyer  

**一句话要点**：提出目标驱动的自适应采样策略，用于机器学习模型预测场量，以降低计算成本。

**关键词**：主动学习, 场量预测, 自适应采样, 高斯过程, 计算流体动力学, 不确定性传播

## 3 点简述
- 核心问题：主动学习策略在预测场量时缺乏通用方法，难以平衡精度与计算成本。
- 方法要点：结合高斯过程模型，同时减少模型认知误差和标量与场量预测差异，模型架构无关。
- 实验或效果：在NASA通用研究模型上验证，相比无主动学习，以显著更小成本实现高精度。

## 摘要（原文）

> Machine learning models are widely regarded as a way forward to tackle multi-query challenges that arise once expensive black-box simulations such as computational fluid dynamics are investigated. However, ensuring the desired level of accuracy for a certain task at minimal computational cost, e.g. as few black-box samples as possible, remains a challenges. Active learning strategies are used for scalar quantities to overcome this challenges and different so-called infill criteria exists and are commonly employed in several scenarios. Even though needed in various field an extension of active learning strategies towards field predictions is still lacking or limited to very specific scenarios and/or model types. In this paper we propose an active learning strategy for machine learning models that are capable if predicting field which is agnostic to the model architecture itself. For doing so, we combine a well-established Gaussian process model for a scalar reference value and simultaneously aim at reducing the epistemic model error and the difference between scalar and field predictions. Different specific forms of the above-mentioned approach are introduced and compared to each other as well as only scalar-valued based infill. Results are presented for the NASA common research model for an uncertainty propagation task showcasing high level of accuracy at significantly smaller cost compared to an approach without active learning.

