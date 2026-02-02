---
layout: default
title: SQUAD: Scalable Quorum Adaptive Decisions via ensemble of early exit neural networks
---

# SQUAD: Scalable Quorum Adaptive Decisions via ensemble of early exit neural networks
**arXiv**：[2601.22711v1](https://arxiv.org/abs/2601.22711) · [PDF](https://arxiv.org/pdf/2601.22711.pdf)  
**作者**：Matteo Gambella, Fabrizio Pittorino, Giuliano Casale, Manuel Roveri  

**一句话要点**：提出SQUAD集成早期退出神经网络，通过共识投票提升不确定性估计并减少推理延迟。

**关键词**：早期退出神经网络, 集成学习, 不确定性估计, 推理加速, 神经架构搜索, 共识投票

## 3 点简述
- 早期退出神经网络依赖单模型置信度阈值，常因校准问题不可靠。
- SQUAD采用基于法定人数的停止准则，通过递增收集预测达成共识以提前退出。
- 实验显示，在可比计算成本下，测试准确率提升达5.95%，推理延迟减少达70.60%。

## 摘要（原文）

> Early-exit neural networks have become popular for reducing inference latency by allowing intermediate predictions when sufficient confidence is achieved. However, standard approaches typically rely on single-model confidence thresholds, which are frequently unreliable due to inherent calibration issues. To address this, we introduce SQUAD (Scalable Quorum Adaptive Decisions), the first inference scheme that integrates early-exit mechanisms with distributed ensemble learning, improving uncertainty estimation while reducing the inference time. Unlike traditional methods that depend on individual confidence scores, SQUAD employs a quorum-based stopping criterion on early-exit learners by collecting intermediate predictions incrementally in order of computational complexity until a consensus is reached and halting the computation at that exit if the consensus is statistically significant. To maximize the efficacy of this voting mechanism, we also introduce QUEST (Quorum Search Technique), a Neural Architecture Search method to select early-exit learners with optimized hierarchical diversity, ensuring learners are complementary at every intermediate layer. This consensus-driven approach yields statistically robust early exits, improving the test accuracy up to 5.95% compared to state-of-the-art dynamic solutions with a comparable computational cost and reducing the inference latency up to 70.60% compared to static ensembles while maintaining a good accuracy.

