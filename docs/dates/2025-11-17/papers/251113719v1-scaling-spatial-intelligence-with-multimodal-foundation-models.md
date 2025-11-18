---
layout: default
title: Scaling Spatial Intelligence with Multimodal Foundation Models
---

# Scaling Spatial Intelligence with Multimodal Foundation Models
**arXiv**：[2511.13719v1](https://arxiv.org/abs/2511.13719) · [PDF](https://arxiv.org/pdf/2511.13719.pdf)  
**作者**：Zhongang Cai, Ruisi Wang, Chenyang Gu, Fanyi Pu, Junxiang Xu, Yubo Wang, Wanqi Yin, Zhitao Yang, Chen Wei, Qingping Sun, Tongxi Zhou, Jiaqi Li, Hui En Pang, Oscar Qian, Yukun Wei, Zhiqian Lin, Xuanke Shi, Kewang Deng, Xiaoyang Han, Zukai Chen, Xiangyu Fan, Hanming Deng, Lewei Lu, Liang Pan, Bo Li, Ziwei Liu, Quan Wang, Dahua Lin, Lei Yang  

**一句话要点**：提出SenseNova-SI系列模型，通过数据扩展提升多模态基础模型的空间智能能力。

**关键词**：空间智能, 多模态基础模型, 数据扩展, 基准测试, 泛化能力

## 3 点简述
- 多模态基础模型在空间智能方面存在显著不足，需要改进。
- 构建SenseNova-SI-8M数据集，包含800万样本，系统训练模型。
- 在多个基准测试中表现优异，如VSI-Bench达68.7%，并分析泛化与风险。

## 摘要（原文）

> Despite remarkable progress, multimodal foundation models still exhibit surprising deficiencies in spatial intelligence. In this work, we explore scaling up multimodal foundation models to cultivate spatial intelligence within the SenseNova-SI family, built upon established multimodal foundations including visual understanding models (i.e., Qwen3-VL and InternVL3) and unified understanding and generation models (i.e., Bagel). We take a principled approach to constructing high-performing and robust spatial intelligence by systematically curating SenseNova-SI-8M: eight million diverse data samples under a rigorous taxonomy of spatial capabilities. SenseNova-SI demonstrates unprecedented performance across a broad range of spatial intelligence benchmarks: 68.7% on VSI-Bench, 43.3% on MMSI, 85.6% on MindCube, 54.6% on ViewSpatial, and 50.1% on SITE, while maintaining strong general multimodal understanding (e.g., 84.9% on MMBench-En). More importantly, we analyze the impact of data scaling, discuss early signs of emergent generalization capabilities enabled by diverse data training, analyze the risk of overfitting and language shortcuts, present a preliminary study on spatial chain-of-thought reasoning, and validate the potential downstream application. SenseNova-SI is an ongoing project, and this report will be updated continuously. All newly trained multimodal foundation models are publicly released to facilitate further research in this direction.

