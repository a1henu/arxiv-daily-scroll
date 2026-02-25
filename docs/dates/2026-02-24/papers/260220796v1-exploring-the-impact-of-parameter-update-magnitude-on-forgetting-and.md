---
layout: default
title: Exploring the Impact of Parameter Update Magnitude on Forgetting and Generalization of Continual Learning
---

# Exploring the Impact of Parameter Update Magnitude on Forgetting and Generalization of Continual Learning
**arXiv**：[2602.20796v1](https://arxiv.org/abs/2602.20796) · [PDF](https://arxiv.org/pdf/2602.20796.pdf)  
**作者**：JinLi He, Liang Bai, Xian Yang  

**一句话要点**：提出基于参数更新幅度的混合策略以优化持续学习中的遗忘与泛化

**关键词**：持续学习, 参数更新幅度, 遗忘机制, 泛化性能, 混合训练策略

## 3 点简述
- 核心问题：参数更新幅度对持续学习中遗忘机制的理论理解不足
- 方法要点：从参数空间漂移角度形式化遗忘，推导最小化遗忘的最优更新幅度
- 实验或效果：混合策略在深度神经网络实验中优于标准训练方法

## 摘要（原文）

> The magnitude of parameter updates are considered a key factor in continual learning. However, most existing studies focus on designing diverse update strategies, while a theoretical understanding of the underlying mechanisms remains limited. Therefore, we characterize model's forgetting from the perspective of parameter update magnitude and formalize it as knowledge degradation induced by task-specific drift in the parameter space, which has not been fully captured in previous studies due to their assumption of a unified parameter space. By deriving the optimal parameter update magnitude that minimizes forgetting, we unify two representative update paradigms, frozen training and initialized training, within an optimization framework for constrained parameter updates. Our theoretical results further reveals that sequence tasks with small parameter distances exhibit better generalization and less forgetting under frozen training rather than initialized training. These theoretical insights inspire a novel hybrid parameter update strategy that adaptively adjusts update magnitude based on gradient directions. Experiments on deep neural networks demonstrate that this hybrid approach outperforms standard training strategies, providing new theoretical perspectives and practical inspiration for designing efficient and scalable continual learning algorithms.

