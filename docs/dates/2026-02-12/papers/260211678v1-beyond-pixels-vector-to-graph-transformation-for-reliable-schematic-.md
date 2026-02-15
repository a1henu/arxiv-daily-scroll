---
layout: default
title: Beyond Pixels: Vector-to-Graph Transformation for Reliable Schematic Auditing
---

# Beyond Pixels: Vector-to-Graph Transformation for Reliable Schematic Auditing
**arXiv**：[2602.11678v1](https://arxiv.org/abs/2602.11678) · [PDF](https://arxiv.org/pdf/2602.11678.pdf)  
**作者**：Chengwei Ma, Zhen Tian, Zhou Zhou, Zhixian Xu, Xiaowei Zhu, Xia Hua, Si Shi, F. Richard Yu  

**一句话要点**：提出向量到图转换管道以解决工程示意图审核中的结构盲问题

**关键词**：工程示意图审核, 向量到图转换, 结构盲, 多模态大语言模型, 属性图, 电气合规检查

## 3 点简述
- 核心问题：多模态大语言模型在工程示意图理解中存在结构盲，无法捕捉拓扑和符号逻辑
- 方法要点：开发V2G管道，将CAD图转换为属性图，节点表示组件，边编码连接性
- 实验或效果：在电气合规检查基准上，V2G显著提升准确性，而领先MLLMs表现接近随机水平

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown remarkable progress in visual understanding, yet they suffer from a critical limitation: structural blindness. Even state-of-the-art models fail to capture topology and symbolic logic in engineering schematics, as their pixel-driven paradigm discards the explicit vector-defined relations needed for reasoning. To overcome this, we propose a Vector-to-Graph (V2G) pipeline that converts CAD diagrams into property graphs where nodes represent components and edges encode connectivity, making structural dependencies explicit and machine-auditable. On a diagnostic benchmark of electrical compliance checks, V2G yields large accuracy gains across all error categories, while leading MLLMs remain near chance level. These results highlight the systemic inadequacy of pixel-based methods and demonstrate that structure-aware representations provide a reliable path toward practical deployment of multimodal AI in engineering domains. To facilitate further research, we release our benchmark and implementation at https://github.com/gm-embodied/V2G-Audit.

