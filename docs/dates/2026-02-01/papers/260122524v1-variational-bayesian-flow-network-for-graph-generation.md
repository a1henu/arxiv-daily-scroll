---
layout: default
title: Variational Bayesian Flow Network for Graph Generation
---

# Variational Bayesian Flow Network for Graph Generation
**arXiv**：[2601.22524v1](https://arxiv.org/abs/2601.22524) · [PDF](https://arxiv.org/pdf/2601.22524.pdf)  
**作者**：Yida Xiong, Jiameng Chen, Xiuwen Gong, Jia Wu, Shirui Pan, Wenbin Hu  

**一句话要点**：提出变分贝叶斯流网络以解决图生成中节点-边耦合编码问题

**关键词**：图生成, 贝叶斯流网络, 变分推断, 节点-边耦合, 结构化精度, 分子图生成

## 3 点简述
- 图生成需处理离散节点和边属性，现有方法常因因子化假设导致节点-边耦合编码不足
- VBFN通过变分提升至联合高斯变分信念族，利用结构化精度实现节点和边的耦合更新
- 在合成和分子图数据集上，VBFN在保真度和多样性方面超越基线方法

## 摘要（原文）

> Graph generation aims to sample discrete node and edge attributes while satisfying coupled structural constraints. Diffusion models for graphs often adopt largely factorized forward-noising, and many flow-matching methods start from factorized reference noise and coordinate-wise interpolation, so node-edge coupling is not encoded by the generative geometry and must be recovered implicitly by the core network, which can be brittle after discrete decoding. Bayesian Flow Networks (BFNs) evolve distribution parameters and naturally support discrete generation. But classical BFNs typically rely on factorized beliefs and independent channels, which limit geometric evidence fusion. We propose Variational Bayesian Flow Network (VBFN), which performs a variational lifting to a tractable joint Gaussian variational belief family governed by structured precisions. Each Bayesian update reduces to solving a symmetric positive definite linear system, enabling coupled node and edge updates within a single fusion step. We construct sample-agnostic sparse precisions from a representation-induced dependency graph, thereby avoiding label leakage while enforcing node-edge consistency. On synthetic and molecular graph datasets, VBFN improves fidelity and diversity, and surpasses baseline methods.

