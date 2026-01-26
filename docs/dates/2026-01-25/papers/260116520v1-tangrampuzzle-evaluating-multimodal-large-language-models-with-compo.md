---
layout: default
title: TangramPuzzle: Evaluating Multimodal Large Language Models with Compositional Spatial Reasoning
---

# TangramPuzzle: Evaluating Multimodal Large Language Models with Compositional Spatial Reasoning
**arXiv**：[2601.16520v1](https://arxiv.org/abs/2601.16520) · [PDF](https://arxiv.org/pdf/2601.16520.pdf)  
**作者**：Daixian Liu, Jiayi Kuang, Yinghui Li, Yangning Li, Di Yin, Haoyu Cao, Xing Sun, Ying Shen, Hai-Tao Zheng, Liang Lin, Philip S. Yu  

**一句话要点**：提出TangramPuzzle基准，通过七巧板游戏评估多模态大语言模型的组合空间推理能力。

**关键词**：多模态大语言模型, 组合空间推理, 几何基准, 七巧板游戏, 符号几何框架, 评估指标

## 3 点简述
- 现有基准在组合空间推理评估上存在简单任务和语义近似问题，缺乏严格数学公式。
- 引入Tangram Construction Expression符号几何框架，基于精确坐标规范减少视觉模糊性。
- 实验显示模型倾向于匹配目标轮廓而忽略几何约束，导致部件变形或失真。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable progress in visual recognition and semantic understanding. Nevertheless, their ability to perform precise compositional spatial reasoning remains largely unexplored. Existing benchmarks often involve relatively simple tasks and rely on semantic approximations or coarse relative positioning, while their evaluation metrics are typically limited and lack rigorous mathematical formulations. To bridge this gap, we introduce TangramPuzzle, a geometry-grounded benchmark designed to evaluate compositional spatial reasoning through the lens of the classic Tangram game. We propose the Tangram Construction Expression (TCE), a symbolic geometric framework that grounds tangram assemblies in exact, machine-verifiable coordinate specifications, to mitigate the ambiguity of visual approximation. We design two complementary tasks: Outline Prediction, which demands inferring global shapes from local components, and End-to-End Code Generation, which requires solving inverse geometric assembly problems. We conduct extensive evaluation experiments on advanced open-source and proprietary models, revealing an interesting insight: MLLMs tend to prioritize matching the target silhouette while neglecting geometric constraints, leading to distortions or deformations of the pieces.

