---
layout: default
title: Text-Guided Layer Fusion Mitigates Hallucination in Multimodal LLMs
---

# Text-Guided Layer Fusion Mitigates Hallucination in Multimodal LLMs
**arXiv**：[2601.03100v1](https://arxiv.org/abs/2601.03100) · [PDF](https://arxiv.org/pdf/2601.03100.pdf)  
**作者**：Chenchen Lin, Sanbao Su, Rachel Luo, Yuxiao Chen, Yan Wang, Marco Pavone, Fei Miao  

**一句话要点**：提出文本引导层融合模块TGIF，以减轻多模态大语言模型的幻觉问题

**关键词**：多模态大语言模型, 视觉幻觉, 层融合, 文本引导, 视觉编码器, 基准测试

## 3 点简述
- 多模态大语言模型依赖单一视觉特征层，导致视觉线索利用不足和幻觉问题
- TGIF模块基于查询动态融合视觉编码器的多层特征，无需更新编码器
- 在LLaVA-1.5-7B中集成TGIF，在幻觉、OCR和VQA基准上取得一致改进

## 摘要（原文）

> Multimodal large language models (MLLMs) typically rely on a single late-layer feature from a frozen vision encoder, leaving the encoder's rich hierarchy of visual cues under-utilized. MLLMs still suffer from visually ungrounded hallucinations, often relying on language priors rather than image evidence. While many prior mitigation strategies operate on the text side, they leave the visual representation unchanged and do not exploit the rich hierarchy of features encoded across vision layers. Existing multi-layer fusion methods partially address this limitation but remain static, applying the same layer mixture regardless of the query. In this work, we introduce TGIF (Text-Guided Inter-layer Fusion), a lightweight module that treats encoder layers as depth-wise "experts" and predicts a prompt-dependent fusion of visual features. TGIF follows the principle of direct external fusion, requires no vision-encoder updates, and adds minimal overhead. Integrated into LLaVA-1.5-7B, TGIF provides consistent improvements across hallucination, OCR, and VQA benchmarks, while preserving or improving performance on ScienceQA, GQA, and MMBench. These results suggest that query-conditioned, hierarchy-aware fusion is an effective way to strengthen visual grounding and reduce hallucination in modern MLLMs.

