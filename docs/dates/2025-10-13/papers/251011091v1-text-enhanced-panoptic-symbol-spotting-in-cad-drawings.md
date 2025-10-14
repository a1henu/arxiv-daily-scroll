---
layout: default
title: Text-Enhanced Panoptic Symbol Spotting in CAD Drawings
---

# Text-Enhanced Panoptic Symbol Spotting in CAD Drawings
**arXiv**：[2510.11091v1](https://arxiv.org/abs/2510.11091) · [PDF](https://arxiv.org/pdf/2510.11091.pdf)  
**作者**：Xianlin Liu, Yan Gong, Bohao Li, Jiajing Huang, Bowen Du, Junchen Ye, Liyan Xu  

**一句话要点**：提出融合文本的CAD图纸全景符号识别框架，以提升复杂图纸理解能力。

**关键词**：CAD图纸分析, 全景符号识别, 文本增强, Transformer模型, 类型感知注意力

## 3 点简述
- 现有方法忽视文本注释和空间关系建模，导致图纸理解不全面。
- 联合建模几何与文本基元，使用Transformer和类型感知注意力机制。
- 在真实数据集上优于现有方法，对复杂CAD图纸具有更强鲁棒性。

## 摘要（原文）

> With the widespread adoption of Computer-Aided Design(CAD) drawings in
> engineering, architecture, and industrial design, the ability to accurately
> interpret and analyze these drawings has become increasingly critical. Among
> various subtasks, panoptic symbol spotting plays a vital role in enabling
> downstream applications such as CAD automation and design retrieval. Existing
> methods primarily focus on geometric primitives within the CAD drawings to
> address this task, but they face following major problems: they usually
> overlook the rich textual annotations present in CAD drawings and they lack
> explicit modeling of relationships among primitives, resulting in
> incomprehensive understanding of the holistic drawings. To fill this gap, we
> propose a panoptic symbol spotting framework that incorporates textual
> annotations. The framework constructs unified representations by jointly
> modeling geometric and textual primitives. Then, using visual features extract
> by pretrained CNN as the initial representations, a Transformer-based backbone
> is employed, enhanced with a type-aware attention mechanism to explicitly model
> the different types of spatial dependencies between various primitives.
> Extensive experiments on the real-world dataset demonstrate that the proposed
> method outperforms existing approaches on symbol spotting tasks involving
> textual annotations, and exhibits superior robustness when applied to complex
> CAD drawings.

