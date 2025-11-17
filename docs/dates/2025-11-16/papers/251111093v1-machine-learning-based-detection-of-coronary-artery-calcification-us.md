---
layout: default
title: Machine-Learning Based Detection of Coronary Artery Calcification Using Synthetic Chest X-Rays
---

# Machine-Learning Based Detection of Coronary Artery Calcification Using Synthetic Chest X-Rays
**arXiv**：[2511.11093v1](https://arxiv.org/abs/2511.11093) · [PDF](https://arxiv.org/pdf/2511.11093.pdf)  
**作者**：Dylan Saeed, Ramtin Gharleghi, Susann Bier, Sonit Singh  

**一句话要点**：提出基于合成胸部X光片的机器学习方法，用于冠状动脉钙化检测

**关键词**：冠状动脉钙化检测, 合成胸部X光, 数字重建放射影像, 深度学习训练, 超分辨率增强, 弱监督学习

## 3 点简述
- 核心问题：CT成本高且胸部X光缺乏可靠标签，限制冠状动脉钙化检测的深度学习发展
- 方法要点：使用数字重建放射影像作为替代训练域，结合超分辨率和对比度增强优化模型
- 实验或效果：轻量CNN从零训练，最佳配置AUC达0.754，优于或持平先前研究

## 摘要（原文）

> Coronary artery calcification (CAC) is a strong predictor of cardiovascular events, with CT-based Agatston scoring widely regarded as the clinical gold standard. However, CT is costly and impractical for large-scale screening, while chest X-rays (CXRs) are inexpensive but lack reliable ground truth labels, constraining deep learning development. Digitally reconstructed radiographs (DRRs) offer a scalable alternative by projecting CT volumes into CXR-like images while inheriting precise labels. In this work, we provide the first systematic evaluation of DRRs as a surrogate training domain for CAC detection. Using 667 CT scans from the COCA dataset, we generate synthetic DRRs and assess model capacity, super-resolution fidelity enhancement, preprocessing, and training strategies. Lightweight CNNs trained from scratch outperform large pretrained networks; pairing super-resolution with contrast enhancement yields significant gains; and curriculum learning stabilises training under weak supervision. Our best configuration achieves a mean AUC of 0.754, comparable to or exceeding prior CXR-based studies. These results establish DRRs as a scalable, label-rich foundation for CAC detection, while laying the foundation for future transfer learning and domain adaptation to real CXRs.

