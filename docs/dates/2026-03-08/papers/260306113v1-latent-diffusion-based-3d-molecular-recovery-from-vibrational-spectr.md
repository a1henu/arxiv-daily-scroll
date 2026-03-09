---
layout: default
title: Latent Diffusion-Based 3D Molecular Recovery from Vibrational Spectra
---

# Latent Diffusion-Based 3D Molecular Recovery from Vibrational Spectra
**arXiv**：[2603.06113v1](https://arxiv.org/abs/2603.06113) · [PDF](https://arxiv.org/pdf/2603.06113.pdf)  
**作者**：Wenjin Wu, Aleš Leonardis, Linjiang Chen, Jianbo Jiao  

**一句话要点**：提出IR-GeoDiff，基于潜在扩散模型从红外光谱恢复三维分子几何结构。

**关键词**：红外光谱, 三维分子恢复, 潜在扩散模型, 分子几何, 注意力分析, 化学信息学

## 3 点简述
- 核心问题：现有方法依赖一维SMILES或二维分子图，无法捕捉光谱特征与三维分子几何的复杂关系。
- 方法要点：通过潜在扩散模型，将光谱信息整合到分子结构的节点和边表示中，以恢复三维分子分布。
- 实验或效果：从光谱和结构角度评估，模型能恢复对应给定光谱的分子分布，注意力分析显示其聚焦于特征官能团区域。

## 摘要（原文）

> Infrared (IR) spectroscopy, a type of vibrational spectroscopy, is widely used for molecular structure determination and provides critical structural information for chemists. However, existing approaches for recovering molecular structures from IR spectra typically rely on one-dimensional SMILES strings or two-dimensional molecular graphs, which fail to capture the intricate relationship between spectral features and three-dimensional molecular geometry. Recent advances in diffusion models have greatly enhanced the ability to generate molecular structures in 3D space. Yet, no existing model has explored the distribution of 3D molecular geometries corresponding to a single IR spectrum. In this work, we introduce IR-GeoDiff, a latent diffusion model that recovers 3D molecular geometries from IR spectra by integrating spectral information into both node and edge representations of molecular structures. We evaluate IR-GeoDiff from both spectral and structural perspectives, demonstrating its ability to recover the molecular distribution corresponding to a given IR spectrum. Furthermore, an attention-based analysis reveals that the model is able to focus on characteristic functional group regions in IR spectra, qualitatively consistent with common chemical interpretation practices.

