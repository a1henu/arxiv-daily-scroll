---
layout: default
title: Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination
---

# Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination
**arXiv**：[2602.09541v1](https://arxiv.org/abs/2602.09541) · [PDF](https://arxiv.org/pdf/2602.09541.pdf)  
**作者**：Ziqiang Shi, Rujie Liu, Shanshan Yu, Satoshi Munakata, Koichi Shirahata  

**一句话要点**：提出Scalpel方法，通过混合高斯桥对齐注意力激活流形，以缓解多模态大模型的幻觉问题。

**关键词**：多模态幻觉缓解, 注意力激活对齐, 高斯混合模型, 熵最优传输, 模型无关方法, 动态干预

## 3 点简述
- 核心问题：大型视觉语言模型因语言模型先验强和跨模态注意力未对齐，常产生与视觉内容不一致的幻觉输出。
- 方法要点：使用高斯混合模型捕捉注意力在信任与幻觉流形中的多峰分布，通过熵最优传输映射高斯组件，动态调整干预强度和方向。
- 实验或效果：在多个数据集和基准测试中，Scalpel有效缓解幻觉，优于先前方法，且无需额外计算，仅需单步解码。

## 摘要（原文）

> Rapid progress in large vision-language models (LVLMs) has achieved unprecedented performance in vision-language tasks. However, due to the strong prior of large language models (LLMs) and misaligned attention across modalities, LVLMs often generate outputs inconsistent with visual content - termed hallucination. To address this, we propose \textbf{Scalpel}, a method that reduces hallucination by refining attention activation distributions toward more credible regions. Scalpel predicts trusted attention directions for each head in Transformer layers during inference and adjusts activations accordingly. It employs a Gaussian mixture model to capture multi-peak distributions of attention in trust and hallucination manifolds, and uses entropic optimal transport (equivalent to Schrödinger bridge problem) to map Gaussian components precisely. During mitigation, Scalpel dynamically adjusts intervention strength and direction based on component membership and mapping relationships between hallucination and trust activations. Extensive experiments across multiple datasets and benchmarks demonstrate that Scalpel effectively mitigates hallucinations, outperforming previous methods and achieving state-of-the-art performance. Moreover, Scalpel is model- and data-agnostic, requiring no additional computation, only a single decoding step.

