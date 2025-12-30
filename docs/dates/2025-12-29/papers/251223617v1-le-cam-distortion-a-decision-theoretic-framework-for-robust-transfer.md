---
layout: default
title: Le Cam Distortion: A Decision-Theoretic Framework for Robust Transfer Learning
---

# Le Cam Distortion: A Decision-Theoretic Framework for Robust Transfer Learning
**arXiv**：[2512.23617v1](https://arxiv.org/abs/2512.23617) · [PDF](https://arxiv.org/pdf/2512.23617.pdf)  
**作者**：Deniz Akdemir  

**一句话要点**：提出基于Le Cam失真度的决策理论框架，以解决分布偏移中负迁移问题，适用于安全关键领域。

**关键词**：迁移学习, 分布偏移, 决策理论, Le Cam失真度, 安全关键应用, 负迁移

## 3 点简述
- 核心问题：无监督域适应中的特征不变性方法在域信息不等时导致负迁移，可能造成灾难性后果。
- 方法要点：利用Le Cam统计实验理论，通过方向可模拟性替代对称不变性，以Le Cam失真度量化迁移风险上界。
- 实验或效果：在基因组学、图像分类和强化学习实验中，实现高精度、零源效用损失和安全策略迁移。

## 摘要（原文）

> Distribution shift is the defining challenge of real-world machine learning. The dominant paradigm--Unsupervised Domain Adaptation (UDA)--enforces feature invariance, aligning source and target representations via symmetric divergence minimization [Ganin et al., 2016]. We demonstrate that this approach is fundamentally flawed: when domains are unequally informative (e.g., high-quality vs degraded sensors), strict invariance necessitates information destruction, causing "negative transfer" that can be catastrophic in safety-critical applications [Wang et al., 2019].
>   We propose a decision-theoretic framework grounded in Le Cam's theory of statistical experiments [Le Cam, 1986], using constructive approximations to replace symmetric invariance with directional simulability. We introduce Le Cam Distortion, quantified by the Deficiency Distance $δ(E_1, E_2)$, as a rigorous upper bound for transfer risk conditional on simulability. Our framework enables transfer without source degradation by learning a kernel that simulates the target from the source. Across five experiments (genomics, vision, reinforcement learning), Le Cam Distortion achieves: (1) near-perfect frequency estimation in HLA genomics (correlation $r=0.999$, matching classical methods), (2) zero source utility loss in CIFAR-10 image classification (81.2% accuracy preserved vs 34.7% drop for CycleGAN), and (3) safe policy transfer in RL control where invariance-based methods suffer catastrophic collapse. Le Cam Distortion provides the first principled framework for risk-controlled transfer learning in domains where negative transfer is unacceptable: medical imaging, autonomous systems, and precision medicine.

