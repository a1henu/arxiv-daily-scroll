---
layout: default
title: Grounding and Enhancing Informativeness and Utility in Dataset Distillation
---

# Grounding and Enhancing Informativeness and Utility in Dataset Distillation
**arXiv**：[2601.21296v1](https://arxiv.org/abs/2601.21296) · [PDF](https://arxiv.org/pdf/2601.21296.pdf)  
**作者**：Shaobo Wang, Yantai Yang, Guo Chen, Peiru Li, Kaixin Li, Yufa Zhou, Zhaorun Chen, Linfeng Zhang  

**一句话要点**：提出InfoUtil框架，通过信息性与效用性平衡优化数据集蒸馏性能

**关键词**：数据集蒸馏, 信息性优化, 效用性优化, 博弈论, 梯度范数, 知识蒸馏

## 3 点简述
- 核心问题：数据集蒸馏中原始与合成数据关系未充分探索，需理论指导
- 方法要点：基于信息性与效用性定义最优蒸馏，结合博弈论与梯度范数优化
- 实验或效果：在ImageNet-1K上使用ResNet-18，性能提升6.1%优于先前方法

## 摘要（原文）

> Dataset Distillation (DD) seeks to create a compact dataset from a large, real-world dataset. While recent methods often rely on heuristic approaches to balance efficiency and quality, the fundamental relationship between original and synthetic data remains underexplored. This paper revisits knowledge distillation-based dataset distillation within a solid theoretical framework. We introduce the concepts of Informativeness and Utility, capturing crucial information within a sample and essential samples in the training set, respectively. Building on these principles, we define optimal dataset distillation mathematically. We then present InfoUtil, a framework that balances informativeness and utility in synthesizing the distilled dataset. InfoUtil incorporates two key components: (1) game-theoretic informativeness maximization using Shapley Value attribution to extract key information from samples, and (2) principled utility maximization by selecting globally influential samples based on Gradient Norm. These components ensure that the distilled dataset is both informative and utility-optimized. Experiments demonstrate that our method achieves a 6.1\% performance improvement over the previous state-of-the-art approach on ImageNet-1K dataset using ResNet-18.

