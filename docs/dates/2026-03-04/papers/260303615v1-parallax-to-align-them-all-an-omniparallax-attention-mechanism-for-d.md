---
layout: default
title: Parallax to Align Them All: An OmniParallax Attention Mechanism for Distributed Multi-View Image Compression
---

# Parallax to Align Them All: An OmniParallax Attention Mechanism for Distributed Multi-View Image Compression
**arXiv**：[2603.03615v1](https://arxiv.org/abs/2603.03615) · [PDF](https://arxiv.org/pdf/2603.03615.pdf)  
**作者**：Haotian Zhang, Feiyue Long, Yixin Yu, Jian Xue, Haocheng Tang, Tongda Xu, Zhenning Shi, Yan Wang, Siwei Ma, Jiaqi Zhang  

**一句话要点**：提出OmniParallax注意力机制以提升分布式多视图图像压缩性能

**关键词**：多视图图像压缩, 分布式编码, 注意力机制, 比特率优化, 解码效率

## 3 点简述
- 分布式多视图图像压缩中现有方法忽视视图间相关性差异，导致编码性能不佳
- 引入OmniParallax注意力机制显式建模任意信息源间相关性，并构建自适应融合模块
- 实验表明ParaHydra框架在比特率节省和解码效率上显著超越现有方法

## 摘要（原文）

> Multi-view image compression (MIC) aims to achieve high compression efficiency by exploiting inter-image correlations, playing a crucial role in 3D applications. As a subfield of MIC, distributed multi-view image compression (DMIC) offers performance comparable to MIC while eliminating the need for inter-view information at the encoder side. However, existing methods in DMIC typically treat all images equally, overlooking the varying degrees of correlation between different views during decoding, which leads to suboptimal coding performance. To address this limitation, we propose a novel $\textbf{OmniParallax Attention Mechanism}$ (OPAM), which is a general mechanism for explicitly modeling correlations and aligned features between arbitrary pairs of information sources. Building upon OPAM, we propose a Parallax Multi Information Fusion Module (PMIFM) to adaptively integrate information from different sources. PMIFM is incorporated into both the joint decoder and the entropy model to construct our end-to-end DMIC framework, $\textbf{ParaHydra}$. Extensive experiments demonstrate that $\textbf{ParaHydra}$ is $\textbf{the first DMIC method}$ to significantly surpass state-of-the-art MIC codecs, while maintaining low computational overhead. Performance gains become more pronounced as the number of input views increases. Compared with LDMIC, $\textbf{ParaHydra}$ achieves bitrate savings of $\textbf{19.72%}$ on WildTrack(3) and up to $\textbf{24.18%}$ on WildTrack(6), while significantly improving coding efficiency (as much as $\textbf{65}\times$ in decoding and $\textbf{34}\times$ in encoding).

