---
layout: default
title: Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks
---

# Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks
**arXiv**：[2602.06526v1](https://arxiv.org/abs/2602.06526) · [PDF](https://arxiv.org/pdf/2602.06526.pdf)  
**作者**：Minjeong Ban, Jeonghwan Choi, Hyangsuk Min, Nicole Hee-Yeon Kim, Minseok Kim, Jae-Gil Lee, Hwanjun Song  

**一句话要点**：提出DREAM框架以解决信息检索基准中缺失标注问题，通过多智能体辩论提升标注准确性和可扩展性。

**关键词**：信息检索评估, 多智能体辩论, 基准数据集, 标注准确性, 可扩展标注, 检索增强生成

## 3 点简述
- 核心问题：信息检索基准数据集存在未标注相关块，导致评估偏差和系统排名失真。
- 方法要点：基于LLM智能体构建多轮辩论框架，通过对立初始立场和迭代互评实现准确标注和可靠人机升级。
- 实验或效果：标注准确率达95.2%，仅需3.5%人工参与，并构建BRIDGE基准揭示29,824个缺失相关块。

## 摘要（原文）

> Information retrieval (IR) evaluation remains challenging due to incomplete IR benchmark datasets that contain unlabeled relevant chunks. While LLMs and LLM-human hybrid strategies reduce costly human effort, they remain prone to LLM overconfidence and ineffective AI-to-human escalation. To address this, we propose DREAM, a multi-round debate-based relevance assessment framework with LLM agents, built on opposing initial stances and iterative reciprocal critique. Through our agreement-based debate, it yields more accurate labeling for certain cases and more reliable AI-to-human escalation for uncertain ones, achieving 95.2% labeling accuracy with only 3.5% human involvement. Using DREAM, we build BRIDGE, a refined benchmark that mitigates evaluation bias and enables fairer retriever comparison by uncovering 29,824 missing relevant chunks. We then re-benchmark IR systems and extend evaluation to RAG, showing that unaddressed holes not only distort retriever rankings but also drive retrieval-generation misalignment. The relevance assessment framework is available at https: //github.com/DISL-Lab/DREAM-ICLR-26; and the BRIDGE dataset is available at https://github.com/DISL-Lab/BRIDGE-Benchmark.

