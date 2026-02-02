---
layout: default
title: EndoCaver: Handling Fog, Blur and Glare in Endoscopic Images via Joint Deblurring-Segmentation
---

# EndoCaver: Handling Fog, Blur and Glare in Endoscopic Images via Joint Deblurring-Segmentation
**arXiv**：[2601.22537v1](https://arxiv.org/abs/2601.22537) · [PDF](https://arxiv.org/pdf/2601.22537.pdf)  
**作者**：Zhuoyu Wu, Wenhui Ou, Pei-Sze Tan, Jiayan Yang, Wenqi Fang, Zheng Wang, Raphaël C. -W. Phan  

**一句话要点**：提出EndoCaver，通过联合去模糊-分割处理内窥镜图像中的雾化、模糊和眩光问题。

**关键词**：内窥镜图像处理, 联合去模糊-分割, 轻量级Transformer, 多任务优化, 临床部署

## 3 点简述
- 核心问题：内窥镜图像常受雾化、运动模糊和眩光影响，降低息肉检测准确性。
- 方法要点：采用轻量级Transformer架构，集成全局注意力模块和去模糊-分割对齐器，实现联合多任务处理。
- 实验或效果：在Kvasir-SEG数据集上，Dice分数达0.922（清洁数据）和0.889（严重退化），参数减少90%。

## 摘要（原文）

> Endoscopic image analysis is vital for colorectal cancer screening, yet real-world conditions often suffer from lens fogging, motion blur, and specular highlights, which severely compromise automated polyp detection. We propose EndoCaver, a lightweight transformer with a unidirectional-guided dual-decoder architecture, enabling joint multi-task capability for image deblurring and segmentation while significantly reducing computational complexity and model parameters. Specifically, it integrates a Global Attention Module (GAM) for cross-scale aggregation, a Deblurring-Segmentation Aligner (DSA) to transfer restoration cues, and a cosine-based scheduler (LoCoS) for stable multi-task optimisation. Experiments on the Kvasir-SEG dataset show that EndoCaver achieves 0.922 Dice on clean data and 0.889 under severe image degradation, surpassing state-of-the-art methods while reducing model parameters by 90%. These results demonstrate its efficiency and robustness, making it well-suited for on-device clinical deployment. Code is available at https://github.com/ReaganWu/EndoCaver.

