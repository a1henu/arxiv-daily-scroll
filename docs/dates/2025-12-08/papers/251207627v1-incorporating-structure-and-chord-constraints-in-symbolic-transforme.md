---
layout: default
title: Incorporating Structure and Chord Constraints in Symbolic Transformer-based Melodic Harmonization
---

# Incorporating Structure and Chord Constraints in Symbolic Transformer-based Melodic Harmonization
**arXiv**：[2512.07627v1](https://arxiv.org/abs/2512.07627) · [PDF](https://arxiv.org/pdf/2512.07627.pdf)  
**作者**：Maximos Kaliakatsos-Papakostas, Konstantinos Soiledis, Theodoros Tsamis, Dimos Makris, Vassilis Katsouros, Emilios Cambouropoulos  

**一句话要点**：提出B*算法以解决基于Transformer的旋律和声中融入预定义和弦约束的问题

**关键词**：旋律和声, Transformer模型, 和弦约束, B*算法, 符号音乐生成, 自回归生成

## 3 点简述
- 核心问题：如何在自回归Transformer模型中强制融入特定位置的和弦约束，确保和声生成符合用户输入
- 方法要点：结合束搜索、A*算法和回溯，设计B*算法，以指数复杂度强制模型满足约束
- 实验或效果：算法为首次尝试，突出任务难度，提供改进空间，但复杂度高，效果未知

## 摘要（原文）

> Transformer architectures offer significant advantages regarding the generation of symbolic music; their capabilities for incorporating user preferences toward what they generate is being studied under many aspects. This paper studies the inclusion of predefined chord constraints in melodic harmonization, i.e., where a desired chord at a specific location is provided along with the melody as inputs and the autoregressive transformer model needs to incorporate the chord in the harmonization that it generates. The peculiarities of involving such constraints is discussed and an algorithm is proposed for tackling this task. This algorithm is called B* and it combines aspects of beam search and A* along with backtracking to force pretrained transformers to satisfy the chord constraints, at the correct onset position within the correct bar. The algorithm is brute-force and has exponential complexity in the worst case; however, this paper is a first attempt to highlight the difficulties of the problem and proposes an algorithm that offers many possibilities for improvements since it accommodates the involvement of heuristics.

