---
layout: default
title: Traffic Image Restoration under Adverse Weather via Frequency-Aware Mamba
---

# Traffic Image Restoration under Adverse Weather via Frequency-Aware Mamba
**arXiv**：[2512.03852v1](https://arxiv.org/abs/2512.03852) · [PDF](https://arxiv.org/pdf/2512.03852.pdf)  
**作者**：Liwen Pan, Longguang Wang, Guangwei Gao, Jun Wang, Jun Shi, Juncheng Li  

**一句话要点**：提出频率感知Mamba以解决恶劣天气下交通图像恢复问题

**关键词**：交通图像恢复, 恶劣天气, 频率感知, Mamba架构, 频域特征提取, 图像重建

## 3 点简述
- 核心问题：现有方法忽视频域先验，Mamba架构在频域特征提取方面潜力未知
- 方法要点：集成频率引导与序列建模，包括双分支特征提取块和先验引导块
- 实验或效果：广泛实验验证了FAMamba的高效性和有效性

## 摘要（原文）

> Traffic image restoration under adverse weather conditions remains a critical challenge for intelligent transportation systems. Existing methods primarily focus on spatial-domain modeling but neglect frequency-domain priors. Although the emerging Mamba architecture excels at long-range dependency modeling through patch-wise correlation analysis, its potential for frequency-domain feature extraction remains unexplored. To address this, we propose Frequency-Aware Mamba (FAMamba), a novel framework that integrates frequency guidance with sequence modeling for efficient image restoration. Our architecture consists of two key components: (1) a Dual-Branch Feature Extraction Block (DFEB) that enhances local-global interaction via bidirectional 2D frequency-adaptive scanning, dynamically adjusting traversal paths based on sub-band texture distributions; and (2) a Prior-Guided Block (PGB) that refines texture details through wavelet-based high-frequency residual learning, enabling high-quality image reconstruction with precise details. Meanwhile, we design a novel Adaptive Frequency Scanning Mechanism (AFSM) for the Mamba architecture, which enables the Mamba to achieve frequency-domain scanning across distinct subgraphs, thereby fully leveraging the texture distribution characteristics inherent in subgraph structures. Extensive experiments demonstrate the efficiency and effectiveness of FAMamba.

