---
layout: default
title: ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization
---

# ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization
**arXiv**：[2602.22948v1](https://arxiv.org/abs/2602.22948) · [PDF](https://arxiv.org/pdf/2602.22948.pdf)  
**作者**：Jiayu Chen, Ruoyu Lin, Zihao Zheng, Jingxin Li, Maoliang Li, Guojie Luo, Xiang chen  

**一句话要点**：提出ToProVAR框架，通过三维熵感知语义分析与稀疏性优化，高效加速视觉自回归模型生成。

**关键词**：视觉自回归模型, 注意力熵分析, 稀疏性优化, 生成加速, 语义保真度, 三维优化

## 3 点简述
- 核心问题：视觉自回归模型在生成后期面临效率瓶颈，传统方法如FastVAR和SkipVAR依赖启发式跳过策略。
- 方法要点：利用注意力熵分析模型架构中不同维度的语义投影，识别参数动态，并基于token、层和尺度三个维度的稀疏性模式设计细粒度优化策略。
- 实验或效果：在Infinity-2B和Infinity-8B模型上实现高达3.4倍加速，同时保持语义保真度和细节，效率和品质均优于传统方法。

## 摘要（原文）

> Visual Autoregressive(VAR) models enhance generation quality but face a critical efficiency bottleneck in later stages. In this paper, we present a novel optimization framework for VAR models that fundamentally differs from prior approaches such as FastVAR and SkipVAR. Instead of relying on heuristic skipping strategies, our method leverages attention entropy to characterize the semantic projections across different dimensions of the model architecture. This enables precise identification of parameter dynamics under varying token granularity levels, semantic scopes, and generation scales. Building on this analysis, we further uncover sparsity patterns along three critical dimensions-token, layer, and scale-and propose a set of fine-grained optimization strategies tailored to these patterns. Extensive evaluation demonstrates that our approach achieves aggressive acceleration of the generation process while significantly preserving semantic fidelity and fine details, outperforming traditional methods in both efficiency and quality. Experiments on Infinity-2B and Infinity-8B models demonstrate that ToProVAR achieves up to 3.4x acceleration with minimal quality loss, effectively mitigating the issues found in prior work. Our code will be made publicly available.

