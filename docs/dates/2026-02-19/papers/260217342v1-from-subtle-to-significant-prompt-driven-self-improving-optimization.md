---
layout: default
title: From Subtle to Significant: Prompt-Driven Self-Improving Optimization in Test-Time Graph OOD Detection
---

# From Subtle to Significant: Prompt-Driven Self-Improving Optimization in Test-Time Graph OOD Detection
**arXiv**：[2602.17342v1](https://arxiv.org/abs/2602.17342) · [PDF](https://arxiv.org/pdf/2602.17342.pdf)  
**作者**：Luzhi Wang, Xuanshuo Fu, He Zhang, Chuang Liu, Xiaobao Wang, Hongbo Liu  

**一句话要点**：提出SIGOOD框架，通过提示驱动自优化解决图神经网络测试时分布外检测问题。

**关键词**：图神经网络, 分布外检测, 测试时训练, 自优化, 提示学习, 能量优化

## 3 点简述
- 核心问题：现有图分布外检测方法多为单次推理，无法渐进修正错误预测以增强分布外信号。
- 方法要点：SIGOOD集成自学习与测试时训练，利用提示增强图放大分布外信号，并通过能量偏好优化损失迭代优化提示。
- 实验或效果：在21个真实数据集上验证了SIGOOD的有效性和优越性能。

## 摘要（原文）

> Graph Out-of-Distribution (OOD) detection aims to identify whether a test graph deviates from the distribution of graphs observed during training, which is critical for ensuring the reliability of Graph Neural Networks (GNNs) when deployed in open-world scenarios. Recent advances in graph OOD detection have focused on test-time training techniques that facilitate OOD detection without accessing potential supervisory information (e.g., training data). However, most of these methods employ a one-pass inference paradigm, which prevents them from progressively correcting erroneous predictions to amplify OOD signals. To this end, we propose a \textbf{S}elf-\textbf{I}mproving \textbf{G}raph \textbf{O}ut-\textbf{o}f-\textbf{D}istribution detector (SIGOOD), which is an unsupervised framework that integrates continuous self-learning with test-time training for effective graph OOD detection. Specifically, SIGOOD generates a prompt to construct a prompt-enhanced graph that amplifies potential OOD signals. To optimize prompts, SIGOOD introduces an Energy Preference Optimization (EPO) loss, which leverages energy variations between the original test graph and the prompt-enhanced graph. By iteratively optimizing the prompt by involving it into the detection model in a self-improving loop, the resulting optimal prompt-enhanced graph is ultimately used for OOD detection. Comprehensive evaluations on 21 real-world datasets confirm the effectiveness and outperformance of our SIGOOD method. The code is at https://github.com/Ee1s/SIGOOD.

