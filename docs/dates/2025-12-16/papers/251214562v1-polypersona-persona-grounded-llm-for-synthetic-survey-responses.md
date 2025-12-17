---
layout: default
title: Polypersona: Persona-Grounded LLM for Synthetic Survey Responses
---

# Polypersona: Persona-Grounded LLM for Synthetic Survey Responses
**arXiv**：[2512.14562v1](https://arxiv.org/abs/2512.14562) · [PDF](https://arxiv.org/pdf/2512.14562.pdf)  
**作者**：Tejaswani Dash, Dinesh Karri, Anudeep Vurity, Gautam Datla, Tazeem Ahmad, Saima Rafi, Rohith Tangudu  

**一句话要点**：提出PolyPersona框架，通过角色条件化微调生成多领域合成调查响应

**关键词**：角色条件化生成, 合成调查数据, LoRA微调, 多领域评估, 紧凑语言模型

## 3 点简述
- 核心问题：如何高效生成角色一致的多领域合成调查数据，以支持可控评估和偏见分析。
- 方法要点：使用LoRA适配器和4位量化指令微调紧凑模型，基于对话数据管道保留角色线索。
- 实验或效果：紧凑模型性能媲美更大基线，BLEU最高0.090，ROUGE-1最高0.429，验证了框架的有效性。

## 摘要（原文）

> This paper introduces PolyPersona, a generative framework for synthesizing persona-conditioned survey responses across multiple domains. The framework instruction-tunes compact chat models using parameter-efficient LoRA adapters with 4-bit quantization under a resource-adaptive training setup. A dialogue-based data pipeline explicitly preserves persona cues, ensuring consistent behavioral alignment across generated responses. Using this pipeline, we construct a dataset of 3,568 synthetic survey responses spanning ten domains and 433 distinct personas, enabling controlled instruction tuning and systematic multi-domain evaluation. We evaluate the generated responses using a multi-metric evaluation suite that combines standard text generation metrics, including BLEU, ROUGE, and BERTScore, with survey-specific metrics designed to assess structural coherence, stylistic consistency, and sentiment alignment.Experimental results show that compact models such as TinyLlama 1.1B and Phi-2 achieve performance comparable to larger 7B to 8B baselines, with a highest BLEU score of 0.090 and ROUGE-1 of 0.429. These findings demonstrate that persona-conditioned fine-tuning enables small language models to generate reliable and coherent synthetic survey data. The proposed framework provides an efficient and reproducible approach for survey data generation, supporting scalable evaluation while facilitating bias analysis through transparent and open protocols.

