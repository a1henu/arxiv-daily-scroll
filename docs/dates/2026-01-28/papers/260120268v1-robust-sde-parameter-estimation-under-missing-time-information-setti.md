---
layout: default
title: Robust SDE Parameter Estimation Under Missing Time Information Setting
---

# Robust SDE Parameter Estimation Under Missing Time Information Setting
**arXiv**：[2601.20268v1](https://arxiv.org/abs/2601.20268) · [PDF](https://arxiv.org/pdf/2601.20268.pdf)  
**作者**：Long Van Tran, Truyen Tran, Phuoc Nguyen  

**一句话要点**：提出同时恢复时间顺序与估计SDE参数的新框架，以解决缺失时间信息场景下的参数估计问题。

**关键词**：随机微分方程, 参数估计, 时间顺序恢复, 分数匹配, 缺失信息处理

## 3 点简述
- 核心问题：SDE参数估计依赖准确时间戳，当时间顺序信息缺失或损坏时，现有方法失效。
- 方法要点：利用前向与后向过程的不对称性，通过分数匹配推断观测对的时间顺序，再排序恢复总顺序并最大似然估计参数。
- 实验或效果：在合成和真实数据集上验证了方法的有效性，扩展了参数估计至时间顺序缺失的敏感领域。

## 摘要（原文）

> Recent advances in stochastic differential equations (SDEs) have enabled robust modeling of real-world dynamical processes across diverse domains, such as finance, health, and systems biology. However, parameter estimation for SDEs typically relies on accurately timestamped observational sequences. When temporal ordering information is corrupted, missing, or deliberately hidden (e.g., for privacy), existing estimation methods often fail. In this paper, we investigate the conditions under which temporal order can be recovered and introduce a novel framework that simultaneously reconstructs temporal information and estimates SDE parameters. Our approach exploits asymmetries between forward and backward processes, deriving a score-matching criterion to infer the correct temporal order between pairs of observations. We then recover the total order via a sorting procedure and estimate SDE parameters from the reconstructed sequence using maximum likelihood. Finally, we conduct extensive experiments on synthetic and real-world datasets to demonstrate the effectiveness of our method, extending parameter estimation to settings with missing temporal order and broadening applicability in sensitive domains.

