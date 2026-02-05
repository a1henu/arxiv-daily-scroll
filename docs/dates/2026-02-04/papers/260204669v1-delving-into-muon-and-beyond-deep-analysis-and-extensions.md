---
layout: default
title: Delving into Muon and Beyond: Deep Analysis and Extensions
---

# Delving into Muon and Beyond: Deep Analysis and Extensions
**arXiv**：[2602.04669v1](https://arxiv.org/abs/2602.04669) · [PDF](https://arxiv.org/pdf/2602.04669.pdf)  
**作者**：Xianbiao Qi, Marco Chen, Jiaquan Ye, Yelin He, Rong Xiao  

**一句话要点**：提出基于谱变换的统一视角分析Muon优化器，并扩展其变体以探索与Adam的关系。

**关键词**：优化器分析, 谱变换, 自适应优化, Muon优化器, Adam比较

## 3 点简述
- 核心问题：Muon优化器的机制及其与自适应优化器如Adam的关系尚不明确。
- 方法要点：将Muon视为谱变换族p=0端点，引入p=1/2、1/4、1变体，应用于动量SGD和RMS归一化更新。
- 实验或效果：RMS归一化更新更稳定，Muon作为谱归一化有效，但未普遍优于Adam。

## 摘要（原文）

> The Muon optimizer has recently attracted considerable attention for its strong empirical performance and use of orthogonalized updates on matrix-shaped parameters, yet its underlying mechanisms and relationship to adaptive optimizers such as Adam remain insufficiently understood. In this work, we aim to address these questions through a unified spectral perspective. Specifically, we view Muon as the p = 0 endpoint of a family of spectral transformations of the form U \boldsymbolΣ^{p} V' , and consider additional variants with p = 1/2 , p = 1/4 , and p = 1 . These transformations are applied to both first-moment updates, as in momentum SGD, and to root-mean-square (RMS) normalized gradient updates as in Adam. To enable efficient computation, we develop a coupled Newton iteration that avoids explicit singular value decomposition. Across controlled experiments, we find that RMS-normalized updates yield more stable optimization than first-moment updates. Moreover, while spectral compression provides strong stabilization benefits under first-moment updates, the Muon update (p = 0) does not consistently outperform Adam. These results suggest that Muon is best understood as an effective form of spectral normalization, but not a universally superior optimization method. Our source code will be released at https://github.com/Ocram7/BeyondMuon.

