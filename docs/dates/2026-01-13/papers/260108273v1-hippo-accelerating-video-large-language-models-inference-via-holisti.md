---
layout: default
title: HIPPO: Accelerating Video Large Language Models Inference via Holistic-aware Parallel Speculative Decoding
---

# HIPPO: Accelerating Video Large Language Models Inference via Holistic-aware Parallel Speculative Decoding
**arXiv**：[2601.08273v1](https://arxiv.org/abs/2601.08273) · [PDF](https://arxiv.org/pdf/2601.08273.pdf)  
**作者**：Qitan Lv, Tianyu Liu, Wen Wu, Xuenan Xu, Bowen Zhou, Feng Wu, Chao Zhang  

**一句话要点**：提出HIPPO框架，通过整体感知并行推测解码加速视频大语言模型推理

**关键词**：视频大语言模型, 推测解码, 推理加速, 语义感知剪枝, 并行算法, 视觉语义保留

## 3 点简述
- 现有视频-LLM推测解码方法因视觉语义保留不足和草稿模型成本限制，加速效果不佳
- HIPPO融合全局注意力与局部语义以高剪枝率保留关键信息，并并行化草稿生成与验证阶段
- 在四个视频-LLM和六个基准测试中，HIPPO实现最高3.51倍加速，优于自回归解码

## 摘要（原文）

> Speculative decoding (SD) has emerged as a promising approach to accelerate LLM inference without sacrificing output quality. Existing SD methods tailored for video-LLMs primarily focus on pruning redundant visual tokens to mitigate the computational burden of massive visual inputs. However, existing methods do not achieve inference acceleration comparable to text-only LLMs. We observe from extensive experiments that this phenomenon mainly stems from two limitations: (i) their pruning strategies inadequately preserve visual semantic tokens, degrading draft quality and acceptance rates; (ii) even with aggressive pruning (e.g., 90% visual tokens removed), the draft model's remaining inference cost limits overall speedup. To address these limitations, we propose HIPPO, a general holistic-aware parallel speculative decoding framework. Specifically, HIPPO proposes (i) a semantic-aware token preservation method, which fuses global attention scores with local visual semantics to retain semantic information at high pruning ratios; (ii) a video parallel SD algorithm that decouples and overlaps draft generation and target verification phases. Experiments on four video-LLMs across six benchmarks demonstrate HIPPO's effectiveness, yielding up to 3.51x speedup compared to vanilla auto-regressive decoding.

