---
layout: default
title: RAL2M: Retrieval Augmented Learning-To-Match Against Hallucination in Compliance-Guaranteed Service Systems
---

# RAL2M: Retrieval Augmented Learning-To-Match Against Hallucination in Compliance-Guaranteed Service Systems
**arXiv**：[2601.02917v1](https://arxiv.org/abs/2601.02917) · [PDF](https://arxiv.org/pdf/2601.02917.pdf)  
**作者**：Mengze Hong, Di Jiang, Jiangtao Wen, Zhiyang Su, Yawen Li, Yanjie Sun, Guan Wang, Chen Jason Zhang  

**一句话要点**：提出检索增强学习匹配框架以解决合规服务系统中的幻觉问题

**关键词**：检索增强学习, 幻觉缓解, 合规服务系统, 查询-响应匹配, 潜在集成策略, LLM重定位

## 3 点简述
- 核心问题：LLM驱动服务系统中幻觉影响合规响应，需显式知识基础。
- 方法要点：将LLM重定位为检索系统中的查询-响应匹配判断器，采用查询自适应潜在集成策略。
- 实验或效果：在大规模基准测试中显著优于基线，有效利用群体智慧。

## 摘要（原文）

> Hallucination is a major concern in LLM-driven service systems, necessitating explicit knowledge grounding for compliance-guaranteed responses. In this paper, we introduce Retrieval-Augmented Learning-to-Match (RAL2M), a novel framework that eliminates generation hallucination by repositioning LLMs as query-response matching judges within a retrieval-based system, providing a robust alternative to purely generative approaches. To further mitigate judgment hallucination, we propose a query-adaptive latent ensemble strategy that explicitly models heterogeneous model competence and interdependencies among LLMs, deriving a calibrated consensus decision. Extensive experiments on large-scale benchmarks demonstrate that the proposed method effectively leverages the "wisdom of the crowd" and significantly outperforms strong baselines. Finally, we discuss best practices and promising directions for further exploiting latent representations in future work.

