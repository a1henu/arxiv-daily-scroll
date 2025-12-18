---
layout: default
title: FlowBind: Efficient Any-to-Any Generation with Bidirectional Flows
---

# FlowBind: Efficient Any-to-Any Generation with Bidirectional Flows
**arXiv**：[2512.15420v1](https://arxiv.org/abs/2512.15420) · [PDF](https://arxiv.org/pdf/2512.15420.pdf)  
**作者**：Yeonwoo Cha, Semin Kim, Jinhyeon Kwon, Seunghoon Hong  

**一句话要点**：提出FlowBind框架，通过共享潜在空间和可逆流实现高效任意模态间生成。

**关键词**：任意模态生成, 流匹配, 可逆流, 共享潜在空间, 跨模态合成

## 3 点简述
- 核心问题：现有基于流的任意模态生成方法效率低，依赖大规模配对数据和高计算成本。
- 方法要点：联合优化共享潜在空间和模态特定可逆流，使用单一流匹配目标简化训练。
- 实验或效果：在文本、图像和音频上实现可比质量，参数减少6倍，训练加速10倍。

## 摘要（原文）

> Any-to-any generation seeks to translate between arbitrary subsets of modalities, enabling flexible cross-modal synthesis. Despite recent success, existing flow-based approaches are challenged by their inefficiency, as they require large-scale datasets often with restrictive pairing constraints, incur high computational cost from modeling joint distribution, and rely on complex multi-stage training. We propose FlowBind, an efficient framework for any-to-any generation. Our approach is distinguished by its simplicity: it learns a shared latent space capturing cross-modal information, with modality-specific invertible flows bridging this latent to each modality. Both components are optimized jointly under a single flow-matching objective, and at inference the invertible flows act as encoders and decoders for direct translation across modalities. By factorizing interactions through the shared latent, FlowBind naturally leverages arbitrary subsets of modalities for training, and achieves competitive generation quality while substantially reducing data requirements and computational cost. Experiments on text, image, and audio demonstrate that FlowBind attains comparable quality while requiring up to 6x fewer parameters and training 10x faster than prior methods. The project page with code is available at https://yeonwoo378.github.io/official_flowbind.

