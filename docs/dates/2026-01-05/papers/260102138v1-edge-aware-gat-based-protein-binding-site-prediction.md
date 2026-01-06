---
layout: default
title: Edge-aware GAT-based protein binding site prediction
---

# Edge-aware GAT-based protein binding site prediction
**arXiv**：[2601.02138v1](https://arxiv.org/abs/2601.02138) · [PDF](https://arxiv.org/pdf/2601.02138.pdf)  
**作者**：Weisen Yang, Hanqing Zhang, Wangren Qiu, Xuan Xiao, Weizhong Lin  

**一句话要点**：提出Edge-aware GAT模型以高效预测蛋白质结合位点

**关键词**：蛋白质结合位点预测, 图注意力网络, 原子级图建模, 边特征增强, 生物分子相互作用

## 3 点简述
- 核心问题：传统方法在捕获复杂空间构象时难以平衡预测精度与计算效率。
- 方法要点：构建原子级图，集成几何描述符、二级结构和溶剂可及性，通过边特征增强注意力机制。
- 实验或效果：在基准数据集上，蛋白质-蛋白质结合位点预测的ROC-AUC达0.93，优于现有方法。

## 摘要（原文）

> Accurate identification of protein binding sites is crucial for understanding biomolecular interaction mechanisms and for the rational design of drug targets. Traditional predictive methods often struggle to balance prediction accuracy with computational efficiency when capturing complex spatial conformations. To address this challenge, we propose an Edge-aware Graph Attention Network (Edge-aware GAT) model for the fine-grained prediction of binding sites across various biomolecules, including proteins, DNA/RNA, ions, ligands, and lipids. Our method constructs atom-level graphs and integrates multidimensional structural features, including geometric descriptors, DSSP-derived secondary structure, and relative solvent accessibility (RSA), to generate spatially aware embedding vectors. By incorporating interatomic distances and directional vectors as edge features within the attention mechanism, the model significantly enhances its representation capacity. On benchmark datasets, our model achieves an ROC-AUC of 0.93 for protein-protein binding site prediction, outperforming several state-of-the-art methods. The use of directional tensor propagation and residue-level attention pooling further improves both binding site localization and the capture of local structural details. Visualizations using PyMOL confirm the model's practical utility and interpretability. To facilitate community access and application, we have deployed a publicly accessible web server at http://119.45.201.89:5000/. In summary, our approach offers a novel and efficient solution that balances prediction accuracy, generalization, and interpretability for identifying functional sites in proteins.

