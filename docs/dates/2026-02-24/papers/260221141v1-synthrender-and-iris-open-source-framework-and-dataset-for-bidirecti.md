---
layout: default
title: SynthRender and IRIS: Open-Source Framework and Dataset for Bidirectional Sim-Real Transfer in Industrial Object Perception
---

# SynthRender and IRIS: Open-Source Framework and Dataset for Bidirectional Sim-Real Transfer in Industrial Object Perception
**arXiv**：[2602.21141v1](https://arxiv.org/abs/2602.21141) · [PDF](https://arxiv.org/pdf/2602.21141.pdf)  
**作者**：Jose Moises Araya-Martinez, Thushar Tom, Adrián Sanchis Reig, Pablo Rey Valiente, Jens Lambrecht, Jörg Krüger  

**一句话要点**：提出SynthRender框架和IRIS数据集，以解决工业物体感知中双向仿真-真实数据迁移问题。

**关键词**：合成图像生成, 域随机化, 仿真-真实迁移, 工业物体感知, 数据集构建

## 3 点简述
- 核心问题：工业物体感知需大量标注数据，但获取成本高，阻碍实际部署。
- 方法要点：开源SynthRender框架，支持引导域随机化生成合成图像，并评估从2D图像创建3D资产的现实到仿真技术。
- 实验或效果：在多个基准测试中表现优异，如公共机器人数据集上达到99.1% mAP@50，并引入IRIS数据集包含32类约20,000标签。

## 摘要（原文）

> Object perception is fundamental for tasks such as robotic material handling and quality inspection. However, modern supervised deep-learning perception models require large datasets for robust automation under semi-uncontrolled conditions. The cost of acquiring and annotating such data for proprietary parts is a major barrier for widespread deployment. In this context, we release SynthRender, an open source framework for synthetic image generation with Guided Domain Randomization capabilities. Furthermore, we benchmark recent Reality-to-Simulation techniques for 3D asset creation from 2D images of real parts. Combined with Domain Randomization, these synthetic assets provide low-overhead, transferable data even for parts lacking 3D files. We also introduce IRIS, the Industrial Real-Sim Imagery Set, containing 32 categories with diverse textures, intra-class variation, strong inter-class similarities and about 20,000 labels. Ablations on multiple benchmarks outline guidelines for efficient data generation with SynthRender. Our method surpasses existing approaches, achieving 99.1% mAP@50 on a public robotics dataset, 98.3% mAP@50 on an automotive benchmark, and 95.3% mAP@50 on IRIS.

