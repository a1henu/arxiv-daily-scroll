---
layout: default
title: Understanding NTK Variance in Implicit Neural Representations
---

# Understanding NTK Variance in Implicit Neural Representations
**arXiv**：[2512.15169v1](https://arxiv.org/abs/2512.15169) · [PDF](https://arxiv.org/pdf/2512.15169.pdf)  
**作者**：Chengguang Ou, Yixin Zhuang  

**一句话要点**：分析隐式神经表示中NTK方差以解释架构选择对谱偏置的影响

**关键词**：隐式神经表示, 神经正切核, 谱偏置, 位置编码, 方差分解, 重建质量

## 3 点简述
- 核心问题：隐式神经表示收敛慢且难以恢复高频细节，与神经正切核条件数相关
- 方法要点：通过分解NTK方差，解释位置编码、球面归一化和哈达玛调制如何改善条件数
- 实验或效果：多任务实验验证方差减少，实现更快收敛和更好重建质量

## 摘要（原文）

> Implicit Neural Representations (INRs) often converge slowly and struggle to recover high-frequency details due to spectral bias. While prior work links this behavior to the Neural Tangent Kernel (NTK), how specific architectural choices affect NTK conditioning remains unclear. We show that many INR mechanisms can be understood through their impact on a small set of pairwise similarity factors and scaling terms that jointly determine NTK eigenvalue variance. For standard coordinate MLPs, limited input-feature interactions induce large eigenvalue dispersion and poor conditioning. We derive closed-form variance decompositions for common INR components and show that positional encoding reshapes input similarity, spherical normalization reduces variance via layerwise scaling, and Hadamard modulation introduces additional similarity factors strictly below one, yielding multiplicative variance reduction. This unified view explains how diverse INR architectures mitigate spectral bias by improving NTK conditioning. Experiments across multiple tasks confirm the predicted variance reductions and demonstrate faster, more stable convergence with improved reconstruction quality.

