---
layout: default
title: Forge-and-Quench: Enhancing Image Generation for Higher Fidelity in Unified Multimodal Models
---

# Forge-and-Quench: Enhancing Image Generation for Higher Fidelity in Unified Multimodal Models
**arXiv**：[2601.04706v1](https://arxiv.org/abs/2601.04706) · [PDF](https://arxiv.org/pdf/2601.04706.pdf)  
**作者**：Yanbing Zeng, Jia Wang, Hanghang Ma, Junqiang Wu, Jie Zhu, Xiaoming Wei, Jie Hu  

**一句话要点**：提出Forge-and-Quench框架，通过理解模型增强统一多模态模型的图像生成保真度

**关键词**：图像生成保真度, 统一多模态模型, Bridge Feature, Bridge Adapter, 视觉引导信号, 训练效率

## 3 点简述
- 核心问题：统一多模态模型中理解如何有效辅助图像生成保真度与细节丰富性
- 方法要点：利用MLLM推理生成增强文本指令，通过Bridge Adapter映射为Bridge Feature视觉引导信号
- 实验或效果：在多个模型上显著提升图像保真度和细节，保持指令跟随准确性并增强世界知识应用

## 摘要（原文）

> Integrating image generation and understanding into a single framework has become a pivotal goal in the multimodal domain. However, how understanding can effectively assist generation has not been fully explored. Unlike previous works that focus on leveraging reasoning abilities and world knowledge from understanding models, this paper introduces a novel perspective: leveraging understanding to enhance the fidelity and detail richness of generated images. To this end, we propose Forge-and-Quench, a new unified framework that puts this principle into practice. In the generation process of our framework, an MLLM first reasons over the entire conversational context, including text instructions, to produce an enhanced text instruction. This refined instruction is then mapped to a virtual visual representation, termed the Bridge Feature, via a novel Bridge Adapter. This feature acts as a crucial link, forging insights from the understanding model to quench and refine the generation process. It is subsequently injected into the T2I backbone as a visual guidance signal, alongside the enhanced text instruction that replaces the original input. To validate this paradigm, we conduct comprehensive studies on the design of the Bridge Feature and Bridge Adapter. Our framework demonstrates exceptional extensibility and flexibility, enabling efficient migration across different MLLM and T2I models with significant savings in training overhead, all without compromising the MLLM's inherent multimodal understanding capabilities. Experiments show that Forge-and-Quench significantly improves image fidelity and detail across multiple models, while also maintaining instruction-following accuracy and enhancing world knowledge application. Models and codes are available at https://github.com/YanbingZeng/Forge-and-Quench.

