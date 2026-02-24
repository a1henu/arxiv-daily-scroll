---
layout: default
title: M3S-Net: Multimodal Feature Fusion Network Based on Multi-scale Data for Ultra-short-term PV Power Forecasting
---

# M3S-Net: Multimodal Feature Fusion Network Based on Multi-scale Data for Ultra-short-term PV Power Forecasting
**arXiv**：[2602.19832v1](https://arxiv.org/abs/2602.19832) · [PDF](https://arxiv.org/pdf/2602.19832.pdf)  
**作者**：Penghui Niu, Taotao Cai, Suqi Zhang, Junhua Gu, Ping Zhang, Qiqi Liu, Jianxin Li  

**一句话要点**：提出M3S-Net多模态特征融合网络，基于多尺度数据解决超短期光伏功率预测中云层细粒度特征与气象数据复杂周期性的耦合问题。

**关键词**：光伏功率预测, 多模态特征融合, 多尺度数据处理, 跨模态交互, 状态空间模型, 超短期预测

## 3 点简述
- 核心问题：光伏功率因太阳辐照间歇性和高频变化，尤其在快速云层移动时，对高渗透率电网稳定性构成挑战，现有方法难以捕捉云层细粒度光学特征和多模态复杂时空耦合。
- 方法要点：采用多尺度部分通道选择网络隔离薄云边界特征，多尺度序列到图像分析网络基于FFT解耦气象数据周期性，并引入跨模态Mamba交互模块通过动态C矩阵交换实现深度结构耦合。
- 实验或效果：在新构建的细粒度光伏功率数据集上验证，M3S-Net在10分钟预测中平均绝对误差比先进基线降低6.2%，代码和数据集将开源。

## 摘要（原文）

> The inherent intermittency and high-frequency variability of solar irradiance, particularly during rapid cloud advection, present significant stability challenges to high-penetration photovoltaic grids. Although multimodal forecasting has emerged as a viable mitigation strategy, existing architectures predominantly rely on shallow feature concatenation and binary cloud segmentation, thereby failing to capture the fine-grained optical features of clouds and the complex spatiotemporal coupling between visual and meteorological modalities. To bridge this gap, this paper proposes M3S-Net, a novel multimodal feature fusion network based on multi-scale data for ultra-short-term PV power forecasting. First, a multi-scale partial channel selection network leverages partial convolutions to explicitly isolate the boundary features of optically thin clouds, effectively transcending the precision limitations of coarse-grained binary masking. Second, a multi-scale sequence to image analysis network employs Fast Fourier Transform (FFT)-based time-frequency representation to disentangle the complex periodicity of meteorological data across varying time horizons. Crucially, the model incorporates a cross-modal Mamba interaction module featuring a novel dynamic C-matrix swapping mechanism. By exchanging state-space parameters between visual and temporal streams, this design conditions the state evolution of one modality on the context of the other, enabling deep structural coupling with linear computational complexity, thus overcoming the limitations of shallow concatenation. Experimental validation on the newly constructed fine-grained PV power dataset demonstrates that M3S-Net achieves a mean absolute error reduction of 6.2% in 10-minute forecasts compared to state-of-the-art baselines. The dataset and source code will be available at https://github.com/she1110/FGPD.

