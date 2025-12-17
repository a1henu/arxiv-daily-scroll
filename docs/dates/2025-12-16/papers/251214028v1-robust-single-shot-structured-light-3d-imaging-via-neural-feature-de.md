---
layout: default
title: Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding
---

# Robust Single-shot Structured Light 3D Imaging via Neural Feature Decoding
**arXiv**：[2512.14028v1](https://arxiv.org/abs/2512.14028) · [PDF](https://arxiv.org/pdf/2512.14028.pdf)  
**作者**：Jiaheng Li, Qiyu Dai, Lihan Li, Praneeth Chakravarthula, He Sun, Baoquan Chen, Wenzheng Chen  

**一句话要点**：提出基于神经特征解码的单次结构光3D成像方法，提升在遮挡和非朗伯表面等挑战场景下的鲁棒性。

**关键词**：单次结构光, 神经特征匹配, 3D成像, 深度估计, 合成数据训练

## 3 点简述
- 传统单次结构光方法在像素域匹配深度对应，易受遮挡、细节和非朗伯表面影响。
- 新方法在特征空间提取神经特征并构建代价体，结合几何先验进行鲁棒匹配。
- 通过合成数据训练，在真实室内环境中优于商业系统和被动立体RGB深度估计方法。

## 摘要（原文）

> We consider the problem of active 3D imaging using single-shot structured light systems, which are widely employed in commercial 3D sensing devices such as Apple Face ID and Intel RealSense. Traditional structured light methods typically decode depth correspondences through pixel-domain matching algorithms, resulting in limited robustness under challenging scenarios like occlusions, fine-structured details, and non-Lambertian surfaces. Inspired by recent advances in neural feature matching, we propose a learning-based structured light decoding framework that performs robust correspondence matching within feature space rather than the fragile pixel domain. Our method extracts neural features from the projected patterns and captured infrared (IR) images, explicitly incorporating their geometric priors by building cost volumes in feature space, achieving substantial performance improvements over pixel-domain decoding approaches. To further enhance depth quality, we introduce a depth refinement module that leverages strong priors from large-scale monocular depth estimation models, improving fine detail recovery and global structural coherence. To facilitate effective learning, we develop a physically-based structured light rendering pipeline, generating nearly one million synthetic pattern-image pairs with diverse objects and materials for indoor settings. Experiments demonstrate that our method, trained exclusively on synthetic data with multiple structured light patterns, generalizes well to real-world indoor environments, effectively processes various pattern types without retraining, and consistently outperforms both commercial structured light systems and passive stereo RGB-based depth estimation methods. Project page: https://namisntimpot.github.io/NSLweb/.

