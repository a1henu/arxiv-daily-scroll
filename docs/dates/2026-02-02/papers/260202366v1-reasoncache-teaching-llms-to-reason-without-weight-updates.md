---
layout: default
title: ReasonCACHE: Teaching LLMs To Reason Without Weight Updates
---

# ReasonCACHE: Teaching LLMs To Reason Without Weight Updates
**arXiv**：[2602.02366v1](https://arxiv.org/abs/2602.02366) · [PDF](https://arxiv.org/pdf/2602.02366.pdf)  
**作者**：Sharut Gupta, Phillip Isola, Stefanie Jegelka, David Lopez-Paz, Kartik Ahuja, Mark Ibrahim, Mohammad Pezeshki  

**一句话要点**：提出ReasonCACHE，通过前缀调优实现无需权重更新的LLM推理学习

**关键词**：大型语言模型, 上下文学习, 前缀调优, 推理学习, 键值缓存, 无权重更新

## 3 点简述
- 核心问题：LLMs在上下文学习中难以高效学习复杂推理，且扩展演示会带来计算和性能问题
- 方法要点：使用前缀调优将演示蒸馏为固定键值缓存，避免上下文过载和权重更新
- 实验或效果：在GPQA-Diamond等基准上超越标准上下文学习，匹配或优于权重更新方法，提升数据、推理和参数效率

## 摘要（原文）

> Can Large language models (LLMs) learn to reason without any weight update and only through in-context learning (ICL)? ICL is strikingly sample-efficient, often learning from only a handful of demonstrations, but complex reasoning tasks typically demand many training examples to learn from. However, naively scaling ICL by adding more demonstrations breaks down at this scale: attention costs grow quadratically, performance saturates or degrades with longer contexts, and the approach remains a shallow form of learning. Due to these limitations, practitioners predominantly rely on in-weight learning (IWL) to induce reasoning. In this work, we show that by using Prefix Tuning, LLMs can learn to reason without overloading the context window and without any weight updates. We introduce $\textbf{ReasonCACHE}$, an instantiation of this mechanism that distills demonstrations into a fixed key-value cache. Empirically, across challenging reasoning benchmarks, including GPQA-Diamond, ReasonCACHE outperforms standard ICL and matches or surpasses IWL approaches. Further, it achieves this all while being more efficient across three key axes: data, inference cost, and trainable parameters. We also theoretically prove that ReasonCACHE can be strictly more expressive than low-rank weight update since the latter ties expressivity to input rank, whereas ReasonCACHE bypasses this constraint by directly injecting key-values into the attention mechanism. Together, our findings identify ReasonCACHE as a middle path between in-context and in-weight learning, providing a scalable algorithm for learning reasoning skills beyond the context window without modifying parameters. Our project page: https://reasoncache.github.io/

