---
layout: default
title: Efficient Adaptive Rejection Sampling for Accelerating Speculative Decoding in Large Language Models
---

# Efficient Adaptive Rejection Sampling for Accelerating Speculative Decoding in Large Language Models
**arXiv**：[2512.13194v1](https://arxiv.org/abs/2512.13194) · [PDF](https://arxiv.org/pdf/2512.13194.pdf)  
**作者**：Chendong Sun  

**一句话要点**：提出高效自适应拒绝采样以解决推测解码中随机拒绝问题

**关键词**：推测解码, 拒绝采样, 大语言模型加速, 自适应阈值, 推理效率

## 3 点简述
- 推测解码的拒绝采样机制依赖固定阈值，导致高不确定性场景下随机拒绝频发
- EARS方法动态调整接受阈值，基于目标模型预测不确定性，减少随机拒绝
- 实验显示EARS在GSM8K基准上提升吞吐量18.12%，精度仅下降0.84%

## 摘要（原文）

> Speculative Decoding is a prominent technique for accelerating the autoregressive inference of large language models (LLMs) by employing a fast draft model to propose candidate token sequences and a large target model to verify them in parallel. However, its core component -- the rejection sampling mechanism -- relies on a fixed, context-independent random threshold. This leads to a significant "random rejection" problem in high-uncertainty generation scenarios, where plausible candidate tokens are frequently rejected due to random chance, undermining inference efficiency. This paper introduces Efficient Adaptive Rejection Sampling (EARS), a novel method that dynamically adjusts the acceptance threshold by incorporating the target model's own predictive uncertainty, measured as \(1 - \max(P_{\mathrm{target}})\). By introducing a tolerance term proportional to this uncertainty, EARS intelligently relaxes the acceptance criterion when the model is uncertain, effectively reducing random rejections while maintaining strict standards when the model is confident. Experiments on creative writing and open-domain QA tasks demonstrate that EARS significantly enhances the efficiency of speculative decoding, achieving up to an 18.12% increase in throughput with a negligible 0.84% accuracy drop on the GSM8K benchmark. The method requires no modifications to model architectures and can be seamlessly integrated into existing speculative decoding frameworks.

