---
layout: default
title: MoVE: Mixture of Value Embeddings -- A New Axis for Scaling Parametric Memory in Autoregressive Models
---

# MoVE: Mixture of Value Embeddings -- A New Axis for Scaling Parametric Memory in Autoregressive Models
**arXiv**：[2601.22887v1](https://arxiv.org/abs/2601.22887) · [PDF](https://arxiv.org/pdf/2601.22887.pdf)  
**作者**：Yangyan Li  

**一句话要点**：提出MoVE机制以解决自回归模型中参数内存与计算成本耦合的问题

**关键词**：自回归建模, 参数内存扩展, 软门控机制, 文本生成, 图像生成, 计算效率

## 3 点简述
- 核心问题：自回归模型扩展参数内存需增加网络深度或宽度，导致计算成本成比例上升
- 方法要点：引入全局可学习值嵌入库和软门控机制，动态混合概念到值投影中
- 实验或效果：在文本和图像生成任务中，MoVE在相同计算预算下实现更低困惑度和更高保真度

## 摘要（原文）

> Autoregressive sequence modeling stands as the cornerstone of modern Generative AI, powering results across diverse modalities ranging from text generation to image generation. However, a fundamental limitation of this paradigm is the rigid structural coupling of model capacity to computational cost: expanding a model's parametric memory -- its repository of factual knowledge or visual patterns -- traditionally requires deepening or widening the network, which incurs a proportional rise in active FLOPs. In this work, we introduce $\textbf{MoVE (Mixture of Value Embeddings)}$, a mechanism that breaks this coupling and establishes a new axis for scaling capacity. MoVE decouples memory from compute by introducing a global bank of learnable value embeddings shared across all attention layers. For every step in the sequence, the model employs a differentiable soft gating mechanism to dynamically mix retrieved concepts from this bank into the standard value projection. This architecture allows parametric memory to be scaled independently of network depth by simply increasing the number of embedding slots. We validate MoVE through strictly controlled experiments on two representative applications of autoregressive modeling: Text Generation and Image Generation. In both domains, MoVE yields consistent performance improvements over standard and layer-wise memory baselines, enabling the construction of "memory-dense" models that achieve lower perplexity and higher fidelity than their dense counterparts at comparable compute budgets.

