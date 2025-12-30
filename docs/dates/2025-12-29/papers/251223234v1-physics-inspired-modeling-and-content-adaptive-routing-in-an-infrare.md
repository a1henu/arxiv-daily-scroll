---
layout: default
title: Physics-Inspired Modeling and Content Adaptive Routing in an Infrared Gas Leak Detection Network
---

# Physics-Inspired Modeling and Content Adaptive Routing in an Infrared Gas Leak Detection Network
**arXiv**：[2512.23234v1](https://arxiv.org/abs/2512.23234) · [PDF](https://arxiv.org/pdf/2512.23234.pdf)  
**作者**：Dongsheng Li, Chaobo Chen, Siling Wang, Song Gao  

**一句话要点**：提出PEG-DRNet以解决红外气体泄漏检测中微弱羽流识别难题，通过物理建模与自适应路由提升性能。

**关键词**：红外气体泄漏检测, 物理建模, 边缘检测, 自适应路由, 多尺度特征融合, 弱目标识别

## 3 点简述
- 核心问题：红外气体泄漏检测因羽流微弱、半透明、边界模糊而困难，需增强弱对比度与边界线索。
- 方法要点：结合Gas Block物理建模气体扩散，AGPEO提取可靠边缘先验，CASR-PAN自适应路由聚合多尺度特征。
- 实验或效果：在IIG数据集上AP达29.8%，AP50达84.3%，优于基线，计算效率高，参数仅14.9M。

## 摘要（原文）

> Detecting infrared gas leaks is critical for environmental monitoring and industrial safety, yet remains difficult because plumes are faint, small, semitransparent, and have weak, diffuse boundaries. We present physics-edge hybrid gas dynamic routing network (PEG-DRNet). First, we introduce the Gas Block, a diffusion-convection unit modeling gas transport: a local branch captures short-range variations, while a large-kernel branch captures long-range propagation. An edge-gated learnable fusion module balances local detail and global context, strengthening weak-contrast plume and contour cues. Second, we propose the adaptive gradient and phase edge operator (AGPEO), computing reliable edge priors from multi-directional gradients and phase-consistent responses. These are transformed by a multi-scale edge perception module (MSEPM) into hierarchical edge features that reinforce boundaries. Finally, the content-adaptive sparse routing path aggregation network (CASR-PAN), with adaptive information modulation modules for fusion and self, selectively propagates informative features across scales based on edge and content cues, improving cross-scale discriminability while reducing redundancy. Experiments on the IIG dataset show that PEG-DRNet achieves an overall AP of 29.8\%, an AP$_{50}$ of 84.3\%, and a small-object AP of 25.3\%, surpassing the RT-DETR-R18 baseline by 3.0\%, 6.5\%, and 5.3\%, respectively, while requiring only 43.7 Gflops and 14.9 M parameters. The proposed PEG-DRNet achieves superior overall performance with the best balance of accuracy and computational efficiency, outperforming existing CNN and Transformer detectors in AP and AP$_{50}$ on the IIG and LangGas dataset.

