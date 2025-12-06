---
layout: default
title: Setting up for failure: automatic discovery of the neural mechanisms of cognitive errors
---

# Setting up for failure: automatic discovery of the neural mechanisms of cognitive errors
**arXiv**：[2512.04808v1](https://arxiv.org/abs/2512.04808) · [PDF](https://arxiv.org/pdf/2512.04808.pdf)  
**作者**：Puria Radmard, Paul M. Bays, Máté Lengyel  

**一句话要点**：提出自动化RNN机制发现方法，通过拟合行为数据揭示认知错误神经机制

**关键词**：循环神经网络, 认知错误机制, 行为数据拟合, 扩散模型训练, 视觉工作记忆

## 3 点简述
- 核心问题：传统RNN建模依赖人工迭代，难以自动发现认知错误的神经机制
- 方法要点：使用非参数生成模型生成替代数据，结合扩散模型训练RNN拟合行为分布
- 实验或效果：在视觉工作记忆任务中，RNN动态匹配猕猴神经数据，预测交换错误机制

## 摘要（原文）

> Discovering the neural mechanisms underpinning cognition is one of the grand challenges of neuroscience. However, previous approaches for building models of RNN dynamics that explain behaviour required iterative refinement of architectures and/or optimisation objectives, resulting in a piecemeal, and mostly heuristic, human-in-the-loop process. Here, we offer an alternative approach that automates the discovery of viable RNN mechanisms by explicitly training RNNs to reproduce behaviour, including the same characteristic errors and suboptimalities, that humans and animals produce in a cognitive task. Achieving this required two main innovations. First, as the amount of behavioural data that can be collected in experiments is often too limited to train RNNs, we use a non-parametric generative model of behavioural responses to produce surrogate data for training RNNs. Second, to capture all relevant statistical aspects of the data, we developed a novel diffusion model-based approach for training RNNs. To showcase the potential of our approach, we chose a visual working memory task as our test-bed, as behaviour in this task is well known to produce response distributions that are patently multimodal (due to swap errors). The resulting network dynamics correctly qualitative features of macaque neural data. Importantly, these results were not possible to obtain with more traditional approaches, i.e., when only a limited set of behavioural signatures (rather than the full richness of behavioural response distributions) were fitted, or when RNNs were trained for task optimality (instead of reproducing behaviour). Our approach also yields novel predictions about the mechanism of swap errors, which can be readily tested in experiments. These results suggest that fitting RNNs to rich patterns of behaviour provides a powerful way to automatically discover mechanisms of important cognitive functions.

