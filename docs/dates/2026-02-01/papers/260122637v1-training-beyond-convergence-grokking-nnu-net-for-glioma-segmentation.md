---
layout: default
title: Training Beyond Convergence: Grokking nnU-Net for Glioma Segmentation in Sub-Saharan MRI
---

# Training Beyond Convergence: Grokking nnU-Net for Glioma Segmentation in Sub-Saharan MRI
**arXiv**：[2601.22637v1](https://arxiv.org/abs/2601.22637) · [PDF](https://arxiv.org/pdf/2601.22637.pdf)  
**作者**：Mohtady Barakat, Omar Salah, Ahmed Yasser, Mostafa Ahmed, Zahirul Arief, Waleed Khan, Dong Zhang, Aondona Iorumbur, Confidence Raymond, Mohannad Barakat, Noha Magdy  

**一句话要点**：利用nnU-Net与超收敛训练提升撒哈拉以南非洲胶质瘤MRI分割性能

**关键词**：胶质瘤分割, nnU-Net, 超收敛, MRI分析, 撒哈拉以南非洲医疗

## 3 点简述
- 针对撒哈拉以南非洲胶质瘤诊断资源有限问题，使用本地数据集训练自动化分割工具。
- 探索超收敛现象，通过延长训练超越收敛点以触发性能跃升，无需额外标注。
- 在BraTS Africa 2025数据集上，超收敛训练将肿瘤核心和增强肿瘤Dice分数提升至约90%。

## 摘要（原文）

> Gliomas are placing an increasingly clinical burden on Sub-Saharan Africa (SSA). In the region, the median survival for patients remains under two years, and access to diagnostic imaging is extremely limited. These constraints highlight an urgent need for automated tools that can extract the maximum possible information from each available scan, tools that are specifically trained on local data, rather than adapted from high-income settings where conditions are vastly different. We utilize the Brain Tumor Segmentation (BraTS) Africa 2025 Challenge dataset, an expert annotated collection of glioma MRIs. Our objectives are: (i) establish a strong baseline with nnUNet on this dataset, and (ii) explore whether the celebrated "grokking" phenomenon an abrupt, late training jump from memorization to superior generalization can be triggered to push performance without extra labels. We evaluate two training regimes. The first is a fast, budget-conscious approach that limits optimization to just a few epochs, reflecting the constrained GPU resources typically available in African institutions. Despite this limitation, nnUNet achieves strong Dice scores: 92.3% for whole tumor (WH), 86.6% for tumor core (TC), and 86.3% for enhancing tumor (ET). The second regime extends training well beyond the point of convergence, aiming to trigger a grokking-driven performance leap. With this approach, we were able to achieve grokking and enhanced our results to higher Dice scores: 92.2% for whole tumor (WH), 90.1% for tumor core (TC), and 90.2% for enhancing tumor (ET).

