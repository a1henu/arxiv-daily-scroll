---
layout: default
title: USF-Net: A Unified Spatiotemporal Fusion Network for Ground-Based Remote Sensing Cloud Image Sequence Extrapolation
---

# USF-Net: A Unified Spatiotemporal Fusion Network for Ground-Based Remote Sensing Cloud Image Sequence Extrapolation
**arXiv**：[2511.09045v1](https://arxiv.org/abs/2511.09045) · [PDF](https://arxiv.org/pdf/2511.09045.pdf)  
**作者**：Penghui Niu, Taotao Cai, Jiashuai She, Yajuan Zhang, Junhua Gua, Ping Zhanga, Jungong Hane, Jianxin Li  

**一句话要点**：提出USF-Net以解决地基遥感云图像序列外推中的自适应特征提取和长程时空依赖建模问题

**关键词**：地基遥感云图像外推, 时空融合网络, 自适应卷积, 低复杂度注意力, 长程时空依赖, 编码器-解码器框架

## 3 点简述
- 核心问题：现有方法依赖静态卷积核，缺乏自适应特征提取，且时空依赖建模不足，计算效率低
- 方法要点：集成自适应大核卷积和低复杂度注意力机制，结合时间流信息，使用USTM和DSM模块
- 实验或效果：在ASI-CIS数据集上，USF-Net在预测精度和计算效率上优于现有方法

## 摘要（原文）

> Ground-based remote sensing cloud image sequence extrapolation is a key research area in the development of photovoltaic power systems. However, existing approaches exhibit several limitations:(1)they primarily rely on static kernels to augment feature information, lacking adaptive mechanisms to extract features at varying resolutions dynamically;(2)temporal guidance is insufficient, leading to suboptimal modeling of long-range spatiotemporal dependencies; and(3)the quadratic computational cost of attention mechanisms is often overlooked, limiting efficiency in practical deployment. To address these challenges, we propose USF-Net, a Unified Spatiotemporal Fusion Network that integrates adaptive large-kernel convolutions and a low-complexity attention mechanism, combining temporal flow information within an encoder-decoder framework. Specifically, the encoder employs three basic layers to extract features. Followed by the USTM, which comprises:(1)a SiB equipped with a SSM that dynamically captures multi-scale contextual information, and(2)a TiB featuring a TAM that effectively models long-range temporal dependencies while maintaining computational efficiency. In addition, a DSM with a TGM is introduced to enable unified modeling of temporally guided spatiotemporal dependencies. On the decoder side, a DUM is employed to address the common "ghosting effect." It utilizes the initial temporal state as an attention operator to preserve critical motion signatures. As a key contribution, we also introduce and release the ASI-CIS dataset. Extensive experiments on ASI-CIS demonstrate that USF-Net significantly outperforms state-of-the-art methods, establishing a superior balance between prediction accuracy and computational efficiency for ground-based cloud extrapolation. The dataset and source code will be available at https://github.com/she1110/ASI-CIS.

