---
layout: default
title: Active Label Cleaning for Reliable Detection of Electron Dense Deposits in Transmission Electron Microscopy Images
---

# Active Label Cleaning for Reliable Detection of Electron Dense Deposits in Transmission Electron Microscopy Images
**arXiv**：[2602.05250v1](https://arxiv.org/abs/2602.05250) · [PDF](https://arxiv.org/pdf/2602.05250.pdf)  
**作者**：Jieyun Tan, Shuo Liu, Guibin Zhang, Ziqi Li, Jian Geng, Lei Zhang, Lei Cao  

**一句话要点**：提出主动标签清洗方法以高效去噪众包标注的透射电镜图像数据集

**关键词**：主动学习, 标签去噪, 透射电镜图像分析, 医学图像检测, 众包标注优化

## 3 点简述
- 核心问题：透射电镜图像中电子致密沉积物检测因高质量标注稀缺和众包标签噪声而受限
- 方法要点：利用主动学习选择高价值噪声样本进行专家重标注，并基于标签与预测差异进行样本选择和噪声分级
- 实验或效果：在私有数据集上AP50达67.18%，比噪声标签训练提升18.83%，以73.30%成本降低达到95.79%全专家标注性能

## 摘要（原文）

> Automated detection of electron dense deposits (EDD) in glomerular disease is hindered by the scarcity of high-quality labeled data. While crowdsourcing reduces annotation cost, it introduces label noise. We propose an active label cleaning method to efficiently denoise crowdsourced datasets. Our approach uses active learning to select the most valuable noisy samples for expert re-annotation, building high-accuracy cleaning models. A Label Selection Module leverages discrepancies between crowdsourced labels and model predictions for both sample selection and instance-level noise grading. Experiments show our method achieves 67.18% AP\textsubscript{50} on a private dataset, an 18.83% improvement over training on noisy labels. This performance reaches 95.79% of that with full expert annotation while reducing annotation cost by 73.30%. The method provides a practical, cost-effective solution for developing reliable medical AI with limited expert resources.

