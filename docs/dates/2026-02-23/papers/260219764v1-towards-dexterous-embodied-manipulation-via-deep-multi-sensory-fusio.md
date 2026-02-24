---
layout: default
title: Towards Dexterous Embodied Manipulation via Deep Multi-Sensory Fusion and Sparse Expert Scaling
---

# Towards Dexterous Embodied Manipulation via Deep Multi-Sensory Fusion and Sparse Expert Scaling
**arXiv**：[2602.19764v1](https://arxiv.org/abs/2602.19764) · [PDF](https://arxiv.org/pdf/2602.19764.pdf)  
**作者**：Yirui Sun, Guangyu Zhuge, Keliang Liu, Jie Gu, Zhihao xia, Qionglin Ren, Chunxu tian, Zhongxue Ga  

**一句话要点**：提出DeMUSE框架，通过深度多感官融合与稀疏专家扩展实现灵巧的具身操作。

**关键词**：多感官融合, 稀疏专家混合, 扩散Transformer, 自适应模态归一化, 具身操作, 物理一致性

## 3 点简述
- 核心问题：现有视觉中心方法忽视力与几何反馈，难以处理复杂物理交互任务。
- 方法要点：采用扩散Transformer融合RGB、深度和6轴力，结合自适应模态归一化与稀疏专家混合提升模型能力。
- 实验或效果：在仿真和真实世界试验中达到83.2%和72.5%成功率，验证了深度多感官集成的必要性。

## 摘要（原文）

> Realizing dexterous embodied manipulation necessitates the deep integration of heterogeneous multimodal sensory inputs. However, current vision-centric paradigms often overlook the critical force and geometric feedback essential for complex tasks. This paper presents DeMUSE, a Deep Multimodal Unified Sparse Experts framework leveraging a Diffusion Transformer to integrate RGB, depth, and 6-axis force into a unified serialized stream. Adaptive Modality-specific Normalization (AdaMN) is employed to recalibrate modality-aware features, mitigating representation imbalance and harmonizing the heterogeneous distributions of multi-sensory signals. To facilitate efficient scaling, the architecture utilizes a Sparse Mixture-of-Experts (MoE) with shared experts, increasing model capacity for physical priors while maintaining the low inference latency required for real-time control. A Joint denoising objective synchronously synthesizes environmental evolution and action sequences to ensure physical consistency. Achieving success rates of 83.2% and 72.5% in simulation and real-world trials, DeMUSE demonstrates state-of-the-art performance, validating the necessity of deep multi-sensory integration for complex physical interactions.

