---
layout: default
title: Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction
---

# Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction
**arXiv**：[2601.19216v1](https://arxiv.org/abs/2601.19216) · [PDF](https://arxiv.org/pdf/2601.19216.pdf)  
**作者**：Chaozheng Wen, Jingwen Tong, Zehong Lin, Chenghong Bian, Jun Zhang  

**一句话要点**：提出URF-GS统一辐射场框架，基于3D高斯溅射和逆渲染，融合视觉与无线感知以构建高精度3D无线电地图。

**关键词**：3D无线电地图, 统一辐射场, 3D高斯溅射, 逆渲染, 视觉无线融合, 频谱预测

## 3 点简述
- 核心问题：现有方法将光学与无线知识视为独立模态，未利用光与电磁传播的物理原理，导致3D无线电地图构建精度受限。
- 方法要点：通过统一辐射场表示，结合3D高斯溅射和逆渲染，从视觉和无线观测中恢复场景几何与材料属性，预测任意收发配置的无线电信号行为。
- 实验或效果：相比基于神经辐射场的方法，空间频谱预测精度提升达24.7%，3D无线电地图构建样本效率提高10倍。

## 摘要（原文）

> The emerging applications of next-generation wireless networks (e.g., immersive 3D communication, low-altitude networks, and integrated sensing and communication) necessitate high-fidelity environmental intelligence. 3D radio maps have emerged as a critical tool for this purpose, enabling spectrum-aware planning and environment-aware sensing by bridging the gap between physical environments and electromagnetic signal propagation. However, constructing accurate 3D radio maps requires fine-grained 3D geometric information and a profound understanding of electromagnetic wave propagation. Existing approaches typically treat optical and wireless knowledge as distinct modalities, failing to exploit the fundamental physical principles governing both light and electromagnetic propagation. To bridge this gap, we propose URF-GS, a unified radio-optical radiation field representation framework for accurate and generalizable 3D radio map construction based on 3D Gaussian splatting (3D-GS) and inverse rendering. By fusing visual and wireless sensing observations, URF-GS recovers scene geometry and material properties while accurately predicting radio signal behavior at arbitrary transmitter-receiver (Tx-Rx) configurations. Experimental results demonstrate that URF-GS achieves up to a 24.7% improvement in spatial spectrum prediction accuracy and a 10x increase in sample efficiency for 3D radio map construction compared with neural radiance field (NeRF)-based methods. This work establishes a foundation for next-generation wireless networks by integrating perception, interaction, and communication through holistic radiation field reconstruction.

