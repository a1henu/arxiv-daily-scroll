---
layout: default
title: RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis
---

# RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis
**arXiv**：[2602.11506v1](https://arxiv.org/abs/2602.11506) · [PDF](https://arxiv.org/pdf/2602.11506.pdf)  
**作者**：Zhen Bi, Xueshu Chen, Luoyang Sun, Yuhang Yao, Qing Shen, Jungang Lou, Cheng Deng  

**一句话要点**：提出RooflineBench基准框架，通过Roofline分析评估设备端小语言模型性能

**关键词**：设备端语言模型, Roofline分析, 性能基准, 硬件异构性, 操作强度, 相对推理潜力

## 3 点简述
- 核心问题：异构硬件上设备端小语言模型性能评估缺乏统一标准
- 方法要点：基于Roofline模型，引入操作强度和相对推理潜力作为新指标
- 实验或效果：分析序列长度和模型深度对性能的影响，识别硬件异构性陷阱

## 摘要（原文）

> The transition toward localized intelligence through Small Language Models (SLMs) has intensified the need for rigorous performance characterization on resource-constrained edge hardware. However, objectively measuring the theoretical performance ceilings of diverse architectures across heterogeneous platforms remains a formidable challenge. In this work, we propose a systematic framework based on the Roofline model that unifies architectural primitives and hardware constraints through the lens of operational intensity (OI). By defining an inference-potential region, we introduce the Relative Inference Potential as a novel metric to compare efficiency differences between Large Language Models (LLMs) on the same hardware substrate. Extensive empirical analysis across diverse compute tiers reveals that variations in performance and OI are significantly influenced by sequence length. We further identify a critical regression in OI as model depth increases. Additionally, our findings highlight an efficiency trap induced by hardware heterogeneity and demonstrate how structural refinements, such as Multi-head Latent Attention (M LA), can effectively unlock latent inference potential across various hardware substrates. These insights provide actionable directions for hardware-software co-design to align neural structures with physical constraints in on-device intelligence. The released code is available in the Appendix C.

