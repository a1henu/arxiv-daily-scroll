---
layout: default
title: From Physical Degradation Models to Task-Aware All-in-One Image Restoration
---

# From Physical Degradation Models to Task-Aware All-in-One Image Restoration
**arXiv**：[2601.10192v1](https://arxiv.org/abs/2601.10192) · [PDF](https://arxiv.org/pdf/2601.10192.pdf)  
**作者**：Hu Gao, Xiaoning Lei, Xichen Xu, Xingjian Wang, Lizhuang Ma  

**一句话要点**：提出OPIR框架，通过物理退化建模实现高效多任务图像恢复。

**关键词**：图像恢复, 多任务学习, 物理退化模型, 逆算子预测, 不确定性感知

## 3 点简述
- 核心问题：现有多任务图像恢复方法因额外学习模块增加复杂性，影响实时性。
- 方法要点：基于物理退化模型预测任务感知逆退化算子，分两阶段恢复并引入不确定性感知图。
- 实验或效果：OPIR在实验中展现优越的多任务恢复性能，同时保持高效性。

## 摘要（原文）

> All-in-one image restoration aims to adaptively handle multiple restoration tasks with a single trained model. Although existing methods achieve promising results by introducing prompt information or leveraging large models, the added learning modules increase system complexity and hinder real-time applicability. In this paper, we adopt a physical degradation modeling perspective and predict a task-aware inverse degradation operator for efficient all-in-one image restoration. The framework consists of two stages. In the first stage, the predicted inverse operator produces an initial restored image together with an uncertainty perception map that highlights regions difficult to reconstruct, ensuring restoration reliability. In the second stage, the restoration is further refined under the guidance of this uncertainty map. The same inverse operator prediction network is used in both stages, with task-aware parameters introduced after operator prediction to adapt to different degradation tasks. Moreover, by accelerating the convolution of the inverse operator, the proposed method achieves efficient all-in-one image restoration. The resulting tightly integrated architecture, termed OPIR, is extensively validated through experiments, demonstrating superior all-in-one restoration performance while remaining highly competitive on task-aligned restoration.

