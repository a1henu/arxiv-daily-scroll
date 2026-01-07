---
layout: default
title: LSP-DETR: Efficient and Scalable Nuclei Segmentation in Whole Slide Images
---

# LSP-DETR: Efficient and Scalable Nuclei Segmentation in Whole Slide Images
**arXiv**：[2601.03163v1](https://arxiv.org/abs/2601.03163) · [PDF](https://arxiv.org/pdf/2601.03163.pdf)  
**作者**：Matěj Pekár, Vít Musil, Rudolf Nenutil, Petr Holub, Tomáš Brázdil  

**一句话要点**：提出LSP-DETR以高效可扩展地分割全切片图像中的细胞核实例

**关键词**：细胞核分割, 全切片图像, Transformer, 实例分割, 计算病理学, 星凸多边形

## 3 点简述
- 核心问题：全切片图像中细胞核实例分割的计算挑战，现有方法依赖分块处理和昂贵后处理，牺牲上下文和效率。
- 方法要点：使用轻量级Transformer和线性复杂度处理更大图像，以星凸多边形表示细胞核，通过径向距离损失自然分割重叠核，无需显式重叠标注或手工后处理。
- 实验或效果：在PanNuke和MoNuSeg上评估，显示强泛化能力和领先效率，比次快方法快五倍以上。

## 摘要（原文）

> Precise and scalable instance segmentation of cell nuclei is essential for computational pathology, yet gigapixel Whole-Slide Images pose major computational challenges. Existing approaches rely on patch-based processing and costly post-processing for instance separation, sacrificing context and efficiency. We introduce LSP-DETR (Local Star Polygon DEtection TRansformer), a fully end-to-end framework that uses a lightweight transformer with linear complexity to process substantially larger images without additional computational cost. Nuclei are represented as star-convex polygons, and a novel radial distance loss function allows the segmentation of overlapping nuclei to emerge naturally, without requiring explicit overlap annotations or handcrafted post-processing. Evaluations on PanNuke and MoNuSeg show strong generalization across tissues and state-of-the-art efficiency, with LSP-DETR being over five times faster than the next-fastest leading method. Code and models are available at https://github.com/RationAI/lsp-detr.

