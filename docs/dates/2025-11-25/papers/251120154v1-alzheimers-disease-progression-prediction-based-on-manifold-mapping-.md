---
layout: default
title: Alzheimers Disease Progression Prediction Based on Manifold Mapping of Irregularly Sampled Longitudinal Data
---

# Alzheimers Disease Progression Prediction Based on Manifold Mapping of Irregularly Sampled Longitudinal Data
**arXiv**：[2511.20154v1](https://arxiv.org/abs/2511.20154) · [PDF](https://arxiv.org/pdf/2511.20154.pdf)  
**作者**：Xin Hong, Ying Shi, Yinhao Li, Yen-Wei Chen  

**一句话要点**：提出R-TNAG框架以解决不规则采样纵向数据中阿尔茨海默病进展预测问题

**关键词**：阿尔茨海默病预测, 不规则采样数据, 黎曼流形学习, 神经ODE, 注意力机制, 纵向数据分析

## 3 点简述
- 核心问题：临床检查不确定性导致纵向成像数据观察间隔不规则，难以建模疾病进展
- 方法要点：通过黎曼流形映射、时间感知神经ODE和注意力门控单元处理不规则间隔
- 实验或效果：在疾病状态预测和认知评分回归中优于现有模型，验证模块互补性和鲁棒性

## 摘要（原文）

> The uncertainty of clinical examinations frequently leads to irregular observation intervals in longitudinal imaging data, posing challenges for modeling disease progression.Most existing imaging-based disease prediction models operate in Euclidean space, which assumes a flat representation of data and fails to fully capture the intrinsic continuity and nonlinear geometric structure of irregularly sampled longitudinal images. To address the challenge of modeling Alzheimers disease (AD) progression from irregularly sampled longitudinal structural Magnetic Resonance Imaging (sMRI) data, we propose a Riemannian manifold mapping, a Time-aware manifold Neural ordinary differential equation, and an Attention-based riemannian Gated recurrent unit (R-TNAG) framework. Our approach first projects features extracted from high-dimensional sMRI into a manifold space to preserve the intrinsic geometry of disease progression. On this representation, a time-aware Neural Ordinary Differential Equation (TNODE) models the continuous evolution of latent states between observations, while an Attention-based Riemannian Gated Recurrent Unit (ARGRU) adaptively integrates historical and current information to handle irregular intervals. This joint design improves temporal consistency and yields robust AD trajectory prediction under irregular sampling.Experimental results demonstrate that the proposed method consistently outperforms state-of-the-art models in both disease status prediction and cognitive score regression. Ablation studies verify the contributions of each module, highlighting their complementary roles in enhancing predictive accuracy. Moreover, the model exhibits stable performance across varying sequence lengths and missing data rates, indicating strong temporal generalizability. Cross-dataset validation further confirms its robustness and applicability in diverse clinical settings.

