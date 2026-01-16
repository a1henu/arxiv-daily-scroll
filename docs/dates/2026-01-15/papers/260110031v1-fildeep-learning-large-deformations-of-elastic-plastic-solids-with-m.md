---
layout: default
title: FilDeep: Learning Large Deformations of Elastic-Plastic Solids with Multi-Fidelity Data
---

# FilDeep: Learning Large Deformations of Elastic-Plastic Solids with Multi-Fidelity Data
**arXiv**：[2601.10031v1](https://arxiv.org/abs/2601.10031) · [PDF](https://arxiv.org/pdf/2601.10031.pdf)  
**作者**：Jianheng Tang, Shilong Tao, Zhe Feng, Haonan Sun, Menglu Wang, Zhanxing Zhu, Yunhuai Liu  

**一句话要点**：提出FilDeep框架，利用多保真度数据解决弹塑性固体大变形计算中的数据量-精度困境。

**关键词**：弹塑性固体大变形, 多保真度数据学习, 注意力机制, 深度学习框架, 制造应用

## 3 点简述
- 核心问题：弹塑性固体大变形计算中，传统数值方法受限，深度学习依赖高质高量数据，但数据获取困难，存在量-精度权衡。
- 方法要点：设计基于保真度的深度学习框架，结合低保真度（量大精度低）和高保真度（量小精度高）数据联合训练，引入注意力跨保真度模块捕获长程物理交互。
- 实验或效果：在拉伸弯曲问题中验证，FilDeep实现先进性能，可高效应用于制造领域，为首次使用多保真度数据的深度学习框架。

## 摘要（原文）

> The scientific computation of large deformations in elastic-plastic solids is crucial in various manufacturing applications. Traditional numerical methods exhibit several inherent limitations, prompting Deep Learning (DL) as a promising alternative. The effectiveness of current DL techniques typically depends on the availability of high-quantity and high-accuracy datasets, which are yet difficult to obtain in large deformation problems. During the dataset construction process, a dilemma stands between data quantity and data accuracy, leading to suboptimal performance in the DL models. To address this challenge, we focus on a representative application of large deformations, the stretch bending problem, and propose FilDeep, a Fidelity-based Deep Learning framework for large Deformation of elastic-plastic solids. Our FilDeep aims to resolve the quantity-accuracy dilemma by simultaneously training with both low-fidelity and high-fidelity data, where the former provides greater quantity but lower accuracy, while the latter offers higher accuracy but in less quantity. In FilDeep, we provide meticulous designs for the practical large deformation problem. Particularly, we propose attention-enabled cross-fidelity modules to effectively capture long-range physical interactions across MF data. To the best of our knowledge, our FilDeep presents the first DL framework for large deformation problems using MF data. Extensive experiments demonstrate that our FilDeep consistently achieves state-of-the-art performance and can be efficiently deployed in manufacturing.

