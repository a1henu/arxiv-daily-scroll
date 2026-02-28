---
layout: default
title: LUMOS: Democratizing SciML Workflows with L0-Regularized Learning for Unified Feature and Parameter Adaptation
---

# LUMOS: Democratizing SciML Workflows with L0-Regularized Learning for Unified Feature and Parameter Adaptation
**arXiv**：[2602.22537v1](https://arxiv.org/abs/2602.22537) · [PDF](https://arxiv.org/pdf/2602.22537.pdf)  
**作者**：Shouwei Gao, Xu Zheng, Dongsheng Luo, Sheng Di, Wenqian Dong  

**一句话要点**：提出LUMOS框架，基于L0正则化学习统一特征选择与模型剪枝，以降低科学机器学习模型设计门槛。

**关键词**：科学机器学习, L0正则化, 特征选择, 模型剪枝, 端到端框架, 分布式训练

## 3 点简述
- 科学机器学习模型设计依赖先验知识与手动调优，特征选择和模型规模确定困难。
- LUMOS采用半随机门控和重参数化技术，动态选择特征并剪枝冗余参数，减少手动干预。
- 在13个科学机器学习任务中，平均实现71.45%参数减少和6.4倍推理加速，并验证了可扩展性。

## 摘要（原文）

> The rapid growth of scientific machine learning (SciML) has accelerated discovery across diverse domains, yet designing effective SciML models remains a challenging task. In practice, building such models often requires substantial prior knowledge and manual expertise, particularly in determining which input features to use and how large the model should be. We introduce LUMOS, an end-to-end framework based on L0-regularized learning that unifies feature selection and model pruning to democratize SciML model design. By employing semi-stochastic gating and reparameterization techniques, LUMOS dynamically selects informative features and prunes redundant parameters during training, reducing the reliance on manual tuning while maintaining predictive accuracy. We evaluate LUMOS across 13 diverse SciML workloads, including cosmology and molecular sciences, and demonstrate its effectiveness and generalizability. Experiments on 13 SciML models show that LUMOS achieves 71.45% parameter reduction and a 6.4x inference speedup on average. Furthermore, Distributed Data Parallel (DDP) training on up to eight GPUs confirms the scalability of

