---
layout: default
title: 3D Field of Junctions: A Noise-Robust, Training-Free Structural Prior for Volumetric Inverse Problems
---

# 3D Field of Junctions: A Noise-Robust, Training-Free Structural Prior for Volumetric Inverse Problems
**arXiv**：[2603.02149v1](https://arxiv.org/abs/2603.02149) · [PDF](https://arxiv.org/pdf/2603.02149.pdf)  
**作者**：Namhoon Kim, Narges Moeini, Justin Romberg, Sara Fridovich-Keil  

**一句话要点**：提出3D Field of Junctions作为无需训练的结构先验，用于低信噪比三维成像逆问题

**关键词**：三维成像逆问题, 结构先验, 无需训练, 体积去噪, 低信噪比, 边缘保持

## 3 点简述
- 核心问题：三维成像逆问题中高噪声导致重建困难，需保持锐利边缘和角结构。
- 方法要点：基于2D Field of Junctions扩展为全三维表示，优化三维楔形连接以解释体积块，并强制重叠块一致性。
- 实验或效果：在低剂量CT、冷冻电子断层扫描和点云去噪等低信噪比任务中，优于经典和神经方法。

## 摘要（原文）

> Volume denoising is a foundational problem in computational imaging, as many 3D imaging inverse problems face high levels of measurement noise. Inspired by the strong 2D image denoising properties of Field of Junctions (ICCV 2021), we propose a novel, fully volumetric 3D Field of Junctions (3D FoJ) representation that optimizes a junction of 3D wedges that best explain each 3D patch of a full volume, while encouraging consistency between overlapping patches. In addition to direct volume denoising, we leverage our 3D FoJ representation as a structural prior that: (i) requires no training data, and thus precludes the risk of hallucination, (ii) preserves and enhances sharp edge and corner structures in 3D, even under low signal to noise ratio (SNR), and (iii) can be used as a drop-in denoising representation via projected or proximal gradient descent for any volumetric inverse problem with low SNR. We demonstrate successful volume reconstruction and denoising with 3D FoJ across three diverse 3D imaging tasks with low-SNR measurements: low-dose X-ray computed tomography (CT), cryogenic electron tomography (cryo-ET), and denoising point clouds such as those from lidar in adverse weather. Across these challenging low-SNR volumetric imaging problems, 3D FoJ outperforms a mixture of classical and neural methods.

