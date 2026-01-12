---
layout: default
title: VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck
---

# VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck
**arXiv**：[2601.05547v1](https://arxiv.org/abs/2601.05547) · [PDF](https://arxiv.org/pdf/2601.05547.pdf)  
**作者**：Feiran Zhang, Yixin Wu, Zhenghua Wang, Xiaohua Wang, Changze Lv, Xuanjing Huang, Xiaoqing Zheng  

**一句话要点**：提出VIB-Probe框架，基于变分信息瓶颈检测和缓解视觉语言模型中的幻觉问题。

**关键词**：视觉语言模型, 幻觉检测, 变分信息瓶颈, 注意力头分析, 推理干预, 多模态任务

## 3 点简述
- 核心问题：视觉语言模型易产生幻觉，现有方法忽视内部机制，直接探测高维状态困难。
- 方法要点：利用变分信息瓶颈理论提取层和头的判别模式，过滤语义噪声，并通过梯度识别因果影响头。
- 实验或效果：在多个基准测试中显著优于现有基线，提供推理时干预策略以缓解幻觉。

## 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated remarkable progress in multimodal tasks, but remain susceptible to hallucinations, where generated text deviates from the underlying visual content. Existing hallucination detection methods primarily rely on output logits or external verification tools, often overlooking their internal mechanisms. In this work, we investigate the outputs of internal attention heads, postulating that specific heads carry the primary signals for truthful generation.However, directly probing these high-dimensional states is challenging due to the entanglement of visual-linguistic syntax and noise. To address this, we propose VIB-Probe, a novel hallucination detection and mitigation framework leveraging the Variational Information Bottleneck (VIB) theory. Our method extracts discriminative patterns across layers and heads while filtering out semantic nuisances through the information bottleneck principle. Furthermore, by leveraging the gradients of our VIB probe, we identify attention heads with strong causal influence on hallucinations and introduce an inference-time intervention strategy for hallucination mitigation. Extensive experiments across diverse benchmarks demonstrate that VIB-Probe significantly outperforms existing baselines in both settings. Our code will be made publicly available.

