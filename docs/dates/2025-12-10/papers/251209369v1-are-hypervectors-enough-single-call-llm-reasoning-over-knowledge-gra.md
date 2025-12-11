---
layout: default
title: Are Hypervectors Enough? Single-Call LLM Reasoning over Knowledge Graphs
---

# Are Hypervectors Enough? Single-Call LLM Reasoning over Knowledge Graphs
**arXiv**：[2512.09369v1](https://arxiv.org/abs/2512.09369) · [PDF](https://arxiv.org/pdf/2512.09369.pdf)  
**作者**：Yezi Liu, William Youngwoo Chung, Hanning Chen, Calvin Yeung, Mohsen Imani  

**一句话要点**：提出PathHD框架，通过超维计算和单次LLM调用实现高效知识图谱推理

**关键词**：知识图谱推理, 超维计算, 大语言模型, 高效推理, 可解释性, 单次调用

## 3 点简述
- 核心问题：现有知识图谱推理方法依赖重神经编码器或多轮LLM调用，导致高延迟、高成本和不透明决策
- 方法要点：使用超维计算编码关系路径，基于块余弦相似度排序候选，单次LLM裁决生成答案和可解释路径
- 实验或效果：在多个数据集上达到或超越基线性能，降低延迟40-60%，减少GPU内存3-5倍，提供忠实路径解释

## 摘要（原文）

> Recent advances in large language models (LLMs) have enabled strong reasoning over both structured and unstructured knowledge. When grounded on knowledge graphs (KGs), however, prevailing pipelines rely on heavy neural encoders to embed and score symbolic paths or on repeated LLM calls to rank candidates, leading to high latency, GPU cost, and opaque decisions that hinder faithful, scalable deployment. We propose PathHD, a lightweight and encoder-free KG reasoning framework that replaces neural path scoring with hyperdimensional computing (HDC) and uses only a single LLM call per query. PathHD encodes relation paths into block-diagonal GHRR hypervectors, ranks candidates with blockwise cosine similarity and Top-K pruning, and then performs a one-shot LLM adjudication to produce the final answer together with cited supporting paths. Technically, PathHD is built on three ingredients: (i) an order-aware, non-commutative binding operator for path composition, (ii) a calibrated similarity for robust hypervector-based retrieval, and (iii) a one-shot adjudication step that preserves interpretability while eliminating per-path LLM scoring. On WebQSP, CWQ, and the GrailQA split, PathHD (i) attains comparable or better Hits@1 than strong neural baselines while using one LLM call per query; (ii) reduces end-to-end latency by $40-60\%$ and GPU memory by $3-5\times$ thanks to encoder-free retrieval; and (iii) delivers faithful, path-grounded rationales that improve error diagnosis and controllability. These results indicate that carefully designed HDC representations provide a practical substrate for efficient KG-LLM reasoning, offering a favorable accuracy-efficiency-interpretability trade-off.

