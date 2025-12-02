---
layout: default
title: First On-Orbit Demonstration of a Geospatial Foundation Model
---

# First On-Orbit Demonstration of a Geospatial Foundation Model
**arXiv**：[2512.01181v1](https://arxiv.org/abs/2512.01181) · [PDF](https://arxiv.org/pdf/2512.01181.pdf)  
**作者**：Andrew Du, Roberto Del Prete, Alejandro Mousist, Nick Manser, Fabrice Marre, Andrew Barton, Carl Seubert, Gabriele Meoni, Tat-Jun Chin  

**一句话要点**：提出紧凑型地理空间基础模型，实现在轨推理以解决资源受限部署问题。

**关键词**：地理空间基础模型, 模型压缩, 在轨推理, Vision Transformer, 资源受限部署, 领域适应

## 3 点简述
- 核心问题：地理空间基础模型尺寸大，难以在资源受限的航天硬件上部署。
- 方法要点：开发基于Vision Transformer的紧凑变体，通过模型压缩和领域适应减少资源需求。
- 实验或效果：在五个下游任务评估，并在国际空间站上成功演示可靠在轨推理。

## 摘要（原文）

> Geospatial foundation models (GeoFMs) promise broad generalisation capacity for Earth observation (EO) tasks, particularly under data-limited conditions. However, their large size poses a barrier to deployment on resource-constrained space hardware. To address this, we present compact variants of a Vision Transformer (ViT)-based GeoFM that preserve downstream task performance while enabling onboard execution. Evaluation across five downstream tasks and validation in two representative flight environments show that model compression and domain adaptation are critical to reducing size and resource demands while maintaining high performance under operational conditions. We further demonstrate reliable on-orbit inference with the IMAGIN-e payload aboard the International Space Station. These results establish a pathway from large GeoFMs to flight-ready, resource-efficient deployments, expanding the feasibility of onboard AI for EO missions.

