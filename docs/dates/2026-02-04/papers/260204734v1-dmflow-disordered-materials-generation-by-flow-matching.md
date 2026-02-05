---
layout: default
title: DMFlow: Disordered Materials Generation by Flow Matching
---

# DMFlow: Disordered Materials Generation by Flow Matching
**arXiv**：[2602.04734v1](https://arxiv.org/abs/2602.04734) · [PDF](https://arxiv.org/pdf/2602.04734.pdf)  
**作者**：Liming Wu, Rui Jiao, Qi Li, Mingze Li, Songyou Li, Shifeng Jin, Wenbing Huang  

**一句话要点**：提出DMFlow框架，通过流匹配生成无序晶体材料以解决AI材料设计中的空白。

**关键词**：无序材料生成, 流匹配, 图神经网络, 晶体结构预测, 黎曼几何

## 3 点简述
- 核心问题：现有深度生成模型主要关注有序晶体，忽略了无序材料的设计需求。
- 方法要点：引入统一表示和黎曼流匹配，结合图神经网络确保物理有效性。
- 实验效果：在晶体结构预测和新材料生成任务中显著优于现有基准。

## 摘要（原文）

> The design of materials with tailored properties is crucial for technological progress. However, most deep generative models focus exclusively on perfectly ordered crystals, neglecting the important class of disordered materials. To address this gap, we introduce DMFlow, a generative framework specifically designed for disordered crystals. Our approach introduces a unified representation for ordered, Substitutionally Disordered (SD), and Positionally Disordered (PD) crystals, and employs a flow matching model to jointly generate all structural components. A key innovation is a Riemannian flow matching framework with spherical reparameterization, which ensures physically valid disorder weights on the probability simplex. The vector field is learned by a novel Graph Neural Network (GNN) that incorporates physical symmetries and a specialized message-passing scheme. Finally, a two-stage discretization procedure converts the continuous weights into multi-hot atomic assignments. To support research in this area, we release a benchmark containing SD, PD, and mixed structures curated from the Crystallography Open Database. Experiments on Crystal Structure Prediction (CSP) and De Novo Generation (DNG) tasks demonstrate that DMFlow significantly outperforms state-of-the-art baselines adapted from ordered crystal generation. We hope our work provides a foundation for the AI-driven discovery of disordered materials.

