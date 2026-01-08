---
layout: default
title: FocusUI: Efficient UI Grounding via Position-Preserving Visual Token Selection
---

# FocusUI: Efficient UI Grounding via Position-Preserving Visual Token Selection
**arXiv**：[2601.03928v1](https://arxiv.org/abs/2601.03928) · [PDF](https://arxiv.org/pdf/2601.03928.pdf)  
**作者**：Mingyu Ouyang, Kevin Qinghong Lin, Mike Zheng Shou, Hwee Tou Ng  

**一句话要点**：提出FocusUI框架，通过位置保持的视觉令牌选择实现高效用户界面定位

**关键词**：用户界面定位, 视觉语言模型, 视觉令牌选择, 位置保持, 高效推理, 计算优化

## 3 点简述
- 核心问题：高分辨率UI截图产生大量视觉令牌，导致计算开销大和注意力稀释，影响定位效率。
- 方法要点：融合指令条件评分和基于规则的UI图评分，选择相关视觉令牌；引入PosPad策略压缩丢弃令牌以保持位置连续性。
- 实验或效果：在四个基准测试中超越基线，ScreenSpot-Pro上性能提升3.7%，仅保留30%令牌时推理加速1.44倍，GPU内存降低17%。

## 摘要（原文）

> Vision-Language Models (VLMs) have shown remarkable performance in User Interface (UI) grounding tasks, driven by their ability to process increasingly high-resolution screenshots. However, screenshots are tokenized into thousands of visual tokens (e.g., about 4700 for 2K resolution), incurring significant computational overhead and diluting attention. In contrast, humans typically focus on regions of interest when interacting with UI. In this work, we pioneer the task of efficient UI grounding. Guided by practical analysis of the task's characteristics and challenges, we propose FocusUI, an efficient UI grounding framework that selects patches most relevant to the instruction while preserving positional continuity for precise grounding. FocusUI addresses two key challenges: (1) Eliminating redundant tokens in visual encoding. We construct patch-level supervision by fusing an instruction-conditioned score with a rule-based UI-graph score that down-weights large homogeneous regions to select distinct and instruction-relevant visual tokens. (2) Preserving positional continuity during visual token selection. We find that general visual token pruning methods suffer from severe accuracy degradation on UI grounding tasks due to broken positional information. We introduce a novel PosPad strategy, which compresses each contiguous sequence of dropped visual tokens into a single special marker placed at the sequence's last index to preserve positional continuity. Comprehensive experiments on four grounding benchmarks demonstrate that FocusUI surpasses GUI-specific baselines. On the ScreenSpot-Pro benchmark, FocusUI-7B achieves a performance improvement of 3.7% over GUI-Actor-7B. Even with only 30% visual token retention, FocusUI-7B drops by only 3.2% while achieving up to 1.44x faster inference and 17% lower peak GPU memory.

