---
layout: default
title: DAVE: Distribution-aware Attribution via ViT Gradient Decomposition
---

# DAVE: Distribution-aware Attribution via ViT Gradient Decomposition
**arXiv**：[2602.06613v1](https://arxiv.org/abs/2602.06613) · [PDF](https://arxiv.org/pdf/2602.06613.pdf)  
**作者**：Adam Wróbel, Siddhartha Gairola, Jacek Tabor, Bernt Schiele, Bartosz Zieliński, Dawid Rymarczyk  

**一句话要点**：提出DAVE方法，通过ViT梯度分解实现分布感知归因，以解决Vision Transformers中归因图不稳定和伪影问题。

**关键词**：Vision Transformers, 归因方法, 梯度分解, 分布感知, 计算机视觉

## 3 点简述
- 核心问题：Vision Transformers的归因图常因架构组件（如补丁嵌入和注意力路由）产生结构化伪影，导致不稳定和低分辨率。
- 方法要点：基于输入梯度的结构化分解，利用ViT架构特性分离局部等变稳定组件与架构诱导伪影。
- 实验或效果：未知，但方法旨在提供数学基础，提高归因图的稳定性和分辨率。

## 摘要（原文）

> Vision Transformers (ViTs) have become a dominant architecture in computer vision, yet producing stable and high-resolution attribution maps for these models remains challenging. Architectural components such as patch embeddings and attention routing often introduce structured artifacts in pixel-level explanations, causing many existing methods to rely on coarse patch-level attributions. We introduce DAVE \textit{(\underline{D}istribution-aware \underline{A}ttribution via \underline{V}iT Gradient D\underline{E}composition)}, a mathematically grounded attribution method for ViTs based on a structured decomposition of the input gradient. By exploiting architectural properties of ViTs, DAVE isolates locally equivariant and stable components of the effective input--output mapping. It separates these from architecture-induced artifacts and other sources of instability.

