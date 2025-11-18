---
layout: default
title: Region-Point Joint Representation for Effective Trajectory Similarity Learning
---

# Region-Point Joint Representation for Effective Trajectory Similarity Learning
**arXiv**：[2511.13125v1](https://arxiv.org/abs/2511.13125) · [PDF](https://arxiv.org/pdf/2511.13125.pdf)  
**作者**：Hao Long, Silin Zhou, Lisi Chen, Shuo Shang  

**一句话要点**：提出RePo方法以联合编码区域和点特征，提升轨迹相似性学习效果

**关键词**：轨迹相似性学习, 区域点联合表示, 对比学习, GPS轨迹分析, 自适应特征融合

## 3 点简述
- 现有方法未能充分利用轨迹信息进行相似性建模
- RePo联合编码区域特征和点特征，并自适应融合
- 实验显示RePo在各项指标上平均准确率提升22.2%

## 摘要（原文）

> Recent learning-based methods have reduced the computational complexity of traditional trajectory similarity computation, but state-of-the-art (SOTA) methods still fail to leverage the comprehensive spectrum of trajectory information for similarity modeling. To tackle this problem, we propose \textbf{RePo}, a novel method that jointly encodes \textbf{Re}gion-wise and \textbf{Po}int-wise features to capture both spatial context and fine-grained moving patterns. For region-wise representation, the GPS trajectories are first mapped to grid sequences, and spatial context are captured by structural features and semantic context enriched by visual features. For point-wise representation, three lightweight expert networks extract local, correlation, and continuous movement patterns from dense GPS sequences. Then, a router network adaptively fuses the learned point-wise features, which are subsequently combined with region-wise features using cross-attention to produce the final trajectory embedding. To train RePo, we adopt a contrastive loss with hard negative samples to provide similarity ranking supervision. Experiment results show that RePo achieves an average accuracy improvement of 22.2\% over SOTA baselines across all evaluation metrics.

