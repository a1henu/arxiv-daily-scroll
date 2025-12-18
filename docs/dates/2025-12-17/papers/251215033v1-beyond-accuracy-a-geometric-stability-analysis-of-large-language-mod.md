---
layout: default
title: Beyond Accuracy: A Geometric Stability Analysis of Large Language Models in Chess Evaluation
---

# Beyond Accuracy: A Geometric Stability Analysis of Large Language Models in Chess Evaluation
**arXiv**：[2512.15033v1](https://arxiv.org/abs/2512.15033) · [PDF](https://arxiv.org/pdf/2512.15033.pdf)  
**作者**：Xidan Song, Weiqi Wang, Ruifeng Cao, Qingya Hu  

**一句话要点**：提出几何稳定性框架以评估大型语言模型在象棋领域的推理稳健性

**关键词**：大型语言模型评估, 几何稳定性分析, 象棋推理, 不变变换, 准确性-稳定性悖论, 模式匹配检测

## 3 点简述
- 核心问题：标准准确度指标无法区分模型是真实几何推理还是表面记忆棋盘状态
- 方法要点：通过棋盘旋转、镜像对称、颜色反转等不变变换测试模型一致性
- 实验或效果：发现准确性-稳定性悖论，部分模型在几何扰动下错误率激增600%以上

## 摘要（原文）

> The evaluation of Large Language Models (LLMs) in complex reasoning domains typically relies on performance alignment with ground-truth oracles. In the domain of chess, this standard manifests as accuracy benchmarks against strong engines like Stockfish. However, high scalar accuracy does not necessarily imply robust conceptual understanding. This paper argues that standard accuracy metrics fail to distinguish between genuine geometric reasoning and the superficial memorization of canonical board states. To address this gap, we propose a Geometric Stability Framework, a novel evaluation methodology that rigorously tests model consistency under invariant transformations-including board rotation, mirror symmetry, color inversion, and format conversion. We applied this framework to a comparative analysis of six state-of-the-art LLMs including GPT-5.1, Claude Sonnet 4.5, and Kimi K2 Turbo, utilizing a dataset of approximately 3,000 positions. Our results reveal a significant Accuracy-Stability Paradox. While models such as GPT-5.1 achieve near-optimal accuracy on standard positions, they exhibit catastrophic degradation under geometric perturbation, specifically in rotation tasks where error rates surge by over 600%. This disparity suggests a reliance on pattern matching over abstract spatial logic. Conversely, Claude Sonnet 4.5 and Kimi K2 Turbo demonstrate superior dual robustness, maintaining high consistency across all transformation axes. Furthermore, we analyze the trade-off between helpfulness and safety, identifying Gemini 2.5 Flash as the leader in illegal state rejection (96.0%). We conclude that geometric stability provides an orthogonal and essential metric for AI evaluation, offering a necessary proxy for disentangling reasoning capabilities from data contamination and overfitting in large-scale models.

