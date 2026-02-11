---
layout: default
title: Sparse Layer Sharpness-Aware Minimization for Efficient Fine-Tuning
---

# Sparse Layer Sharpness-Aware Minimization for Efficient Fine-Tuning
**arXiv**：[2602.09395v1](https://arxiv.org/abs/2602.09395) · [PDF](https://arxiv.org/pdf/2602.09395.pdf)  
**作者**：Yifei Cheng, Xianglin Yang, Guoxia Wang, Chao Huang, Fei Ma, Dianhai Yu, Xiaochun Cao, Li Shen  

**一句话要点**：提出稀疏层锐度感知最小化方法，以高效微调模型并降低计算成本。

**关键词**：锐度感知最小化, 稀疏技术, 模型微调, 计算效率, 多臂老虎机, 反向传播优化

## 3 点简述
- 核心问题：锐度感知最小化因额外参数扰动步骤导致计算成本加倍，成为实际应用瓶颈。
- 方法要点：将梯度上升和下降步骤的层动态选择建模为多臂老虎机问题，按梯度范数采样部分层参与反向传播。
- 实验效果：在多个任务中性能媲美先进基线，显著减少反向传播中活跃参数比例，验证算法效率。

## 摘要（原文）

> Sharpness-aware minimization (SAM) seeks the minima with a flat loss landscape to improve the generalization performance in machine learning tasks, including fine-tuning. However, its extra parameter perturbation step doubles the computation cost, which becomes the bottleneck of SAM in the practical implementation. In this work, we propose an approach SL-SAM to break this bottleneck by introducing the sparse technique to layers. Our key innovation is to frame the dynamic selection of layers for both the gradient ascent (perturbation) and descent (update) steps as a multi-armed bandit problem. At the beginning of each iteration, SL-SAM samples a part of the layers of the model according to the gradient norm to participate in the backpropagation of the following parameter perturbation and update steps, thereby reducing the computation complexity. We then provide the analysis to guarantee the convergence of SL-SAM. In the experiments of fine-tuning models in several tasks, SL-SAM achieves the performances comparable to the state-of-the-art baselines, including a \#1 rank on LLM fine-tuning. Meanwhile, SL-SAM significantly reduces the ratio of active parameters in backpropagation compared to vanilla SAM (SL-SAM activates 47\%, 22\% and 21\% parameters on the vision, moderate and large language model respectively while vanilla SAM always activates 100\%), verifying the efficiency of our proposed algorithm.

