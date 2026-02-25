---
layout: default
title: Benchmarking GNN Models on Molecular Regression Tasks with CKA-Based Representation Analysis
---

# Benchmarking GNN Models on Molecular Regression Tasks with CKA-Based Representation Analysis
**arXiv**：[2602.20573v1](https://arxiv.org/abs/2602.20573) · [PDF](https://arxiv.org/pdf/2602.20573.pdf)  
**作者**：Rajan, Ishaan Gupta  

**一句话要点**：通过CKA分析评估GNN在分子回归任务中的性能，并融合指纹提升预测效果

**关键词**：分子图神经网络, 表示相似性分析, 层次融合框架, 分子回归任务, CKA评估

## 3 点简述
- 研究GNN在小数据集上的效能及不同架构的归纳偏差，系统评估四种GNN模型
- 提出GNN与分子指纹的层次融合框架，在多个数据集上性能优于或匹配独立模型
- 使用CKA分析表示相似性，发现GNN与指纹嵌入空间独立，同构模型间表示高度收敛

## 摘要（原文）

> Molecules are commonly represented as SMILES strings, which can be readily converted to fixed-size molecular fingerprints. These fingerprints serve as feature vectors to train ML/DL models for molecular property prediction tasks in the field of computational chemistry, drug discovery, biochemistry, and materials science. Recent research has demonstrated that SMILES can be used to construct molecular graphs where atoms are nodes ($V$) and bonds are edges ($E$). These graphs can subsequently be used to train geometric DL models like GNN. GNN learns the inherent structural relationships within a molecule rather than depending on fixed-size fingerprints. Although GNN are powerful aggregators, their efficacy on smaller datasets and inductive biases across different architectures is less studied. In our present study, we performed a systematic benchmarking of four different GNN architectures across a diverse domain of datasets (physical chemistry, biological, and analytical). Additionally, we have also implemented a hierarchical fusion (GNN+FP) framework for target prediction. We observed that the fusion framework consistently outperforms or matches the performance of standalone GNN (RMSE improvement > $7\%$) and baseline models. Further, we investigated the representational similarity using centered kernel alignment (CKA) between GNN and fingerprint embeddings and found that they occupy highly independent latent spaces (CKA $\le0.46$). The cross-architectural CKA score suggests a high convergence between isotopic models like GCN, GraphSAGE and GIN (CKA $\geq0.88$), with GAT learning moderately independent representation (CKA $0.55-0.80$).

