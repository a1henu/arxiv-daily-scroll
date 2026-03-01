---
layout: default
title: Robust Human Trajectory Prediction via Self-Supervised Skeleton Representation Learning
---

# Robust Human Trajectory Prediction via Self-Supervised Skeleton Representation Learning
**arXiv**：[2602.22791v1](https://arxiv.org/abs/2602.22791) · [PDF](https://arxiv.org/pdf/2602.22791.pdf)  
**作者**：Taishu Arashima, Hiroshi Kera, Kazuhiko Kawamoto  

**一句话要点**：提出基于自监督骨架表示学习的方法，以增强遮挡场景下人体轨迹预测的鲁棒性。

**关键词**：人体轨迹预测, 骨架表示学习, 自监督学习, 掩码自编码, 鲁棒性增强

## 3 点简述
- 核心问题：真实环境中骨架数据常因遮挡导致关节缺失，降低轨迹预测准确性。
- 方法要点：采用掩码自编码预训练自监督骨架表示模型，以补全缺失关节信息。
- 实验或效果：在易遮挡场景中，方法提升对缺失骨架数据的鲁棒性，且不牺牲预测精度，优于基线模型。

## 摘要（原文）

> Human trajectory prediction plays a crucial role in applications such as autonomous navigation and video surveillance. While recent works have explored the integration of human skeleton sequences to complement trajectory information, skeleton data in real-world environments often suffer from missing joints caused by occlusions. These disturbances significantly degrade prediction accuracy, indicating the need for more robust skeleton representations. We propose a robust trajectory prediction method that incorporates a self-supervised skeleton representation model pretrained with masked autoencoding. Experimental results in occlusion-prone scenarios show that our method improves robustness to missing skeletal data without sacrificing prediction accuracy, and consistently outperforms baseline models in clean-to-moderate missingness regimes.

