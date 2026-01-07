---
layout: default
title: InfiniDepth: Arbitrary-Resolution and Fine-Grained Depth Estimation with Neural Implicit Fields
---

# InfiniDepth: Arbitrary-Resolution and Fine-Grained Depth Estimation with Neural Implicit Fields
**arXiv**：[2601.03252v1](https://arxiv.org/abs/2601.03252) · [PDF](https://arxiv.org/pdf/2601.03252.pdf)  
**作者**：Hao Yu, Haotong Lin, Jiawei Wang, Jiaxin Li, Yida Wang, Xueyang Zhang, Yue Wang, Xiaowei Zhou, Ruizhen Hu, Sida Peng  

**一句话要点**：提出InfiniDepth，通过神经隐式场实现任意分辨率与细粒度深度估计

**关键词**：神经隐式场, 深度估计, 任意分辨率, 细粒度恢复, 局部隐式解码器, 合成基准测试

## 3 点简述
- 现有深度估计方法受限于离散图像网格，难以扩展至任意分辨率并恢复几何细节
- 采用神经隐式场表示深度，通过局部隐式解码器在连续坐标查询深度
- 在合成与真实基准测试中达到先进性能，尤其在细节区域表现优异

## 摘要（原文）

> Existing depth estimation methods are fundamentally limited to predicting depth on discrete image grids. Such representations restrict their scalability to arbitrary output resolutions and hinder the geometric detail recovery. This paper introduces InfiniDepth, which represents depth as neural implicit fields. Through a simple yet effective local implicit decoder, we can query depth at continuous 2D coordinates, enabling arbitrary-resolution and fine-grained depth estimation. To better assess our method's capabilities, we curate a high-quality 4K synthetic benchmark from five different games, spanning diverse scenes with rich geometric and appearance details. Extensive experiments demonstrate that InfiniDepth achieves state-of-the-art performance on both synthetic and real-world benchmarks across relative and metric depth estimation tasks, particularly excelling in fine-detail regions. It also benefits the task of novel view synthesis under large viewpoint shifts, producing high-quality results with fewer holes and artifacts.

