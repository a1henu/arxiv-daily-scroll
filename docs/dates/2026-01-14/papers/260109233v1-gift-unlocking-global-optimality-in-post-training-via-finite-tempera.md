---
layout: default
title: GIFT: Unlocking Global Optimality in Post-Training via Finite-Temperature Gibbs Initialization
---

# GIFT: Unlocking Global Optimality in Post-Training via Finite-Temperature Gibbs Initialization
**arXiv**：[2601.09233v1](https://arxiv.org/abs/2601.09233) · [PDF](https://arxiv.org/pdf/2601.09233.pdf)  
**作者**：Zhengyang Zhao, Lu Ma, Yizhen Jiang, Xiaochen Ma, Zimo Meng, Chengyu Shen, Lexiang Tang, Haoze Sun, Peng Pei, Wentao Zhang  

**一句话要点**：提出GIFT方法以解决大推理模型后训练中的优化失配问题

**关键词**：后训练优化, 大推理模型, 监督微调, 强化学习, 分布桥梁, 全局最优性

## 3 点简述
- 核心问题：标准SFT导致分布坍缩，限制了后续RL的探索空间
- 方法要点：将监督作为有限温度能量势，建立分布桥梁确保目标一致性
- 实验效果：作为RL初始化显著优于标准SFT及其他基线方法

## 摘要（原文）

> The prevailing post-training paradigm for Large Reasoning Models (LRMs)--Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL)--suffers from an intrinsic optimization mismatch: the rigid supervision inherent in SFT induces distributional collapse, thereby exhausting the exploration space necessary for subsequent RL. In this paper, we reformulate SFT within a unified post-training framework and propose Gibbs Initialization with Finite Temperature (GIFT). We characterize standard SFT as a degenerate zero-temperature limit that suppresses base priors. Conversely, GIFT incorporates supervision as a finite-temperature energy potential, establishing a distributional bridge that ensures objective consistency throughout the post-training pipeline. Our experiments demonstrate that GIFT significantly outperforms standard SFT and other competitive baselines when utilized for RL initialization, providing a mathematically principled pathway toward achieving global optimality in post-training. Our code is available at https://github.com/zzy1127/GIFT.

