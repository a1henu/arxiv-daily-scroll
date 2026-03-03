---
layout: default
title: EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and Post-Training
---

# EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and Post-Training
**arXiv**：[2603.02041v1](https://arxiv.org/abs/2603.02041) · [PDF](https://arxiv.org/pdf/2603.02041.pdf)  
**作者**：Aleksei Dorkin, Taido Purason, Emil Kalbaliyev, Hele-Andra Kuulmets, Marii Ojastu, Mark Fišel, Tanel Alumäe, Eleri Aedmaa, Krister Kruusmaa, Kairit Sirts  

**一句话要点**：提出通过持续预训练与后训练增强爱沙尼亚语在预训练多语言大模型中的能力

**关键词**：持续预训练, 多语言大模型, 爱沙尼亚语增强, 后训练对齐, 指令微调

## 3 点简述
- 核心问题：英语中心化训练导致小语种性能不足，需提升爱沙尼亚语能力
- 方法要点：基于Llama 3.1 8B，采用混合数据持续预训练，结合后训练对齐技术
- 实验或效果：在爱沙尼亚语基准上全面改进，同时保持英语性能

## 摘要（原文）

> Large language models (LLMs) are predominantly trained on English-centric data, resulting in uneven performance for smaller languages. We study whether continued pretraining (CPT) can substantially improve Estonian capabilities in a pretrained multilingual LLM while preserving its English and general reasoning performance. Using Llama 3.1 8B as the main base model, we perform CPT on a mixture that increases Estonian exposure while approximating the original training distribution through English replay and the inclusion of code, mathematics, and instruction-like data. We subsequently apply supervised fine-tuning, preference optimization, and chat vector merging to introduce robust instruction-following behavior. Evaluation on a comprehensive suite of Estonian benchmarks shows consistent gains in linguistic competence, knowledge, reasoning, translation quality, and instruction-following compared to the original base model and its instruction-tuned variant, while maintaining competitive performance on English benchmarks. These findings indicate that CPT, with an appropriately balanced data mixture, together with post-training alignment, can substantially improve single-language capabilities in pretrained multilingual LLMs.

