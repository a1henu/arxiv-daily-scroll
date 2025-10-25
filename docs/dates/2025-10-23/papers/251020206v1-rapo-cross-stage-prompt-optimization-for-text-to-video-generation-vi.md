---
layout: default
title: RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling
---

# RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling
**arXiv**：[2510.20206v1](https://arxiv.org/abs/2510.20206) · [PDF](https://arxiv.org/pdf/2510.20206.pdf)  
**作者**：Bingjie Gao, Qianli Ma, Xiaoxue Wu, Shuai Yang, Guanzhou Lan, Haonan Zhao, Jiaxuan Chen, Qingyang Liu, Yu Qiao, Xinyuan Chen, Yaohui Wang, Li Niu  

**一句话要点**：提出RAPO++框架以优化文本到视频生成的提示设计

**关键词**：文本到视频生成, 提示优化, 数据对齐, 测试时缩放, LLM微调, 扩散模型

## 3 点简述
- 用户提示短小、非结构化且与训练数据不匹配，限制扩散模型生成潜力
- 采用三阶段优化：数据对齐、测试时迭代缩放和LLM微调，无需修改生成主干
- 在多个模型和基准上显著提升语义对齐、组合推理、时间稳定性和物理合理性

## 摘要（原文）

> Prompt design plays a crucial role in text-to-video (T2V) generation, yet
> user-provided prompts are often short, unstructured, and misaligned with
> training data, limiting the generative potential of diffusion-based T2V models.
> We present \textbf{RAPO++}, a cross-stage prompt optimization framework that
> unifies training-data--aligned refinement, test-time iterative scaling, and
> large language model (LLM) fine-tuning to substantially improve T2V generation
> without modifying the underlying generative backbone. In \textbf{Stage 1},
> Retrieval-Augmented Prompt Optimization (RAPO) enriches user prompts with
> semantically relevant modifiers retrieved from a relation graph and refactors
> them to match training distributions, enhancing compositionality and
> multi-object fidelity. \textbf{Stage 2} introduces Sample-Specific Prompt
> Optimization (SSPO), a closed-loop mechanism that iteratively refines prompts
> using multi-source feedback -- including semantic alignment, spatial fidelity,
> temporal coherence, and task-specific signals such as optical flow -- yielding
> progressively improved video generation quality. \textbf{Stage 3} leverages
> optimized prompt pairs from SSPO to fine-tune the rewriter LLM, internalizing
> task-specific optimization patterns and enabling efficient, high-quality prompt
> generation even before inference. Extensive experiments across five
> state-of-the-art T2V models and five benchmarks demonstrate that RAPO++
> achieves significant gains in semantic alignment, compositional reasoning,
> temporal stability, and physical plausibility, outperforming existing methods
> by large margins. Our results highlight RAPO++ as a model-agnostic,
> cost-efficient, and scalable solution that sets a new standard for prompt
> optimization in T2V generation. The code is available at
> https://github.com/Vchitect/RAPO.

