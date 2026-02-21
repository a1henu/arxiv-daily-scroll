---
layout: default
title: Tracing Copied Pixels and Regularizing Patch Affinity in Copy Detection
---

# Tracing Copied Pixels and Regularizing Patch Affinity in Copy Detection
**arXiv**：[2602.17484v1](https://arxiv.org/abs/2602.17484) · [PDF](https://arxiv.org/pdf/2602.17484.pdf)  
**作者**：Yichen Lu, Siwei Nie, Minlong Lu, Xudong Yang, Xiaobo Zhang, Peng Zhang  

**一句话要点**：提出PixTrace和CopyNCE以提升图像复制检测中精细编辑的识别能力

**关键词**：图像复制检测, 自监督学习, 像素追踪, 对比学习, 块亲和性正则化

## 3 点简述
- 核心问题：自监督学习在图像复制检测中因缺乏细粒度对应学习，难以处理复杂编辑。
- 方法要点：引入PixTrace模块追踪像素坐标，并设计CopyNCE损失正则化块亲和性。
- 实验或效果：在DISC21数据集上实现先进性能，并增强可解释性。

## 摘要（原文）

> Image Copy Detection (ICD) aims to identify manipulated content between image pairs through robust feature representation learning. While self-supervised learning (SSL) has advanced ICD systems, existing view-level contrastive methods struggle with sophisticated edits due to insufficient fine-grained correspondence learning. We address this limitation by exploiting the inherent geometric traceability in edited content through two key innovations. First, we propose PixTrace - a pixel coordinate tracking module that maintains explicit spatial mappings across editing transformations. Second, we introduce CopyNCE, a geometrically-guided contrastive loss that regularizes patch affinity using overlap ratios derived from PixTrace's verified mappings. Our method bridges pixel-level traceability with patch-level similarity learning, suppressing supervision noise in SSL training. Extensive experiments demonstrate not only state-of-the-art performance (88.7% uAP / 83.9% RP90 for matcher, 72.6% uAP / 68.4% RP90 for descriptor on DISC21 dataset) but also better interpretability over existing methods.

