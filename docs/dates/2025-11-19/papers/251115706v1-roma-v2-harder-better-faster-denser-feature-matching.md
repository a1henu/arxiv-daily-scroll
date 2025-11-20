---
layout: default
title: RoMa v2: Harder Better Faster Denser Feature Matching
---

# RoMa v2: Harder Better Faster Denser Feature Matching
**arXiv**：[2511.15706v1](https://arxiv.org/abs/2511.15706) · [PDF](https://arxiv.org/pdf/2511.15706.pdf)  
**作者**：Johan Edstedt, David Nordström, Yushan Zhang, Georg Bökman, Jonathan Astermark, Viktor Larsson, Anders Heyden, Fredrik Kahl, Mårten Wadenbäck, Michael Felsberg  

**一句话要点**：提出RoMa v2密集特征匹配模型，通过架构、训练和优化改进解决复杂场景匹配问题

**关键词**：密集特征匹配, 匹配架构设计, 两阶段训练, CUDA优化, DINOv3基础模型

## 3 点简述
- 核心问题：现有密集匹配器在复杂场景中性能差或失败，高精度模型速度慢
- 方法要点：构建新匹配架构与损失，结合多样训练分布和两阶段流水线
- 实验或效果：在广泛实验中，模型准确度显著优于先前方法，达到新SOTA

## 摘要（原文）

> Dense feature matching aims to estimate all correspondences between two images of a 3D scene and has recently been established as the gold-standard due to its high accuracy and robustness. However, existing dense matchers still fail or perform poorly for many hard real-world scenarios, and high-precision models are often slow, limiting their applicability. In this paper, we attack these weaknesses on a wide front through a series of systematic improvements that together yield a significantly better model. In particular, we construct a novel matching architecture and loss, which, combined with a curated diverse training distribution, enables our model to solve many complex matching tasks. We further make training faster through a decoupled two-stage matching-then-refinement pipeline, and at the same time, significantly reduce refinement memory usage through a custom CUDA kernel. Finally, we leverage the recent DINOv3 foundation model along with multiple other insights to make the model more robust and unbiased. In our extensive set of experiments we show that the resulting novel matcher sets a new state-of-the-art, being significantly more accurate than its predecessors. Code is available at https://github.com/Parskatt/romav2

