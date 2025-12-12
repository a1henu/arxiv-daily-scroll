---
layout: default
title: Hyperspectral Image Data Reduction for Endmember Extraction
---

# Hyperspectral Image Data Reduction for Endmember Extraction
**arXiv**：[2512.10506v1](https://arxiv.org/abs/2512.10506) · [PDF](https://arxiv.org/pdf/2512.10506.pdf)  
**作者**：Tomohiko Mizutani  

**一句话要点**：提出数据缩减自字典方法以降低高光谱图像端元提取的计算成本

**关键词**：高光谱图像, 端元提取, 数据缩减, 自字典方法, 线性混合模型

## 3 点简述
- 核心问题：自字典方法计算成本高，限制大规模高光谱图像应用
- 方法要点：基于线性混合模型和纯像素假设，移除不含端元的像素以缩减数据
- 实验或效果：数值实验显示方法显著减少计算时间且保持提取精度

## 摘要（原文）

> Endmember extraction from hyperspectral images aims to identify the spectral signatures of materials present in a scene. Recent studies have shown that self-dictionary methods can achieve high extraction accuracy; however, their high computational cost limits their applicability to large-scale hyperspectral images. Although several approaches have been proposed to mitigate this issue, it remains a major challenge. Motivated by this situation, this paper pursues a data reduction approach. Assuming that the hyperspectral image follows the linear mixing model with the pure-pixel assumption, we develop a data reduction technique that removes pixels that do not contain endmembers. We analyze the theoretical properties of this reduction step and show that it preserves pixels that lie close to the endmembers. Building on this result, we propose a data-reduced self-dictionary method that integrates the data reduction with a self-dictionary method based on a linear programming formulation. Numerical experiments demonstrate that the proposed method can substantially reduce the computational time of the original self-dictionary method without sacrificing endmember extraction accuracy.

