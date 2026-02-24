---
layout: default
title: Relational Feature Caching for Accelerating Diffusion Transformers
---

# Relational Feature Caching for Accelerating Diffusion Transformers
**arXiv**：[2602.19506v1](https://arxiv.org/abs/2602.19506) · [PDF](https://arxiv.org/pdf/2602.19506.pdf)  
**作者**：Byunggwan Son, Jeimin Jeon, Jeongwoo Choi, Bumsub Ham  

**一句话要点**：提出关系特征缓存以加速扩散变换器，通过输入-输出关系提升特征预测精度

**关键词**：扩散变换器, 特征缓存, 加速推理, 关系特征估计, 缓存调度

## 3 点简述
- 核心问题：现有基于时间外推的特征缓存方法因输出特征变化幅度不规则导致显著预测误差，影响性能
- 方法要点：引入关系特征估计，利用输入特征预测输出变化幅度，并结合关系缓存调度，基于输入估计误差以选择性执行完整计算
- 实验或效果：在多种扩散变换器模型上广泛实验，RFC显著优于先前方法，提升加速效果

## 摘要（原文）

> Feature caching approaches accelerate diffusion transformers (DiTs) by storing the output features of computationally expensive modules at certain timesteps, and exploiting them for subsequent steps to reduce redundant computations. Recent forecasting-based caching approaches employ temporal extrapolation techniques to approximate the output features with cached ones. Although effective, relying exclusively on temporal extrapolation still suffers from significant prediction errors, leading to performance degradation. Through a detailed analysis, we find that 1) these errors stem from the irregular magnitude of changes in the output features, and 2) an input feature of a module is strongly correlated with the corresponding output. Based on this, we propose relational feature caching (RFC), a novel framework that leverages the input-output relationship to enhance the accuracy of the feature prediction. Specifically, we introduce relational feature estimation (RFE) to estimate the magnitude of changes in the output features from the inputs, enabling more accurate feature predictions. We also present relational cache scheduling (RCS), which estimates the prediction errors using the input features and performs full computations only when the errors are expected to be substantial. Extensive experiments across various DiT models demonstrate that RFC consistently outperforms prior approaches significantly. Project page is available at https://cvlab.yonsei.ac.kr/projects/RFC

