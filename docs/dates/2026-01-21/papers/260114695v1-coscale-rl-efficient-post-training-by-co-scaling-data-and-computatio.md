---
layout: default
title: CoScale-RL: Efficient Post-Training by Co-Scaling Data and Computation
---

# CoScale-RL: Efficient Post-Training by Co-Scaling Data and Computation
**arXiv**：[2601.14695v1](https://arxiv.org/abs/2601.14695) · [PDF](https://arxiv.org/pdf/2601.14695.pdf)  
**作者**：Yutong Chen, Jiandong Gao, Ji Wu  

**一句话要点**：提出CoScale-RL以提升大型推理模型的后训练数据与计算效率

**关键词**：后训练缩放, 强化学习稳定化, 模型合并, 数据效率, 计算效率, 大型推理模型

## 3 点简述
- 核心问题：大型推理模型训练不稳定，尤其在难题或弱基础模型上
- 方法要点：通过扩展解决方案和计算rollout，结合Re-distillation模型合并技术
- 实验或效果：在四个基准测试上平均准确率提升3.76倍，无需大量监督微调数据集

## 摘要（原文）

> Training Large Reasoning Model (LRM) is usually unstable and unpredictable, especially on hard problems or weak foundation models. We found that the current post-training scaling strategy can still improve on these cases. We propose CoScale-RL, a novel scaling strategy with better data and computational efficiency. We first scale up solutions to make problems solvable. The core idea is to collect multiple solutions for each problem, rather than simply enlarging the dataset. Then, we scale up rollout computation to stabilize Reinforcement Learning. We further leverage a model merge technique called Re-distillation to sustain or even improve computational efficiency when scaling up. Our method significantly improves data and computational efficiency, with an average 3.76$\times$ accuracy improvement on four benchmarks. CoScale-RL is able to improve an LRM's ability boundary without an extensive SFT dataset. Our method provides a new scaling direction to further improve LRM's reasoning ability.

