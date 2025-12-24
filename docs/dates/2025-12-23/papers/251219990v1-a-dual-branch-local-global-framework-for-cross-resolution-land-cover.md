---
layout: default
title: A Dual-Branch Local-Global Framework for Cross-Resolution Land Cover Mapping
---

# A Dual-Branch Local-Global Framework for Cross-Resolution Land Cover Mapping
**arXiv**：[2512.19990v1](https://arxiv.org/abs/2512.19990) · [PDF](https://arxiv.org/pdf/2512.19990.pdf)  
**作者**：Peng Gao, Ke Li, Di Wang, Yongshan Zhu, Yiming Zhang, Xuemei Luo, Yifeng Wang  

**一句话要点**：提出DDTM双分支弱监督框架，解决跨分辨率土地覆盖映射中的分辨率不匹配问题。

**关键词**：跨分辨率土地覆盖映射, 弱监督学习, 扩散模型, Transformer, 伪标签评估, 语义分割

## 3 点简述
- 核心问题：跨分辨率土地覆盖映射中，粗分辨率监督与细粒度空间结构对齐困难，导致噪声监督和精度下降。
- 方法要点：采用扩散分支细化局部语义，Transformer分支增强全局上下文一致性，并设计伪标签置信度评估模块减少噪声。
- 实验或效果：在Chesapeake Bay基准测试中达到66.52% mIoU，优于现有弱监督方法。

## 摘要（原文）

> Cross-resolution land cover mapping aims to produce high-resolution semantic predictions from coarse or low-resolution supervision, yet the severe resolution mismatch makes effective learning highly challenging. Existing weakly supervised approaches often struggle to align fine-grained spatial structures with coarse labels, leading to noisy supervision and degraded mapping accuracy. To tackle this problem, we propose DDTM, a dual-branch weakly supervised framework that explicitly decouples local semantic refinement from global contextual reasoning. Specifically, DDTM introduces a diffusion-based branch to progressively refine fine-scale local semantics under coarse supervision, while a transformer-based branch enforces long-range contextual consistency across large spatial extents. In addition, we design a pseudo-label confidence evaluation module to mitigate noise induced by cross-resolution inconsistencies and to selectively exploit reliable supervisory signals. Extensive experiments demonstrate that DDTM establishes a new state-of-the-art on the Chesapeake Bay benchmark, achieving 66.52\% mIoU and substantially outperforming prior weakly supervised methods. The code is available at https://github.com/gpgpgp123/DDTM.

