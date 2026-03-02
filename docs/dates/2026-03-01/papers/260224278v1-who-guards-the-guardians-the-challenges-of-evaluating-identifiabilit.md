---
layout: default
title: Who Guards the Guardians? The Challenges of Evaluating Identifiability of Learned Representations
---

# Who Guards the Guardians? The Challenges of Evaluating Identifiability of Learned Representations
**arXiv**：[2602.24278v1](https://arxiv.org/abs/2602.24278) · [PDF](https://arxiv.org/pdf/2602.24278.pdf)  
**作者**：Shruti Joshi, Théo Saulus, Wieland Brendel, Philippe Brouillard, Dhanya Sridhar, Patrik Reizinger  

**一句话要点**：揭示评估指标在表示学习可识别性中的局限性并提出验证框架

**关键词**：表示学习, 可识别性评估, 评估指标, 数据生成过程, 编码器几何, 压力测试

## 3 点简述
- 核心问题：标准评估指标在可识别性评估中可能产生误判，因隐含数据生成和编码器假设
- 方法要点：建立分类法分离数据生成假设与编码器几何，界定现有指标的有效域
- 实验或效果：发布评估套件用于可重复的压力测试和比较，验证指标失效场景

## 摘要（原文）

> Identifiability in representation learning is commonly evaluated using standard metrics (e.g., MCC, DCI, R^2) on synthetic benchmarks with known ground-truth factors. These metrics are assumed to reflect recovery up to the equivalence class guaranteed by identifiability theory. We show that this assumption holds only under specific structural conditions: each metric implicitly encodes assumptions about both the data-generating process (DGP) and the encoder. When these assumptions are violated, metrics become misspecified and can produce systematic false positives and false negatives. Such failures occur both within classical identifiability regimes and in post-hoc settings where identifiability is most needed. We introduce a taxonomy separating DGP assumptions from encoder geometry, use it to characterise the validity domains of existing metrics, and release an evaluation suite for reproducible stress testing and comparison.

