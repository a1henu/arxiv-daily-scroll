---
layout: default
title: Shiva-DiT: Residual-Based Differentiable Top-$k$ Selection for Efficient Diffusion Transformers
---

# Shiva-DiT: Residual-Based Differentiable Top-$k$ Selection for Efficient Diffusion Transformers
**arXiv**：[2602.05605v1](https://arxiv.org/abs/2602.05605) · [PDF](https://arxiv.org/pdf/2602.05605.pdf)  
**作者**：Jiaji Zhang, Hailiang Zhao, Guoxuan Zhu, Ruichao Sun, Jiaju Wu, Xinkui Zhao, Hanlin Tang, Weiyi Lu, Kan Liu, Tao Lan, Lin Qu, Shuiguang Deng  

**一句话要点**：提出Shiva-DiT，通过残差可微Top-k选择解决扩散Transformer计算成本高的问题

**关键词**：扩散Transformer, 可微剪枝, 残差估计, 自适应调度, 计算效率

## 3 点简述
- 扩散Transformer因自注意力二次缩放导致计算成本过高
- 采用残差可微Top-k选择，结合残差感知直通估计器实现静态预算和可学习性
- 实验在SD3.5等模型上实现1.54倍加速，保真度优于基线

## 摘要（原文）

> Diffusion Transformers (DiTs) incur prohibitive computational costs due to the quadratic scaling of self-attention. Existing pruning methods fail to simultaneously satisfy differentiability, efficiency, and the strict static budgets required for hardware overhead. To address this, we propose Shiva-DiT, which effectively reconciles these conflicting requirements via Residual-Based Differentiable Top-$k$ Selection. By leveraging a residual-aware straight-through estimator, our method enforces deterministic token counts for static compilation while preserving end-to-end learnability through residual gradient estimation. Furthermore, we introduce a Context-Aware Router and Adaptive Ratio Policy to autonomously learn an adaptive pruning schedule. Experiments on mainstream models, including SD3.5, demonstrate that Shiva-DiT establishes a new Pareto frontier, achieving a 1.54$\times$ wall-clock speedup with superior fidelity compared to existing baselines, effectively eliminating ragged tensor overheads.

