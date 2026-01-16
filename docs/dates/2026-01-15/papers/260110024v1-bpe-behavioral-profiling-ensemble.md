---
layout: default
title: BPE: Behavioral Profiling Ensemble
---

# BPE: Behavioral Profiling Ensemble
**arXiv**：[2601.10024v1](https://arxiv.org/abs/2601.10024) · [PDF](https://arxiv.org/pdf/2601.10024.pdf)  
**作者**：Yanxin Liu, Yunqi Zhang  

**一句话要点**：提出行为画像集成框架以解决传统集成方法忽视模型内在行为差异的问题

**关键词**：集成学习, 行为画像, 动态集成选择, 模型偏差, 预测性能

## 3 点简述
- 传统集成方法如Stacking和动态集成选择主要依赖模型间差异，忽略模型内在行为特性
- BPE为每个模型构建行为画像，基于测试实例响应与画像的偏差计算集成权重
- 在合成和真实数据集上，BPE在预测精度、计算效率和存储资源利用方面优于基线

## 摘要（原文）

> Ensemble learning is widely recognized as a pivotal strategy for pushing the boundaries of predictive performance. Traditional static ensemble methods, such as Stacking, typically assign weights by treating each base learner as a holistic entity, thereby overlooking the fact that individual models exhibit varying degrees of competence across different regions of the instance space. To address this limitation, Dynamic Ensemble Selection (DES) was introduced. However, both static and dynamic approaches predominantly rely on the divergence among different models as the basis for integration. This inter-model perspective neglects the intrinsic characteristics of the models themselves and necessitates a heavy reliance on validation sets for competence estimation. In this paper, we propose the Behavioral Profiling Ensemble (BPE) framework, which introduces a novel paradigm shift. Unlike traditional methods, BPE constructs a ``behavioral profile'' intrinsic to each model and derives integration weights based on the deviation between the model's response to a specific test instance and its established behavioral profile. Extensive experiments on both synthetic and real-world datasets demonstrate that the algorithm derived from the BPE framework achieves significant improvements over state-of-the-art ensemble baselines. These gains are evident not only in predictive accuracy but also in computational efficiency and storage resource utilization across various scenarios.

