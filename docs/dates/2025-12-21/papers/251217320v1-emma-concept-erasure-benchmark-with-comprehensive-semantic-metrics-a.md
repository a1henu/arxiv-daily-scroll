---
layout: default
title: EMMA: Concept Erasure Benchmark with Comprehensive Semantic Metrics and Diverse Categories
---

# EMMA: Concept Erasure Benchmark with Comprehensive Semantic Metrics and Diverse Categories
**arXiv**：[2512.17320v1](https://arxiv.org/abs/2512.17320) · [PDF](https://arxiv.org/pdf/2512.17320.pdf)  
**作者**：Lu Wei, Yuta Nakashima, Noa Garcia  

**一句话要点**：提出EMMA基准以全面评估文本到图像生成中的概念擦除技术

**关键词**：概念擦除, 文本到图像生成, 基准评估, 鲁棒性测试, 偏见分析, 隐私保护

## 3 点简述
- 核心问题：现有概念擦除方法评估局限，依赖简单提示，缺乏对隐式描述和偏见的测试
- 方法要点：EMMA基准涵盖12个指标，测试五个维度，包括鲁棒性、偏见和社会意识分析
- 实验或效果：分析五种方法，发现现有方法在隐式提示和视觉相似概念上表现不佳，部分放大偏见

## 摘要（原文）

> The widespread adoption of text-to-image (T2I) generation has raised concerns about privacy, bias, and copyright violations. Concept erasure techniques offer a promising solution by selectively removing undesired concepts from pre-trained models without requiring full retraining. However, these methods are often evaluated on a limited set of concepts, relying on overly simplistic and direct prompts. To test the boundaries of concept erasure techniques, and assess whether they truly remove targeted concepts from model representations, we introduce EMMA, a benchmark that evaluates five key dimensions of concept erasure over 12 metrics. EMMA goes beyond standard metrics like image quality and time efficiency, testing robustness under challenging conditions, including indirect descriptions, visually similar non-target concepts, and potential gender and ethnicity bias, providing a socially aware analysis of method behavior. Using EMMA, we analyze five concept erasure methods across five domains (objects, celebrities, art styles, NSFW, and copyright). Our results show that existing methods struggle with implicit prompts (i.e., generating the erased concept when it is indirectly referenced) and visually similar non-target concepts (i.e., failing to generate non-targeted concepts resembling the erased one), while some amplify gender and ethnicity bias compared to the original model.

