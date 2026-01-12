---
layout: default
title: Circular Reasoning: Understanding Self-Reinforcing Loops in Large Reasoning Models
---

# Circular Reasoning: Understanding Self-Reinforcing Loops in Large Reasoning Models
**arXiv**：[2601.05693v1](https://arxiv.org/abs/2601.05693) · [PDF](https://arxiv.org/pdf/2601.05693.pdf)  
**作者**：Zenghao Duan, Liang Pang, Zihao Wei, Wenbin Duan, Yuxin Tian, Shicheng Xu, Jingcheng Deng, Zhiyi Yin, Xueqi Cheng  

**一句话要点**：提出Circular Reasoning概念与LoopBench数据集，分析大推理模型中的自强化循环问题

**关键词**：大推理模型, 循环推理, 注意力机制, 推理失败, 数据集构建, 早期预测

## 3 点简述
- 核心问题：大推理模型在推理时易陷入自强化循环，导致计算浪费和推理失败
- 方法要点：引入LoopBench数据集，通过CUSUM算法预测循环，揭示V形注意力机制驱动循环
- 实验或效果：跨模型验证预测准确性，阐明长链推理稳定性

## 摘要（原文）

> Despite the success of test-time scaling, Large Reasoning Models (LRMs) frequently encounter repetitive loops that lead to computational waste and inference failure. In this paper, we identify a distinct failure mode termed Circular Reasoning. Unlike traditional model degeneration, this phenomenon manifests as a self-reinforcing trap where generated content acts as a logical premise for its own recurrence, compelling the reiteration of preceding text. To systematically analyze this phenomenon, we introduce LoopBench, a dataset designed to capture two distinct loop typologies: numerical loops and statement loops. Mechanistically, we characterize circular reasoning as a state collapse exhibiting distinct boundaries, where semantic repetition precedes textual repetition. We reveal that reasoning impasses trigger the loop onset, which subsequently persists as an inescapable cycle driven by a self-reinforcing V-shaped attention mechanism. Guided by these findings, we employ the Cumulative Sum (CUSUM) algorithm to capture these precursors for early loop prediction. Experiments across diverse LRMs validate its accuracy and elucidate the stability of long-chain reasoning.

