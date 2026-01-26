---
layout: default
title: Towards a Theoretical Understanding to the Generalization of RLHF
---

# Towards a Theoretical Understanding to the Generalization of RLHF
**arXiv**：[2601.16403v1](https://arxiv.org/abs/2601.16403) · [PDF](https://arxiv.org/pdf/2601.16403.pdf)  
**作者**：Zhaochun Li, Mingyang Yi, Yue Wang, Shisheng Cui, Yong Liu  

**一句话要点**：基于算法稳定性框架，在线性奖励模型下建立RLHF的理论泛化边界

**关键词**：强化学习人类反馈, 泛化理论, 算法稳定性, 线性奖励模型, 大语言模型对齐

## 3 点简述
- 核心问题：RLHF在高维设置下的理论泛化性质未知，需探索其泛化能力
- 方法要点：在线性奖励模型下，通过算法稳定性框架分析端到端学习，证明特征覆盖条件下的泛化界
- 实验或效果：理论结果可推广至梯度上升和随机梯度上升算法，为RLHF的实证泛化提供新理论证据

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) and its variants have emerged as the dominant approaches for aligning Large Language Models with human intent. While empirically effective, the theoretical generalization properties of these methods in high-dimensional settings remain to be explored. To this end, we build the generalization theory on RLHF of LLMs under the linear reward model, through the framework of algorithmic stability. In contrast to the existing works built upon the consistency of maximum likelihood estimations on reward model, our analysis is presented under an end-to-end learning framework, which is consistent with practice. Concretely, we prove that under a key \textbf{feature coverage} condition, the empirical optima of policy model have a generalization bound of order $\mathcal{O}(n^{-\frac{1}{2}})$. Moreover, the results can be extrapolated to parameters obtained by gradient-based learning algorithms, i.e., Gradient Ascent (GA) and Stochastic Gradient Ascent (SGA). Thus, we argue that our results provide new theoretical evidence for the empirically observed generalization of LLMs after RLHF.

