---
layout: default
title: BikeActions: An Open Platform and Benchmark for Cyclist-Centric VRU Action Recognition
---

# BikeActions: An Open Platform and Benchmark for Cyclist-Centric VRU Action Recognition
**arXiv**：[2601.10521v1](https://arxiv.org/abs/2601.10521) · [PDF](https://arxiv.org/pdf/2601.10521.pdf)  
**作者**：Max A. Buettner, Kanak Mazumder, Luca Koecher, Mario Finkbeiner, Sebastian Niebler, Fabian B. Flohr  

**一句话要点**：提出FUSE-Bike平台与BikeActions数据集，以解决密集共享空间中骑行者视角的VRU行为识别问题。

**关键词**：VRU行为识别, 多模态数据集, 骑行者视角, 图卷积网络, Transformer模型, 自动驾驶感知

## 3 点简述
- 核心问题：现有研究多关注车辆视角的行人行为，密集共享空间中的VRU交互行为识别不足。
- 方法要点：开发FUSE-Bike多模态感知平台，采集骑行者视角数据，构建BikeActions数据集含5类动作标注。
- 实验或效果：评估图卷积和Transformer模型，建立首个性能基准，并开源数据、工具和代码促进研究。

## 摘要（原文）

> Anticipating the intentions of Vulnerable Road Users (VRUs) is a critical challenge for safe autonomous driving (AD) and mobile robotics. While current research predominantly focuses on pedestrian crossing behaviors from a vehicle's perspective, interactions within dense shared spaces remain underexplored. To bridge this gap, we introduce FUSE-Bike, the first fully open perception platform of its kind. Equipped with two LiDARs, a camera, and GNSS, it facilitates high-fidelity, close-range data capture directly from a cyclist's viewpoint. Leveraging this platform, we present BikeActions, a novel multi-modal dataset comprising 852 annotated samples across 5 distinct action classes, specifically tailored to improve VRU behavior modeling. We establish a rigorous benchmark by evaluating state-of-the-art graph convolution and transformer-based models on our publicly released data splits, establishing the first performance baselines for this challenging task. We release the full dataset together with data curation tools, the open hardware design, and the benchmark code to foster future research in VRU action understanding under https://iv.ee.hm.edu/bikeactions/.

