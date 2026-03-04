---
layout: default
title: From "What" to "How": Constrained Reasoning for Autoregressive Image Generation
---

# From "What" to "How": Constrained Reasoning for Autoregressive Image Generation
**arXiv**：[2603.02712v1](https://arxiv.org/abs/2603.02712) · [PDF](https://arxiv.org/pdf/2603.02712.pdf)  
**作者**：Ruxue Yan, Xubo Liu, Wenya Guo, Zhengkun Zhang, Ying Zhang, Xiaojie Yuan  

**一句话要点**：提出CoR-Painter框架，通过约束推理解决自回归图像生成中的空间模糊问题。

**关键词**：自回归图像生成, 约束推理, 空间关系建模, 双目标优化, 图像合成质量

## 3 点简述
- 核心问题：现有方法仅重写提示描述内容，缺乏对图像整体结构的推理，导致空间模糊和不现实重叠。
- 方法要点：引入约束推理，从输入提示推导视觉约束，指导生成详细描述，并采用双目标GRPO策略优化推理和投影过程。
- 实验或效果：在T2I-CompBench等基准测试中实现SOTA性能，空间指标显著提升，如T2I-CompBench上提高5.41%。

## 摘要（原文）

> Autoregressive image generation has seen recent improvements with the introduction of chain-of-thought and reinforcement learning. However, current methods merely specify "What" details to depict by rewriting the input prompt, yet fundamentally fail to reason about "How" to structure the overall image. This inherent limitation gives rise to persistent issues, such as spatial ambiguity directly causing unrealistic object overlaps. To bridge this gap, we propose CoR-Painter, a novel framework that pioneers a "How-to-What" paradigm by introducing Constrained Reasoning to guide the autoregressive generation. Specifically, it first deduces "How to draw" by deriving a set of visual constraints from the input prompt, which explicitly govern spatial relationships, key attributes, and compositional rules. These constraints steer the subsequent generation of a detailed description "What to draw", providing a structurally sound and coherent basis for accurate visual synthesis. Additionally, we introduce a Dual-Objective GRPO strategy that specifically optimizes the textual constrained reasoning and visual projection processes to ensure the coherence and quality of the entire generation pipeline. Extensive experiments on T2I-CompBench, GenEval, and WISE demonstrate that our method achieves state-of-the-art performance, with significant improvements in spatial metrics (e.g., +5.41% on T2I-CompBench).

