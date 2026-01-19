---
layout: default
title: Unlocking the Potentials of Retrieval-Augmented Generation for Diffusion Language Models
---

# Unlocking the Potentials of Retrieval-Augmented Generation for Diffusion Language Models
**arXiv**：[2601.11342v1](https://arxiv.org/abs/2601.11342) · [PDF](https://arxiv.org/pdf/2601.11342.pdf)  
**作者**：Chuanyue Yu, Jiahui Wang, Yuhan Li, Heng Chang, Ge Lan, Qingyun Sun, Jia Li, Jianxin Li, Ziwei Zhang  

**一句话要点**：提出SPREAD框架以解决扩散语言模型在检索增强生成中的语义漂移问题

**关键词**：扩散语言模型, 检索增强生成, 语义漂移, 去噪策略, 查询相关性引导

## 3 点简述
- 核心问题：扩散语言模型在RAG中因去噪策略导致响应语义漂移，生成精度低
- 方法要点：引入查询相关性引导的去噪策略，主动控制去噪轨迹以保持语义对齐
- 实验或效果：SPREAD显著提升生成精度，有效缓解语义漂移，增强RAG性能

## 摘要（原文）

> Diffusion Language Models (DLMs) have recently demonstrated remarkable capabilities in natural language processing tasks. However, the potential of Retrieval-Augmented Generation (RAG), which shows great successes for enhancing large language models (LLMs), has not been well explored, due to the fundamental difference between LLM and DLM decoding. To fill this critical gap, we systematically test the performance of DLMs within the RAG framework. Our findings reveal that DLMs coupled with RAG show promising potentials with stronger dependency on contextual information, but suffer from limited generation precision. We identify a key underlying issue: Response Semantic Drift (RSD), where the generated answer progressively deviates from the query's original semantics, leading to low precision content. We trace this problem to the denoising strategies in DLMs, which fail to maintain semantic alignment with the query throughout the iterative denoising process. To address this, we propose Semantic-Preserving REtrieval-Augmented Diffusion (SPREAD), a novel framework that introduces a query-relevance-guided denoising strategy. By actively guiding the denoising trajectory, SPREAD ensures the generation remains anchored to the query's semantics and effectively suppresses drift. Experimental results demonstrate that SPREAD significantly enhances the precision and effectively mitigates RSD of generated answers within the RAG framework.

