---
layout: default
title: TacMamba: A Tactile History Compression Adapter Bridging Fast Reflexes and Slow VLA Reasoning
---

# TacMamba: A Tactile History Compression Adapter Bridging Fast Reflexes and Slow VLA Reasoning
**arXiv**：[2603.01700v1](https://arxiv.org/abs/2603.01700) · [PDF](https://arxiv.org/pdf/2603.01700.pdf)  
**作者**：Zhenan Wang, Yanzhe Wang, Meixuan Ren, Peng Li, Yang Liu, Yifei Nie, Limin Long, Yun Ye, Xiaofeng Wang, Zhen Zhu, Huixu Dong  

**一句话要点**：提出TacMamba架构，通过触觉历史压缩适配器解决触觉与视觉融合的时空不匹配问题。

**关键词**：触觉感知, 时空融合, Mamba模型, 实时处理, 视觉语言动作模型, 自监督学习

## 3 点简述
- 核心问题：触觉感知需高频处理与长时记忆，而视觉策略在低频控制下运行，现有架构难以融合。
- 方法要点：设计Mamba基触觉历史压缩器，以O(1)延迟编码力历史，实现与VLA模型的即插即用融合。
- 实验效果：在离散计数和隐式状态切换任务中，TacMamba达到100%成功率，优于纯视觉基线。

## 摘要（原文）

> In visually ambiguous manipulation such as detecting button click tactile feedback is often the sole source of ground truth. However, fusing tactile data poses a significant challenge due to a spatiotemporal mismatch: tactile perception requires high-frequency processing with long-horizon memory (System 1), whereas visual policies operate at low control frequencies (System 2). Existing architectures struggle to bridge this gap: Transformers are computationally prohibitive for high-frequency loops (>100Hz), while LSTMs suffer from forgetting over extended interaction histories. In this paper, we introduce TacMamba, a hierarchical architecture that aligns high-bandwidth tactile reflexes with low-frequency visual planning. Our approach comprises three core contributions: (1) a custom high-frequency tactile interface designed for flexible integration; (2) a Mamba-based Tactile History Compressor that encodes continuous force history into a compact state with O(1) inference latency (0.45 ms), enabling plug-and-play fusion with VLA models without joint pre-training and (3) a Tactile-Guided Dual-Stage Training strategy that leverages temporal discrimination for self-supervised representation learning and phase-uniform sampling to mitigate data sparsity. Experiments on discrete counting and implicit state switching demonstrate that TacMamba achieves 100% success rates, significantly outperforming the visual-only pi_0.5 baseline, while strictly satisfying hard real-time constraints.

