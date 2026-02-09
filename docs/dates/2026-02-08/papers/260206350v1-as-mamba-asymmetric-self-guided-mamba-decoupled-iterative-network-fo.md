---
layout: default
title: AS-Mamba: Asymmetric Self-Guided Mamba Decoupled Iterative Network for Metal Artifact Reduction
---

# AS-Mamba: Asymmetric Self-Guided Mamba Decoupled Iterative Network for Metal Artifact Reduction
**arXiv**：[2602.06350v1](https://arxiv.org/abs/2602.06350) · [PDF](https://arxiv.org/pdf/2602.06350.pdf)  
**作者**：Bowen Ning, Zekun Zhou, Xinyi Zhong, Zhongzhen Wang, HongXin Wu, HaiTao Wang, Liu Shi, Qiegen Liu  

**一句话要点**：提出AS-Mamba网络，通过状态空间模型和频域校正减少CT金属伪影。

**关键词**：金属伪影减少, 状态空间模型, 频域校正, 自引导对比学习, CT图像重建

## 3 点简述
- 核心问题：金属伪影破坏CT图像质量，现有方法难以捕捉方向性几何特征。
- 方法要点：利用Mamba架构捕获方向性伪影，结合频域校正和自引导对比正则化。
- 实验或效果：在公共和临床CBCT数据集上验证，有效抑制条纹伪影并保留结构细节。

## 摘要（原文）

> Metal artifact significantly degrades Computed Tomography (CT) image quality, impeding accurate clinical diagnosis. However, existing deep learning approaches, such as CNN and Transformer, often fail to explicitly capture the directional geometric features of artifacts, leading to compromised structural restoration. To address these limitations, we propose the Asymmetric Self-Guided Mamba (AS-Mamba) for metal artifact reduction. Specifically, the linear propagation of metal-induced streak artifacts aligns well with the sequential modeling capability of State Space Models (SSMs). Consequently, the Mamba architecture is leveraged to explicitly capture and suppress these directional artifacts. Simultaneously, a frequency domain correction mechanism is incorporated to rectify the global amplitude spectrum, thereby mitigating intensity inhomogeneity caused by beam hardening. Furthermore, to bridge the distribution gap across diverse clinical scenarios, we introduce a self-guided contrastive regularization strategy. Extensive experiments on public andclinical dental CBCT datasets demonstrate that AS-Mamba achieves superior performance in suppressing directional streaks and preserving structural details, validating the effectiveness of integrating physical geometric priors into deep network design.

