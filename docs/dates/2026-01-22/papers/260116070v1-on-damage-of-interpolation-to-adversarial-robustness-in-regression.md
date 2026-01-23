---
layout: default
title: On damage of interpolation to adversarial robustness in regression
---

# On damage of interpolation to adversarial robustness in regression
**arXiv**：[2601.16070v1](https://arxiv.org/abs/2601.16070) · [PDF](https://arxiv.org/pdf/2601.16070.pdf)  
**作者**：Jingfu Peng, Yuhong Yang  

**一句话要点**：揭示插值对回归中对抗鲁棒性的损害，提出简单尺寸诅咒现象

**关键词**：对抗鲁棒性, 非参数回归, 插值估计器, 未来X攻击, 简单尺寸诅咒

## 3 点简述
- 研究插值估计器在非参数回归中的对抗鲁棒性，发现其易受未来X攻击影响
- 理论分析表明插值导致次优性能，完美拟合会显著损害鲁棒性
- 数值实验支持理论发现，揭示高插值区域存在简单尺寸诅咒现象

## 摘要（原文）

> Deep neural networks (DNNs) typically involve a large number of parameters and are trained to achieve zero or near-zero training error. Despite such interpolation, they often exhibit strong generalization performance on unseen data, a phenomenon that has motivated extensive theoretical investigations. Comforting results show that interpolation indeed may not affect the minimax rate of convergence under the squared error loss. In the mean time, DNNs are well known to be highly vulnerable to adversarial perturbations in future inputs. A natural question then arises: Can interpolation also escape from suboptimal performance under a future $X$-attack? In this paper, we investigate the adversarial robustness of interpolating estimators in a framework of nonparametric regression. A finding is that interpolating estimators must be suboptimal even under a subtle future $X$-attack, and achieving perfect fitting can substantially damage their robustness. An interesting phenomenon in the high interpolation regime, which we term the curse of simple size, is also revealed and discussed. Numerical experiments support our theoretical findings.

