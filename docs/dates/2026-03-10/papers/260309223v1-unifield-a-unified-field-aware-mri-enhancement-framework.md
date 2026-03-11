---
layout: default
title: UniField: A Unified Field-Aware MRI Enhancement Framework
---

# UniField: A Unified Field-Aware MRI Enhancement Framework
**arXiv**：[2603.09223v1](https://arxiv.org/abs/2603.09223) · [PDF](https://arxiv.org/pdf/2603.09223.pdf)  
**作者**：Yiyang Lin, Chenhui Wang, Zhihao Peng, Yixuan Yuan  

**一句话要点**：提出UniField统一框架，通过共享退化模式增强多场强MRI，提升泛化能力。

**关键词**：MRI场强增强, 统一框架, 3D基础模型, 场感知谱校正, 多场强数据集

## 3 点简述
- 现有方法孤立处理场强增强任务，忽略共享退化模式，限制模型泛化。
- UniField利用预训练3D基础模型处理完整体积信息，并引入场感知谱校正机制优化高频细节。
- 实验显示PSNR平均提升约1.81 dB，SSIM提升9.47%，并发布大规模配对多场强数据集。

## 摘要（原文）

> Magnetic Resonance Imaging (MRI) field-strength enhancement holds immense value for both clinical diagnostics and advanced research. However, existing methods typically focus on isolated enhancement tasks, such as specific 64mT-to-3T or 3T-to-7T transitions using limited subject cohorts, thereby failing to exploit the shared degradation patterns inherent across different field strengths and severely restricting model generalization. To address this challenge, we propose \methodname, a unified framework integrating multiple modalities and enhancement tasks to mutually promote representation learning by exploiting these shared degradation characteristics. Specifically, our main contributions are threefold. Firstly, to overcome MRI data scarcity and capture continuous anatomical structures, \methodname departs from conventional methods that treat 3D MRI volumes as independent 2D slices. Instead, we directly exploit comprehensive 3D volumetric information by leveraging pre-trained 3D foundation models, thereby embedding generalized and robust structural representations to significantly boost enhancement performance. In addition, to mitigate the spectral bias of mainstream flow-matching models that often over-smooth high-frequency details, we explicitly incorporate the physical mechanisms of magnetic fields to introduce a Field-Aware Spectral Rectification Mechanism (FASRM), tailoring customized spectral corrections to distinct field strengths. Finally, to resolve the fundamental data bottleneck, we organize and publicly release a comprehensive paired multi-field MRI dataset, which is an order of magnitude larger than existing datasets. Extensive experiments demonstrate our method's superiority over state-of-the-art approaches, achieving an average improvement of approximately 1.81 dB in PSNR and 9.47\% in SSIM. Code will be released upon acceptance.

