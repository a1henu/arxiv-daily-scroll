---
layout: default
title: Rethinking Large Language Models For Irregular Time Series Classification In Critical Care
---

# Rethinking Large Language Models For Irregular Time Series Classification In Critical Care
**arXiv**：[2601.16516v1](https://arxiv.org/abs/2601.16516) · [PDF](https://arxiv.org/pdf/2601.16516.pdf)  
**作者**：Feixiang Zheng, Yu Wu, Cecilia Mascolo, Ting Dang  

**一句话要点**：评估大语言模型在ICU不规则时间序列分类中的编码器与对齐策略

**关键词**：不规则时间序列, 大语言模型, ICU监测, 编码器设计, 多模态对齐, 分类性能

## 3 点简述
- 核心问题：大语言模型在ICU高缺失率不规则时间序列上的有效性未知
- 方法要点：系统测试编码器设计和对齐策略对性能的影响
- 实验或效果：编码器建模不规则性提升性能，但训练时间长且数据稀缺时表现不佳

## 摘要（原文）

> Time series data from the Intensive Care Unit (ICU) provides critical information for patient monitoring. While recent advancements in applying Large Language Models (LLMs) to time series modeling (TSM) have shown great promise, their effectiveness on the irregular ICU data, characterized by particularly high rates of missing values, remains largely unexplored. This work investigates two key components underlying the success of LLMs for TSM: the time series encoder and the multimodal alignment strategy. To this end, we establish a systematic testbed to evaluate their impact across various state-of-the-art LLM-based methods on benchmark ICU datasets against strong supervised and self-supervised baselines. Results reveal that the encoder design is more critical than the alignment strategy. Encoders that explicitly model irregularity achieve substantial performance gains, yielding an average AUPRC increase of $12.8\%$ over the vanilla Transformer. While less impactful, the alignment strategy is also noteworthy, with the best-performing semantically rich, fusion-based strategy achieving a modest $2.9\%$ improvement over cross-attention. However, LLM-based methods require at least 10$\times$ longer training than the best-performing irregular supervised models, while delivering only comparable performance. They also underperform in data-scarce few-shot learning settings. These findings highlight both the promise and current limitations of LLMs for irregular ICU time series. The code is available at https://github.com/mHealthUnimelb/LLMTS.

