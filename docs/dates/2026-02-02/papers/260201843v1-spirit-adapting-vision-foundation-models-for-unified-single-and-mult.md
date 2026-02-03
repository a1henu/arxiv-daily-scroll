---
layout: default
title: SPIRIT: Adapting Vision Foundation Models for Unified Single- and Multi-Frame Infrared Small Target Detection
---

# SPIRIT: Adapting Vision Foundation Models for Unified Single- and Multi-Frame Infrared Small Target Detection
**arXiv**：[2602.01843v1](https://arxiv.org/abs/2602.01843) · [PDF](https://arxiv.org/pdf/2602.01843.pdf)  
**作者**：Qian Xu, Xi Li, Fei Gao, Jie Guo, Haojuan Yuan, Shuaipeng Fan, Mingjin Zhang  

**一句话要点**：提出SPIRIT框架，通过物理信息插件适配视觉基础模型，统一单帧与多帧红外小目标检测。

**关键词**：红外小目标检测, 视觉基础模型适配, 物理信息插件, 时空统一框架, 记忆注意力机制

## 3 点简述
- 核心问题：红外小目标信号弱、语义线索少，直接使用视觉基础模型和外观驱动跨帧关联不可靠。
- 方法要点：空间上使用PIFR抑制背景增强目标信号，时间上使用PGMA注入历史空间先验约束跨帧关联。
- 实验效果：在多个基准测试中优于基于视觉基础模型的基线，达到SOTA性能。

## 摘要（原文）

> Infrared small target detection (IRSTD) is crucial for surveillance and early-warning, with deployments spanning both single-frame analysis and video-mode tracking. A practical solution should leverage vision foundation models (VFMs) to mitigate infrared data scarcity, while adopting a memory-attention-based temporal propagation framework that unifies single- and multi-frame inference. However, infrared small targets exhibit weak radiometric signals and limited semantic cues, which differ markedly from visible-spectrum imagery. This modality gap makes direct use of semantics-oriented VFMs and appearance-driven cross-frame association unreliable for IRSTD: hierarchical feature aggregation can submerge localized target peaks, and appearance-only memory attention becomes ambiguous, leading to spurious clutter associations. To address these challenges, we propose SPIRIT, a unified and VFM-compatible framework that adapts VFMs to IRSTD via lightweight physics-informed plug-ins. Spatially, PIFR refines features by approximating rank-sparsity decomposition to suppress structured background components and enhance sparse target-like signals. Temporally, PGMA injects history-derived soft spatial priors into memory cross-attention to constrain cross-frame association, enabling robust video detection while naturally reverting to single-frame inference when temporal context is absent. Experiments on multiple IRSTD benchmarks show consistent gains over VFM-based baselines and SOTA performance.

