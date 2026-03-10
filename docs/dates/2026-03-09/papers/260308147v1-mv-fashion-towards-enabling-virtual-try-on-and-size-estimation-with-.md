---
layout: default
title: MV-Fashion: Towards Enabling Virtual Try-On and Size Estimation with Multi-View Paired Data
---

# MV-Fashion: Towards Enabling Virtual Try-On and Size Estimation with Multi-View Paired Data
**arXiv**：[2603.08147v1](https://arxiv.org/abs/2603.08147) · [PDF](https://arxiv.org/pdf/2603.08147.pdf)  
**作者**：Hunor Laczkó, Libang Jia, Loc-Phat Truong, Diego Hernández, Sergio Escalera, Jordi Gonzalez, Meysam Madadi  

**一句话要点**：提出MV-Fashion多视角数据集以解决时尚分析中虚拟试穿和尺寸估计的数据不足问题

**关键词**：多视角数据集, 虚拟试穿, 服装尺寸估计, 语义标注, 配对数据, 时尚分析

## 3 点简述
- 现有4D人体数据集缺乏真实服装动态或任务特定标注，阻碍时尚研究
- MV-Fashion提供大规模多视角视频，包含像素级语义标注、材料属性和配对数据
- 基于该数据集建立虚拟试穿、尺寸估计和新视角合成的基准，支持领域应用

## 摘要（原文）

> Existing 4D human datasets fall short for fashion-specific research, lacking either realistic garment dynamics or task-specific annotations. Synthetic datasets suffer from a realism gap, whereas real-world captures lack the detailed annotations and paired data required for virtual try-on (VTON) and size estimation tasks. To bridge this gap, we introduce MV-Fashion, a large-scale, multi-view video dataset engineered for domain-specific fashion analysis. MV-Fashion features 3,273 sequences (72.5 million frames) from 80 diverse subjects wearing 3-10 outfits each. It is designed to capture complex, real-world garment dynamics, including multiple layers and varied styling (e.g. rolled sleeves, tucked shirt). A core contribution is a rich data representation that includes pixel-level semantic annotations, ground-truth material properties like elasticity, and 3D point clouds. Crucially for VTON applications, MV-Fashion provides paired data: multi-view synchronized captures of worn garments alongside their corresponding flat, catalogue images. We leverage this dataset to establish baselines for fashion-centric tasks, including virtual try-on, clothing size estimation, and novel view synthesis. The dataset is available at https://hunorlaczko.github.io/MV-Fashion .

