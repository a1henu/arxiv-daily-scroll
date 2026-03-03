---
layout: default
title: Neural Operator-Grounded Continuous Tensor Function Representation and Its Applications
---

# Neural Operator-Grounded Continuous Tensor Function Representation and Its Applications
**arXiv**：[2603.01812v1](https://arxiv.org/abs/2603.01812) · [PDF](https://arxiv.org/pdf/2603.01812.pdf)  
**作者**：Ruoyang Su, Xi-Le Zhao, Sheng Liu, Wei-Hao Wu, Yisi Luo, Michael K. Ng  

**一句话要点**：提出神经算子驱动的连续张量函数表示以更忠实表示复杂多维数据

**关键词**：连续张量函数, 神经算子, 模-n算子, 数据补全, 多维数据表示

## 3 点简述
- 核心问题：现有连续张量函数表示因基于离散线性模-n积而潜力受限
- 方法要点：用连续非线性模-n算子替代模-n积，构建神经算子驱动的连续张量函数表示
- 实验或效果：在网格和非网格数据上验证了该表示在数据补全中的优越性

## 摘要（原文）

> Recently, continuous tensor functions have attracted increasing attention, because they can unifiedly represent data both on mesh grids and beyond mesh grids. However, since mode-$n$ product is essentially discrete and linear, the potential of current continuous tensor function representations is still locked. To break this bottleneck, we suggest neural operator-grounded mode-$n$ operators as a continuous and nonlinear alternative of discrete and linear mode-$n$ product. Instead of mapping the discrete core tensor to the discrete target tensor, proposed mode-$n$ operator directly maps the continuous core tensor function to the continuous target tensor function, which provides a genuine continuous representation of real-world data and can ameliorate discretization artifacts. Empowering with continuous and nonlinear mode-$n$ operators, we propose a neural operator-grounded continuous tensor function representation (abbreviated as NO-CTR), which can more faithfully represent complex real-world data compared with classic discrete tensor representations and continuous tensor function representations. Theoretically, we also prove that any continuous tensor function can be approximated by NO-CTR. To examine the capability of NO-CTR, we suggest an NO-CTR-based multi-dimensional data completion model. Extensive experiments across various data on regular mesh grids (multi-spectral images and color videos), on mesh girds with different resolutions (Sentinel-2 images) and beyond mesh grids (point clouds) demonstrate the superiority of NO-CTR.

