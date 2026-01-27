---
layout: default
title: LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction
---

# LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction
**arXiv**：[2601.18475v1](https://arxiv.org/abs/2601.18475) · [PDF](https://arxiv.org/pdf/2601.18475.pdf)  
**作者**：Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  

**一句话要点**：提出StreamLoD-GS框架，基于LoD结构优化3D高斯泼溅，以解决流式自由视点视频重建中的效率与存储问题。

**关键词**：流式自由视点视频, 3D高斯泼溅, LoD结构, 运动分割, 量化残差, 视频重建

## 3 点简述
- 核心问题：流式自由视点视频重建面临稀疏输入、高训练成本和带宽限制，需快速优化和高保真重建。
- 方法要点：采用锚点和八叉树的LoD结构，结合高斯丢弃和GMM运动分割，动态优化并减少存储。
- 实验或效果：在质量、效率和存储方面达到竞争性或领先性能，验证了方法的有效性。

## 摘要（原文）

> Free-Viewpoint Video (FVV) reconstruction enables photorealistic and interactive 3D scene visualization; however, real-time streaming is often bottlenecked by sparse-view inputs, prohibitive training costs, and bandwidth constraints. While recent 3D Gaussian Splatting (3DGS) has advanced FVV due to its superior rendering speed, Streaming Free-Viewpoint Video (SFVV) introduces additional demands for rapid optimization, high-fidelity reconstruction under sparse constraints, and minimal storage footprints. To bridge this gap, we propose StreamLoD-GS, an LoD-based Gaussian Splatting framework designed specifically for SFVV. Our approach integrates three core innovations: 1) an Anchor- and Octree-based LoD-structured 3DGS with a hierarchical Gaussian dropout technique to ensure efficient and stable optimization while maintaining high-quality rendering; 2) a GMM-based motion partitioning mechanism that separates dynamic and static content, refining dynamic regions while preserving background stability; and 3) a quantized residual refinement framework that significantly reduces storage requirements without compromising visual fidelity. Extensive experiments demonstrate that StreamLoD-GS achieves competitive or state-of-the-art performance in terms of quality, efficiency, and storage.

