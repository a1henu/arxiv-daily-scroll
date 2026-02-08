---
layout: default
title: LD-SLRO: Latent Diffusion Structured Light for 3-D Reconstruction of Highly Reflective Objects
---

# LD-SLRO: Latent Diffusion Structured Light for 3-D Reconstruction of Highly Reflective Objects
**arXiv**：[2602.05434v1](https://arxiv.org/abs/2602.05434) · [PDF](https://arxiv.org/pdf/2602.05434.pdf)  
**作者**：Sanghoon Jeon, Gihyun Jung, Suhyeon Ka, Jae-Sang Hyun  

**一句话要点**：提出LD-SLRO方法，基于潜在扩散模型恢复高反射物体条纹图像以提升三维重建精度

**关键词**：三维重建, 条纹投影轮廓术, 潜在扩散模型, 高反射表面, 条纹恢复

## 3 点简述
- 核心问题：高反射物体表面导致条纹投影畸变或丢失，影响三维重建。
- 方法要点：编码条纹图像提取潜在特征，用潜在扩散模型抑制反射伪影并恢复条纹信息。
- 实验或效果：实验显示方法优于现有技术，平均均方根误差从1.8176毫米降至0.9619毫米。

## 摘要（原文）

> Fringe projection profilometry-based 3-D reconstruction of objects with high reflectivity and low surface roughness remains a significant challenge. When measuring such glossy surfaces, specular reflection and indirect illumination often lead to severe distortion or loss of the projected fringe patterns. To address these issues, we propose a latent diffusion-based structured light for reflective objects (LD-SLRO). Phase-shifted fringe images captured from highly reflective surfaces are first encoded to extract latent representations that capture surface reflectance characteristics. These latent features are then used as conditional inputs to a latent diffusion model, which probabilistically suppresses reflection-induced artifacts and recover lost fringe information, yielding high-quality fringe images. The proposed components, including the specular reflection encoder, time-variant channel affine layer, and attention modules, further improve fringe restoration quality. In addition, LD-SLRO provides high flexibility in configuring the input and output fringe sets. Experimental results demonstrate that the proposed method improves both fringe quality and 3-D reconstruction accuracy over state-of-the-art methods, reducing the average root-mean-squared error from 1.8176 mm to 0.9619 mm.

