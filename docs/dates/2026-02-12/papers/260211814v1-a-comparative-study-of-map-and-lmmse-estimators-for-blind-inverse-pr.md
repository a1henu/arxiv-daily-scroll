---
layout: default
title: A Comparative Study of MAP and LMMSE Estimators for Blind Inverse Problems
---

# A Comparative Study of MAP and LMMSE Estimators for Blind Inverse Problems
**arXiv**：[2602.11814v1](https://arxiv.org/abs/2602.11814) · [PDF](https://arxiv.org/pdf/2602.11814.pdf)  
**作者**：Nathan Buskulic, Luca Calatroni  

**一句话要点**：比较MAP与LMMSE估计器在盲反问题中的性能，显示LMMSE更稳健且可优化MAP初始化

**关键词**：盲反问题, MAP估计, LMMSE估计, 盲去卷积, 参数调优, 初始化策略

## 3 点简述
- 研究盲反问题中MAP方法因非凸性和非可识别性导致的不稳定性
- 提出LMMSE估计器作为替代方案，在受控二维盲去卷积实验中表现更可靠
- 实验表明LMMSE可作为MAP的有效初始化，提升性能并减少参数敏感性

## 摘要（原文）

> Maximum-a-posteriori (MAP) approaches are an effective framework for inverse problems with known forward operators, particularly when combined with expressive priors and careful parameter selection. In blind settings, however, their use becomes significantly less stable due to the inherent non-convexity of the problem and the potential non-identifiability of the solutions. (Linear) minimum mean square error (MMSE) estimators provide a compelling alternative that can circumvent these limitations. In this work, we study synthetic two-dimensional blind deconvolution problems under fully controlled conditions, with complete prior knowledge of both the signal and kernel distributions. We compare tailored MAP algorithms with simple LMMSE estimators whose functional form is closely related to that of an optimal Tikhonov estimator. Our results show that, even in these highly controlled settings, MAP methods remain unstable and require extensive parameter tuning, whereas the LMMSE estimator yields a robust and reliable baseline. Moreover, we demonstrate empirically that the LMMSE solution can serve as an effective initialization for MAP approaches, improving their performance and reducing sensitivity to regularization parameters, thereby opening the door to future theoretical and practical developments.

