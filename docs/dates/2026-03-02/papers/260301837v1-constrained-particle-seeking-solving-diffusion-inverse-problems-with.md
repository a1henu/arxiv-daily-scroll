---
layout: default
title: Constrained Particle Seeking: Solving Diffusion Inverse Problems with Just Forward Passes
---

# Constrained Particle Seeking: Solving Diffusion Inverse Problems with Just Forward Passes
**arXiv**：[2603.01837v1](https://arxiv.org/abs/2603.01837) · [PDF](https://arxiv.org/pdf/2603.01837.pdf)  
**作者**：Hongkun Dou, Zike Chen, Zeyu Li, Hongjue Li, Lijun Yang, Yue Deng  

**一句话要点**：提出约束粒子搜索以解决无梯度扩散逆问题

**关键词**：扩散模型, 逆问题求解, 无梯度优化, 约束优化, 粒子搜索

## 3 点简述
- 核心问题：现有扩散逆问题方法依赖前向过程梯度，在梯度未知时受限
- 方法要点：将逆问题重构为约束优化，利用粒子信息主动搜索最优解
- 实验或效果：在图像和科学逆问题上媲美梯度方法，优于无梯度替代

## 摘要（原文）

> Diffusion models have gained prominence as powerful generative tools for solving inverse problems due to their ability to model complex data distributions. However, existing methods typically rely on complete knowledge of the forward observation process to compute gradients for guided sampling, limiting their applicability in scenarios where such information is unavailable. In this work, we introduce \textbf{\emph{Constrained Particle Seeking (CPS)}}, a novel gradient-free approach that leverages all candidate particle information to actively search for the optimal particle while incorporating constraints aligned with high-density regions of the unconditional prior. Unlike previous methods that passively select promising candidates, CPS reformulates the inverse problem as a constrained optimization task, enabling more flexible and efficient particle seeking. We demonstrate that CPS can effectively solve both image and scientific inverse problems, achieving results comparable to gradient-based methods while significantly outperforming gradient-free alternatives. Code is available at https://github.com/deng-ai-lab/CPS.

