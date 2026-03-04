---
layout: default
title: TenExp: Mixture-of-Experts-Based Tensor Decomposition Structure Search Framework
---

# TenExp: Mixture-of-Experts-Based Tensor Decomposition Structure Search Framework
**arXiv**：[2603.02720v1](https://arxiv.org/abs/2603.02720) · [PDF](https://arxiv.org/pdf/2603.02720.pdf)  
**作者**：Ting-Wei Zhou, Xi-Le Zhao, Sheng Liu, Wei-Hao Wu, Yu-Bang Zheng, Deyu Meng  

**一句话要点**：提出TenExp框架，基于专家混合动态搜索张量分解结构以捕获数据低秩结构

**关键词**：张量分解, 结构搜索, 专家混合, 低秩结构, 无监督学习

## 3 点简述
- 核心问题：现有张量分解结构搜索方法受限于固定因子交互族，无法实现分解混合
- 方法要点：设计无监督专家混合框架，动态选择和激活合适张量分解，提供单分解和混合分解能力
- 实验或效果：在合成和真实数据集上验证优于现有方法，理论分析提供近似误差界

## 摘要（原文）

> Recently, tensor decompositions continue to emerge and receive increasing attention. Selecting a suitable tensor decomposition to exactly capture the low-rank structures behind the data is at the heart of the tensor decomposition field, which remains a challenging and relatively under-explored problem. Current tensor decomposition structure search methods are still confined by a fixed factor-interaction family (e.g., tensor contraction) and cannot deliver the mixture of decompositions. To address this problem, we elaborately design a mixture-of-experts-based tensor decomposition structure search framework (termed as TenExp), which allows us to dynamically select and activate suitable tensor decompositions in an unsupervised fashion. This framework enjoys two unique advantages over the state-of-the-art tensor decomposition structure search methods. Firstly, TenExp can provide a suitable single decomposition beyond a fixed factor-interaction family. Secondly, TenExp can deliver a suitable mixture of decompositions beyond a single decomposition. Theoretically, we also provide the approximation error bound of TenExp, which reveals the approximation capability of TenExp. Extensive experiments on both synthetic and realistic datasets demonstrate the superiority of the proposed TenExp compared to the state-of-the-art tensor decomposition-based methods.

