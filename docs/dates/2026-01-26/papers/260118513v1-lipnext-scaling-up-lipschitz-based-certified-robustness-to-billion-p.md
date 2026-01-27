---
layout: default
title: LipNeXt: Scaling up Lipschitz-based Certified Robustness to Billion-parameter Models
---

# LipNeXt: Scaling up Lipschitz-based Certified Robustness to Billion-parameter Models
**arXiv**：[2601.18513v1](https://arxiv.org/abs/2601.18513) · [PDF](https://arxiv.org/pdf/2601.18513.pdf)  
**作者**：Kai Hu, Haoqi Hu, Matt Fredrikson  

**一句话要点**：提出LipNeXt架构以扩展Lipschitz认证鲁棒性至十亿参数模型

**关键词**：Lipschitz认证, 鲁棒性保证, 正交流形优化, 空间移位模块, 大规模模型训练, 确定性认证

## 3 点简述
- 核心问题：Lipschitz认证在模型规模、训练效率和ImageNet性能上难以扩展。
- 方法要点：采用无约束、无卷积的1-Lipschitz架构，结合流形优化和空间移位模块。
- 实验效果：在多个数据集上实现最优清洁和认证鲁棒精度，ImageNet上提升CRA达8%。

## 摘要（原文）

> Lipschitz-based certification offers efficient, deterministic robustness guarantees but has struggled to scale in model size, training efficiency, and ImageNet performance. We introduce \emph{LipNeXt}, the first \emph{constraint-free} and \emph{convolution-free} 1-Lipschitz architecture for certified robustness. LipNeXt is built using two techniques: (1) a manifold optimization procedure that updates parameters directly on the orthogonal manifold and (2) a \emph{Spatial Shift Module} to model spatial pattern without convolutions. The full network uses orthogonal projections, spatial shifts, a simple 1-Lipschitz $β$-Abs nonlinearity, and $L_2$ spatial pooling to maintain tight Lipschitz control while enabling expressive feature mixing. Across CIFAR-10/100 and Tiny-ImageNet, LipNeXt achieves state-of-the-art clean and certified robust accuracy (CRA), and on ImageNet it scales to 1-2B large models, improving CRA over prior Lipschitz models (e.g., up to $+8\%$ at $\varepsilon{=}1$) while retaining efficient, stable low-precision training. These results demonstrate that Lipschitz-based certification can benefit from modern scaling trends without sacrificing determinism or efficiency.

