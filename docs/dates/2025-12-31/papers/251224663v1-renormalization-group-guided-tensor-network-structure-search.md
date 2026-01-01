---
layout: default
title: Renormalization Group Guided Tensor Network Structure Search
---

# Renormalization Group Guided Tensor Network Structure Search
**arXiv**：[2512.24663v1](https://arxiv.org/abs/2512.24663) · [PDF](https://arxiv.org/pdf/2512.24663.pdf)  
**作者**：Maolin Wang, Bowen Yu, Sheng Zhang, Linjie Mi, Wanyu Wang, Yiqi Wang, Pengyue Jia, Xuetao Wei, Zenglin Xu, Ruocheng Guo, Xiangyu Zhao  

**一句话要点**：提出RGTN框架，通过重整化群引导多尺度搜索，以解决张量网络结构搜索中的计算可处理性和结构适应性挑战。

**关键词**：张量网络结构搜索, 重整化群, 多尺度优化, 张量分解, 视频补全, 计算效率

## 3 点简述
- 核心问题：现有方法面临单尺度优化、离散搜索空间和结构-参数分离导致的效率低下和适应性不足。
- 方法要点：基于重整化群理论，使用动态尺度变换和可学习边门实现连续结构演化，结合节点张力和边信息流等物理量指导搜索。
- 实验或效果：在光场数据、高阶合成张量和视频补全任务中，RGTN实现最优压缩比，运行速度比现有方法快4-600倍。

## 摘要（原文）

> Tensor network structure search (TN-SS) aims to automatically discover optimal network topologies and rank configurations for efficient tensor decomposition in high-dimensional data representation. Despite recent advances, existing TN-SS methods face significant limitations in computational tractability, structure adaptivity, and optimization robustness across diverse tensor characteristics. They struggle with three key challenges: single-scale optimization missing multi-scale structures, discrete search spaces hindering smooth structure evolution, and separated structure-parameter optimization causing computational inefficiency. We propose RGTN (Renormalization Group guided Tensor Network search), a physics-inspired framework transforming TN-SS via multi-scale renormalization group flows. Unlike fixed-scale discrete search methods, RGTN uses dynamic scale-transformation for continuous structure evolution across resolutions. Its core innovation includes learnable edge gates for optimization-stage topology modification and intelligent proposals based on physical quantities like node tension measuring local stress and edge information flow quantifying connectivity importance. Starting from low-complexity coarse scales and refining to finer ones, RGTN finds compact structures while escaping local minima via scale-induced perturbations. Extensive experiments on light field data, high-order synthetic tensors, and video completion tasks show RGTN achieves state-of-the-art compression ratios and runs 4-600$\times$ faster than existing methods, validating the effectiveness of our physics-inspired approach.

