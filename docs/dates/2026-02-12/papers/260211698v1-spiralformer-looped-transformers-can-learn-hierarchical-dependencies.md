---
layout: default
title: SpiralFormer: Looped Transformers Can Learn Hierarchical Dependencies via Multi-Resolution Recursion
---

# SpiralFormer: Looped Transformers Can Learn Hierarchical Dependencies via Multi-Resolution Recursion
**arXiv**：[2602.11698v1](https://arxiv.org/abs/2602.11698) · [PDF](https://arxiv.org/pdf/2602.11698.pdf)  
**作者**：Chengting Yu, Xiaobo Shu, Yadao Wang, Yizhen Zhang, Haoyi Wu, You Wu, Rujiao Long, Ziheng Chen, Yuchi Xu, Wenbo Su, Bo Zheng  

**一句话要点**：提出SpiralFormer，通过多分辨率递归提升循环Transformer的层次依赖学习能力与效率。

**关键词**：循环Transformer, 多分辨率递归, 层次依赖学习, 计算效率, 迭代细化, 序列建模

## 3 点简述
- 早期循环Transformer在计算效率上常落后于非循环基线，需改进递归机制。
- SpiralFormer引入多分辨率递归调度，在不同尺度上实现迭代功能专业化。
- 实验显示，在160M至1.4B模型规模上，SpiralFormer在参数和计算效率上优于基线。

## 摘要（原文）

> Recursive (looped) Transformers decouple computational depth from parameter depth by repeatedly applying shared layers, providing an explicit architectural primitive for iterative refinement and latent reasoning. However, early looped Transformers often underperform non-recursive baselines of equal compute. While recent literature has introduced more effective recursion mechanisms to mitigate this gap, existing architectures still operate at a fixed, full-token resolution, neglecting the potential efficiency of computing over compressed latent representations. In this paper, we propose SpiralFormer, a looped Transformer that executes recurrence under a multi-resolution recursion schedule. We provide probing evidence that multi-resolution recursion enables the model to learn hierarchical dependencies by inducing iteration-wise functional specialization across different scales. Empirically, SpiralFormer achieves better parameter and compute efficiency than both looped and non-looped baselines across model scales from 160M to 1.4B, establishing sequence resolution as a potential axis for scaling recursive architectures.

