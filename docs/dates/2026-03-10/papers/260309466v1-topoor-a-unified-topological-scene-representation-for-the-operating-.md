---
layout: default
title: TopoOR: A Unified Topological Scene Representation for the Operating Room
---

# TopoOR: A Unified Topological Scene Representation for the Operating Room
**arXiv**：[2603.09466v1](https://arxiv.org/abs/2603.09466) · [PDF](https://arxiv.org/pdf/2603.09466.pdf)  
**作者**：Tony Danjun Wang, Ka Young Kim, Tolga Birdal, Nassir Navab, Lennart Bastian  

**一句话要点**：提出TopoOR统一拓扑场景表示，以高阶结构建模手术室多模态交互，提升表达力与推理能力。

**关键词**：手术室场景理解, 高阶拓扑表示, 多模态融合, 注意力机制, 安全关键推理

## 3 点简述
- 现有手术场景图受限于二元结构，无法有效建模高阶关系和几何流形。
- TopoOR通过高阶拓扑单元表示实体交互，并设计高阶注意力机制保留多模态结构。
- 实验在无菌违规检测、机器人阶段预测等任务上优于传统图和LLM基线。

## 摘要（原文）

> Surgical Scene Graphs abstract the complexity of surgical operating rooms (OR) into a structure of entities and their relations, but existing paradigms suffer from strictly dyadic structural limitations. Frameworks that predominantly rely on pairwise message passing or tokenized sequences flatten the manifold geometry inherent to relational structures and lose structure in the process. We introduce TopoOR, a new paradigm that models multimodal operating rooms as a higher-order structure, innately preserving pairwise and group relationships. By lifting interactions between entities into higher-order topological cells, TopoOR natively models complex dynamics and multimodality present in the OR. This topological representation subsumes traditional scene graphs, thereby offering strictly greater expressivity. We also propose a higher-order attention mechanism that explicitly preserves manifold structure and modality-specific features throughout hierarchical relational attention. In this way, we circumvent combining 3D geometry, audio, and robot kinematics into a single joint latent representation, preserving the precise multimodal structure required for safety-critical reasoning, unlike existing methods. Extensive experiments demonstrate that our approach outperforms traditional graph and LLM-based baselines across sterility breach detection, robot phase prediction, and next-action anticipation

