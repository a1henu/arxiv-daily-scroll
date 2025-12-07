---
layout: default
title: Environment-Aware Channel Inference via Cross-Modal Flow: From Multimodal Sensing to Wireless Channels
---

# Environment-Aware Channel Inference via Cross-Modal Flow: From Multimodal Sensing to Wireless Channels
**arXiv**：[2512.04966v1](https://arxiv.org/abs/2512.04966) · [PDF](https://arxiv.org/pdf/2512.04966.pdf)  
**作者**：Guangming Liang, Mingjie Yang, Dongzhu Liu, Paul Henderson, Lajos Hanzo  

**一句话要点**：提出基于跨模态流匹配的无导频信道推断方法，利用多模态感知数据估计无线信道状态信息。

**关键词**：无线信道推断, 多模态感知, 流匹配, 数据驱动框架, 大规模MIMO, 实时估计

## 3 点简述
- 核心问题：大规模MIMO系统中导频估计开销大，尤其在高速移动环境下，获取准确信道状态信息困难。
- 方法要点：采用数据驱动框架，将多模态感知数据映射到信道域，通过条件流匹配和模态对齐损失学习信道分布。
- 实验或效果：基于Sionna和Blender构建数据生成器，系统级评估显示在信道估计精度和频谱效率上优于基准方法。

## 摘要（原文）

> Accurate channel state information (CSI) underpins reliable and efficient wireless communication. However, acquiring CSI via pilot estimation incurs substantial overhead, especially in massive multiple-input multiple-output (MIMO) systems operating in high-Doppler environments. By leveraging the growing availability of environmental sensing data, this treatise investigates pilot-free channel inference that estimates complete CSI directly from multimodal observations, including camera images, LiDAR point clouds, and GPS coordinates. In contrast to prior studies that rely on predefined channel models, we develop a data-driven framework that formulates the sensing-to-channel mapping as a cross-modal flow matching problem. The framework fuses multimodal features into a latent distribution within the channel domain, and learns a velocity field that continuously transforms the latent distribution toward the channel distribution. To make this formulation tractable and efficient, we reformulate the problem as an equivalent conditional flow matching objective and incorporate a modality alignment loss, while adopting low-latency inference mechanisms to enable real-time CSI estimation. In experiments, we build a procedural data generator based on Sionna and Blender to support realistic modeling of sensing scenes and wireless propagation. System-level evaluations demonstrate significant improvements over pilot- and sensing-based benchmarks in both channel estimation accuracy and spectral efficiency for the downstream beamforming task.

