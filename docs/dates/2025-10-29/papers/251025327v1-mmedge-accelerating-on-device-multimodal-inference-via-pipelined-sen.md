---
layout: default
title: MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding
---

# MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding
**arXiv**：[2510.25327v1](https://arxiv.org/abs/2510.25327) · [PDF](https://arxiv.org/pdf/2510.25327.pdf)  
**作者**：Runxi Huang, Mingxuan Yu, Mingyu Tsoi, Xiaomin Ouyang  

**一句话要点**：提出MMEdge框架，通过流水线感知与编码加速边缘设备多模态推理。

**关键词**：边缘计算, 多模态推理, 流水线处理, 自适应优化, 实时系统

## 3 点简述
- 核心问题：边缘设备多模态推理中感知动态与模型执行紧耦合，忽略模态间依赖。
- 方法要点：分解推理为细粒度单元，引入时间聚合模块和自适应优化机制。
- 实验或效果：在无人机测试中显著降低延迟，保持高任务准确性。

## 摘要（原文）

> Real-time multimodal inference on resource-constrained edge devices is
> essential for applications such as autonomous driving, human-computer
> interaction, and mobile health. However, prior work often overlooks the tight
> coupling between sensing dynamics and model execution, as well as the complex
> inter-modality dependencies. In this paper, we propose MMEdge, an new on-device
> multi-modal inference framework based on pipelined sensing and encoding.
> Instead of waiting for complete sensor inputs, MMEdge decomposes the entire
> inference process into a sequence of fine-grained sensing and encoding units,
> allowing computation to proceed incrementally as data arrive. MMEdge also
> introduces a lightweight but effective temporal aggregation module that
> captures rich temporal dynamics across different pipelined units to maintain
> accuracy performance. Such pipelined design also opens up opportunities for
> fine-grained cross-modal optimization and early decision-making during
> inference. To further enhance system performance under resource variability and
> input data complexity, MMEdge incorporates an adaptive multimodal configuration
> optimizer that dynamically selects optimal sensing and model configurations for
> each modality under latency constraints, and a cross-modal speculative skipping
> mechanism that bypasses future units of slower modalities when early
> predictions reach sufficient confidence. We evaluate MMEdge using two public
> multimodal datasets and deploy it on a real-world unmanned aerial vehicle
> (UAV)-based multimodal testbed. The results show that MMEdge significantly
> reduces end-to-end latency while maintaining high task accuracy across various
> system and data dynamics.

