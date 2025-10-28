---
layout: default
title: Residual Diffusion Bridge Model for Image Restoration
---

# Residual Diffusion Bridge Model for Image Restoration
**arXiv**：[2510.23116v1](https://arxiv.org/abs/2510.23116) · [PDF](https://arxiv.org/pdf/2510.23116.pdf)  
**作者**：Hebaixu Wang, Jing Zhang, Haoyang Chen, Haonan Guo, Di Wang, Jiayi Ma, Bo Du  

**一句话要点**：提出残差扩散桥模型以解决图像修复中未退化区域失真问题

**关键词**：图像修复, 扩散桥模型, 残差调制, 随机微分方程, 自适应恢复

## 3 点简述
- 核心问题：现有扩散桥模型缺乏统一分析视角，全局噪声注入导致未退化区域失真。
- 方法要点：理论推导扩散桥随机微分方程，利用残差自适应调制噪声注入与去除。
- 实验或效果：在多种图像修复任务中实现最优性能，代码已公开。

## 摘要（原文）

> Diffusion bridge models establish probabilistic paths between arbitrary
> paired distributions and exhibit great potential for universal image
> restoration. Most existing methods merely treat them as simple variants of
> stochastic interpolants, lacking a unified analytical perspective. Besides,
> they indiscriminately reconstruct images through global noise injection and
> removal, inevitably distorting undegraded regions due to imperfect
> reconstruction. To address these challenges, we propose the Residual Diffusion
> Bridge Model (RDBM). Specifically, we theoretically reformulate the stochastic
> differential equations of generalized diffusion bridge and derive the
> analytical formulas of its forward and reverse processes. Crucially, we
> leverage the residuals from given distributions to modulate the noise injection
> and removal, enabling adaptive restoration of degraded regions while preserving
> intact others. Moreover, we unravel the fundamental mathematical essence of
> existing bridge models, all of which are special cases of RDBM and empirically
> demonstrate the optimality of our proposed models. Extensive experiments are
> conducted to demonstrate the state-of-the-art performance of our method both
> qualitatively and quantitatively across diverse image restoration tasks. Code
> is publicly available at https://github.com/MiliLab/RDBM.

