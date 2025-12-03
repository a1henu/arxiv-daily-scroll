---
layout: default
title: AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry
---

# AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry
**arXiv**：[2512.03018v1](https://arxiv.org/abs/2512.03018) · [PDF](https://arxiv.org/pdf/2512.03018.pdf)  
**作者**：Xiang Xu, Pradeep Kumar Jayaraman, Joseph G. Lambourne, Yilin Liu, Durvesh Malpure, Pete Meltzer  

**一句话要点**：提出AutoBrep，通过自回归Transformer统一编码拓扑与几何，以解决B-Rep高质量端到端生成挑战。

**关键词**：边界表示生成, 自回归Transformer, 统一拓扑几何编码, 计算机辅助设计, 端到端建模

## 3 点简述
- 核心问题：B-Rep端到端生成中，精确几何与封闭拓扑的联合建模仍具挑战。
- 方法要点：采用统一标记化方案，将几何与拓扑编码为序列，基于广度优先遍历自回归生成。
- 实验或效果：在质量和封闭性上优于基线，支持复杂实体生成和用户可控自动补全。

## 摘要（原文）

> The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep.

