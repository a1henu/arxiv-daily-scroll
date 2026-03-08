---
layout: default
title: Mixture of Universal Experts: Scaling Virtual Width via Depth-Width Transformation
---

# Mixture of Universal Experts: Scaling Virtual Width via Depth-Width Transformation
**arXiv**：[2603.04971v1](https://arxiv.org/abs/2603.04971) · [PDF](https://arxiv.org/pdf/2603.04971.pdf)  
**作者**：Yilong Chen, Naibin Gu, Junyuan Shang, Zhenyu Zhang, Yuchen Feng, Jiawei Sheng, Tingwen Liu, Shuohuan Wang, Yu Sun, Hua Wu, Haifeng Wang  

**一句话要点**：提出混合通用专家以通过深度-宽度转换扩展虚拟宽度，解决MoE模型容量与计算解耦的扩展限制。

**关键词**：混合专家模型, 虚拟宽度扩展, 深度-宽度转换, 通用专家池, 负载平衡优化, 模型架构缩放

## 3 点简述
- 核心问题：MoE模型受物理深度和宽度限制，难以在固定每令牌激活预算下扩展容量。
- 方法要点：引入虚拟宽度维度，通过层无关通用专家池重用，结合交错旋转拓扑和深度感知负载平衡。
- 实验或效果：在多个扩展场景中优于基线MoE模型，最高提升1.3%，并支持现有检查点渐进转换。

## 摘要（原文）

> Mixture-of-Experts (MoE) decouples model capacity from per-token computation, yet their scalability remains limited by the physical dimensions of depth and width. To overcome this, we propose Mixture of Universal Experts (MOUE),a MoE generalization introducing a novel scaling dimension: Virtual Width. In general, MoUE aims to reuse a universal layer-agnostic expert pool across layers, converting depth into virtual width under a fixed per-token activation budget. However, two challenges remain: a routing path explosion from recursive expert reuse, and a mismatch between the exposure induced by reuse and the conventional load-balancing objectives. We address these with three core components: a Staggered Rotational Topology for structured expert sharing, a Universal Expert Load Balance for depth-aware exposure correction, and a Universal Router with lightweight trajectory state for coherent multi-step routing. Empirically, MoUE consistently outperforms matched MoE baselines by up to 1.3% across scaling regimes, enables progressive conversion of existing MoE checkpoints with up to 4.2% gains, and reveals a new scaling dimension for MoE architectures.

