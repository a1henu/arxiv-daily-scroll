---
layout: default
title: DANCE: Dynamic, Available, Neighbor-gated Condensation for Federated Text-Attributed Graphs
---

# DANCE: Dynamic, Available, Neighbor-gated Condensation for Federated Text-Attributed Graphs
**arXiv**：[2601.16519v1](https://arxiv.org/abs/2601.16519) · [PDF](https://arxiv.org/pdf/2601.16519.pdf)  
**作者**：Zekai Chen, Haodong Lu, Xunkai Li, Henan Sun, Jia Li, Hongchao Qin, Rong-Hua Li, Guoren Wang  

**一句话要点**：提出DANCE以解决联邦文本属性图学习中的开销、次优和可解释性问题

**关键词**：联邦图学习, 文本属性图, 图压缩, 大语言模型, 可解释性, 动态优化

## 3 点简述
- 核心问题：联邦文本属性图学习面临LLM处理长文本的高开销、固定压缩导致次优性能及黑盒摘要缺乏可解释性
- 方法要点：DANCE采用轮次动态压缩，利用最新全局模型刷新，并存储可本地检查的证据包以追踪预测来源
- 实验或效果：在8个数据集上，以8%压缩比提升准确率2.33%，令牌使用减少33.42%

## 摘要（原文）

> Federated graph learning (FGL) enables collaborative training on graph data across multiple clients. With the rise of large language models (LLMs), textual attributes in FGL graphs are gaining attention. Text-attributed graph federated learning (TAG-FGL) improves FGL by explicitly leveraging LLMs to process and integrate these textual features. However, current TAG-FGL methods face three main challenges: \textbf{(1) Overhead.} LLMs for processing long texts incur high token and computation costs. To make TAG-FGL practical, we introduce graph condensation (GC) to reduce computation load, but this choice also brings new issues. \textbf{(2) Suboptimal.} To reduce LLM overhead, we introduce GC into TAG-FGL by compressing multi-hop texts/neighborhoods into a condensed core with fixed LLM surrogates. However, this one-shot condensation is often not client-adaptive, leading to suboptimal performance. \textbf{(3) Interpretability.} LLM-based condensation further introduces a black-box bottleneck: summaries lack faithful attribution and clear grounding to specific source spans, making local inspection and auditing difficult. To address the above issues, we propose \textbf{DANCE}, a new TAG-FGL paradigm with GC. To improve \textbf{suboptimal} performance, DANCE performs round-wise, model-in-the-loop condensation refresh using the latest global model. To enhance \textbf{interpretability}, DANCE preserves provenance by storing locally inspectable evidence packs that trace predictions to selected neighbors and source text spans. Across 8 TAG datasets, DANCE improves accuracy by \textbf{2.33\%} at an \textbf{8\%} condensation ratio, with \textbf{33.42\%} fewer tokens than baselines.

