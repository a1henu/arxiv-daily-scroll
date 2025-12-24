---
layout: default
title: SweRank+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization
---

# SweRank+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization
**arXiv**：[2512.20482v1](https://arxiv.org/abs/2512.20482) · [PDF](https://arxiv.org/pdf/2512.20482.pdf)  
**作者**：Revanth Gangi Reddy, Ye Liu, Wenting Zhao, JaeHyeok Doo, Tarun Suresh, Daniel Lee, Caiming Xiong, Yingbo Zhou, Semih Yavuz, Shafiq Joty  

**一句话要点**：提出SweRank+框架，通过多轮推理提升多语言代码库问题定位的准确性。

**关键词**：代码排名, 多语言代码库, 问题定位, 多轮推理, 代理搜索, 跨语言嵌入

## 3 点简述
- 核心问题：现有代码排名方法多为Python中心且单次搜索，难以准确映射多语言代码库中的自然语言错误描述。
- 方法要点：结合SweRankMulti（跨语言代码排名工具）与SweRankAgent（代理搜索循环），实现迭代多轮推理。
- 实验或效果：在多语言基准测试中，SweRankMulti达到新SOTA，SweRankAgent进一步超越单次排名。

## 摘要（原文）

> Maintaining large-scale, multilingual codebases hinges on accurately localizing issues, which requires mapping natural-language error descriptions to the relevant functions that need to be modified. However, existing ranking approaches are often Python-centric and perform a single-pass search over the codebase. This work introduces SweRank+, a framework that couples SweRankMulti, a cross-lingual code ranking tool, with SweRankAgent, an agentic search setup, for iterative, multi-turn reasoning over the code repository. SweRankMulti comprises a code embedding retriever and a listwise LLM reranker, and is trained using a carefully curated large-scale issue localization dataset spanning multiple popular programming languages. SweRankAgent adopts an agentic search loop that moves beyond single-shot localization with a memory buffer to reason and accumulate relevant localization candidates over multiple turns. Our experiments on issue localization benchmarks spanning various languages demonstrate new state-of-the-art performance with SweRankMulti, while SweRankAgent further improves localization over single-pass ranking.

