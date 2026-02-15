---
layout: default
title: Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning
---

# Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning
**arXiv**：[2602.11882v1](https://arxiv.org/abs/2602.11882) · [PDF](https://arxiv.org/pdf/2602.11882.pdf)  
**作者**：Suraj Ranganath, Anish Patnaik, Vaishak Menon  

**一句话要点**：研究比特分配对世界模型规划的影响，以提升高效空间推理的精度

**关键词**：世界模型规划, 空间推理, 低比特量化, 比特分配, 高效计算, 模块感知量化

## 3 点简述
- 核心问题：低比特规划性能主要取决于总比特宽度还是模块间比特分配
- 方法要点：在Wall规划任务上使用DINO-WM进行配对目标混合比特评估，比较均匀、混合、非对称和分层量化变体
- 实验或效果：观察到三阶段模式，4比特设置对分配敏感，保留编码器精度可改善规划，混合与均匀INT4的差异受预算条件影响

## 摘要（原文）

> Efficient spatial reasoning requires world models that remain reliable under tight precision budgets. We study whether low-bit planning behavior is determined mostly by total bitwidth or by where bits are allocated across modules. Using DINO-WM on the Wall planning task, we run a paired-goal mixed-bit evaluation across uniform, mixed, asymmetric, and layerwise variants under two planner budgets. We observe a consistent three-regime pattern: 8-bit and 6-bit settings remain close to FP16, 3-bit settings collapse, and 4-bit settings are allocation-sensitive. In that transition region, preserving encoder precision improves planning relative to uniform quantization, and near-size asymmetric variants show the same encoder-side direction. In a later strict 22-cell replication with smaller per-cell episode count, the mixed-versus-uniform INT4 sign becomes budget-conditioned, which further highlights the sensitivity of this transition regime. These findings motivate module-aware, budget-aware quantization policies as a broader research direction for efficient spatial reasoning. Code and run artifacts are available at https://github.com/suraj-ranganath/DINO-MBQuant.

