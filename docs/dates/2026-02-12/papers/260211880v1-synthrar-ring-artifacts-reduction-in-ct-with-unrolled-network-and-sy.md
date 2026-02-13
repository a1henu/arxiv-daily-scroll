---
layout: default
title: SynthRAR: Ring Artifacts Reduction in CT with Unrolled Network and Synthetic Data Training
---

# SynthRAR: Ring Artifacts Reduction in CT with Unrolled Network and Synthetic Data Training
**arXiv**：[2602.11880v1](https://arxiv.org/abs/2602.11880) · [PDF](https://arxiv.org/pdf/2602.11880.pdf)  
**作者**：Hongxu Yang, Levente Lippenszky, Edina Timko, Gopal Avinash  

**一句话要点**：提出SynthRAR方法，通过展开网络和合成数据训练解决CT环状伪影问题。

**关键词**：CT环状伪影减少, 展开网络, 合成数据训练, 逆问题求解, CT几何建模

## 3 点简述
- 核心问题：CT探测器响应不一致导致环状伪影，影响临床使用。
- 方法要点：基于非理想探测器响应理论，用展开网络结合CT几何前向投影进行逆问题求解。
- 实验或效果：合成数据训练模型在多种扫描几何和解剖区域评估中优于现有方法。

## 摘要（原文）

> Defective and inconsistent responses in CT detectors can cause ring and streak artifacts in the reconstructed images, making them unusable for clinical purposes. In recent years, several ring artifact reduction solutions have been proposed in the image domain or in the sinogram domain using supervised deep learning methods. However, these methods require dedicated datasets for training, leading to a high data collection cost. Furthermore, existing approaches focus exclusively on either image-space or sinogram-space correction, neglecting the intrinsic correlations from the forward operation of the CT geometry. Based on the theoretical analysis of non-ideal CT detector responses, the RAR problem is reformulated as an inverse problem by using an unrolled network, which considers non-ideal response together with linear forward-projection with CT geometry. Additionally, the intrinsic correlations of ring artifacts between the sinogram and image domains are leveraged through synthetic data derived from natural images, enabling the trained model to correct artifacts without requiring real-world clinical data. Extensive evaluations on diverse scanning geometries and anatomical regions demonstrate that the model trained on synthetic data consistently outperforms existing state-of-the-art methods.

