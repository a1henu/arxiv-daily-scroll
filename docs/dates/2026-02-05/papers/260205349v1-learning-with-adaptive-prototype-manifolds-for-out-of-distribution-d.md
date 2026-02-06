---
layout: default
title: Learning with Adaptive Prototype Manifolds for Out-of-Distribution Detection
---

# Learning with Adaptive Prototype Manifolds for Out-of-Distribution Detection
**arXiv**：[2602.05349v1](https://arxiv.org/abs/2602.05349) · [PDF](https://arxiv.org/pdf/2602.05349.pdf)  
**作者**：Ningkang Peng, JiuTao Zhou, Yuhao Zhang, Xiaoqian Peng, Qianfeng Yu, Linjing Qian, Tingyu Lu, Yi Chen, Yanhui Gu  

**一句话要点**：提出APEX框架，通过自适应原型流形和后验感知评分解决分布外检测中的原型碰撞与学习-推断脱节问题。

**关键词**：分布外检测, 自适应原型流形, 后验感知评分, 原型学习, 特征流形优化, 最小描述长度

## 3 点简述
- 核心问题：现有基于原型的方法受限于静态同质性假设和学习-推断脱节，导致原型碰撞和性能受限。
- 方法要点：引入自适应原型流形（APM）自动确定每类最优原型复杂度，以及后验感知OOD评分（PAOS）量化原型质量。
- 实验或效果：在CIFAR-100等基准上验证，APEX达到新的最先进性能，优于现有方法。

## 摘要（原文）

> Out-of-distribution (OOD) detection is a critical task for the safe deployment of machine learning models in the real world. Existing prototype-based representation learning methods have demonstrated exceptional performance. Specifically, we identify two fundamental flaws that universally constrain these methods: the Static Homogeneity Assumption (fixed representational resources for all classes) and the Learning-Inference Disconnect (discarding rich prototype quality knowledge at inference). These flaws fundamentally limit the model's capacity and performance. To address these issues, we propose APEX (Adaptive Prototype for eXtensive OOD Detection), a novel OOD detection framework designed via a Two-Stage Repair process to optimize the learned feature manifold. APEX introduces two key innovations to address these respective flaws: (1) an Adaptive Prototype Manifold (APM), which leverages the Minimum Description Length (MDL) principle to automatically determine the optimal prototype complexity $K_c^*$ for each class, thereby fundamentally resolving prototype collision; and (2) a Posterior-Aware OOD Scoring (PAOS) mechanism, which quantifies prototype quality (cohesion and separation) to bridge the learning-inference disconnect. Comprehensive experiments on benchmarks such as CIFAR-100 validate the superiority of our method, where APEX achieves new state-of-the-art performance.

