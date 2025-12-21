---
layout: default
title: EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation
---

# EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation
**arXiv**：[2512.16360v1](https://arxiv.org/abs/2512.16360) · [PDF](https://arxiv.org/pdf/2512.16360.pdf)  
**作者**：Haotian Ling, Zequn Chen, Qiuying Chen, Donglin Di, Yongjia Ma, Hao Li, Chen Wei, Zhulin Tao, Xun Yang  

**一句话要点**：提出EverybodyDance，基于二分图身份匹配解决多角色动画中的身份对应问题

**关键词**：多角色动画, 身份对应, 二分图匹配, 掩码查询注意力, 动画一致性, 评估基准

## 3 点简述
- 核心问题：多角色动画中，角色位置交换时身份对应（IC）难以保持，影响动画一致性。
- 方法要点：构建身份匹配图（IMG），通过掩码查询注意力计算亲和度，优化图结构指标以强制IC正确性。
- 实验或效果：在身份对应评估基准上，EverybodyDance在IC和视觉保真度上显著优于现有基线。

## 摘要（原文）

> Consistent pose-driven character animation has achieved remarkable progress in single-character scenarios. However, extending these advances to multi-character settings is non-trivial, especially when position swap is involved. Beyond mere scaling, the core challenge lies in enforcing correct Identity Correspondence (IC) between characters in reference and generated frames. To address this, we introduce EverybodyDance, a systematic solution targeting IC correctness in multi-character animation. EverybodyDance is built around the Identity Matching Graph (IMG), which models characters in the generated and reference frames as two node sets in a weighted complete bipartite graph. Edge weights, computed via our proposed Mask-Query Attention (MQA), quantify the affinity between each pair of characters. Our key insight is to formalize IC correctness as a graph structural metric and to optimize it during training. We also propose a series of targeted strategies tailored for multi-character animation, including identity-embedded guidance, a multi-scale matching strategy, and pre-classified sampling, which work synergistically. Finally, to evaluate IC performance, we curate the Identity Correspondence Evaluation benchmark, dedicated to multi-character IC correctness. Extensive experiments demonstrate that EverybodyDance substantially outperforms state-of-the-art baselines in both IC and visual fidelity.

