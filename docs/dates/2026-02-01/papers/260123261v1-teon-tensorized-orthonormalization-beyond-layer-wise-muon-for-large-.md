---
layout: default
title: TEON: Tensorized Orthonormalization Beyond Layer-Wise Muon for Large Language Model Pre-Training
---

# TEON: Tensorized Orthonormalization Beyond Layer-Wise Muon for Large Language Model Pre-Training
**arXiv**：[2601.23261v1](https://arxiv.org/abs/2601.23261) · [PDF](https://arxiv.org/pdf/2601.23261.pdf)  
**作者**：Ruijie Zhang, Yequan Zhao, Ziyue Liu, Zhengyang Wang, Dongyang Li, Yupeng Su, Sijia Liu, Zheng Zhang  

**一句话要点**：提出TEON优化器，通过张量化正交化提升大语言模型预训练效率

**关键词**：大语言模型预训练, 优化器设计, 张量正交化, 梯度优化, 收敛性分析

## 3 点简述
- 核心问题：Muon优化器仅层内正交化，可能限制梯度优化效率
- 方法要点：将梯度建模为高阶张量，实现跨层正交化，理论保证收敛性
- 实验或效果：在GPT和LLaMA架构上验证，提升困惑度，鲁棒性强

## 摘要（原文）

> The Muon optimizer has demonstrated strong empirical performance in pre-training large language models by performing matrix-level gradient (or momentum) orthogonalization in each layer independently. In this work, we propose TEON, a principled generalization of Muon that extends orthogonalization beyond individual layers by modeling the gradients of a neural network as a structured higher-order tensor. We present TEON's improved convergence guarantee over layer-wise Muon, and further develop a practical instantiation of TEON based on the theoretical analysis with corresponding ablation. We evaluate our approach on two widely adopted architectures: GPT-style models, ranging from 130M to 774M parameters, and LLaMA-style models, ranging from 60M to 1B parameters. Experimental results show that TEON consistently improves training and validation perplexity across model scales and exhibits strong robustness under various approximate SVD schemes.

