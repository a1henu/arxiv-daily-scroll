---
layout: default
title: Sparse3DPR: Training-Free 3D Hierarchical Scene Parsing and Task-Adaptive Subgraph Reasoning from Sparse RGB Views
---

# Sparse3DPR: Training-Free 3D Hierarchical Scene Parsing and Task-Adaptive Subgraph Reasoning from Sparse RGB Views
**arXiv**：[2511.07813v1](https://arxiv.org/abs/2511.07813) · [PDF](https://arxiv.org/pdf/2511.07813.pdf)  
**作者**：Haida Feng, Hao Wei, Zewen Xu, Haolin Wang, Chade Li, Yihong Wu  

**一句话要点**：提出Sparse3DPR训练无关框架，利用稀疏RGB视图实现3D场景解析与推理

**关键词**：3D场景理解, 训练无关方法, 场景图推理, 稀疏视图输入, 层次化解析

## 3 点简述
- 核心问题：训练无关3D场景理解方法在精度和效率上存在不足
- 方法要点：引入层次化平面增强场景图和任务自适应子图提取
- 实验或效果：在Space3D-Bench上精度提升28.7%，速度提升78.2%

## 摘要（原文）

> Recently, large language models (LLMs) have been explored widely for 3D scene understanding. Among them, training-free approaches are gaining attention for their flexibility and generalization over training-based methods. However, they typically struggle with accuracy and efficiency in practical deployment. To address the problems, we propose Sparse3DPR, a novel training-free framework for open-ended scene understanding, which leverages the reasoning capabilities of pre-trained LLMs and requires only sparse-view RGB inputs. Specifically, we introduce a hierarchical plane-enhanced scene graph that supports open vocabulary and adopts dominant planar structures as spatial anchors, which enables clearer reasoning chains and more reliable high-level inferences. Furthermore, we design a task-adaptive subgraph extraction method to filter query-irrelevant information dynamically, reducing contextual noise and improving 3D scene reasoning efficiency and accuracy. Experimental results demonstrate the superiority of Sparse3DPR, which achieves a 28.7% EM@1 improvement and a 78.2% speedup compared with ConceptGraphs on the Space3D-Bench. Moreover, Sparse3DPR obtains comparable performance to training-based methods on ScanQA, with additional real-world experiments confirming its robustness and generalization capability.

