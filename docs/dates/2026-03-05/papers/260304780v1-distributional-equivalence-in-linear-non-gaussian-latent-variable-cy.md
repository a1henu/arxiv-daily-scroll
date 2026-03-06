---
layout: default
title: Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning
---

# Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning
**arXiv**：[2603.04780v1](https://arxiv.org/abs/2603.04780) · [PDF](https://arxiv.org/pdf/2603.04780.pdf)  
**作者**：Haoyue Dai, Immanuel Albrecht, Peter Spirtes, Kun Zhang  

**一句话要点**：提出线性非高斯隐变量循环因果模型的分布等价性表征与学习方法

**关键词**：因果发现, 隐变量模型, 分布等价, 线性非高斯, 循环因果, 边秩约束

## 3 点简述
- 核心问题：隐变量因果发现缺乏一般性等价表征，阻碍无结构假设方法设计
- 方法要点：建立任意隐变量结构和循环下分布等价的图准则，引入边秩约束新工具
- 实验或效果：提供遍历等价类过程与数据恢复算法，实现首个无结构假设隐变量发现

## 摘要（原文）

> Causal discovery with latent variables is a fundamental task. Yet most existing methods rely on strong structural assumptions, such as enforcing specific indicator patterns for latents or restricting how they can interact with others. We argue that a core obstacle to a general, structural-assumption-free approach is the lack of an equivalence characterization: without knowing what can be identified, one generally cannot design methods for how to identify it. In this work, we aim to close this gap for linear non-Gaussian models. We establish the graphical criterion for when two graphs with arbitrary latent structure and cycles are distributionally equivalent, that is, they induce the same observed distribution set. Key to our approach is a new tool, edge rank constraints, which fills a missing piece in the toolbox for latent-variable causal discovery in even broader settings. We further provide a procedure to traverse the whole equivalence class and develop an algorithm to recover models from data up to such equivalence. To our knowledge, this is the first equivalence characterization with latent variables in any parametric setting without structural assumptions, and hence the first structural-assumption-free discovery method. Code and an interactive demo are available at https://equiv.cc.

