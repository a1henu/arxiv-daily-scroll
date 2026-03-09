---
layout: default
title: Solving Jigsaw Puzzles in the Wild: Human-Guided Reconstruction of Cultural Heritage Fragments
---

# Solving Jigsaw Puzzles in the Wild: Human-Guided Reconstruction of Cultural Heritage Fragments
**arXiv**：[2603.06389v1](https://arxiv.org/abs/2603.06389) · [PDF](https://arxiv.org/pdf/2603.06389.pdf)  
**作者**：Omidreza Safaei, Sinem Aslan, Sebastiano Vascon, Luca Palmieri, Marina Khoroshiltseva, Marcello Pelillo  

**一句话要点**：提出人机交互拼图框架以解决大规模文化遗产碎片重建问题

**关键词**：文化遗产重建, 人机交互, 拼图求解, 松弛标记, 大规模碎片, 考古学

## 3 点简述
- 核心问题：真实考古碎片因侵蚀、缺失和形状不规则，传统自动方法难以处理大规模重建。
- 方法要点：结合自动松弛标记求解器与交互式人工指导，支持迭代锁定和修正，提升语义和几何一致性。
- 实验或效果：在RePAIR基准上，混合方法在准确性和效率上优于全自动和手动基线。

## 摘要（原文）

> Reassembling real-world archaeological artifacts from fragmented pieces poses significant challenges due to erosion, missing regions, irregular shapes, and large-scale ambiguity. Traditional jigsaw puzzle solvers, often designed for clean synthetic scenarios, struggle under these conditions, especially when the number of fragments grows into the thousands, as in the RePAIR benchmark. In this paper, we propose a human-in-the-loop (HIL) puzzle solving framework designed to address the complexity and scale of real-world cultural heritage reconstruction. Our approach integrates an automatic relaxation-labeling solver with interactive human guidance, allowing users to iteratively lock verified placements, correct errors, and guide the system toward semantically and geometrically coherent assemblies. We introduce two complementary interaction strategies, Iterative Anchoring and Continuous Interactive Refinement, which support scalable reconstruction across varying levels of ambiguity and puzzle size. Experiments on several RePAIR groups demonstrate that our hybrid approach substantially outperforms both fully automatic and manual baselines in accuracy and efficiency, offering a practical solution for large-scale expert-in-the-loop artifact reassembly.

