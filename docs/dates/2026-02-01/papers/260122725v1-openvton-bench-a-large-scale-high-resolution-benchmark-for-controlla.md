---
layout: default
title: OpenVTON-Bench: A Large-Scale High-Resolution Benchmark for Controllable Virtual Try-On Evaluation
---

# OpenVTON-Bench: A Large-Scale High-Resolution Benchmark for Controllable Virtual Try-On Evaluation
**arXiv**：[2601.22725v1](https://arxiv.org/abs/2601.22725) · [PDF](https://arxiv.org/pdf/2601.22725.pdf)  
**作者**：Jin Li, Tao Chen, Shuai Jiang, Weijie Wang, Jingwen Luo, Chenhui Wu  

**一句话要点**：提出OpenVTON-Bench大规模高分辨率基准，以解决虚拟试衣系统评估的可靠性问题。

**关键词**：虚拟试衣评估, 大规模基准, 高分辨率图像, 多模态评估, 语义一致性, 扩散模型

## 3 点简述
- 核心问题：传统评估指标难以量化虚拟试衣的纹理细节和语义一致性，现有数据集在规模和多样性上不足。
- 方法要点：构建约100K高分辨率图像对，使用DINOv3聚类和Gemini密集标注，提出多模态评估协议测量五个维度。
- 实验或效果：评估协议与人类判断高度一致（Kendall's τ为0.833），优于SSIM等传统指标。

## 摘要（原文）

> Recent advances in diffusion models have significantly elevated the visual fidelity of Virtual Try-On (VTON) systems, yet reliable evaluation remains a persistent bottleneck. Traditional metrics struggle to quantify fine-grained texture details and semantic consistency, while existing datasets fail to meet commercial standards in scale and diversity. We present OpenVTON-Bench, a large-scale benchmark comprising approximately 100K high-resolution image pairs (up to $1536 \times 1536$). The dataset is constructed using DINOv3-based hierarchical clustering for semantically balanced sampling and Gemini-powered dense captioning, ensuring a uniform distribution across 20 fine-grained garment categories. To support reliable evaluation, we propose a multi-modal protocol that measures VTON quality along five interpretable dimensions: background consistency, identity fidelity, texture fidelity, shape plausibility, and overall realism. The protocol integrates VLM-based semantic reasoning with a novel Multi-Scale Representation Metric based on SAM3 segmentation and morphological erosion, enabling the separation of boundary alignment errors from internal texture artifacts. Experimental results show strong agreement with human judgments (Kendall's $τ$ of 0.833 vs. 0.611 for SSIM), establishing a robust benchmark for VTON evaluation.

