---
layout: default
title: NeuroMamba: Multi-Perspective Feature Interaction with Visual Mamba for Neuron Segmentation
---

# NeuroMamba: Multi-Perspective Feature Interaction with Visual Mamba for Neuron Segmentation
**arXiv**：[2601.15929v1](https://arxiv.org/abs/2601.15929) · [PDF](https://arxiv.org/pdf/2601.15929.pdf)  
**作者**：Liuyun Jiang, Yizhuo Lu, Yanchao Zhang, Jiazheng Liu, Hua Han  

**一句话要点**：提出NeuroMamba框架，结合视觉Mamba与多视角特征交互，用于神经元分割以解决长程依赖与细节保留问题。

**关键词**：神经元分割, 视觉Mamba, 多视角特征交互, 长程依赖建模, 体素细节保留, EM数据集

## 3 点简述
- 核心问题：神经元形态不规则且密集交织，现有CNN方法缺乏长程上下文，Transformer方法因分块丢失体素细节导致边界不精确。
- 方法要点：设计通道门控边界判别特征提取器增强局部形态线索，引入空间连续特征提取器集成分辨率感知扫描机制，实现无分块全局建模。
- 实验或效果：在四个公开EM数据集上达到最先进性能，验证了对各向同性和各向异性分辨率的优异适应性。

## 摘要（原文）

> Neuron segmentation is the cornerstone of reconstructing comprehensive neuronal connectomes, which is essential for deciphering the functional organization of the brain. The irregular morphology and densely intertwined structures of neurons make this task particularly challenging. Prevailing CNN-based methods often fail to resolve ambiguous boundaries due to the lack of long-range context, whereas Transformer-based methods suffer from boundary imprecision caused by the loss of voxel-level details during patch partitioning. To address these limitations, we propose NeuroMamba, a multi-perspective framework that exploits the linear complexity of Mamba to enable patch-free global modeling and synergizes this with complementary local feature modeling, thereby efficiently capturing long-range dependencies while meticulously preserving fine-grained voxel details. Specifically, we design a channel-gated Boundary Discriminative Feature Extractor (BDFE) to enhance local morphological cues. Complementing this, we introduce the Spatial Continuous Feature Extractor (SCFE), which integrates a resolution-aware scanning mechanism into the Visual Mamba architecture to adaptively model global dependencies across varying data resolutions. Finally, a cross-modulation mechanism synergistically fuses these multi-perspective features. Our method demonstrates state-of-the-art performance across four public EM datasets, validating its exceptional adaptability to both anisotropic and isotropic resolutions. The source code will be made publicly available.

