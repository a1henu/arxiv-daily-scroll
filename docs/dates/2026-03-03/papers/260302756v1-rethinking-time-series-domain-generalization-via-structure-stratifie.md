---
layout: default
title: Rethinking Time Series Domain Generalization via Structure-Stratified Calibration
---

# Rethinking Time Series Domain Generalization via Structure-Stratified Calibration
**arXiv**：[2603.02756v1](https://arxiv.org/abs/2603.02756) · [PDF](https://arxiv.org/pdf/2603.02756.pdf)  
**作者**：Jinyang Li, Shuhao Mei, Xiaoyu Xiao, Shuhang Li, Ruoxi Yun, Jinbo Sun  

**一句话要点**：提出结构分层校准框架以解决时间序列跨域泛化中的结构异质性问题

**关键词**：时间序列分析, 跨域泛化, 结构分层校准, 动态系统, 零样本学习, 负迁移缓解

## 3 点简述
- 核心问题：时间序列跨域泛化中，结构异质性导致全局对齐易产生虚假对应和负迁移
- 方法要点：通过结构分层校准，区分结构一致样本并在兼容簇内进行幅度校准
- 实验或效果：在19个公共数据集上零样本设置下显著优于基线，验证结构一致性的重要性

## 摘要（原文）

> For time series arising from latent dynamical systems, existing cross-domain generalization methods commonly assume that samples are comparably meaningful within a shared representation space. In real-world settings, however, different datasets often originate from structurally heterogeneous families of dynamical systems, leading to fundamentally distinct feature distributions. Under such circumstances, performing global alignment while neglecting structural differences is highly prone to establishing spurious correspondences and inducing negative transfer. From the new perspective of cross-domain structural correspondence failure, we revisit this problem and propose a structurally stratified calibration framework. This approach explicitly distinguishes structurally consistent samples and performs amplitude calibration exclusively within structurally compatible sample clusters, thereby effectively alleviating generalization failures caused by structural incompatibility. Notably, the proposed framework achieves substantial performance improvements through a concise and computationally efficient calibration strategy. Evaluations on 19 public datasets (100.3k samples) demonstrate that SSCF significantly outperforms strong baselines under the zero-shot setting. These results confirm that establishing structural consistency prior to alignment constitutes a more reliable and effective pathway for improving cross-domain generalization of time series governed by latent dynamical systems.

