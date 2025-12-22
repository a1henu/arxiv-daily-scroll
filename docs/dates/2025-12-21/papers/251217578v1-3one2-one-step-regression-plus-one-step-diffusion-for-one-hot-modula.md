---
layout: default
title: 3One2: One-step Regression Plus One-step Diffusion for One-hot Modulation in Dual-path Video Snapshot Compressive Imaging
---

# 3One2: One-step Regression Plus One-step Diffusion for One-hot Modulation in Dual-path Video Snapshot Compressive Imaging
**arXiv**：[2512.17578v1](https://arxiv.org/abs/2512.17578) · [PDF](https://arxiv.org/pdf/2512.17578.pdf)  
**作者**：Ge Wang, Xing Liu, Xin Yuan  

**一句话要点**：提出3One2算法，结合一步回归与一步扩散，用于双路径视频快照压缩成像中的独热调制重建。

**关键词**：视频快照压缩成像, 独热调制, 扩散模型, 生成式视频修复, 双光路系统, 时间解耦

## 3 点简述
- 核心问题：独热调制在视频SCI中可实现完美时间解耦，但现有算法未能充分利用其潜力，导致重建质量受限。
- 方法要点：将重建任务转化为生成式视频修复问题，设计SDE前向过程，并引入一步回归初始化加一步扩散细化的框架。
- 实验或效果：在合成数据集和真实场景中验证了方法的有效性，通过双光路互补信息缓解空间退化。

## 摘要（原文）

> Video snapshot compressive imaging (SCI) captures dynamic scene sequences through a two-dimensional (2D) snapshot, fundamentally relying on optical modulation for hardware compression and the corresponding software reconstruction. While mainstream video SCI using random binary modulation has demonstrated success, it inevitably results in temporal aliasing during compression. One-hot modulation, activating only one sub-frame per pixel, provides a promising solution for achieving perfect temporal decoupling, thereby alleviating issues associated with aliasing. However, no algorithms currently exist to fully exploit this potential. To bridge this gap, we propose an algorithm specifically designed for one-hot masks. First, leveraging the decoupling properties of one-hot modulation, we transform the reconstruction task into a generative video inpainting problem and introduce a stochastic differential equation (SDE) of the forward process that aligns with the hardware compression process. Next, we identify limitations of the pure diffusion method for video SCI and propose a novel framework that combines one-step regression initialization with one-step diffusion refinement. Furthermore, to mitigate the spatial degradation caused by one-hot modulation, we implement a dual optical path at the hardware level, utilizing complementary information from another path to enhance the inpainted video. To our knowledge, this is the first work integrating diffusion into video SCI reconstruction. Experiments conducted on synthetic datasets and real scenes demonstrate the effectiveness of our method.

