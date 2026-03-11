---
layout: default
title: Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers
---

# Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers
**arXiv**：[2603.09453v1](https://arxiv.org/abs/2603.09453) · [PDF](https://arxiv.org/pdf/2603.09453.pdf)  
**作者**：Albus Yizhuo Li, Matthew Wicker  

**一句话要点**：提出变分混合专家路由以在大规模基础模型中实现校准不确定性量化

**关键词**：混合专家模型, 不确定性量化, 变分推断, 基础模型, 路由网络, 校准误差

## 3 点简述
- 核心问题：贝叶斯方法在大规模基础模型中计算开销高，难以实现不确定性量化
- 方法要点：将贝叶斯推理限制在专家选择阶段，使用变分推断或温度参数建模不确定性
- 实验或效果：在噪声下路由稳定性提升38%，校准误差降低94%，额外计算开销小于1%

## 摘要（原文）

> Foundation models are increasingly being deployed in contexts where understanding the uncertainty of their outputs is critical to ensuring responsible deployment. While Bayesian methods offer a principled approach to uncertainty quantification, their computational overhead renders their use impractical for training or inference at foundation model scale. State-of-the-art models achieve parameter counts in the trillions through carefully engineered sparsity including Mixture-of-Experts (MoE) layers. In this work, we demonstrate calibrated uncertainty at scale by introducing Variational Mixture-of-Experts Routing (VMoER), a structured Bayesian approach for modelling uncertainty in MoE layers. VMoER confines Bayesian inference to the expert-selection stage which is typically done by a deterministic routing network. We instantiate VMoER using two inference strategies: amortised variational inference over routing logits and inferring a temperature parameter for stochastic expert selection. Across tested foundation models, VMoER improves routing stability under noise by 38\%, reduces calibration error by 94\%, and increases out-of-distribution AUROC by 12\%, while incurring less than 1\% additional FLOPs. These results suggest VMoER offers a scalable path toward robust and uncertainty-aware foundation models.

