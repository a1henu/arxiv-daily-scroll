---
layout: default
title: CTForensics: A Comprehensive Dataset and Method for AI-Generated CT Image Detection
---

# CTForensics: A Comprehensive Dataset and Method for AI-Generated CT Image Detection
**arXiv**：[2603.01878v1](https://arxiv.org/abs/2603.01878) · [PDF](https://arxiv.org/pdf/2603.01878.pdf)  
**作者**：Yiheng Li, Zichang Tan, Guoqing Xu, Yijun Ye, Yang Yang, Zhen Lei  

**一句话要点**：提出CTForensics数据集与ESF-CTFD方法以解决AI生成CT图像检测的泛化与敏感性问题

**关键词**：CT图像伪造检测, 生成AI安全, 多域特征融合, 医学影像数据集, 泛化能力评估

## 3 点简述
- 核心问题：现有CT伪造检测缺乏评估泛化能力的数据集，且方法对CT特定伪造痕迹不敏感
- 方法要点：ESF-CTFD通过小波、空间和频域多尺度特征融合，高效捕获伪造线索
- 实验或效果：ESF-CTFD在多种CT生成模型上表现优于现有方法，泛化能力更强

## 摘要（原文）

> With the rapid development of generative AI in medical imaging, synthetic Computed Tomography (CT) images have demonstrated great potential in applications such as data augmentation and clinical diagnosis, but they also introduce serious security risks. Despite the increasing security concerns, existing studies on CT forgery detection are still limited and fail to adequately address real-world challenges. These limitations are mainly reflected in two aspects: the absence of datasets that can effectively evaluate model generalization to reflect the real-world application requirements, and the reliance on detection methods designed for natural images that are insensitive to CT-specific forgery artifacts. In this view, we propose CTForensics, a comprehensive dataset designed to systematically evaluate the generalization capability of CT forgery detection methods, which includes ten diverse CT generative methods. Moreover, we introduce the Enhanced Spatial-Frequency CT Forgery Detector (ESF-CTFD), an efficient CNN-based neural network that captures forgery cues across the wavelet, spatial, and frequency domains. First, it transforms the input CT image into three scales and extracts features at each scale via the Wavelet-Enhanced Central Stem. Then, starting from the largest-scale features, the Spatial Process Block gradually performs feature fusion with the smaller-scale ones. Finally, the Frequency Process Block learns frequency-domain information for predicting the final results. Experiments demonstrate that ESF-CTFD consistently outperforms existing methods and exhibits superior generalization across different CT generative models.

