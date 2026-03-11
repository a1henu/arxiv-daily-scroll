---
layout: default
title: a-TMFG: Scalable Triangulated Maximally Filtered Graphs via Approximate Nearest Neighbors
---

# a-TMFG: Scalable Triangulated Maximally Filtered Graphs via Approximate Nearest Neighbors
**arXiv**：[2603.09564v1](https://arxiv.org/abs/2603.09564) · [PDF](https://arxiv.org/pdf/2603.09564.pdf)  
**作者**：Lionel Yelibi  

**一句话要点**：提出a-TMFG算法以解决大规模数据集上三角最大过滤图构建的内存与计算瓶颈

**关键词**：三角最大过滤图, 近似最近邻, 大规模图构建, 内存管理, 监督学习, 无监督学习

## 3 点简述
- 传统TMFG需预计算密集相关矩阵，限制其在大规模数据集的应用
- a-TMFG利用k近邻图进行初始构建，并动态搜索估计缺失相关性以控制组合爆炸
- 算法在百万级观测数据集上测试，验证了其对参数和噪声的鲁棒性

## 摘要（原文）

> The traditional Triangular Maximally Filtered Graph (TMFG) construction requires pre-computation and storage of a dense correlation matrix; this limits its applicability to small and medium-sized datasets. Here we identify key memory and runtime complexity challenges when using TMFG at scale. We then present the Approximate Triangular Maximally Filtered Graph (a-TMFG) algorithm. This is a novel approach to scaling the construction of artificial graphs from data inspired by TMFG. The method employs k-Nearest Neighbors Graphs (kNNG) for initial construction, and implements a memory management strategy to search and estimate missing correlations on-the-fly. This provides representations to control combinatorial explosion. The algorithm is tested for robustness to the parameters and noise, and is evaluated on datasets with millions of observations. This new method provides a parsimonious way to construct graphs for use-cases where graphs are used as input to supervised and unsupervised learning but where no natural graph exists.

