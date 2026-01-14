---
layout: default
title: Geo-NVS-w: Geometry-Aware Novel View Synthesis In-the-Wild with an SDF Renderer
---

# Geo-NVS-w: Geometry-Aware Novel View Synthesis In-the-Wild with an SDF Renderer
**arXiv**：[2601.08371v1](https://arxiv.org/abs/2601.08371) · [PDF](https://arxiv.org/pdf/2601.08371.pdf)  
**作者**：Anastasios Tsalakopoulos, Angelos Kanlis, Evangelos Chatzis, Antonis Karakottas, Dimitrios Zarpalas  

**一句话要点**：提出Geo-NVS-w框架，基于SDF几何表示解决野外图像集合中几何不一致的新视角合成问题。

**关键词**：新视角合成, 几何表示, 有符号距离函数, 野外图像, 几何保持损失, 能耗优化

## 3 点简述
- 核心问题：现有野外新视角合成方法缺乏复杂表面几何基础，易产生不一致结果。
- 方法要点：利用有符号距离函数（SDF）几何表示指导渲染，并引入几何保持损失以保留细节。
- 实验或效果：实现竞争性渲染性能，能耗比类似方法降低4-5倍，生成逼真且几何连贯的结果。

## 摘要（原文）

> We introduce Geo-NVS-w, a geometry-aware framework for high-fidelity novel view synthesis from unstructured, in-the-wild image collections. While existing in-the-wild methods already excel at novel view synthesis, they often lack geometric grounding on complex surfaces, sometimes producing results that contain inconsistencies. Geo-NVS-w addresses this limitation by leveraging an underlying geometric representation based on a Signed Distance Function (SDF) to guide the rendering process. This is complemented by a novel Geometry-Preservation Loss which ensures that fine structural details are preserved. Our framework achieves competitive rendering performance, while demonstrating a 4-5x reduction reduction in energy consumption compared to similar methods. We demonstrate that Geo-NVS-w is a robust method for in-the-wild NVS, yielding photorealistic results with sharp, geometrically coherent details.

