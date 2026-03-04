---
layout: default
title: Combinatorial Sparse PCA Beyond the Spiked Identity Model
---

# Combinatorial Sparse PCA Beyond the Spiked Identity Model
**arXiv**：[2603.02607v1](https://arxiv.org/abs/2603.02607) · [PDF](https://arxiv.org/pdf/2603.02607.pdf)  
**作者**：Syamantak Kumar, Purnamrita Sarkar, Kevin Tian, Peiyuan Zhang  

**一句话要点**：提出组合稀疏PCA方法，超越尖峰恒等模型，适用于一般协方差矩阵。

**关键词**：稀疏主成分分析, 组合算法, 高维统计, 尖峰模型, 截断幂法, 协方差矩阵

## 3 点简述
- 稀疏PCA中组合算法通常仅分析于尖峰恒等模型，存在局限性。
- 提出新组合方法，基于截断幂法变体，保证全局收敛，适用于一般协方差。
- 方法在合成和真实稀疏PCA数据集上评估，样本和时间复杂度可控。

## 摘要（原文）

> Sparse PCA is one of the most well-studied problems in high-dimensional statistics. In this problem, we are given samples from a distribution with covariance $Σ$, whose top eigenvector $v \in R^d$ is $s$-sparse. Existing sparse PCA algorithms can be broadly categorized into (1) combinatorial algorithms (e.g., diagonal or elementwise covariance thresholding) and (2) SDP-based algorithms. While combinatorial algorithms are much simpler, they are typically only analyzed under the spiked identity model (where $Σ= I_d + γvv^\top$ for some $γ> 0$), whereas SDP-based algorithms require no additional assumptions on $Σ$.
>   We demonstrate explicit counterexample covariances $Σ$ against the success of standard combinatorial algorithms for sparse PCA, when moving beyond the spiked identity model. In light of this discrepancy, we give the first combinatorial method for sparse PCA that provably succeeds for general $Σ$ using $s^2 \cdot \mathrm{polylog}(d)$ samples and $d^2 \cdot \mathrm{poly}(s, \log(d))$ time, by providing a global convergence guarantee on a variant of the truncated power method of Yuan and Zhang (2013). We provide a natural generalization of our method to recovering a vector in a sparse leading eigenspace. Finally, we evaluate our method on synthetic and real-world sparse PCA datasets.

