---
layout: default
title: SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection
---

# SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection
**arXiv**：[2601.03024v1](https://arxiv.org/abs/2601.03024) · [PDF](https://arxiv.org/pdf/2601.03024.pdf)  
**作者**：Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang  

**一句话要点**：提出SA-ResGS框架，通过自增强点云和残差学习，提升主动场景重建中下一最佳视图选择的稳定性和不确定性量化。

**关键词**：3D高斯溅射, 下一最佳视图选择, 不确定性量化, 残差学习, 主动场景重建, 自增强点云

## 3 点简述
- 核心问题：主动场景重建中，稀疏宽基线视图导致不确定性量化不稳定和高斯分布监督不足。
- 方法要点：引入自增强点云进行场景覆盖估计，并结合残差学习策略增强高不确定性高斯分布的梯度流。
- 实验或效果：在主动视图选择实验中，SA-ResGS在重建质量和视图选择鲁棒性上优于现有基线方法。

## 摘要（原文）

> We propose Self-Augmented Residual 3D Gaussian Splatting (SA-ResGS), a novel framework to stabilize uncertainty quantification and enhancing uncertainty-aware supervision in next-best-view (NBV) selection for active scene reconstruction. SA-ResGS improves both the reliability of uncertainty estimates and their effectiveness for supervision by generating Self-Augmented point clouds (SA-Points) via triangulation between a training view and a rasterized extrapolated view, enabling efficient scene coverage estimation. While improving scene coverage through physically guided view selection, SA-ResGS also addresses the challenge of under-supervised Gaussians, exacerbated by sparse and wide-baseline views, by introducing the first residual learning strategy tailored for 3D Gaussian Splatting. This targeted supervision enhances gradient flow in high-uncertainty Gaussians by combining uncertainty-driven filtering with dropout- and hard-negative-mining-inspired sampling. Our contributions are threefold: (1) a physically grounded view selection strategy that promotes efficient and uniform scene coverage; (2) an uncertainty-aware residual supervision scheme that amplifies learning signals for weakly contributing Gaussians, improving training stability and uncertainty estimation across scenes with diverse camera distributions; (3) an implicit unbiasing of uncertainty quantification as a consequence of constrained view selection and residual supervision, which together mitigate conflicting effects of wide-baseline exploration and sparse-view ambiguity in NBV planning. Experiments on active view selection demonstrate that SA-ResGS outperforms state-of-the-art baselines in both reconstruction quality and view selection robustness.

