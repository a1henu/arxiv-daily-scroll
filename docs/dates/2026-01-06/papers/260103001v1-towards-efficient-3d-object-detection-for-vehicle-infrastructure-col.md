---
layout: default
title: Towards Efficient 3D Object Detection for Vehicle-Infrastructure Collaboration via Risk-Intent Selection
---

# Towards Efficient 3D Object Detection for Vehicle-Infrastructure Collaboration via Risk-Intent Selection
**arXiv**：[2601.03001v1](https://arxiv.org/abs/2601.03001) · [PDF](https://arxiv.org/pdf/2601.03001.pdf)  
**作者**：Li Wang, Boqi Li, Hang Chen, Xingjian Wu, Yichen Wang, Jiewen Tan, Xinyu Zhang, Huaping Liu  

**一句话要点**：提出风险意图选择框架RiSe，通过选择性特征融合解决车路协同感知中的带宽与冗余问题。

**关键词**：车路协同感知, 三维目标检测, 特征选择性融合, 风险意图选择, 带宽效率优化

## 3 点简述
- 核心问题：车路协同感知中通信带宽与特征冗余的权衡，现有方法传输非关键背景区域特征效率低。
- 方法要点：基于势场理论评估运动风险，结合自运动先验预测关键鸟瞰图区域，实现语义选择性特征融合。
- 实验或效果：在DeepAccident数据集上，通信量降至全特征共享的0.71%，同时保持先进检测精度。

## 摘要（原文）

> Vehicle-Infrastructure Collaborative Perception (VICP) is pivotal for resolving occlusion in autonomous driving, yet the trade-off between communication bandwidth and feature redundancy remains a critical bottleneck. While intermediate fusion mitigates data volume compared to raw sharing, existing frameworks typically rely on spatial compression or static confidence maps, which inefficiently transmit spatially redundant features from non-critical background regions. To address this, we propose Risk-intent Selective detection (RiSe), an interaction-aware framework that shifts the paradigm from identifying visible regions to prioritizing risk-critical ones. Specifically, we introduce a Potential Field-Trajectory Correlation Model (PTCM) grounded in potential field theory to quantitatively assess kinematic risks. Complementing this, an Intention-Driven Area Prediction Module (IDAPM) leverages ego-motion priors to proactively predict and filter key Bird's-Eye-View (BEV) areas essential for decision-making. By integrating these components, RiSe implements a semantic-selective fusion scheme that transmits high-fidelity features only from high-interaction regions, effectively acting as a feature denoiser. Extensive experiments on the DeepAccident dataset demonstrate that our method reduces communication volume to 0.71\% of full feature sharing while maintaining state-of-the-art detection accuracy, establishing a competitive Pareto frontier between bandwidth efficiency and perception performance.

