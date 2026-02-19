---
layout: default
title: Retrieval Collapses When AI Pollutes the Web
---

# Retrieval Collapses When AI Pollutes the Web
**arXiv**：[2602.16136v1](https://arxiv.org/abs/2602.16136) · [PDF](https://arxiv.org/pdf/2602.16136.pdf)  
**作者**：Hongyeon Yu, Dongchan Kim, Young-Bum Kim  

**一句话要点**：提出检索崩溃概念以揭示AI生成内容污染网络对信息检索的结构性风险

**关键词**：检索崩溃, AI生成内容污染, 信息检索风险, 检索增强生成, 对抗性内容, 网络基础系统

## 3 点简述
- 核心问题：AI生成内容在网络中泛滥，导致检索系统依赖合成证据，引发检索崩溃，侵蚀信息源多样性。
- 方法要点：通过控制实验分析高质量SEO内容和对抗性内容对检索的影响，定义检索崩溃为两阶段过程。
- 实验或效果：SEO污染下，67%池污染导致超80%暴露污染，对抗污染中，BM25基线暴露约19%有害内容，LLM排序器抑制能力更强。

## 摘要（原文）

> The rapid proliferation of AI-generated content on the Web presents a structural risk to information retrieval, as search engines and Retrieval-Augmented Generation (RAG) systems increasingly consume evidence produced by the Large Language Models (LLMs). We characterize this ecosystem-level failure mode as Retrieval Collapse, a two-stage process where (1) AI-generated content dominates search results, eroding source diversity, and (2) low-quality or adversarial content infiltrates the retrieval pipeline. We analyzed this dynamic through controlled experiments involving both high-quality SEO-style content and adversarially crafted content. In the SEO scenario, a 67\% pool contamination led to over 80\% exposure contamination, creating a homogenized yet deceptively healthy state where answer accuracy remains stable despite the reliance on synthetic sources. Conversely, under adversarial contamination, baselines like BM25 exposed $\sim$19\% of harmful content, whereas LLM-based rankers demonstrated stronger suppression capabilities. These findings highlight the risk of retrieval pipelines quietly shifting toward synthetic evidence and the need for retrieval-aware strategies to prevent a self-reinforcing cycle of quality decline in Web-grounded systems.

