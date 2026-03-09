---
layout: default
title: MoE Lens -- An Expert Is All You Need
---

# MoE Lens -- An Expert Is All You Need
**arXiv**：[2603.05806v1](https://arxiv.org/abs/2603.05806) · [PDF](https://arxiv.org/pdf/2603.05806.pdf)  
**作者**：Marmik Chaudhari, Idhant Gulati, Nishkal Hundia, Pranav Karra, Shivam Raval  

**一句话要点**：提出MoE Lens方法分析专家专业化，揭示稀疏激活模型依赖少数专家，为推理优化提供依据。

**关键词**：专家混合模型, 专家专业化分析, 路由分布, 推理优化, 模型剪枝, 知识定位

## 3 点简述
- 核心问题：MoE模型专家专业化行为理解不足，影响推理和内存成本优化。
- 方法要点：通过领域特定路由模式和早期解码框架，系统分析专家贡献和路由分布。
- 实验或效果：在DeepSeekMoE上验证，少数专家主导路由，单专家输出与全集成高度相似，困惑度仅增5%。

## 摘要（原文）

> Mixture of Experts (MoE) models enable parameter-efficient scaling through sparse expert activations, yet optimizing their inference and memory costs remains challenging due to limited understanding of their specialization behavior. We present a systematic analysis of expert specialization in MoEs through two complementary approaches: domain-specific routing patterns and an early decoding framework that tracks expert contributions to output representations. Our analysis of the DeepSeekMoE model reveals that despite having 64 routed experts with 6 active for each layer's computation, the model predominantly relies on a few specialized experts, with the top-weighted expert's output closely approximating the full ensemble prediction. We quantitatively validate these findings through a systematic analysis of the token routing distribution, demonstrating that very few experts handle over 50\% of routing decisions across different specialized domains. Hidden state similarity between single and ensemble experts for every layer is extremely high, with some layers having cosine similarity as high as 0.95 and perplexity increasing by only 5\% when using a single expert across all three domains. Our results indicate that Mixture of Experts models exhibit concentrated expertise highlighting potential opportunities for inference optimization through targeted expert pruning while maintaining model performance and opening avenues towards studying localization of learned knowledge in these models.

