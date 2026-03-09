---
layout: default
title: Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion
---

# Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion
**arXiv**：[2603.06577v1](https://arxiv.org/abs/2603.06577) · [PDF](https://arxiv.org/pdf/2603.06577.pdf)  
**作者**：Lijiang Li, Zuwei Long, Yunhang Shen, Heting Gao, Haoyu Cao, Xing Sun, Caifeng Shan, Ran He, Chaoyou Fu  

**一句话要点**：提出Omni-Diffusion，基于掩码离散扩散模型统一多模态理解与生成

**关键词**：多模态大语言模型, 离散扩散模型, 掩码建模, 统一理解与生成, 多模态令牌

## 3 点简述
- 核心问题：现有MLLMs多采用自回归架构，在架构设计上存在效率与效果提升空间
- 方法要点：使用掩码离散扩散模型直接建模离散多模态令牌的联合分布
- 实验或效果：在多种基准测试中优于或持平现有处理两模态以上的多模态系统

## 摘要（原文）

> While recent multimodal large language models (MLLMs) have made impressive strides, they predominantly employ a conventional autoregressive architecture as their backbone, leaving significant room to explore effective and efficient alternatives in architectural design. Concurrently, recent studies have successfully applied discrete diffusion models to various domains, such as visual understanding and image generation, revealing their considerable potential as a promising backbone for multimodal systems. Drawing inspiration from these pioneering research, we introduce Omni-Diffusion, the first any-to-any multimodal language model built entirely on mask-based discrete diffusion models, which unifies understanding and generation across text, speech, and images. Omni-Diffusion employs a unified mask-based discrete diffusion model to directly capture the joint distribution over discrete multimodal tokens. This approach supports not only bimodal tasks but also more complex scenarios involving multiple modalities. On a diverse set of benchmarks, our method outperforms or performs on par with existing multimodal systems that process two or more modalities, highlighting the significant promise of diffusion models in powering the next generation of multimodal foundation models. Project webpage: https://omni-diffusion.github.io.

