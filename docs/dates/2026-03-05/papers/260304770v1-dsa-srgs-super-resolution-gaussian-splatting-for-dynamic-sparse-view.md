---
layout: default
title: DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction
---

# DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction
**arXiv**：[2603.04770v1](https://arxiv.org/abs/2603.04770) · [PDF](https://arxiv.org/pdf/2603.04770.pdf)  
**作者**：Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  

**一句话要点**：提出DSA-SRGS框架，通过超分辨率高斯溅射解决动态稀疏视图DSA重建中细节恢复不足的问题。

**关键词**：数字减影血管造影, 高斯溅射, 超分辨率重建, 动态神经表示, 稀疏视图重建, 血管细节恢复

## 3 点简述
- 核心问题：现有动态稀疏视图DSA重建方法受输入投影分辨率限制，超分辨率时易产生模糊和锯齿伪影，影响血管细节恢复。
- 方法要点：引入多保真度纹理学习模块，结合置信感知策略和辐射亚像素致密化，优化4D高斯核以提升重建分辨率。
- 实验或效果：在两个临床DSA数据集上验证，DSA-SRGS在定量指标和视觉保真度上显著优于现有方法。

## 摘要（原文）

> Digital subtraction angiography (DSA) is a key imaging technique for the auxiliary diagnosis and treatment of cerebrovascular diseases. Recent advancements in gaussian splatting and dynamic neural representations have enabled robust 3D vessel reconstruction from sparse dynamic inputs. However, these methods are fundamentally constrained by the resolution of input projections, where performing naive upsampling to enhance rendering resolution inevitably results in severe blurring and aliasing artifacts. Such lack of super-resolution capability prevents the reconstructed 4D models from recovering fine-grained vascular details and intricate branching structures, which restricts their application in precision diagnosis and treatment. To solve this problem, this paper proposes DSA-SRGS, the first super-resolution gaussian splatting framework for dynamic sparse-view DSA reconstruction. Specifically, we introduce a Multi-Fidelity Texture Learning Module that integrates high-quality priors from a fine-tuned DSA-specific super-resolution model, into the 4D reconstruction optimization. To mitigate potential hallucination artifacts from pseudo-labels, this module employs a Confidence-Aware Strategy to adaptively weight supervision signals between the original low-resolution projections and the generated high-resolution pseudo-labels. Furthermore, we develop Radiative Sub-Pixel Densification, an adaptive strategy that leverages gradient accumulation from high-resolution sub-pixel sampling to refine the 4D radiative gaussian kernels. Extensive experiments on two clinical DSA datasets demonstrate that DSA-SRGS significantly outperforms state-of-the-art methods in both quantitative metrics and qualitative visual fidelity.

