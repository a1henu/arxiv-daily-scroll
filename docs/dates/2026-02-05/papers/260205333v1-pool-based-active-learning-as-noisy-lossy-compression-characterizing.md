---
layout: default
title: Pool-based Active Learning as Noisy Lossy Compression: Characterizing Label Complexity via Finite Blocklength Analysis
---

# Pool-based Active Learning as Noisy Lossy Compression: Characterizing Label Complexity via Finite Blocklength Analysis
**arXiv**：[2602.05333v1](https://arxiv.org/abs/2602.05333) · [PDF](https://arxiv.org/pdf/2602.05333.pdf)  
**作者**：Kosuke Sugiyama, Masato Uchida  

**一句话要点**：提出信息论框架分析池式主动学习的理论极限，通过噪声有损压缩建模

**关键词**：池式主动学习, 信息论分析, 噪声有损压缩, 有限块长分析, 标签复杂度, 泛化误差

## 3 点简述
- 核心问题：池式主动学习中数据选择与学习的理论极限分析不足
- 方法要点：将池式主动学习映射为噪声有损压缩问题，应用有限块长分析
- 实验或效果：推导标签复杂度和泛化误差的下界，揭示过拟合和归纳偏差影响

## 摘要（原文）

> This paper proposes an information-theoretic framework for analyzing the theoretical limits of pool-based active learning (AL), in which a subset of instances is selectively labeled. The proposed framework reformulates pool-based AL as a noisy lossy compression problem by mapping pool observations to noisy symbol observations, data selection to compression, and learning to decoding. This correspondence enables a unified information-theoretic analysis of data selection and learning in pool-based AL. Applying finite blocklength analysis of noisy lossy compression, we derive information-theoretic lower bounds on label complexity and generalization error that serve as theoretical limits for a given learning algorithm under its associated optimal data selection strategy. Specifically, our bounds include terms that reflect overfitting induced by the learning algorithm and the discrepancy between its inductive bias and the target task, and are closely related to established information-theoretic bounds and stability theory, which have not been previously applied to the analysis of pool-based AL. These properties yield a new theoretical perspective on pool-based AL.

