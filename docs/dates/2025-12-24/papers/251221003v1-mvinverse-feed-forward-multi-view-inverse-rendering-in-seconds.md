---
layout: default
title: MVInverse: Feed-forward Multi-view Inverse Rendering in Seconds
---

# MVInverse: Feed-forward Multi-view Inverse Rendering in Seconds
**arXiv**：[2512.21003v1](https://arxiv.org/abs/2512.21003) · [PDF](https://arxiv.org/pdf/2512.21003.pdf)  
**作者**：Xiangzuo Wu, Chengwei Ren, Jun Zhou, Xiu Li, Yuan Liu  

**一句话要点**：提出前馈多视角逆渲染框架，通过交替注意力实现秒级预测，提升多视角一致性和泛化能力。

**关键词**：多视角逆渲染, 前馈网络, 交替注意力, 材质一致性, 泛化微调, 真实场景应用

## 3 点简述
- 核心问题：现有单视角方法忽略跨视角关系，多视角优化方法计算成本高且难以扩展。
- 方法要点：使用前馈网络直接预测材质和光照，通过交替注意力捕获视角内光照交互和视角间材质一致性。
- 实验或效果：在基准数据集上实现多视角一致性、材质和法线估计质量的先进性能，并通过一致性微调增强真实场景泛化。

## 摘要（原文）

> Multi-view inverse rendering aims to recover geometry, materials, and illumination consistently across multiple viewpoints. When applied to multi-view images, existing single-view approaches often ignore cross-view relationships, leading to inconsistent results. In contrast, multi-view optimization methods rely on slow differentiable rendering and per-scene refinement, making them computationally expensive and hard to scale. To address these limitations, we introduce a feed-forward multi-view inverse rendering framework that directly predicts spatially varying albedo, metallic, roughness, diffuse shading, and surface normals from sequences of RGB images. By alternating attention across views, our model captures both intra-view long-range lighting interactions and inter-view material consistency, enabling coherent scene-level reasoning within a single forward pass. Due to the scarcity of real-world training data, models trained on existing synthetic datasets often struggle to generalize to real-world scenes. To overcome this limitation, we propose a consistency-based finetuning strategy that leverages unlabeled real-world videos to enhance both multi-view coherence and robustness under in-the-wild conditions. Extensive experiments on benchmark datasets demonstrate that our method achieves state-of-the-art performance in terms of multi-view consistency, material and normal estimation quality, and generalization to real-world imagery.

