---
layout: default
title: Tracing Copied Pixels and Regularizing Patch Affinity in Copy Detection
---

# Tracing Copied Pixels and Regularizing Patch Affinity in Copy Detection
**arXiv**：[2602.17484v1](https://arxiv.org/abs/2602.17484) · [PDF](https://arxiv.org/pdf/2602.17484.pdf)  
**作者**：Yichen Lu, Siwei Nie, Minlong Lu, Xudong Yang, Xiaobo Zhang, Peng Zhang  

**一句话要点**：提出PixTrace和CopyNCE以增强图像复制检测中的细粒度对应学习

**关键词**：图像复制检测, 自监督学习, 像素坐标跟踪, 对比学习, 细粒度对应, 几何引导

## 3 点简述
- 现有自监督学习方法在复杂编辑下因细粒度对应不足而性能受限
- 通过像素坐标跟踪模块和几何引导对比损失，桥接像素级可追踪性与块级相似性学习
- 在DISC21数据集上实现领先性能，并提升可解释性

## 摘要（原文）

> Image Copy Detection (ICD) aims to identify manipulated content between image pairs through robust feature representation learning. While self-supervised learning (SSL) has advanced ICD systems, existing view-level contrastive methods struggle with sophisticated edits due to insufficient fine-grained correspondence learning. We address this limitation by exploiting the inherent geometric traceability in edited content through two key innovations. First, we propose PixTrace - a pixel coordinate tracking module that maintains explicit spatial mappings across editing transformations. Second, we introduce CopyNCE, a geometrically-guided contrastive loss that regularizes patch affinity using overlap ratios derived from PixTrace's verified mappings. Our method bridges pixel-level traceability with patch-level similarity learning, suppressing supervision noise in SSL training. Extensive experiments demonstrate not only state-of-the-art performance (88.7% uAP / 83.9% RP90 for matcher, 72.6% uAP / 68.4% RP90 for descriptor on DISC21 dataset) but also better interpretability over existing methods.

