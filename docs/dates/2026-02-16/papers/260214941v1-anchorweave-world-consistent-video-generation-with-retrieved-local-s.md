---
layout: default
title: AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories
---

# AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories
**arXiv**：[2602.14941v1](https://arxiv.org/abs/2602.14941) · [PDF](https://arxiv.org/pdf/2602.14941.pdf)  
**作者**：Zun Wang, Han Lin, Jaehong Yoon, Jaemin Cho, Yue Zhang, Mohit Bansal  

**一句话要点**：提出AnchorWeave框架，通过检索局部几何记忆解决长视频生成中的空间一致性挑战

**关键词**：视频生成, 空间一致性, 局部几何记忆, 多锚点控制, 检索机制

## 3 点简述
- 核心问题：现有基于全局3D重建的方法因视角错位导致几何噪声，影响视频生成质量
- 方法要点：使用多个局部几何记忆替代全局记忆，通过多锚点编织控制器整合以协调不一致性
- 实验或效果：实验显示AnchorWeave显著提升长期场景一致性，同时保持视觉质量，验证了局部几何条件化等有效性

## 摘要（原文）

> Maintaining spatial world consistency over long horizons remains a central challenge for camera-controllable video generation. Existing memory-based approaches often condition generation on globally reconstructed 3D scenes by rendering anchor videos from the reconstructed geometry in the history. However, reconstructing a global 3D scene from multiple views inevitably introduces cross-view misalignment, as pose and depth estimation errors cause the same surfaces to be reconstructed at slightly different 3D locations across views. When fused, these inconsistencies accumulate into noisy geometry that contaminates the conditioning signals and degrades generation quality. We introduce AnchorWeave, a memory-augmented video generation framework that replaces a single misaligned global memory with multiple clean local geometric memories and learns to reconcile their cross-view inconsistencies. To this end, AnchorWeave performs coverage-driven local memory retrieval aligned with the target trajectory and integrates the selected local memories through a multi-anchor weaving controller during generation. Extensive experiments demonstrate that AnchorWeave significantly improves long-term scene consistency while maintaining strong visual quality, with ablation and analysis studies further validating the effectiveness of local geometric conditioning, multi-anchor control, and coverage-driven retrieval.

