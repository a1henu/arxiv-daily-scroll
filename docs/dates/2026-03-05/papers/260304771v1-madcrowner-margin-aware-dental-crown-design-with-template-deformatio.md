---
layout: default
title: MADCrowner: Margin Aware Dental Crown Design with Template Deformation and Refinement
---

# MADCrowner: Margin Aware Dental Crown Design with Template Deformation and Refinement
**arXiv**：[2603.04771v1](https://arxiv.org/abs/2603.04771) · [PDF](https://arxiv.org/pdf/2603.04771.pdf)  
**作者**：Linda Wei, Chang Liu, Wenran Zhang, Yuxuan Hu, Ruiyang Li, Feng Qi, Changyao Tian, Ke Wang, Yuanyuan Wang, Shaoting Zhang, Dimitris Metaxas, Hongsheng Li  

**一句话要点**：提出MADCrowner框架，通过模板变形与细化实现牙冠设计的自动化，解决现有方法分辨率不足和表面重建过度延伸问题。

**关键词**：牙冠设计, 模板变形, 边缘分割, 口内扫描, 网格生成, 临床工作流

## 3 点简述
- 核心问题：现有基于学习的牙冠设计方法存在空间分辨率不足、输出噪声和表面重建过度延伸的挑战。
- 方法要点：结合CrownDeformR进行模板变形和CrownSegger进行边缘分割，引入临床工作流启发，利用多尺度编码器提取解剖上下文。
- 实验或效果：在大规模口内扫描数据集上验证，几何精度和临床可行性显著优于现有方法。

## 摘要（原文）

> Dental crown restoration is one of the most common treatment modalities for tooth defect, where personalized dental crown design is critical. While computer-aided design (CAD) systems have notably enhanced the efficiency of dental crown design, extensive manual adjustments are still required in the clinic workflow. Recent studies have explored the application of learning-based methods for the automated generation of restorative dental crowns. Nevertheless, these approaches were challenged by inadequate spatial resolution, noisy outputs, and overextension of surface reconstruction. To address these limitations, we propose \totalframework, a margin-aware mesh generation framework comprising CrownDeformR and CrownSegger. Inspired by the clinic manual workflow of dental crown design, we designed CrownDeformR to deform an initial template to the target crown based on anatomical context, which is extracted by a multi-scale intraoral scan encoder. Additionally, we introduced \marginseg, a novel margin segmentation network, to extract the cervical margin of the target tooth. The performance of CrownDeformR improved with the cervical margin as an extra constraint. And it was also utilized as the boundary condition for the tailored postprocessing method, which removed the overextended area of the reconstructed surface. We constructed a large-scale intraoral scan dataset and performed extensive experiments. The proposed method significantly outperformed existing approaches in both geometric accuracy and clinical feasibility.

