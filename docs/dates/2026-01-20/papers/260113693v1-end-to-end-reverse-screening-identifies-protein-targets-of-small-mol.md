---
layout: default
title: End-to-End Reverse Screening Identifies Protein Targets of Small Molecules Using HelixFold3
---

# End-to-End Reverse Screening Identifies Protein Targets of Small Molecules Using HelixFold3
**arXiv**：[2601.13693v1](https://arxiv.org/abs/2601.13693) · [PDF](https://arxiv.org/pdf/2601.13693.pdf)  
**作者**：Shengjie Xu, Xianbin Ye, Mengran Zhu, Xiaonan Zhang, Shanzhuo Zhang, Xiaomin Fang  

**一句话要点**：提出基于HelixFold3的端到端反向筛选策略，以解决小分子蛋白靶标识别中的复杂交互建模问题。

**关键词**：反向筛选, 蛋白质靶标识别, HelixFold3, 端到端建模, 小分子对接

## 3 点简述
- 核心问题：反向筛选因小分子与结构多样蛋白质交互建模复杂，传统分步方法易传播误差。
- 方法要点：利用HelixFold3统一框架，同时建模蛋白质折叠和小分子配体对接。
- 实验或效果：在约百个小分子上验证，相比传统反向对接，提升筛选准确性和结构保真度。

## 摘要（原文）

> Identifying protein targets for small molecules, or reverse screening, is essential for understanding drug action, guiding compound repurposing, predicting off-target effects, and elucidating the molecular mechanisms of bioactive compounds. Despite its critical role, reverse screening remains challenging because accurately capturing interactions between a small molecule and structurally diverse proteins is inherently complex, and conventional step-wise workflows often propagate errors across decoupled steps such as target structure modeling, pocket identification, docking, and scoring. Here, we present an end-to-end reverse screening strategy leveraging HelixFold3, a high-accuracy biomolecular structure prediction model akin to AlphaFold3, which simultaneously models the folding of proteins from a protein library and the docking of small-molecule ligands within a unified framework. We validate this approach on a diverse and representative set of approximately one hundred small molecules. Compared with conventional reverse docking, our method improves screening accuracy and demonstrates enhanced structural fidelity, binding-site precision, and target prioritization. By systematically linking small molecules to their protein targets, this framework establishes a scalable and straightforward platform for dissecting molecular mechanisms, exploring off-target interactions, and supporting rational drug discovery.

