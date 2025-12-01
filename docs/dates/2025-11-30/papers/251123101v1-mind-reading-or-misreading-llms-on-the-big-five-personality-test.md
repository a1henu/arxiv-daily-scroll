---
layout: default
title: Mind Reading or Misreading? LLMs on the Big Five Personality Test
---

# Mind Reading or Misreading? LLMs on the Big Five Personality Test
**arXiv**：[2511.23101v1](https://arxiv.org/abs/2511.23101) · [PDF](https://arxiv.org/pdf/2511.23101.pdf)  
**作者**：Francesco Di Cursi, Chiara Boldrini, Marco Conti, Andrea Passarella  

**一句话要点**：评估大语言模型在二元五因素模型下自动人格预测的适用性，揭示其局限与改进方向。

**关键词**：自动人格预测, 大语言模型评估, 五因素模型, 提示策略, 零样本学习, 性能偏差分析

## 3 点简述
- 核心问题：评估大语言模型在零样本二元五因素模型下自动人格预测的可靠性与偏差。
- 方法要点：测试五种模型，包括GPT-4和开源替代，使用最小与富提示策略，分析三类数据集。
- 实验或效果：富提示减少无效输出但引入预测偏差，开放性和宜人性相对易检测，整体性能不稳定。

## 摘要（原文）

> We evaluate large language models (LLMs) for automatic personality prediction from text under the binary Five Factor Model (BIG5). Five models -- including GPT-4 and lightweight open-source alternatives -- are tested across three heterogeneous datasets (Essays, MyPersonality, Pandora) and two prompting strategies (minimal vs. enriched with linguistic and psychological cues). Enriched prompts reduce invalid outputs and improve class balance, but also introduce a systematic bias toward predicting trait presence. Performance varies substantially: Openness and Agreeableness are relatively easier to detect, while Extraversion and Neuroticism remain challenging. Although open-source models sometimes approach GPT-4 and prior benchmarks, no configuration yields consistently reliable predictions in zero-shot binary settings. Moreover, aggregate metrics such as accuracy and macro-F1 mask significant asymmetries, with per-class recall offering clearer diagnostic value. These findings show that current out-of-the-box LLMs are not yet suitable for APPT, and that careful coordination of prompt design, trait framing, and evaluation metrics is essential for interpretable results.

