---
layout: default
title: RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis
---

# RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis
**arXiv**：[2602.11506v1](https://arxiv.org/abs/2602.11506) · [PDF](https://arxiv.org/pdf/2602.11506.pdf)  
**作者**：Zhen Bi, Xueshu Chen, Luoyang Sun, Yuhang Yao, Qing Shen, Jungang Lou, Cheng Deng  

**一句话要点**：提出RooflineBench基准框架，通过屋顶线分析评估设备端小语言模型性能

**关键词**：设备端语言模型, 屋顶线分析, 操作强度, 异构硬件, 性能基准, 硬件软件协同设计

## 3 点简述
- 核心问题：设备端小语言模型在异构硬件上的理论性能上限难以客观衡量
- 方法要点：基于屋顶线模型，通过操作强度统一架构原语和硬件约束，引入相对推理潜力指标
- 实验或效果：分析显示序列长度和模型深度显著影响性能，结构优化如多头潜在注意力可提升效率

## 摘要（原文）

> The transition toward localized intelligence through Small Language Models (SLMs) has intensified the need for rigorous performance characterization on resource-constrained edge hardware. However, objectively measuring the theoretical performance ceilings of diverse architectures across heterogeneous platforms remains a formidable challenge. In this work, we propose a systematic framework based on the Roofline model that unifies architectural primitives and hardware constraints through the lens of operational intensity (OI). By defining an inference-potential region, we introduce the Relative Inference Potential as a novel metric to compare efficiency differences between Large Language Models (LLMs) on the same hardware substrate. Extensive empirical analysis across diverse compute tiers reveals that variations in performance and OI are significantly influenced by sequence length. We further identify a critical regression in OI as model depth increases. Additionally, our findings highlight an efficiency trap induced by hardware heterogeneity and demonstrate how structural refinements, such as Multi-head Latent Attention (M LA), can effectively unlock latent inference potential across various hardware substrates. These insights provide actionable directions for hardware-software co-design to align neural structures with physical constraints in on-device intelligence. The released code is available in the Appendix C.

