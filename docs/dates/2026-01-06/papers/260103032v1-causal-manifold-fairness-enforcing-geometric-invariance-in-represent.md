---
layout: default
title: Causal Manifold Fairness: Enforcing Geometric Invariance in Representation Learning
---

# Causal Manifold Fairness: Enforcing Geometric Invariance in Representation Learning
**arXiv**：[2601.03032v1](https://arxiv.org/abs/2601.03032) · [PDF](https://arxiv.org/pdf/2601.03032.pdf)  
**作者**：Vidhi Rathore  

**一句话要点**：提出因果流形公平性框架，通过几何不变性解决机器学习公平性问题

**关键词**：因果推理, 几何深度学习, 公平性学习, 流形学习, 表示学习

## 3 点简述
- 核心问题：传统公平性方法忽略敏感属性对数据流形几何结构的因果扭曲
- 方法要点：结合因果推理与几何深度学习，强制解码器的雅可比和海森矩阵约束以保持局部黎曼几何不变
- 实验或效果：在合成结构因果模型上验证，有效解耦几何扭曲并平衡公平性与任务效用

## 摘要（原文）

> Fairness in machine learning is increasingly critical, yet standard approaches often treat data as static points in a high-dimensional space, ignoring the underlying generative structure. We posit that sensitive attributes (e.g., race, gender) do not merely shift data distributions but causally warp the geometry of the data manifold itself. To address this, we introduce Causal Manifold Fairness (CMF), a novel framework that bridges causal inference and geometric deep learning. CMF learns a latent representation where the local Riemannian geometry, defined by the metric tensor and curvature, remains invariant under counterfactual interventions on sensitive attributes. By enforcing constraints on the Jacobian and Hessian of the decoder, CMF ensures that the rules of the latent space (distances and shapes) are preserved across demographic groups. We validate CMF on synthetic Structural Causal Models (SCMs), demonstrating that it effectively disentangles sensitive geometric warping while preserving task utility, offering a rigorous quantification of the fairness-utility trade-off via geometric metrics.

