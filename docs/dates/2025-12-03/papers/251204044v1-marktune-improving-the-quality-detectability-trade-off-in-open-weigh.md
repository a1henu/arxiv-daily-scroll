---
layout: default
title: MarkTune: Improving the Quality-Detectability Trade-off in Open-Weight LLM Watermarking
---

# MarkTune: Improving the Quality-Detectability Trade-off in Open-Weight LLM Watermarking
**arXiv**：[2512.04044v1](https://arxiv.org/abs/2512.04044) · [PDF](https://arxiv.org/pdf/2512.04044.pdf)  
**作者**：Yizhou Zhao, Zhiwei Steven Wu, Adam Block  

**一句话要点**：提出MarkTune框架以改善开源大语言模型水印的质量与可检测性权衡

**关键词**：开源大语言模型, 水印技术, 策略微调, 质量检测权衡, 泛化能力

## 3 点简述
- 核心问题：开源模型水印需平衡检测能力与文本质量，现有方法如GaussMark存在质量下降问题。
- 方法要点：基于理论推导，采用策略微调框架，将水印信号作为奖励并正则化以保持质量。
- 实验或效果：提升GaussMark的权衡曲线，接近推理时水印性能，并展示抗攻击和泛化能力。

## 摘要（原文）

> Watermarking aims to embed hidden signals in generated text that can be reliably detected when given access to a secret key. Open-weight language models pose acute challenges for such watermarking schemes because the inference-time interventions that dominate contemporary approaches cannot be enforced once model weights are public. Existing watermaking techniques for open-weight models, such as the recently proposed GaussMark, typically rely on small modifications to model weights, which can yield signals detectable to those equipped with a secret key, but achieving detection power comparable to inference-time watermarks generally requires weight perturbations that noticeably reduce generation quality. We introduce MarkTune, a theoretically principled, on-policy fine-tuning framework that treats the GaussMark signal as a reward while simultaneously regularizing against degradation in text quality. We derive MarkTune as an improvement on GaussMark and demonstrate that MarkTune consistently improves the quality-detectability trade-off over GaussMark by steering finer-grained, watermark-aware weight updates within the model's representation space while preserving generation quality. Empirically, we show that MarkTune pushes the quality-detectability frontier of GaussMark close to that of inference-time watermarking, remains robust to paraphrasing and fine-tuning attacks, and exhibits strong generalization: a model fine-tuned on one dataset retains substantial watermark detection power on unseen datasets. Together, these results establish MarkTune as a general strategy for embedding robust, high-quality watermarks into open-weight LMs.

