---
layout: default
title: InstanceV: Instance-Level Video Generation
---

# InstanceV: Instance-Level Video Generation
**arXiv**：[2511.23146v1](https://arxiv.org/abs/2511.23146) · [PDF](https://arxiv.org/pdf/2511.23146.pdf)  
**作者**：Yuheng Chen, Teng Hu, Jiangning Zhang, Zhucun Xue, Ran Yi, Lizhuang Ma  

**一句话要点**：提出InstanceV框架，通过实例级控制解决文本到视频生成中细粒度可控性不足的问题。

**关键词**：实例级视频生成, 文本到视频扩散模型, 细粒度可控性, 实例感知注意力, 视频生成基准

## 3 点简述
- 核心问题：现有文本到视频模型缺乏对实例级细粒度生成的控制能力。
- 方法要点：引入Instance-aware Masked Cross-Attention机制，利用实例级定位信息生成空间位置正确的实例。
- 实验或效果：在InstanceBench基准上，InstanceV在实例级可控性和视频质量方面优于现有模型。

## 摘要（原文）

> Recent advances in text-to-video diffusion models have enabled the generation of high-quality videos conditioned on textual descriptions. However, most existing text-to-video models rely solely on textual conditions, lacking general fine-grained controllability over video generation. To address this challenge, we propose InstanceV, a video generation framework that enables i) instance-level control and ii) global semantic consistency. Specifically, with the aid of proposed Instance-aware Masked Cross-Attention mechanism, InstanceV maximizes the utilization of additional instance-level grounding information to generate correctly attributed instances at designated spatial locations. To improve overall consistency, We introduce the Shared Timestep-Adaptive Prompt Enhancement module, which connects local instances with global semantics in a parameter-efficient manner. Furthermore, we incorporate Spatially-Aware Unconditional Guidance during both training and inference to alleviate the disappearance of small instances. Finally, we propose a new benchmark, named InstanceBench, which combines general video quality metrics with instance-aware metrics for more comprehensive evaluation on instance-level video generation. Extensive experiments demonstrate that InstanceV not only achieves remarkable instance-level controllability in video generation, but also outperforms existing state-of-the-art models in both general quality and instance-aware metrics across qualitative and quantitative evaluations.

