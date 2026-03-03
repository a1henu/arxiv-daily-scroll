---
layout: default
title: WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories
---

# WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories
**arXiv**：[2603.02049v1](https://arxiv.org/abs/2603.02049) · [PDF](https://arxiv.org/pdf/2603.02049.pdf)  
**作者**：Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  

**一句话要点**：提出WorldStereo框架，通过几何记忆模块桥接相机引导视频生成与3D场景重建

**关键词**：视频扩散模型, 3D场景重建, 相机控制, 几何记忆, 多视角一致性, 世界模型

## 3 点简述
- 核心问题：现有视频扩散模型生成视频时相机可控性有限，导致多视角不一致，难以重建一致3D场景
- 方法要点：引入全局几何记忆和空间立体记忆模块，分别提供粗结构先验和细粒度细节约束，实现精确相机控制下的多视角一致视频生成
- 实验或效果：在相机引导视频生成和3D重建基准测试中验证有效性，能作为世界模型处理多样场景生成任务，输出高保真3D结果

## 摘要（原文）

> Recent advances in foundational Video Diffusion Models (VDMs) have yielded significant progress. Yet, despite the remarkable visual quality of generated videos, reconstructing consistent 3D scenes from these outputs remains challenging, due to limited camera controllability and inconsistent generated content when viewed from distinct camera trajectories. In this paper, we propose WorldStereo, a novel framework that bridges camera-guided video generation and 3D reconstruction via two dedicated geometric memory modules. Formally, the global-geometric memory enables precise camera control while injecting coarse structural priors through incrementally updated point clouds. Moreover, the spatial-stereo memory constrains the model's attention receptive fields with 3D correspondence to focus on fine-grained details from the memory bank. These components enable WorldStereo to generate multi-view-consistent videos under precise camera control, facilitating high-quality 3D reconstruction. Furthermore, the flexible control branch-based WorldStereo shows impressive efficiency, benefiting from the distribution matching distilled VDM backbone without joint training. Extensive experiments across both camera-guided video generation and 3D reconstruction benchmarks demonstrate the effectiveness of our approach. Notably, we show that WorldStereo acts as a powerful world model, tackling diverse scene generation tasks (whether starting from perspective or panoramic images) with high-fidelity 3D results. Models will be released.

