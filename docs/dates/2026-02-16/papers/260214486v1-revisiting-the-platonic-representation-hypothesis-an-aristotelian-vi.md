---
layout: default
title: Revisiting the Platonic Representation Hypothesis: An Aristotelian View
---

# Revisiting the Platonic Representation Hypothesis: An Aristotelian View
**arXiv**：[2602.14486v1](https://arxiv.org/abs/2602.14486) · [PDF](https://arxiv.org/pdf/2602.14486.pdf)  
**作者**：Fabian Gröger, Shuo Wen, Maria Brbić  

**一句话要点**：提出基于排列的零校准框架，以修正网络规模对表示相似性度量的混淆，重新评估柏拉图表示假设。

**关键词**：表示相似性度量, 网络规模校准, 柏拉图表示假设, 亚里士多德表示假设, 局部邻域关系, 统计校准框架

## 3 点简述
- 核心问题：现有表示相似性度量受网络规模（深度或宽度）影响，导致相似性分数系统性膨胀，可能误导对表示收敛性的评估。
- 方法要点：引入基于排列的零校准框架，将任何表示相似性度量转换为具有统计保证的校准分数，以消除规模效应。
- 实验或效果：校准后，全局谱度量的收敛现象基本消失，而局部邻域相似性（非局部距离）在不同模态间仍保持显著一致性，提出亚里士多德表示假设。

## 摘要（原文）

> The Platonic Representation Hypothesis suggests that representations from neural networks are converging to a common statistical model of reality. We show that the existing metrics used to measure representational similarity are confounded by network scale: increasing model depth or width can systematically inflate representational similarity scores. To correct these effects, we introduce a permutation-based null-calibration framework that transforms any representational similarity metric into a calibrated score with statistical guarantees. We revisit the Platonic Representation Hypothesis with our calibration framework, which reveals a nuanced picture: the apparent convergence reported by global spectral measures largely disappears after calibration, while local neighborhood similarity, but not local distances, retains significant agreement across different modalities. Based on these findings, we propose the Aristotelian Representation Hypothesis: representations in neural networks are converging to shared local neighborhood relationships.

