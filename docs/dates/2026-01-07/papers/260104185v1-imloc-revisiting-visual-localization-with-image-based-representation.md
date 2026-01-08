---
layout: default
title: ImLoc: Revisiting Visual Localization with Image-based Representation
---

# ImLoc: Revisiting Visual Localization with Image-based Representation
**arXiv**：[2601.04185v1](https://arxiv.org/abs/2601.04185) · [PDF](https://arxiv.org/pdf/2601.04185.pdf)  
**作者**：Xudong Jiang, Fangjinhua Wang, Silvano Galliani, Christoph Vogel, Marc Pollefeys  

**一句话要点**：提出ImLoc方法，通过图像增强深度图以解决视觉定位中2D与3D表示的权衡问题。

**关键词**：视觉定位, 图像表示, 深度估计, 密集匹配, GPU加速, 基准测试

## 3 点简述
- 核心问题：现有视觉定位方法在2D图像易维护与3D结构高精度间存在权衡，难以兼顾更新与几何推理。
- 方法要点：采用2D图像表示，增强估计深度图以捕获几何结构，结合密集匹配器提升精度，支持压缩与GPU加速实现高效存储计算。
- 实验或效果：在标准基准测试中达到最高精度，优于现有内存效率方法，代码开源便于复现。

## 摘要（原文）

> Existing visual localization methods are typically either 2D image-based, which are easy to build and maintain but limited in effective geometric reasoning, or 3D structure-based, which achieve high accuracy but require a centralized reconstruction and are difficult to update. In this work, we revisit visual localization with a 2D image-based representation and propose to augment each image with estimated depth maps to capture the geometric structure. Supported by the effective use of dense matchers, this representation is not only easy to build and maintain, but achieves highest accuracy in challenging conditions. With compact compression and a GPU-accelerated LO-RANSAC implementation, the whole pipeline is efficient in both storage and computation and allows for a flexible trade-off between accuracy and highest memory efficiency. Our method achieves a new state-of-the-art accuracy on various standard benchmarks and outperforms existing memory-efficient methods at comparable map sizes. Code will be available at https://github.com/cvg/Hierarchical-Localization.

