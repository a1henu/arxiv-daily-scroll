---
layout: default
title: Causal Neural Probabilistic Circuits
---

# Causal Neural Probabilistic Circuits
**arXiv**：[2603.01372v1](https://arxiv.org/abs/2603.01372) · [PDF](https://arxiv.org/pdf/2603.01372.pdf)  
**作者**：Weixin Chen, Han Zhao  

**一句话要点**：提出因果神经概率电路以解决概念瓶颈模型中因果依赖忽略的问题

**关键词**：概念瓶颈模型, 因果推理, 概率电路, 干预学习, 可解释人工智能

## 3 点简述
- 概念瓶颈模型支持干预但忽略概念间因果依赖
- 结合神经属性预测器与因果概率电路，支持精确因果推理
- 在五个基准数据集上，相比基线模型，CNPC在不同干预属性数量下实现更高任务准确率

## 摘要（原文）

> Concept Bottleneck Models (CBMs) enhance the interpretability of end-to-end neural networks by introducing a layer of concepts and predicting the class label from the concept predictions. A key property of CBMs is that they support interventions, i.e., domain experts can correct mispredicted concept values at test time to improve the final accuracy. However, typical CBMs apply interventions by overwriting only the corrected concept while leaving other concept predictions unchanged, which ignores causal dependencies among concepts. To address this, we propose the Causal Neural Probabilistic Circuit (CNPC), which combines a neural attribute predictor with a causal probabilistic circuit compiled from a causal graph. This circuit supports exact, tractable causal inference that inherently respects causal dependencies. Under interventions, CNPC models the class distribution based on a Product of Experts (PoE) that fuses the attribute predictor's predictive distribution with the interventional marginals computed by the circuit. We theoretically characterize the compositional interventional error of CNPC w.r.t. its modules and identify conditions under which CNPC closely matches the ground-truth interventional class distribution. Experiments on five benchmark datasets in both in-distribution and out-of-distribution settings show that, compared with five baseline models, CNPC achieves higher task accuracy across different numbers of intervened attributes.

