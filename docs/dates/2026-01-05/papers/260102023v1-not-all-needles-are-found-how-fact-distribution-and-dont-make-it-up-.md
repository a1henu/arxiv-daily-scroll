---
layout: default
title: Not All Needles Are Found: How Fact Distribution and Don't Make It Up Prompts Shape Literal Extraction, Logical Inference, and Hallucination Risks in Long-Context LLMs
---

# Not All Needles Are Found: How Fact Distribution and Don't Make It Up Prompts Shape Literal Extraction, Logical Inference, and Hallucination Risks in Long-Context LLMs
**arXiv**：[2601.02023v1](https://arxiv.org/abs/2601.02023) · [PDF](https://arxiv.org/pdf/2601.02023.pdf)  
**作者**：Amirali Ebrahimzadeh, Seyyed M. Salili  

**一句话要点**：研究事实分布与反幻觉提示对长上下文LLMs信息提取、推理和幻觉风险的影响

**关键词**：长上下文语言模型, 信息提取, 逻辑推理, 幻觉风险, 事实分布, 基准测试

## 3 点简述
- 核心问题：长上下文LLMs在信息提取和推理中的可靠性受上下文长度和事实分布影响
- 方法要点：引入扩展的针在干草堆基准，评估字面提取、逻辑推理和幻觉风险
- 实验或效果：发现性能随模型和条件变化，反幻觉提示可能降低准确性

## 摘要（原文）

> Large language models (LLMs) increasingly support very long input contexts. Yet it remains unclear how reliably they extract and infer information at scale. Performance varies with context length and strongly interacts with how information is distributed in real-world corpora. Motivated by these observations, we study how fact placement, corpus-level fact distributions, and Don't Make It Up prompts influence model behavior. We introduce an extended needle-in-a-haystack benchmark across four production-scale models: Gemini-2.5-flash, ChatGPT-5-mini, Claude-4.5-haiku, and Deepseek-v3.2-chat. Unlike prior work, we separately evaluate literal extraction, logical inference, and hallucination risk. Our study considers both positional effects and realistic distributions of evidence across long contexts, as well as prompts that explicitly discourage fabrication. We find that longer contexts alone do not guarantee better performance and can be detrimental when relevant evidence is diluted or widely dispersed. Performance varies substantially across models: some show severe degradation under realistic conditions, while others remain more robust at longer context lengths. Anti-hallucination (AH) instructions can make some models overly conservative, sharply reducing accuracy in literal extraction and logical inference. While we do not directly compare retrieval-augmented generation (RAG) and cache-augmented generation (CAG), our results suggest many failures stem from ineffective context utilization. Models often struggle to identify and prioritize relevant information even when it is present. These findings have direct practical implications, as enterprise workflows increasingly involve pasting large volumes of unfiltered documents into LLM prompts. Effective context length and model-specific robustness to long contexts are therefore critical for reliable LLM deployment in research and business.

