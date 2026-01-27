---
layout: default
title: Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM
---

# Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM
**arXiv**：[2601.18306v1](https://arxiv.org/abs/2601.18306) · [PDF](https://arxiv.org/pdf/2601.18306.pdf)  
**作者**：Everlyn Asiko Chimoto, Mostafa Elhoushi, Bruce A. Bassett  

**一句话要点**：提出多语言校准集以提升量化多语言大语言模型的性能

**关键词**：量化校准, 多语言模型, 性能优化, 语言对齐, 激活分布

## 3 点简述
- 量化多语言大模型时，仅用英语校准集导致性能下降，问题未充分探索
- 系统评估单语言和多语言校准集，发现非英语和混合集显著降低困惑度
- 实验显示校准集与评估语言对齐时改进最大，激活范围差异影响特定组合

## 摘要（原文）

> Quantization is an effective technique for reducing the storage footprint and computational costs of Large Language Models (LLMs), but it often results in performance degradation. Existing post-training quantization methods typically use small, English-only calibration sets; however, their impact on multilingual models remains underexplored. We systematically evaluate eight calibration settings (five single-language and three multilingual mixes) on two quantizers (GPTQ, AWQ) on data from 10 languages. Our findings reveal a consistent trend: non-English and multilingual calibration sets significantly improve perplexity compared to English-only baselines. Specifically, we observe notable average perplexity gains across both quantizers on Llama3.1 8B and Qwen2.5 7B, with multilingual mixes achieving the largest overall reductions of up to 3.52 points in perplexity. Furthermore, our analysis indicates that tailoring calibration sets to the evaluation language yields the largest improvements for individual languages, underscoring the importance of linguistic alignment. We also identify specific failure cases where certain language-quantizer combinations degrade performance, which we trace to differences in activation range distributions across languages. These results highlight that static one-size-fits-all calibration is suboptimal and that tailoring calibration data, both in language and diversity, plays a crucial role in robustly quantizing multilingual LLMs.

