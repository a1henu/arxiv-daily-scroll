---
layout: default
title: TFEC: Multivariate Time-Series Clustering via Temporal-Frequency Enhanced Contrastive Learning
---

# TFEC: Multivariate Time-Series Clustering via Temporal-Frequency Enhanced Contrastive Learning
**arXiv**：[2601.07550v1](https://arxiv.org/abs/2601.07550) · [PDF](https://arxiv.org/pdf/2601.07550.pdf)  
**作者**：Zexi Tan, Tao Xie, Haoyi Xiao, Baoyao Yang, Yuzhu Ji, An Zeng, Xiang Zhang, Yiqun Zhang  

**一句话要点**：提出TFEC框架，通过时频增强对比学习解决多元时间序列聚类中的样本构造和归纳偏差问题。

**关键词**：多元时间序列聚类, 对比学习, 时频增强, 表示学习, 聚类分布优化

## 3 点简述
- 现有基于对比学习的多元时间序列聚类方法忽视聚类信息，且增强策略破坏时间依赖性和周期性。
- 引入时频协同增强机制，设计双路径表示与聚类分布学习框架，联合优化聚类结构和表示保真度。
- 在六个真实数据集上验证，平均NMI提升4.48%，消融实验支持设计有效性。

## 摘要（原文）

> Multivariate Time-Series (MTS) clustering is crucial for signal processing and data analysis. Although deep learning approaches, particularly those leveraging Contrastive Learning (CL), are prominent for MTS representation, existing CL-based models face two key limitations: 1) neglecting clustering information during positive/negative sample pair construction, and 2) introducing unreasonable inductive biases, e.g., destroying time dependence and periodicity through augmentation strategies, compromising representation quality. This paper, therefore, proposes a Temporal-Frequency Enhanced Contrastive (TFEC) learning framework. To preserve temporal structure while generating low-distortion representations, a temporal-frequency Co-EnHancement (CoEH) mechanism is introduced. Accordingly, a synergistic dual-path representation and cluster distribution learning framework is designed to jointly optimize cluster structure and representation fidelity. Experiments on six real-world benchmark datasets demonstrate TFEC's superiority, achieving 4.48% average NMI gains over SOTA methods, with ablation studies validating the design. The code of the paper is available at: https://github.com/yueliangy/TFEC.

