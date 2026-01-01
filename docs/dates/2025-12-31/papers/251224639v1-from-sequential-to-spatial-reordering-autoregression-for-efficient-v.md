---
layout: default
title: From Sequential to Spatial: Reordering Autoregression for Efficient Visual Generation
---

# From Sequential to Spatial: Reordering Autoregression for Efficient Visual Generation
**arXiv**：[2512.24639v1](https://arxiv.org/abs/2512.24639) · [PDF](https://arxiv.org/pdf/2512.24639.pdf)  
**作者**：Siyang Wang, Hanting Li, Wei Li, Jie Hu, Xinghao Chen, Feng Zhao  

**一句话要点**：提出RadAR框架，通过径向并行预测和动态输出校正，提升自回归视觉生成的推理效率。

**关键词**：自回归视觉生成, 并行推理, 径向拓扑, 嵌套注意力, 高效生成

## 3 点简述
- 核心问题：传统自回归模型顺序解码导致视觉生成推理效率低下。
- 方法要点：基于径向拓扑组织生成过程，实现环状并行预测，并引入嵌套注意力机制校正输出。
- 实验或效果：未知，但设计旨在显著提高并行化并保持场景结构一致性。

## 摘要（原文）

> Inspired by the remarkable success of autoregressive models in language modeling, this paradigm has been widely adopted in visual generation. However, the sequential token-by-token decoding mechanism inherent in traditional autoregressive models leads to low inference efficiency.In this paper, we propose RadAR, an efficient and parallelizable framework designed to accelerate autoregressive visual generation while preserving its representational capacity. Our approach is motivated by the observation that visual tokens exhibit strong local dependencies and spatial correlations with their neighbors--a property not fully exploited in standard raster-scan decoding orders. Specifically, we organize the generation process around a radial topology: an initial token is selected as the starting point, and all other tokens are systematically grouped into multiple concentric rings according to their spatial distances from this center. Generation then proceeds in a ring-wise manner, from inner to outer regions, enabling the parallel prediction of all tokens within the same ring. This design not only preserves the structural locality and spatial coherence of visual scenes but also substantially increases parallelization. Furthermore, to address the risk of inconsistent predictions arising from simultaneous token generation with limited context, we introduce a nested attention mechanism. This mechanism dynamically refines implausible outputs during the forward pass, thereby mitigating error accumulation and preventing model collapse. By integrating radial parallel prediction with dynamic output correction, RadAR significantly improves generation efficiency.

