---
layout: default
title: LeMoF: Level-guided Multimodal Fusion for Heterogeneous Clinical Data
---

# LeMoF: Level-guided Multimodal Fusion for Heterogeneous Clinical Data
**arXiv**：[2601.10092v1](https://arxiv.org/abs/2601.10092) · [PDF](https://arxiv.org/pdf/2601.10092.pdf)  
**作者**：Jongseok Kim, Seongae Kang, Jonghwan Shin, Yuhan Lee, Ohyun Jo  

**一句话要点**：提出LeMoF框架，通过层级引导融合解决临床多模态数据集成中的表示利用不足问题。

**关键词**：多模态融合, 临床预测, 层级表示, 异构数据, ICU数据分析

## 3 点简述
- 现有方法依赖静态模态集成，未能充分利用模态特定表示。
- LeMoF选择性融合编码器不同层级的表示，分离学习全局模态级预测和层级特定判别表示。
- 在ICU住院时长预测实验中，LeMoF优于现有技术，层级集成是关键因素。

## 摘要（原文）

> Multimodal clinical prediction is widely used to integrate heterogeneous data such as Electronic Health Records (EHR) and biosignals. However, existing methods tend to rely on static modality integration schemes and simple fusion strategies. As a result, they fail to fully exploit modality-specific representations. In this paper, we propose Level-guided Modal Fusion (LeMoF), a novel framework that selectively integrates level-guided representations within each modality. Each level refers to a representation extracted from a different layer of the encoder. LeMoF explicitly separates and learns global modality-level predictions from level-specific discriminative representations. This design enables LeMoF to achieve a balanced performance between prediction stability and discriminative capability even in heterogeneous clinical environments. Experiments on length of stay prediction using Intensive Care Unit (ICU) data demonstrate that LeMoF consistently outperforms existing state-of-the-art multimodal fusion techniques across various encoder configurations. We also confirmed that level-wise integration is a key factor in achieving robust predictive performance across various clinical conditions.

