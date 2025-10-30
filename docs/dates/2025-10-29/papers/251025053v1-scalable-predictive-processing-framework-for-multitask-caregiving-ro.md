---
layout: default
title: Scalable predictive processing framework for multitask caregiving robots
---

# Scalable predictive processing framework for multitask caregiving robots
**arXiv**：[2510.25053v1](https://arxiv.org/abs/2510.25053) · [PDF](https://arxiv.org/pdf/2510.25053.pdf)  
**作者**：Hayato Idei, Tamon Miyake, Tetsuya Ogata, Yuichi Yamashita  

**一句话要点**：提出基于预测处理的分层多模态RNN，用于多任务护理机器人

**关键词**：预测处理, 多模态学习, 分层RNN, 护理机器人, 自由能原理

## 3 点简述
- 现有护理机器人任务特定且依赖手工预处理，泛化能力受限
- 模型整合高维视触觉输入，无需降维或任务特定特征工程
- 在模拟中展示分层动态自组织、鲁棒性和非对称干扰学习

## 摘要（原文）

> The rapid aging of societies is intensifying demand for autonomous care
> robots; however, most existing systems are task-specific and rely on
> handcrafted preprocessing, limiting their ability to generalize across diverse
> scenarios. A prevailing theory in cognitive neuroscience proposes that the
> human brain operates through hierarchical predictive processing, which
> underlies flexible cognition and behavior by integrating multimodal sensory
> signals. Inspired by this principle, we introduce a hierarchical multimodal
> recurrent neural network grounded in predictive processing under the
> free-energy principle, capable of directly integrating over 30,000-dimensional
> visuo-proprioceptive inputs without dimensionality reduction. The model was
> able to learn two representative caregiving tasks, rigid-body repositioning and
> flexible-towel wiping, without task-specific feature engineering. We
> demonstrate three key properties: (i) self-organization of hierarchical latent
> dynamics that regulate task transitions, capture variability in uncertainty,
> and infer occluded states; (ii) robustness to degraded vision through
> visuo-proprioceptive integration; and (iii) asymmetric interference in
> multitask learning, where the more variable wiping task had little influence on
> repositioning, whereas learning the repositioning task led to a modest
> reduction in wiping performance, while the model maintained overall robustness.
> Although the evaluation was limited to simulation, these results establish
> predictive processing as a universal and scalable computational principle,
> pointing toward robust, flexible, and autonomous caregiving robots while
> offering theoretical insight into the human brain's ability to achieve flexible
> adaptation in uncertain real-world environments.

