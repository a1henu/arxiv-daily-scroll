---
layout: default
title: SSMG-Nav: Enhancing Lifelong Object Navigation with Semantic Skeleton Memory Graph
---

# SSMG-Nav: Enhancing Lifelong Object Navigation with Semantic Skeleton Memory Graph
**arXiv**：[2603.01813v1](https://arxiv.org/abs/2603.01813) · [PDF](https://arxiv.org/pdf/2603.01813.pdf)  
**作者**：Haochen Niu, Lantao Zhang, Xingwu Ji, Rendong Ying, Peilin Liu, Fei Wen  

**一句话要点**：提出SSMG-Nav框架，基于语义骨架记忆图增强终身物体导航性能

**关键词**：物体导航, 语义记忆图, 多模态处理, 长视规划, 终身学习, 视觉语言模型

## 3 点简述
- 核心问题：终身物体导航中现有方法未充分利用持久记忆，依赖单模态输入和短视策略，导致效率低下。
- 方法要点：构建语义骨架记忆图整合历史观测，结合视觉语言模型处理多模态目标，使用长视规划器优化路径以减少回溯。
- 实验或效果：在终身和标准物体导航基准测试中，相比基线方法，实现了更高的成功率和路径效率。

## 摘要（原文）

> Navigating to out-of-sight targets from human instructions in unfamiliar environments is a core capability for service robots. Despite substantial progress, most approaches underutilize reusable, persistent memory, constraining performance in lifelong settings. Many are additionally limited to single-modality inputs and employ myopic greedy policies, which often induce inefficient back-and-forth maneuvers (BFMs). To address such limitations, we introduce SSMG-Nav, a framework for object navigation built on a \textit{Semantic Skeleton Memory Graph} (SSMG) that consolidates past observations into a spatially aligned, persistent memory anchored by topological keypoints (e.g., junctions, room centers). SSMG clusters nearby entities into subgraphs, unifying entity- and space-level semantics to yield a compact set of candidate destinations. To support multimodal targets (images, objects, and text), we integrate a vision-language model (VLM). For each subgraph, a multimodal prompt synthesized from memory guides the VLM to infer a target belief over destinations. A long-horizon planner then trades off this belief against traversability costs to produce a visit sequence that minimizes expected path length, thereby reducing backtracking. Extensive experiments on challenging lifelong benchmarks and standard ObjectNav benchmarks demonstrate that, compared to strong baselines, our method achieves higher success rates and greater path efficiency, validating the effectiveness of SSMG-Nav.

