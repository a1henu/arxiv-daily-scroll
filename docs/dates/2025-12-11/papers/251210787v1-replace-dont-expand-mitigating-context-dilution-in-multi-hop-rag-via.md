---
layout: default
title: Replace, Don't Expand: Mitigating Context Dilution in Multi-Hop RAG via Fixed-Budget Evidence Assembly
---

# Replace, Don't Expand: Mitigating Context Dilution in Multi-Hop RAG via Fixed-Budget Evidence Assembly
**arXiv**：[2512.10787v1](https://arxiv.org/abs/2512.10787) · [PDF](https://arxiv.org/pdf/2512.10787.pdf)  
**作者**：Moshe Lahmy, Roi Yozevitch  

**一句话要点**：提出SEAL-RAG方法，通过固定预算证据替换策略解决多跳RAG中的上下文稀释问题

**关键词**：检索增强生成, 多跳问答, 上下文管理, 实体锚定检索, 证据替换策略, 固定预算检索

## 3 点简述
- 多跳查询中初始检索遗漏桥接事实导致RAG系统失效，现有方法扩展上下文易引发信息稀释
- SEAL-RAG采用搜索-提取-评估-循环机制，通过实体锚定提取和针对性查询动态替换干扰证据
- 在HotpotQA和2WikiMultiHopQA上显著提升答案正确性和证据精度，保持可预测计算成本

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems often fail on multi-hop queries when the initial retrieval misses a bridge fact. Prior corrective approaches, such as Self-RAG, CRAG, and Adaptive-$k$, typically address this by \textit{adding} more context or pruning existing lists. However, simply expanding the context window often leads to \textbf{context dilution}, where distractors crowd out relevant information. We propose \textbf{SEAL-RAG}, a training-free controller that adopts a \textbf{``replace, don't expand''} strategy to fight context dilution under a fixed retrieval depth $k$. SEAL executes a (\textbf{S}earch $\rightarrow$ \textbf{E}xtract $\rightarrow$ \textbf{A}ssess $\rightarrow$ \textbf{L}oop) cycle: it performs on-the-fly, entity-anchored extraction to build a live \textit{gap specification} (missing entities/relations), triggers targeted micro-queries, and uses \textit{entity-first ranking} to actively swap out distractors for gap-closing evidence. We evaluate SEAL-RAG against faithful re-implementations of Basic RAG, CRAG, Self-RAG, and Adaptive-$k$ in a shared environment on \textbf{HotpotQA} and \textbf{2WikiMultiHopQA}. On HotpotQA ($k=3$), SEAL improves answer correctness by \textbf{+3--13 pp} and evidence precision by \textbf{+12--18 pp} over Self-RAG. On 2WikiMultiHopQA ($k=5$), it outperforms Adaptive-$k$ by \textbf{+8.0 pp} in accuracy and maintains \textbf{96\%} evidence precision compared to 22\% for CRAG. These gains are statistically significant ($p<0.001$). By enforcing fixed-$k$ replacement, SEAL yields a predictable cost profile while ensuring the top-$k$ slots are optimized for precision rather than mere breadth. We release our code and data at https://github.com/mosherino/SEAL-RAG.

