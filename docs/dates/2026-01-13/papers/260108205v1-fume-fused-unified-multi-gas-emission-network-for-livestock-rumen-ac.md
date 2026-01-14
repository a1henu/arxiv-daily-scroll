---
layout: default
title: FUME: Fused Unified Multi-Gas Emission Network for Livestock Rumen Acidosis Detection
---

# FUME: Fused Unified Multi-Gas Emission Network for Livestock Rumen Acidosis Detection
**arXiv**：[2601.08205v1](https://arxiv.org/abs/2601.08205) · [PDF](https://arxiv.org/pdf/2601.08205.pdf)  
**作者**：Taminul Islam, Toqi Tahamid Sarker, Mohamed Embaby, Khaled R Ahmed, Amer AbuGhazaleh  

**一句话要点**：提出FUME网络，通过双气体光学成像在体外条件下检测奶牛瘤胃酸中毒。

**关键词**：瘤胃酸中毒检测, 双气体光学成像, 轻量深度学习, 气体羽流分割, 多任务学习, 体外监测

## 3 点简述
- 核心问题：奶牛瘤胃酸中毒诊断依赖侵入性pH测量，难以连续监测。
- 方法要点：使用轻量双流架构，融合CO2和CH4排放模式，联合优化气体羽流分割与健康分类。
- 实验或效果：在自建数据集上实现80.99% mIoU和98.82%分类准确率，计算成本降低10倍。

## 摘要（原文）

> Ruminal acidosis is a prevalent metabolic disorder in dairy cattle causing significant economic losses and animal welfare concerns. Current diagnostic methods rely on invasive pH measurement, limiting scalability for continuous monitoring. We present FUME (Fused Unified Multi-gas Emission Network), the first deep learning approach for rumen acidosis detection from dual-gas optical imaging under in vitro conditions. Our method leverages complementary carbon dioxide (CO2) and methane (CH4) emission patterns captured by infrared cameras to classify rumen health into Healthy, Transitional, and Acidotic states. FUME employs a lightweight dual-stream architecture with weight-shared encoders, modality-specific self-attention, and channel attention fusion, jointly optimizing gas plume segmentation and classification of dairy cattle health. We introduce the first dual-gas OGI dataset comprising 8,967 annotated frames across six pH levels with pixel-level segmentation masks. Experiments demonstrate that FUME achieves 80.99% mIoU and 98.82% classification accuracy while using only 1.28M parameters and 1.97G MACs--outperforming state-of-the-art methods in segmentation quality with 10x lower computational cost. Ablation studies reveal that CO2 provides the primary discriminative signal and dual-task learning is essential for optimal performance. Our work establishes the feasibility of gas emission-based livestock health monitoring, paving the way for practical, in vitro acidosis detection systems. Codes are available at https://github.com/taminulislam/fume.

