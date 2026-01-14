---
layout: default
title: SnapGen++: Unleashing Diffusion Transformers for Efficient High-Fidelity Image Generation on Edge Devices
---

# SnapGen++: Unleashing Diffusion Transformers for Efficient High-Fidelity Image Generation on Edge Devices
**arXiv**：[2601.08303v1](https://arxiv.org/abs/2601.08303) · [PDF](https://arxiv.org/pdf/2601.08303.pdf)  
**作者**：Dongting Hu, Aarush Gupta, Magzhan Gabidolla, Arpit Sahni, Huseyin Coskun, Yanyu Li, Yerlan Idelbayev, Ahsan Mahmood, Aleksei Lebedev, Dishani Lahiri, Anujraaj Goyal, Ju Hu, Mingming Gong, Sergey Tulyakov, Anil Kag  

**一句话要点**：提出SnapGen++框架，结合稀疏注意力、弹性训练和知识蒸馏，实现边缘设备高效高保真图像生成。

**关键词**：扩散变换器, 边缘计算, 稀疏注意力, 弹性训练, 知识蒸馏, 图像生成

## 3 点简述
- 核心问题：扩散变换器计算和内存成本高，难以在边缘设备部署。
- 方法要点：设计紧凑架构、弹性训练框架和知识引导蒸馏，优化资源利用。
- 实验或效果：实现低延迟生成（如4步），适合实时应用，保持变换器级质量。

## 摘要（原文）

> Recent advances in diffusion transformers (DiTs) have set new standards in image generation, yet remain impractical for on-device deployment due to their high computational and memory costs. In this work, we present an efficient DiT framework tailored for mobile and edge devices that achieves transformer-level generation quality under strict resource constraints. Our design combines three key components. First, we propose a compact DiT architecture with an adaptive global-local sparse attention mechanism that balances global context modeling and local detail preservation. Second, we propose an elastic training framework that jointly optimizes sub-DiTs of varying capacities within a unified supernetwork, allowing a single model to dynamically adjust for efficient inference across different hardware. Finally, we develop Knowledge-Guided Distribution Matching Distillation, a step-distillation pipeline that integrates the DMD objective with knowledge transfer from few-step teacher models, producing high-fidelity and low-latency generation (e.g., 4-step) suitable for real-time on-device use. Together, these contributions enable scalable, efficient, and high-quality diffusion models for deployment on diverse hardware.

