---
layout: default
title: Seeing Right but Saying Wrong: Inter- and Intra-Layer Refinement in MLLMs without Training
---

# Seeing Right but Saying Wrong: Inter- and Intra-Layer Refinement in MLLMs without Training
**arXiv**：[2601.07359v1](https://arxiv.org/abs/2601.07359) · [PDF](https://arxiv.org/pdf/2601.07359.pdf)  
**作者**：Shezheng Song, Shasha Li, Jie Yu  

**一句话要点**：提出DualPD解码策略以解决MLLMs中视觉注意不一致导致的预测错误问题

**关键词**：多模态大语言模型, 注意机制, 解码策略, 视觉语言任务, 无训练优化

## 3 点简述
- 核心问题：MLLMs内部深层注意正确但最终预测受早期层噪声注意误导，导致理解与表达不一致
- 方法要点：DualPD包含层间注意引导对比logits模块和头间信息过滤模块，无需训练提升视觉理解
- 实验或效果：在LLaVA和Qwen-VL模型上多基准测试显示，DualPD一致提高准确性，证实有效性和泛化性

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated strong capabilities across a variety of vision-language tasks. However, their internal reasoning often exhibits a critical inconsistency: although deeper layers may attend to the correct visual regions, final predictions are frequently misled by noisy attention from earlier layers. This results in a disconnect between what the model internally understands and what it ultimately expresses, a phenomenon we describe as seeing it right but saying it wrong. To address this issue, we propose DualPD, a dual-perspective decoding refinement strategy that enhances the visual understanding without any additional training. DualPD consists of two components. (1) The layer-wise attention-guided contrastive logits module captures how the belief in the correct answer evolves by comparing output logits between layers that exhibit the largest attention shift. (2) The head-wise information filtering module suppresses low-contribution attention heads that focus on irrelevant regions, thereby improving attention quality within each layer. Experiments conducted on both the LLaVA and Qwen-VL model families across multiple multimodal benchmarks demonstrate that DualPD consistently improves accuracy without training, confirming its effectiveness and generalizability. The code will be released upon publication.

