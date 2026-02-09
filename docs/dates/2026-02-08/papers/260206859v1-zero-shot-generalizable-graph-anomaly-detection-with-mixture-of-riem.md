---
layout: default
title: Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts
---

# Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts
**arXiv**：[2602.06859v1](https://arxiv.org/abs/2602.06859) · [PDF](https://arxiv.org/pdf/2602.06859.pdf)  
**作者**：Xinyu Zhao, Qingyun Sun, Jiayi Luo, Xingcheng Fu, Jianxin Li  

**一句话要点**：提出GAD-MoRE框架，通过黎曼专家混合解决零样本图异常检测的几何差异问题

**关键词**：图异常检测, 零样本学习, 黎曼几何, 专家混合, 跨域泛化

## 3 点简述
- 现有零样本图异常检测方法忽略异常模式的几何差异，限制跨域泛化能力
- GAD-MoRE采用多黎曼专家网络，在不同曲率空间建模异常，并引入异常感知特征对齐模块
- 零样本实验显示GAD-MoRE优于现有方法，甚至超越目标域有标签微调的强基线

## 摘要（原文）

> Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graphs from different domains into a single static curvature space can distort the structural signatures of anomalies. To address the challenge that a single curvature space cannot capture geometry-dependent graph anomaly patterns, we propose GAD-MoRE, a novel framework for zero-shot Generalizable Graph Anomaly Detection with a Mixture of Riemannian Experts architecture. Specifically, to ensure that each anomaly pattern is modeled in the Riemannian space where it is most detectable, GAD-MoRE employs a set of specialized Riemannian expert networks, each operating in a distinct curvature space. To align raw node features with curvature-specific anomaly characteristics, we introduce an anomaly-aware multi-curvature feature alignment module that projects inputs into parallel Riemannian spaces, enabling the capture of diverse geometric characteristics. Finally, to facilitate better generalization beyond seen patterns, we design a memory-based dynamic router that adaptively assigns each input to the most compatible expert based on historical reconstruction performance on similar anomalies. Extensive experiments in the zero-shot setting demonstrate that GAD-MoRE significantly outperforms state-of-the-art generalist GAD baselines, and even surpasses strong competitors that are few-shot fine-tuned with labeled data from the target domain.

