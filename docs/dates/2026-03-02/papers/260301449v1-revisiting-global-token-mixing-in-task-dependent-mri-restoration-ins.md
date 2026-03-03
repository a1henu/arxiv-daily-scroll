---
layout: default
title: Revisiting Global Token Mixing in Task-Dependent MRI Restoration: Insights from Minimal Gated CNN Baselines
---

# Revisiting Global Token Mixing in Task-Dependent MRI Restoration: Insights from Minimal Gated CNN Baselines
**arXiv**：[2603.01449v1](https://arxiv.org/abs/2603.01449) · [PDF](https://arxiv.org/pdf/2603.01449.pdf)  
**作者**：Xiangjian Hou, Chao Qin, Chang Ni, Xin Wang, Chun Yuan, Xiaodong Ma  

**一句话要点**：通过最小门控CNN基线评估全局令牌混合在任务依赖MRI恢复中的效用

**关键词**：MRI恢复, 全局令牌混合, 门控CNN, 任务依赖分析, 数据一致性, 空间异方差噪声

## 3 点简述
- 核心问题：全局令牌混合在MRI恢复中是否普遍有益，需考虑任务差异和物理约束。
- 方法要点：建立控制测试台，比较局部门控CNN及其大场变体与全局模型。
- 实验或效果：在加速重建和超分辨率中局部模型具竞争力，去噪中全局模型表现最佳。

## 摘要（原文）

> Global token mixing, implemented via self-attention or state-space sequence models, has become a popular model design choice for MRI restoration. However, MRI restoration tasks differ substantially in how their degradations vary over image and k-space domains, and in the degree to which global coupling is already imposed by physics-driven data consistency terms. In this work, we ask the question whether global token mixing is actually beneficial in each individual task across three representative settings: accelerated MRI reconstruction with explicit data consistency, MRI super-resolution with k-space center cropping, and denoising of clinical carotid MRI data with spatially heteroscedastic noise. To reduce confounding factors, we establish a controlled testbed comparing a minimal local gated CNN and its large-field variant, benchmarking them directly against state-of-the-art global models under aligned training and evaluation protocols. For accelerated MRI reconstruction, the minimal unrolled gated-CNN baseline is already highly competitive compared to recent token-mixing approaches in public reconstruction benchmarks, suggesting limited additional benefits when the forward model and data-consistency steps provide strong global constraints. For super-resolution, where low-frequency k-space data are largely preserved by the controlled low-pass degradation, local gated models remain competitive, and a lightweight large-field variant yields only modest improvements. In contrast, for denoising with pronounced spatially heteroscedastic noise, token-mixing models achieve the strongest overall performance, consistent with the need to estimate spatially varying reliability. In conclusion, our results demonstrate that the utility of global token mixing in MRI restoration is task-dependent, and it should be tailored to the underlying imaging physics and degradation structure.

