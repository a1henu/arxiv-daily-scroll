---
layout: default
title: Learning Continuous Solvent Effects from Transient Flow Data: A Graph Neural Network Benchmark on Catechol Rearrangement
---

# Learning Continuous Solvent Effects from Transient Flow Data: A Graph Neural Network Benchmark on Catechol Rearrangement
**arXiv**：[2512.19530v1](https://arxiv.org/abs/2512.19530) · [PDF](https://arxiv.org/pdf/2512.19530.pdf)  
**作者**：Hongsheng Xing, Qiuxin Si  

**一句话要点**：提出混合图神经网络架构以解决连续溶剂效应预测问题

**关键词**：图神经网络, 溶剂效应预测, 连续溶剂表示, 反应产率预测, 高通量数据集

## 3 点简述
- 核心问题：传统方法将溶剂视为离散变量，难以预测连续溶剂组成下的反应产率。
- 方法要点：结合图注意力网络、差分反应指纹和连续溶剂编码，构建混合GNN模型。
- 实验效果：在Catechol基准上，MSE达0.0039，比基线方法误差降低60%以上。

## 摘要（原文）

> Predicting reaction outcomes across continuous solvent composition ranges remains a critical challenge in organic synthesis and process chemistry. Traditional machine learning approaches often treat solvent identity as a discrete categorical variable, which prevents systematic interpolation and extrapolation across the solvent space. This work introduces the \textbf{Catechol Benchmark}, a high-throughput transient flow chemistry dataset comprising 1,227 experimental yield measurements for the rearrangement of allyl-substituted catechol in 24 pure solvents and their binary mixtures, parameterized by continuous volume fractions ($\% B$). We evaluate various architectures under rigorous leave-one-solvent-out and leave-one-mixture-out protocols to test generalization to unseen chemical environments.
>   Our results demonstrate that classical tabular methods (e.g., Gradient-Boosted Decision Trees) and large language model embeddings (e.g., Qwen-7B) struggle with quantitative precision, yielding Mean Squared Errors (MSE) of 0.099 and 0.129, respectively. In contrast, we propose a hybrid GNN-based architecture that integrates Graph Attention Networks (GATs) with Differential Reaction Fingerprints (DRFP) and learned mixture-aware solvent encodings. This approach achieves an \textbf{MSE of 0.0039} ($\pm$ 0.0003), representing a 60\% error reduction over competitive baselines and a $>25\times$ improvement over tabular ensembles. Ablation studies confirm that explicit molecular graph message-passing and continuous mixture encoding are essential for robust generalization. The complete dataset, evaluation protocols, and reference implementations are released to facilitate data-efficient reaction prediction and continuous solvent representation learning.

