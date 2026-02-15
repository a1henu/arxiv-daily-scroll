---
layout: default
title: Detecting RLVR Training Data via Structural Convergence of Reasoning
---

# Detecting RLVR Training Data via Structural Convergence of Reasoning
**arXiv**：[2602.11792v1](https://arxiv.org/abs/2602.11792) · [PDF](https://arxiv.org/pdf/2602.11792.pdf)  
**作者**：Hongbo Zhang, Yue Yang, Jianhao Yan, Guangsheng Bao, Yue Zhang, Yue Zhang  

**一句话要点**：提出Min-$k$NN距离方法以检测RLVR训练数据，基于推理结构收敛特征

**关键词**：强化学习验证奖励, 训练数据检测, 推理模型, 黑盒检测, 基准污染, 结构收敛

## 3 点简述
- 核心问题：RLVR训练数据未公开，导致基准污染担忧，传统基于似然的检测方法失效
- 方法要点：利用RLVR诱导的推理结构收敛特征，通过采样补全计算最小k近邻编辑距离作为黑盒检测器
- 实验或效果：在多个RLVR训练模型上验证，能可靠区分训练与未见样本，优于现有基线方法

## 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) is central to training modern reasoning models, but the undisclosed training data raises concerns about benchmark contamination. Unlike pretraining methods, which optimize models using token-level probabilities, RLVR fine-tunes models based on reward feedback from self-generated reasoning trajectories, making conventional likelihood-based detection methods less effective. We show that RLVR induces a distinctive behavioral signature: prompts encountered during RLVR training result in more rigid and similar generations, while unseen prompts retain greater diversity. We introduce Min-$k$NN Distance, a simple black-box detector that quantifies this collapse by sampling multiple completions for a given prompt and computing the average of the $k$ smallest nearest-neighbor edit distances. Min-$k$NN Distance requires no access to the reference model or token probabilities. Experiments across multiple RLVR-trained reasoning models show that Min-$k$NN Distance reliably distinguishes RL-seen examples from unseen ones and outperforms existing membership inference and RL contamination detection baselines.

