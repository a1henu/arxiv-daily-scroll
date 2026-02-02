---
layout: default
title: Graph Attention Network for Node Regression on Random Geometric Graphs with Erdős--Rényi contamination
---

# Graph Attention Network for Node Regression on Random Geometric Graphs with Erdős--Rényi contamination
**arXiv**：[2601.23239v1](https://arxiv.org/abs/2601.23239) · [PDF](https://arxiv.org/pdf/2601.23239.pdf)  
**作者**：Somak Laha, Suqi Liu, Morgane Austern  

**一句话要点**：提出基于图注意力网络的节点回归方法，用于处理随机几何图中节点特征和边同时受噪声污染的问题。

**关键词**：图注意力网络, 节点回归, 随机几何图, 噪声污染, 统计保证, 去噪代理特征

## 3 点简述
- 研究图注意力网络在节点特征和边同时受噪声污染时的统计优势，填补现有理论空白。
- 设计任务特定的图注意力网络，通过构建去噪代理特征进行回归，证明其在估计回归系数和预测响应方面优于普通最小二乘法和图卷积网络。
- 在合成数据和真实世界图上验证理论结果，展示注意力机制在节点回归任务中的有效性。

## 摘要（原文）

> Graph attention networks (GATs) are widely used and often appear robust to noise in node covariates and edges, yet rigorous statistical guarantees demonstrating a provable advantage of GATs over non-attention graph neural networks~(GNNs) are scarce. We partially address this gap for node regression with graph-based errors-in-variables models under simultaneous covariate and edge corruption: responses are generated from latent node-level covariates, but only noise-perturbed versions of the latent covariates are observed; and the sample graph is a random geometric graph created from the node covariates but contaminated by independent Erdős--Rényi edges. We propose and analyze a carefully designed, task-specific GAT that constructs denoised proxy features for regression. We prove that regressing the response variables on the proxies achieves lower error asymptotically in (a) estimating the regression coefficient compared to the ordinary least squares (OLS) estimator on the noisy node covariates, and (b) predicting the response for an unlabelled node compared to a vanilla graph convolutional network~(GCN) -- under mild growth conditions. Our analysis leverages high-dimensional geometric tail bounds and concentration for neighbourhood counts and sample covariances. We verify our theoretical findings through experiments on synthetically generated data. We also perform experiments on real-world graphs and demonstrate the effectiveness of the attention mechanism in several node regression tasks.

