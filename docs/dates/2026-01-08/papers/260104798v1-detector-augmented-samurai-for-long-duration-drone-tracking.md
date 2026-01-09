---
layout: default
title: Detector-Augmented SAMURAI for Long-Duration Drone Tracking
---

# Detector-Augmented SAMURAI for Long-Duration Drone Tracking
**arXiv**：[2601.04798v1](https://arxiv.org/abs/2601.04798) · [PDF](https://arxiv.org/pdf/2601.04798.pdf)  
**作者**：Tamara R. Lenhard, Andreas Weinmann, Hichem Snoussi, Tobias Koch  

**一句话要点**：提出检测器增强SAMURAI以提升城市环境中无人机长时跟踪的鲁棒性

**关键词**：无人机跟踪, 长时跟踪, 检测器增强, SAMURAI模型, 城市监控, 鲁棒性提升

## 3 点简述
- 核心问题：基于检测器的无人机跟踪存在时间不一致性，且RGB跟踪研究有限，依赖传统运动模型。
- 方法要点：首次系统评估SAMURAI在无人机跟踪中的潜力，并引入检测器增强扩展以减轻边界框初始化和序列长度敏感性。
- 实验或效果：扩展方法在复杂城市环境中显著提升鲁棒性，尤其在长序列和无人机退出重入事件中，成功率提高达+0.393。

## 摘要（原文）

> Robust long-term tracking of drone is a critical requirement for modern surveillance systems, given their increasing threat potential. While detector-based approaches typically achieve strong frame-level accuracy, they often suffer from temporal inconsistencies caused by frequent detection dropouts. Despite its practical relevance, research on RGB-based drone tracking is still limited and largely reliant on conventional motion models. Meanwhile, foundation models like SAMURAI have established their effectiveness across other domains, exhibiting strong category-agnostic tracking performance. However, their applicability in drone-specific scenarios has not been investigated yet. Motivated by this gap, we present the first systematic evaluation of SAMURAI's potential for robust drone tracking in urban surveillance settings. Furthermore, we introduce a detector-augmented extension of SAMURAI to mitigate sensitivity to bounding-box initialization and sequence length. Our findings demonstrate that the proposed extension significantly improves robustness in complex urban environments, with pronounced benefits in long-duration sequences - especially under drone exit-re-entry events. The incorporation of detector cues yields consistent gains over SAMURAI's zero-shot performance across datasets and metrics, with success rate improvements of up to +0.393 and FNR reductions of up to -0.475.

