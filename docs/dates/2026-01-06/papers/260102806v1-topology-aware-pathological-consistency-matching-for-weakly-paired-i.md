---
layout: default
title: Topology-aware Pathological Consistency Matching for Weakly-Paired IHC Virtual Staining
---

# Topology-aware Pathological Consistency Matching for Weakly-Paired IHC Virtual Staining
**arXiv**：[2601.02806v1](https://arxiv.org/abs/2601.02806) · [PDF](https://arxiv.org/pdf/2601.02806.pdf)  
**作者**：Mingzhou Jiang, Jiaying Zhou, Nan Zeng, Mickael Li, Qijie Tang, Chao He, Huazhu Fu, Honghui He  

**一句话要点**：提出拓扑感知病理一致性匹配框架以解决弱配对H&E到IHC虚拟染色中的空间错位问题

**关键词**：虚拟染色, 弱配对学习, 图对比学习, 拓扑感知, 病理一致性, 免疫组化

## 3 点简述
- 核心问题：H&E到IHC虚拟染色中，相邻切片作为真值导致弱配对数据，存在空间错位和局部变形，阻碍监督学习。
- 方法要点：引入拓扑感知一致性匹配机制，通过图对比学习和拓扑扰动学习鲁棒匹配模式，确保结构一致性；并基于节点重要性对齐病理阳性区域以增强病理一致性。
- 实验或效果：在两个基准数据集上的四个染色任务中，方法优于现有技术，生成质量更高且临床相关性更强。

## 摘要（原文）

> Immunohistochemical (IHC) staining provides crucial molecular characterization of tissue samples and plays an indispensable role in the clinical examination and diagnosis of cancers. However, compared with the commonly used Hematoxylin and Eosin (H&E) staining, IHC staining involves complex procedures and is both time-consuming and expensive, which limits its widespread clinical use. Virtual staining converts H&E images to IHC images, offering a cost-effective alternative to clinical IHC staining. Nevertheless, using adjacent slides as ground truth often results in weakly-paired data with spatial misalignment and local deformations, hindering effective supervised learning. To address these challenges, we propose a novel topology-aware framework for H&E-to-IHC virtual staining. Specifically, we introduce a Topology-aware Consistency Matching (TACM) mechanism that employs graph contrastive learning and topological perturbations to learn robust matching patterns despite spatial misalignments, ensuring structural consistency. Furthermore, we propose a Topology-constrained Pathological Matching (TCPM) mechanism that aligns pathological positive regions based on node importance to enhance pathological consistency. Extensive experiments on two benchmarks across four staining tasks demonstrate that our method outperforms state-of-the-art approaches, achieving superior generation quality with higher clinical relevance.

