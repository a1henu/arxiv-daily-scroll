---
layout: default
title: DAV-GSWT: Diffusion-Active-View Sampling for Data-Efficient Gaussian Splatting Wang Tiles
---

# DAV-GSWT: Diffusion-Active-View Sampling for Data-Efficient Gaussian Splatting Wang Tiles
**arXiv**：[2602.15355v1](https://arxiv.org/abs/2602.15355) · [PDF](https://arxiv.org/pdf/2602.15355.pdf)  
**作者**：Rong Fu, Jiekai Wu, Haiyun Wei, Yee Tan Jia, Wenxin Zhang, Yang Li, Xiaowen Ma, Wangyu Wu, Simon Fong  

**一句话要点**：提出DAV-GSWT框架，利用扩散先验和主动视角采样，从少量输入合成高质量高斯泼溅Wang Tiles。

**关键词**：高斯泼溅渲染, Wang Tiles生成, 扩散模型, 主动视角采样, 数据高效合成, 虚拟环境构建

## 3 点简述
- 核心问题：现有Wang Tiles方法依赖密集采样，数据效率低，难以生成大规模虚拟环境。
- 方法要点：结合分层不确定性量化和扩散模型，主动选择信息视角并补全缺失结构细节。
- 实验或效果：显著减少所需数据量，保持视觉完整性和交互性能，适用于大规模场景。

## 摘要（原文）

> The emergence of 3D Gaussian Splatting has fundamentally redefined the capabilities of photorealistic neural rendering by enabling high-throughput synthesis of complex environments. While procedural methods like Wang Tiles have recently been integrated to facilitate the generation of expansive landscapes, these systems typically remain constrained by a reliance on densely sampled exemplar reconstructions. We present DAV-GSWT, a data-efficient framework that leverages diffusion priors and active view sampling to synthesize high-fidelity Gaussian Splatting Wang Tiles from minimal input observations. By integrating a hierarchical uncertainty quantification mechanism with generative diffusion models, our approach autonomously identifies the most informative viewpoints while hallucinating missing structural details to ensure seamless tile transitions. Experimental results indicate that our system significantly reduces the required data volume while maintaining the visual integrity and interactive performance necessary for large-scale virtual environments.

