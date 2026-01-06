---
layout: default
title: Beyond Segmentation: An Oil Spill Change Detection Framework Using Synthetic SAR Imagery
---

# Beyond Segmentation: An Oil Spill Change Detection Framework Using Synthetic SAR Imagery
**arXiv**：[2601.02139v1](https://arxiv.org/abs/2601.02139) · [PDF](https://arxiv.org/pdf/2601.02139.pdf)  
**作者**：Chenyang Lai, Shuaiyu Chen, Tianjin Huang, Siyang Song, Guangliang Cheng, Chunbo Luo, Zeyu Fu  

**一句话要点**：提出OSCD框架与TAHI方法，通过合成SAR图像解决油污检测中高误报问题

**关键词**：油污检测, 合成孔径雷达, 变化检测, 图像合成, 环境监测

## 3 点简述
- 核心问题：传统单图分割方法难以区分油污与类似海洋特征，导致高误报率。
- 方法要点：引入OSCD双时相任务，使用TAHI框架合成无油污前图像以增强变化检测。
- 实验或效果：构建首个OSCD数据集，验证方法显著降低误报并提升检测准确性。

## 摘要（原文）

> Marine oil spills are urgent environmental hazards that demand rapid and reliable detection to minimise ecological and economic damage. While Synthetic Aperture Radar (SAR) imagery has become a key tool for large-scale oil spill monitoring, most existing detection methods rely on deep learning-based segmentation applied to single SAR images. These static approaches struggle to distinguish true oil spills from visually similar oceanic features (e.g., biogenic slicks or low-wind zones), leading to high false positive rates and limited generalizability, especially under data-scarce conditions. To overcome these limitations, we introduce Oil Spill Change Detection (OSCD), a new bi-temporal task that focuses on identifying changes between pre- and post-spill SAR images. As real co-registered pre-spill imagery is not always available, we propose the Temporal-Aware Hybrid Inpainting (TAHI) framework, which generates synthetic pre-spill images from post-spill SAR data. TAHI integrates two key components: High-Fidelity Hybrid Inpainting for oil-free reconstruction, and Temporal Realism Enhancement for radiometric and sea-state consistency. Using TAHI, we construct the first OSCD dataset and benchmark several state-of-the-art change detection models. Results show that OSCD significantly reduces false positives and improves detection accuracy compared to conventional segmentation, demonstrating the value of temporally-aware methods for reliable, scalable oil spill monitoring in real-world scenarios.

