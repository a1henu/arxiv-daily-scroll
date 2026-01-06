---
layout: default
title: TopoLoRA-SAM: Topology-Aware Parameter-Efficient Adaptation of Foundation Segmenters for Thin-Structure and Cross-Domain Binary Semantic Segmentation
---

# TopoLoRA-SAM: Topology-Aware Parameter-Efficient Adaptation of Foundation Segmenters for Thin-Structure and Cross-Domain Binary Semantic Segmentation
**arXiv**：[2601.02273v1](https://arxiv.org/abs/2601.02273) · [PDF](https://arxiv.org/pdf/2601.02273.pdf)  
**作者**：Salim Khazem  

**一句话要点**：提出TopoLoRA-SAM，通过拓扑感知参数高效适配解决基础分割模型在细薄结构和跨域二值语义分割中的挑战。

**关键词**：参数高效适配, 拓扑感知分割, 二值语义分割, 细薄结构分割, 跨域分割, 低秩适应

## 3 点简述
- 核心问题：基础分割模型如SAM在细薄结构（如视网膜血管）和噪声模态（如SAR图像）的域特定二值语义分割中适应困难，全微调计算成本高且易导致灾难性遗忘。
- 方法要点：在冻结ViT编码器中注入LoRA，结合轻量空间卷积适配器和可选的基于可微分clDice的拓扑感知监督，实现参数高效适配。
- 实验或效果：在五个基准数据集上评估，仅训练5.2%参数（约4.9M），在视网膜血管分割中取得最佳平均Dice，整体平均Dice最优，在CHASE_DB1上显著提升分割准确性和鲁棒性。

## 摘要（原文）

> Foundation segmentation models such as the Segment Anything Model (SAM) exhibit strong zero-shot generalization through large-scale pretraining, but adapting them to domain-specific semantic segmentation remains challenging, particularly for thin structures (e.g., retinal vessels) and noisy modalities (e.g., SAR imagery). Full fine-tuning is computationally expensive and risks catastrophic forgetting. We propose \textbf{TopoLoRA-SAM}, a topology-aware and parameter-efficient adaptation framework for binary semantic segmentation. TopoLoRA-SAM injects Low-Rank Adaptation (LoRA) into the frozen ViT encoder, augmented with a lightweight spatial convolutional adapter and optional topology-aware supervision via differentiable clDice. We evaluate our approach on five benchmarks spanning retinal vessel segmentation (DRIVE, STARE, CHASE\_DB1), polyp segmentation (Kvasir-SEG), and SAR sea/land segmentation (SL-SSDD), comparing against U-Net, DeepLabV3+, SegFormer, and Mask2Former. TopoLoRA-SAM achieves the best retina-average Dice and the best overall average Dice across datasets, while training only \textbf{5.2\%} of model parameters ($\sim$4.9M). On the challenging CHASE\_DB1 dataset, our method substantially improves segmentation accuracy and robustness, demonstrating that topology-aware parameter-efficient adaptation can match or exceed fully fine-tuned specialist models. Code is available at : https://github.com/salimkhazem/Seglab.git

