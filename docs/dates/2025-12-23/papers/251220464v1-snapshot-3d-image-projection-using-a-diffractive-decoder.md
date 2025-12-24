---
layout: default
title: Snapshot 3D image projection using a diffractive decoder
---

# Snapshot 3D image projection using a diffractive decoder
**arXiv**：[2512.20464v1](https://arxiv.org/abs/2512.20464) · [PDF](https://arxiv.org/pdf/2512.20464.pdf)  
**作者**：Cagatay Isil, Alexander Chen, Yuhang Li, F. Onuralp Ardic, Shiqi Chen, Che-Yung Shen, Aydogan Ozcan  

**一句话要点**：提出基于衍射解码器的快照3D图像投影系统，以解决高轴向分辨率下衍射串扰的挑战。

**关键词**：3D图像投影, 衍射光学解码器, 深度学习优化, 轴向分辨率, 快照成像, 体积显示

## 3 点简述
- 核心问题：3D图像投影中，轴向平面密集时衍射串扰增加，影响深度分辨率。
- 方法要点：结合数字编码器和衍射光学解码器，通过深度学习优化实现快照多平面投影。
- 实验或效果：实验验证了28个轴向切片的体积图像投影，轴向分离可达波长量级。

## 摘要（原文）

> 3D image display is essential for next-generation volumetric imaging; however, dense depth multiplexing for 3D image projection remains challenging because diffraction-induced cross-talk rapidly increases as the axial image planes get closer. Here, we introduce a 3D display system comprising a digital encoder and a diffractive optical decoder, which simultaneously projects different images onto multiple target axial planes with high axial resolution. By leveraging multi-layer diffractive wavefront decoding and deep learning-based end-to-end optimization, the system achieves high-fidelity depth-resolved 3D image projection in a snapshot, enabling axial plane separations on the order of a wavelength. The digital encoder leverages a Fourier encoder network to capture multi-scale spatial and frequency-domain features from input images, integrates axial position encoding, and generates a unified phase representation that simultaneously encodes all images to be axially projected in a single snapshot through a jointly-optimized diffractive decoder. We characterized the impact of diffractive decoder depth, output diffraction efficiency, spatial light modulator resolution, and axial encoding density, revealing trade-offs that govern axial separation and 3D image projection quality. We further demonstrated the capability to display volumetric images containing 28 axial slices, as well as the ability to dynamically reconfigure the axial locations of the image planes, performed on demand. Finally, we experimentally validated the presented approach, demonstrating close agreement between the measured results and the target images. These results establish the diffractive 3D display system as a compact and scalable framework for depth-resolved snapshot 3D image projection, with potential applications in holographic displays, AR/VR interfaces, and volumetric optical computing.

