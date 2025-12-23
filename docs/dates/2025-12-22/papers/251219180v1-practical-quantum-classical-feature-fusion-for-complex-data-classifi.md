---
layout: default
title: Practical Quantum-Classical Feature Fusion for complex data Classification
---

# Practical Quantum-Classical Feature Fusion for complex data Classification
**arXiv**：[2512.19180v1](https://arxiv.org/abs/2512.19180) · [PDF](https://arxiv.org/pdf/2512.19180.pdf)  
**作者**：Azadeh Alavi, Fatemeh Kouchmeshki, Abdolrahman Alavi  

**一句话要点**：提出跨注意力中融合架构，通过多模态融合提升量子-经典混合学习在复杂数据分类中的性能。

**关键词**：量子-经典混合学习, 多模态融合, 跨注意力机制, 复杂数据分类, NISQ量子计算

## 3 点简述
- 核心问题：现有量子-经典混合架构将量子电路作为孤立特征提取器，忽略模态差异，导致复杂数据分类性能受限。
- 方法要点：设计跨注意力中融合架构，让经典表示通过注意力块查询量子特征令牌，并保持残差连接。
- 实验或效果：在多个数据集上评估，跨注意力中融合模型表现一致竞争，在复杂数据集上通常优于纯量子或标准混合模型。

## 摘要（原文）

> Hybrid quantum and classical learning aims to couple quantum feature maps with the robustness of classical neural networks, yet most architectures treat the quantum circuit as an isolated feature extractor and merge its measurements with classical representations by direct concatenation. This neglects that the quantum and classical branches constitute distinct computational modalities and limits reliable performance on complex, high dimensional tabular and semi structured data, including remote sensing, environmental monitoring, and medical diagnostics. We present a multimodal formulation of hybrid learning and propose a cross attention mid fusion architecture in which a classical representation queries quantum derived feature tokens through an attention block with residual connectivity. The quantum branch is kept within practical NISQ budgets and uses up to nine qubits. We evaluate on Wine, Breast Cancer, Forest CoverType, FashionMNIST, and SteelPlatesFaults, comparing a quantum only model, a classical baseline, residual hybrid models, and the proposed mid fusion model under a consistent protocol. Pure quantum and standard hybrid designs underperform due to measurement induced information loss, while cross attention mid fusion is consistently competitive and improves performance on the more complex datasets in most cases. These findings suggest that quantum derived information becomes most valuable when integrated through principled multimodal fusion rather than used in isolation or loosely appended to classical features.

