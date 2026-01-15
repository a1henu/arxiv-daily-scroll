---
layout: default
title: Towards Robust Cross-Dataset Object Detection Generalization under Domain Specificity
---

# Towards Robust Cross-Dataset Object Detection Generalization under Domain Specificity
**arXiv**：[2601.09497v1](https://arxiv.org/abs/2601.09497) · [PDF](https://arxiv.org/pdf/2601.09497.pdf)  
**作者**：Ritabrata Chakraborty, Hrishit Mitra, Shivakumara Palaiahnakote, Umapada Pal  

**一句话要点**：研究跨数据集目标检测泛化，揭示设置特异性下的性能结构并提供评估指导。

**关键词**：跨数据集目标检测, 域偏移, 设置特异性, 开放标签对齐, 泛化评估

## 3 点简述
- 核心问题：目标检测器在跨数据集时性能下降，尤其在设置特异性差异下。
- 方法要点：将数据集分为设置无关和设置特定类型，分析跨类型迁移的稳定性与不对称性。
- 实验或效果：通过开放标签对齐缓解标签不匹配，但域偏移在硬场景中仍主导性能下降。

## 摘要（原文）

> Object detectors often perform well in-distribution, yet degrade sharply on a different benchmark. We study cross-dataset object detection (CD-OD) through a lens of setting specificity. We group benchmarks into setting-agnostic datasets with diverse everyday scenes and setting-specific datasets tied to a narrow environment, and evaluate a standard detector family across all train--test pairs. This reveals a clear structure in CD-OD: transfer within the same setting type is relatively stable, while transfer across setting types drops substantially and is often asymmetric. The most severe breakdowns occur when transferring from specific sources to agnostic targets, and persist after open-label alignment, indicating that domain shift dominates in the hardest regimes. To disentangle domain shift from label mismatch, we compare closed-label transfer with an open-label protocol that maps predicted classes to the nearest target label using CLIP similarity. Open-label evaluation yields consistent but bounded gains, and many corrected cases correspond to semantic near-misses supported by the image evidence. Overall, we provide a principled characterization of CD-OD under setting specificity and practical guidance for evaluating detectors under distribution shift. Code will be released at \href{[https://github.com/Ritabrata04/cdod-icpr.git}{https://github.com/Ritabrata04/cdod-icpr}.

