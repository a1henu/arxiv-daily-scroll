---
layout: default
title: Splatwizard: A Benchmark Toolkit for 3D Gaussian Splatting Compression
---

# Splatwizard: A Benchmark Toolkit for 3D Gaussian Splatting Compression
**arXiv**：[2512.24742v1](https://arxiv.org/abs/2512.24742) · [PDF](https://arxiv.org/pdf/2512.24742.pdf)  
**作者**：Xiang Liu, Yimin Zhou, Jinxiang Wang, Yujun Huang, Shuzhao Xie, Shiyu Qin, Mingyao Hong, Jiawei Li, Yaowei Wang, Zhi Wang, Shu-Tao Xia, Bin Chen  

**一句话要点**：提出Splatwizard基准工具包以解决3D高斯泼溅压缩评估标准化不足的问题

**关键词**：3D高斯泼溅, 压缩评估, 基准工具包, 实时视图合成, 性能指标自动化

## 3 点简述
- 核心问题：3D高斯泼溅算法激增，缺乏统一评估工具，尤其在压缩任务中。
- 方法要点：提供易用框架，支持新模型实现和现有技术集成，自动化计算关键性能指标。
- 实验或效果：包含图像质量、重建网格倒角距离、渲染帧率和资源消耗等综合评估。

## 摘要（原文）

> The recent advent of 3D Gaussian Splatting (3DGS) has marked a significant breakthrough in real-time novel view synthesis. However, the rapid proliferation of 3DGS-based algorithms has created a pressing need for standardized and comprehensive evaluation tools, especially for compression task. Existing benchmarks often lack the specific metrics necessary to holistically assess the unique characteristics of different methods, such as rendering speed, rate distortion trade-offs memory efficiency, and geometric accuracy. To address this gap, we introduce Splatwizard, a unified benchmark toolkit designed specifically for benchmarking 3DGS compression models. Splatwizard provides an easy-to-use framework to implement new 3DGS compression model and utilize state-of-the-art techniques proposed by previous work. Besides, an integrated pipeline that automates the calculation of key performance indicators, including image-based quality metrics, chamfer distance of reconstruct mesh, rendering frame rates, and computational resource consumption is included in the framework as well. Code is available at https://github.com/splatwizard/splatwizard

