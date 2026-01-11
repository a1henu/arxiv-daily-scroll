---
layout: default
title: On the Holistic Approach for Detecting Human Image Forgery
---

# On the Holistic Approach for Detecting Human Image Forgery
**arXiv**：[2601.04715v1](https://arxiv.org/abs/2601.04715) · [PDF](https://arxiv.org/pdf/2601.04715.pdf)  
**作者**：Xiao Guo, Jie Zhu, Anil Jain, Xiaoming Liu  

**一句话要点**：提出HuForDet框架以解决人类图像伪造检测的碎片化问题，实现全谱检测。

**关键词**：人类图像伪造检测, 双分支架构, 多模态大语言模型, 自适应LoG模块, 数据集构建

## 3 点简述
- 核心问题：现有方法碎片化，无法泛化到面部和全身伪造的完整范围。
- 方法要点：采用双分支架构，结合面部伪造检测和基于MLLM的上下文一致性分析。
- 实验或效果：在统一数据集上实现SOTA性能，展现跨伪造类型的鲁棒性。

## 摘要（原文）

> The rapid advancement of AI-generated content (AIGC) has escalated the threat of deepfakes, from facial manipulations to the synthesis of entire photorealistic human bodies. However, existing detection methods remain fragmented, specializing either in facial-region forgeries or full-body synthetic images, and consequently fail to generalize across the full spectrum of human image manipulations. We introduce HuForDet, a holistic framework for human image forgery detection, which features a dual-branch architecture comprising: (1) a face forgery detection branch that employs heterogeneous experts operating in both RGB and frequency domains, including an adaptive Laplacian-of-Gaussian (LoG) module designed to capture artifacts ranging from fine-grained blending boundaries to coarse-scale texture irregularities; and (2) a contextualized forgery detection branch that leverages a Multi-Modal Large Language Model (MLLM) to analyze full-body semantic consistency, enhanced with a confidence estimation mechanism that dynamically weights its contribution during feature fusion. We curate a human image forgery (HuFor) dataset that unifies existing face forgery data with a new corpus of full-body synthetic humans. Extensive experiments show that our HuForDet achieves state-of-the-art forgery detection performance and superior robustness across diverse human image forgeries.

