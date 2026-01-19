---
layout: default
title: Think-Clip-Sample: Slow-Fast Frame Selection for Video Understanding
---

# Think-Clip-Sample: Slow-Fast Frame Selection for Video Understanding
**arXiv**：[2601.11359v1](https://arxiv.org/abs/2601.11359) · [PDF](https://arxiv.org/pdf/2601.11359.pdf)  
**作者**：Wenhui Tan, Ruihua Song, Jiaze Li, Jianzhong Ju, Zhenbo Luo  

**一句话要点**：提出Think-Clip-Sample框架，通过多查询推理和片段级慢快采样提升长视频理解性能与效率。

**关键词**：长视频理解, 多模态大语言模型, 帧选择, 训练免费框架, 效率优化

## 3 点简述
- 核心问题：多模态大语言模型在长视频理解中受计算限制和帧选择不佳影响性能。
- 方法要点：采用训练免费框架，结合多查询推理捕获问题与视频互补方面，以及片段级慢快采样平衡局部细节与全局上下文。
- 实验或效果：在MLVU等基准上提升准确率最高6.9%，推理时间减少50%时仍保持可比性能。

## 摘要（原文）

> Recent progress in multi-modal large language models (MLLMs) has significantly advanced video understanding. However, their performance on long-form videos remains limited by computational constraints and suboptimal frame selection. We present Think-Clip-Sample (TCS), a training-free framework that enhances long video understanding through two key components: (i) Multi-Query Reasoning, which generates multiple queries to capture complementary aspects of the question and video; and (ii) Clip-level Slow-Fast Sampling, which adaptively balances dense local details and sparse global context. Extensive experiments on MLVU, LongVideoBench, and VideoMME demonstrate that TCS consistently improves performance across different MLLMs, boosting up to 6.9% accuracy, and is capable of achieving comparable accuracy with 50% fewer inference time cost, highlighting both efficiency and efficacy of TCS on long video understanding.

